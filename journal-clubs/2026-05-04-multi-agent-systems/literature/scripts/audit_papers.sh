#!/usr/bin/env bash
set -euo pipefail

required_files=(
    metadata.yaml
    summary.md
    notes.md
    claims.md
    paper.pdf
)

fail=0
count=0

while IFS= read -r dir; do
    count=$((count + 1))
    missing=()

    for file in "${required_files[@]}"; do
        if [ ! -f "$dir/$file" ]; then
            missing+=("$file")
        fi
    done

    if [ "${#missing[@]}" -gt 0 ]; then
        fail=1
        printf 'MISSING %-48s %s\n' "$(basename "$dir")" "${missing[*]}"
    else
        printf 'OK      %s\n' "$(basename "$dir")"
    fi
done < <(find papers -mindepth 1 -maxdepth 1 -type d | sort)

echo
echo "Checked ${count} paper folders."

if [ "$fail" -ne 0 ]; then
    exit 1
fi
