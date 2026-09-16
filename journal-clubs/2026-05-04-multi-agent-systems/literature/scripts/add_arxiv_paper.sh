#!/usr/bin/env bash
set -euo pipefail

usage() {
    cat <<'USAGE'
Usage: scripts/add_arxiv_paper.sh [options] <arxiv_id> [short_slug] [title]

Examples:
  scripts/add_arxiv_paper.sh 2308.08155 AutoGen "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
  scripts/add_arxiv_paper.sh --no-source 2308.08155 AutoGen "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
  scripts/add_arxiv_paper.sh --refresh-metadata --no-source 2308.08155 AutoGen

By default, the script downloads the PDF, attempts to download arXiv source,
fetches arXiv metadata politely, and creates metadata/summary/notes/claims
stubs when missing.

Options:
  --source              Download arXiv source when available (default)
  --no-source           Skip arXiv source download
  --metadata            Fetch cached arXiv metadata for new stubs (default)
  --no-metadata         Do not call the arXiv API
  --refresh-metadata    Refresh metadata.yaml even if it already exists
  --refresh-cache       Force a fresh arXiv API request instead of using cache

Environment:
  ARXIV_CACHE_DIR             Metadata cache directory (default: .cache/arxiv)
  ARXIV_API_MIN_INTERVAL      Seconds between API calls (default: 3)
  ARXIV_API_MAX_ATTEMPTS      Metadata fetch attempts (default: 4)
USAGE
}

download_source=1
fetch_metadata=1
refresh_metadata=0
refresh_cache=0
while [ $# -gt 0 ]; do
    case "$1" in
        --source)
            download_source=1
            shift
            ;;
        --no-source)
            download_source=0
            shift
            ;;
        --metadata)
            fetch_metadata=1
            shift
            ;;
        --no-metadata)
            fetch_metadata=0
            shift
            ;;
        --refresh-metadata)
            fetch_metadata=1
            refresh_metadata=1
            shift
            ;;
        --refresh-cache)
            fetch_metadata=1
            refresh_cache=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        --)
            shift
            break
            ;;
        -*)
            echo "Unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
        *)
            break
            ;;
    esac
done

if [ $# -lt 1 ]; then
    usage >&2
    exit 1
fi

arxiv_id="$1"
short_slug="${2:-$arxiv_id}"
title="${3:-TODO: title}"
paper_id="${short_slug}_${arxiv_id}"
dir="papers/${paper_id}"
cache_dir="${ARXIV_CACHE_DIR:-.cache/arxiv}"
api_min_interval="${ARXIV_API_MIN_INTERVAL:-3}"
api_max_attempts="${ARXIV_API_MAX_ATTEMPTS:-4}"

yaml_escape() {
    printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'
}

normalize_ws() {
    tr '\r\n\t' '   ' | sed 's/  */ /g; s/^ //; s/ $//'
}

cache_key() {
    printf '%s' "$1" | sed 's/[^A-Za-z0-9._-]/_/g'
}

acquire_api_lock() {
    mkdir -p "$cache_dir"
    api_lock_dir="$cache_dir/api.lock"
    api_lock_owned=0
    waited=0

    while ! mkdir "$api_lock_dir" 2>/dev/null; do
        waited=$((waited + 1))
        if [ "$waited" -ge 600 ]; then
            echo "Warning: timed out waiting for arXiv API lock" >&2
            return 1
        fi
        sleep 1
    done

    api_lock_owned=1
}

release_api_lock() {
    if [ "${api_lock_owned:-0}" -eq 1 ] && [ "${api_lock_dir:-}" ]; then
        rmdir "$api_lock_dir" 2>/dev/null || true
        api_lock_owned=0
    fi
}

wait_for_api_slot() {
    last_request_file="$cache_dir/last_api_request"

    if [ -f "$last_request_file" ]; then
        now="$(date +%s)"
        last="$(cat "$last_request_file" 2>/dev/null || printf '0')"

        case "$last" in
            ''|*[!0-9]*)
                last=0
                ;;
        esac

        elapsed=$((now - last))
        if [ "$elapsed" -lt "$api_min_interval" ]; then
            sleep $((api_min_interval - elapsed))
        fi
    fi
}

retry_after_seconds() {
    headers_file="$1"
    retry_after="$(awk 'tolower($1)=="retry-after:" {gsub(/\r/, "", $2); print $2; exit}' "$headers_file")"

    case "$retry_after" in
        ''|*[!0-9]*)
            return 1
            ;;
        *)
            printf '%s\n' "$retry_after"
            ;;
    esac
}

default_backoff_seconds() {
    attempt="$1"
    case "$attempt" in
        1) printf '30\n' ;;
        2) printf '120\n' ;;
        3) printf '300\n' ;;
        *) printf '600\n' ;;
    esac
}

fetch_arxiv_metadata() {
    id="$1"
    key="$(cache_key "$id")"
    metadata_dir="$cache_dir/metadata"
    cache_file="$metadata_dir/${key}.xml"

    if [ -f "$cache_file" ] && [ "$refresh_cache" -eq 0 ]; then
        printf '%s\n' "$cache_file"
        return 0
    fi

    mkdir -p "$metadata_dir"

    if ! acquire_api_lock; then
        return 1
    fi

    tmp_body="$(mktemp "${TMPDIR:-/tmp}/arxiv-body.XXXXXX")"
    tmp_headers="$(mktemp "${TMPDIR:-/tmp}/arxiv-headers.XXXXXX")"
    attempt=1
    result=1

    while [ "$attempt" -le "$api_max_attempts" ]; do
        wait_for_api_slot

        http_code="$(
            curl -sS -L \
                -D "$tmp_headers" \
                -o "$tmp_body" \
                -w '%{http_code}' \
                --get \
                --data-urlencode "id_list=${id}" \
                --data 'max_results=1' \
                'https://export.arxiv.org/api/query' || true
        )"
        date +%s > "$cache_dir/last_api_request"

        if [ "$http_code" = "200" ] && grep -q '<entry>' "$tmp_body"; then
            mv "$tmp_body" "$cache_file"
            result=0
            break
        fi

        if [ "$http_code" = "429" ] || [ "$http_code" = "503" ]; then
            delay="$(retry_after_seconds "$tmp_headers" || default_backoff_seconds "$attempt")"
            echo "arXiv API returned HTTP ${http_code}; retrying in ${delay}s (attempt ${attempt}/${api_max_attempts})" >&2
            sleep "$delay"
        else
            echo "Warning: arXiv metadata fetch failed for ${id} (HTTP ${http_code})" >&2
            break
        fi

        attempt=$((attempt + 1))
    done

    rm -f "$tmp_body" "$tmp_headers"
    release_api_lock

    if [ "$result" -eq 0 ]; then
        printf '%s\n' "$cache_file"
    fi

    return "$result"
}

xml_string() {
    xml_file="$1"
    xpath="$2"

    xmllint --xpath "string(${xpath})" "$xml_file" 2>/dev/null | normalize_ws || true
}

xml_authors() {
    xml_file="$1"
    count="$(xmllint --xpath 'count(//*[local-name()="entry"]/*[local-name()="author"])' "$xml_file" 2>/dev/null || printf '0')"
    count="${count%%.*}"

    case "$count" in
        ''|*[!0-9]*)
            count=0
            ;;
    esac

    i=1
    while [ "$i" -le "$count" ]; do
        xmllint --xpath "string((//*[local-name()='entry']/*[local-name()='author'])[${i}]/*[local-name()='name'])" "$xml_file" 2>/dev/null | normalize_ws || true
        printf '\n'
        i=$((i + 1))
    done
}

write_authors_yaml() {
    authors_text="$1"

    if [ -z "$authors_text" ]; then
        printf 'authors: []\n'
        return
    fi

    printf 'authors:\n'
    printf '%s\n' "$authors_text" | while IFS= read -r author; do
        if [ -n "$author" ]; then
            printf '  - "%s"\n' "$(yaml_escape "$author")"
        fi
    done
}

authors_inline() {
    authors_text="$1"

    if [ -z "$authors_text" ]; then
        printf 'TODO'
        return
    fi

    printf '%s\n' "$authors_text" | awk 'NF { if (out) out = out ", " $0; else out = $0 } END { print out }'
}

metadata_xml=""
metadata_title=""
metadata_authors=""
metadata_published=""
metadata_date=""
metadata_venue=""
api_lock_dir=""
api_lock_owned=0

trap 'release_api_lock' EXIT
trap 'release_api_lock; exit 130' INT
trap 'release_api_lock; exit 143' TERM

mkdir -p "$dir"

if [ -f "$dir/paper.pdf" ]; then
    echo "PDF already exists: $dir/paper.pdf"
else
    echo "Downloading PDF..."
    curl -fsSL "https://arxiv.org/pdf/${arxiv_id}.pdf" -o "$dir/paper.pdf"
fi

if [ "$download_source" -eq 1 ]; then
    if [ -d "$dir/source" ] && [ "$(find "$dir/source" -mindepth 1 -print -quit 2>/dev/null)" ]; then
        echo "Source already exists: $dir/source"
    else
        mkdir -p "$dir/source"
        echo "Downloading source..."
        if curl -fsSL "https://arxiv.org/e-print/${arxiv_id}" -o "$dir/source/source.tar.gz"; then
            (
                cd "$dir/source"
                if file source.tar.gz | grep -q 'gzip'; then
                    tar xzf source.tar.gz 2>/dev/null && rm source.tar.gz
                elif file source.tar.gz | grep -q 'tar'; then
                    tar xf source.tar.gz 2>/dev/null && rm source.tar.gz
                elif file source.tar.gz | grep -q 'LaTeX\|TeX\|ASCII\|UTF-8'; then
                    mv source.tar.gz main.tex
                else
                    echo "Warning: unknown source format, kept as source.tar.gz"
                fi
            )
        else
            echo "Warning: could not download source; leaving source/ empty" >&2
        fi
    fi
fi

if [ "$fetch_metadata" -eq 1 ] && { [ ! -f "$dir/metadata.yaml" ] || [ "$refresh_metadata" -eq 1 ]; }; then
    if metadata_xml="$(fetch_arxiv_metadata "$arxiv_id")"; then
        metadata_title="$(xml_string "$metadata_xml" '//*[local-name()="entry"]/*[local-name()="title"]')"
        metadata_authors="$(xml_authors "$metadata_xml" | sed '/^$/d')"
        metadata_published="$(xml_string "$metadata_xml" '//*[local-name()="entry"]/*[local-name()="published"]')"
        metadata_date="$(printf '%s' "$metadata_published" | sed 's/T.*//; s/^\([0-9][0-9][0-9][0-9]-[0-9][0-9]\).*/\1/')"
        metadata_venue="Preprint"
    else
        echo "Warning: proceeding without arXiv metadata for ${arxiv_id}" >&2
    fi
fi

if [ -n "$metadata_title" ]; then
    title="$metadata_title"
fi

title_yaml="$(yaml_escape "$title")"
authors_for_summary="$(authors_inline "$metadata_authors")"
date_for_summary="${metadata_date:-TODO}"
venue_for_summary="${metadata_venue:-TODO}"

if [ ! -f "$dir/metadata.yaml" ] || [ "$refresh_metadata" -eq 1 ]; then
    {
        printf 'id: %s\n' "$paper_id"
        printf 'title: "%s"\n' "$title_yaml"
        write_authors_yaml "$metadata_authors"
        printf 'arxiv: "%s"\n' "$arxiv_id"
        printf 'date: "%s"\n' "$metadata_date"
        printf 'venue: %s\n' "${metadata_venue:-\"\"}"
        printf 'status: seed\n'
        printf 'topics: []\n'
        printf 'artifacts:\n'
        printf '  pdf: paper.pdf\n'
        if [ -d "$dir/source" ]; then
            printf '  source: source/\n'
        fi
        printf 'summary: "TODO: one-sentence reason this paper belongs in the corpus."\n'
    } > "$dir/metadata.yaml"
fi

if [ ! -f "$dir/summary.md" ]; then
    cat > "$dir/summary.md" <<EOF
# ${title}

**Authors:** ${authors_for_summary}
**arXiv:** ${arxiv_id}
**Venue:** ${venue_for_summary}
**Date:** ${date_for_summary}

## Problem
TODO

## Method
TODO

## Key Findings
- TODO

## Tags
TODO

## Connections
- TODO
EOF
fi

if [ ! -f "$dir/notes.md" ]; then
    cat > "$dir/notes.md" <<'EOF'
# Notes

## Why It Matters
TODO

## When To Cite
TODO

## Key Terms
TODO
EOF
fi

if [ ! -f "$dir/claims.md" ]; then
    cat > "$dir/claims.md" <<'EOF'
# Claims

## Claim 1
**Claim:** TODO

**Evidence:** TODO

**Caveats/Scope:** TODO

**Source pointers:** TODO
EOF
fi

tex_count=0
if [ -d "$dir/source" ]; then
    tex_count="$(find "$dir/source" -name '*.tex' 2>/dev/null | wc -l | tr -d ' ')"
fi

echo "Done: $dir (${tex_count} .tex files found)"
