#!/usr/bin/env bash
set -euo pipefail

usage() {
    cat <<'USAGE'
Usage: scripts/sync_seed_papers.sh [options]

Reads docs/seeds.md and creates missing papers/<Slug>_<arxiv-id>/ folders for
arXiv-backed seed papers. Dry-run is the default.

Options:
  --execute       Actually create missing folders and download PDFs
  --source        Download arXiv source in addition to PDFs
  --metadata      Fetch arXiv API metadata while creating folders
  --limit N       Process at most N missing arXiv seeds
  -h, --help      Show this help

Defaults are intentionally conservative for bulk sync:
  dry-run, --no-source, --no-metadata

Examples:
  scripts/sync_seed_papers.sh
  scripts/sync_seed_papers.sh --execute --limit 10
  scripts/sync_seed_papers.sh --execute --metadata
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
seed_file="$repo_root/docs/seeds.md"
add_script="$repo_root/scripts/add_arxiv_paper.sh"

execute=0
download_source=0
fetch_metadata=0
limit=""

while [ $# -gt 0 ]; do
    case "$1" in
        --execute)
            execute=1
            shift
            ;;
        --source)
            download_source=1
            shift
            ;;
        --metadata)
            fetch_metadata=1
            shift
            ;;
        --limit)
            if [ $# -lt 2 ]; then
                echo "Missing value for --limit" >&2
                exit 1
            fi
            limit="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
    esac
done

if [ ! -f "$seed_file" ]; then
    echo "Missing seed file: $seed_file" >&2
    exit 1
fi

if [ ! -x "$add_script" ]; then
    echo "Missing executable add script: $add_script" >&2
    exit 1
fi

case "$limit" in
    ""|*[!0-9]*)
        if [ -n "$limit" ]; then
            echo "--limit must be a positive integer" >&2
            exit 1
        fi
        ;;
    0)
        echo "--limit must be a positive integer" >&2
        exit 1
        ;;
esac

is_arxiv_id() {
    case "$1" in
        [0-9][0-9][0-9][0-9].[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9].[0-9][0-9][0-9][0-9][0-9])
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

paper_exists() {
    arxiv_id="$1"
    paper_dir="$(find "$repo_root/papers" -mindepth 1 -maxdepth 1 -type d -name "*_${arxiv_id}" -print -quit)"
    [ -n "$paper_dir" ] && [ -f "$paper_dir/paper.pdf" ]
}

slug_from_title() {
    title="$1"
    candidate=""
    prefix=""

    candidate="$(
        printf '%s' "$title" \
            | sed -n 's/.*(\([A-Za-z0-9][A-Za-z0-9-]*\)).*/\1/p' \
            | tail -n 1
    )"

    if [ -n "$candidate" ] && printf '%s' "$candidate" | grep -Eq '^([A-Z0-9-]{2,}|[A-Za-z0-9-]*[a-z][A-Z][A-Za-z0-9-]*)$'; then
        printf '%s\n' "$candidate" | sed 's/[^A-Za-z0-9][^A-Za-z0-9]*/_/g; s/^_//; s/_$//'
        return
    fi

    case "$title" in
        *:*)
            prefix="${title%%:*}"
            if printf '%s' "$prefix" | grep -Eq '^[A-Za-z0-9-]+$'; then
                printf '%s\n' "$prefix" | sed 's/[^A-Za-z0-9][^A-Za-z0-9]*//g'
                return
            fi
            title="$prefix"
            ;;
    esac

    printf '%s' "$title" \
        | sed 's/&/ And /g; s/[^A-Za-z0-9][^A-Za-z0-9]*/ /g' \
        | awk '
            {
                out = ""
                for (i = 1; i <= NF; i++) {
                    word = $i
                    lower = tolower(word)
                    if (out == "" && (lower == "a" || lower == "an" || lower == "the" || lower == "towards" || lower == "toward")) {
                        continue
                    }
                    if (length(out) + length(word) > 40) {
                        break
                    }
                    out = out word
                }
                if (out == "") {
                    out = "Paper"
                }
                print out
            }
        '
}

parse_seeds() {
    awk -F '|' '
        /^\|[[:space:]]*[0-9]+[[:space:]]*\|/ {
            for (i = 1; i <= NF; i++) {
                gsub(/^[ \t]+|[ \t]+$/, "", $i)
            }
            print $3 "\t" $5 "\t" $6 "\t" $7
        }
    ' "$seed_file"
}

processed=0
existing=0
missing=0
skipped=0
failed=0

cd "$repo_root"

while IFS="$(printf '\t')" read -r title arxiv_id sub_area role; do
    if ! is_arxiv_id "$arxiv_id"; then
        skipped=$((skipped + 1))
        printf 'SKIP non-arXiv %-24s %s\n' "$arxiv_id" "$title"
        continue
    fi

    if paper_exists "$arxiv_id"; then
        existing=$((existing + 1))
        printf 'OK   %-24s %s\n' "$arxiv_id" "$title"
        continue
    fi

    if [ -n "$limit" ] && [ "$processed" -ge "$limit" ]; then
        continue
    fi

    missing=$((missing + 1))
    processed=$((processed + 1))
    slug="$(slug_from_title "$title")"
    printf 'ADD  %-24s %-50s %s\n' "$arxiv_id" "$slug" "$title"

    if [ "$execute" -eq 1 ]; then
        args=()

        if [ "$download_source" -eq 1 ]; then
            args+=("--source")
        else
            args+=("--no-source")
        fi

        if [ "$fetch_metadata" -eq 1 ]; then
            args+=("--metadata")
        else
            args+=("--no-metadata")
        fi

        if ! "$add_script" "${args[@]}" "$arxiv_id" "$slug" "$title"; then
            failed=$((failed + 1))
            printf 'FAIL %-24s %s\n' "$arxiv_id" "$title" >&2
        fi
    fi
done < <(parse_seeds)

echo
echo "Existing arXiv seed folders: $existing"
echo "Missing arXiv seed folders shown/processed: $missing"
echo "Skipped non-arXiv seeds: $skipped"
echo "Failed additions: $failed"

if [ "$execute" -ne 1 ]; then
    echo "Dry run only. Re-run with --execute to create folders."
elif [ "$failed" -ne 0 ]; then
    exit 1
fi
