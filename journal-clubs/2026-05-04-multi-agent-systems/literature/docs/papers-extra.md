# Extra Papers Corpus

Use this when you want agents to inspect broad candidate papers without
promoting those papers into the reviewed `papers/` corpus.

The reviewed corpus contract still lives in `papers/README.md`: create
`papers/<slug>_<id>/` only for active seeds, top-100 selections, or papers that
have been reviewed deeply enough to deserve local notes and claims.

## Why This Exists

The 1000-paper field map is useful for finding hidden gems, but most rows do
not have local paper artifacts. Bulk-generating full paper folders would make
unresolved or unread papers look reviewed. `papers_extra/` solves the
acquisition problem while keeping curation status honest.

## Download Artifacts

Dry run:

```bash
python3 scripts/sync_papers_extra.py
```

Download all inferable PDFs:

```bash
python3 scripts/sync_papers_extra.py --execute
```

Download the curated 400 first:

```bash
python3 scripts/sync_papers_extra.py --execute --rank-max 400
```

Download in batches:

```bash
python3 scripts/sync_papers_extra.py --execute --rank-min 401 --limit 100
```

The script writes:

```text
papers_extra/multi-agent-triaged/manifest.csv
papers_extra/multi-agent-triaged/<rank>_<id>/paper.pdf
papers_extra/multi-agent-triaged/<rank>_<id>/source/
```

By default, arXiv rows get both `paper.pdf` and unpacked arXiv source when
available. Add `--no-source` for PDF-only acquisition, or `--no-pdf` when you
only want source.

Generated manifests and paper artifact folders under
`papers_extra/multi-agent-triaged/` are git-ignored, so bulk paper acquisition does
not bloat the repo.

## What The Script Can Resolve

The downloader is intentionally conservative. It resolves:

- arXiv IDs and arXiv URLs
- arXiv e-print source archives for rows with arXiv IDs
- OpenReview IDs in the form `OpenReview:<id>`
- direct PDF URLs already present in the field map
- existing curated PDFs under `papers/*/paper.pdf`
- existing curated source trees under `papers/*/source/`

It leaves DOI-only, paywalled, HTML-only landing pages, and non-arXiv source as
unresolved or unavailable in the manifest. Those can be handled manually or by
improving the field map with better open-access URLs.

## Agent Workflow

Give reviewing agents `papers_extra/multi-agent-triaged/manifest.csv` plus
`docs/review-rubric.md`. Each row has an `artifact_path`; for extra papers this
is a folder with `paper.pdf` and/or `source/`. Prefer `source_path` when it is
`existing`, `present`, or `downloaded`; use `pdf_path` as fallback when source
is unavailable. Review outputs should be written separately.

Only promote a paper into `papers/` after review shows it is a seed, top-100
candidate, or locally useful deep-review target.
