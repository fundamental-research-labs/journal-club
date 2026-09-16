# Paper Folder Contract

The `papers/` directory is the maintained local corpus for papers that are active seeds or selected for the final Top 100 list. It is not the broad candidate pool. Broad candidates stay in `docs/candidates.md` until promoted.

## Inclusion Rule

Create a folder in `papers/` when a paper is one of:

- An active seed in `docs/seeds.md`
- A selected entry in `docs/top100.md`
- A paper reviewed deeply enough that local notes, claims, or figures are useful

Do not create a folder merely because a paper appears in the candidate pool.

## Directory Naming

Use:

```text
papers/<ShortSlug>_<stable-id>/
```

For arXiv papers, use the arXiv ID as the stable ID:

```text
papers/AutoGen_2308.08155/
```

For non-arXiv papers, use a compact stable key such as `WooldridgeJennings_1995` or `AlphaStar_Nature_2019`.

## Required Files

Every paper folder should have:

```text
metadata.yaml   # Machine-readable bibliographic and curation metadata
summary.md      # Human-readable structured summary
notes.md        # Working notes: why it matters, when to cite, key terms
claims.md       # Main claims, evidence, caveats, and source pointers
paper.pdf       # Local PDF when legally and practically available
```

`source/` is optional. Keep source when you need LaTeX, figures, tables, appendix details, or reproducible extraction. Do not require source for every Top 100 entry.

## Metadata Shape

Use this shape for `metadata.yaml`:

```yaml
id: AutoGen_2308.08155
title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
authors:
  - Author One
  - Author Two
arxiv: "2308.08155"
date: "2023-08"
venue: Preprint
status: seed
topics:
  - multi-agent frameworks
  - agent communication
artifacts:
  pdf: paper.pdf
  source: source/
summary: "One-sentence reason this paper belongs in the corpus."
```

For non-arXiv papers, replace `arxiv` with `doi`, `url`, or another stable identifier.

Use `status` values consistently:

- `seed`: active seed for expansion
- `top100`: selected for the final list
- `reviewed`: locally reviewed but not necessarily selected
- `candidate`: unusual, only when a folder exists before promotion

## Summary Files

Keep summaries concise but useful. Prefer these headings:

```markdown
# Paper Title

**Authors:** ...
**arXiv/DOI:** ...
**Venue:** ...
**Date:** ...

## Problem
## Method
## Key Findings
## Tags
## Connections
```

`notes.md` and `claims.md` can start as stubs, but they should make the review state explicit with `TODO` markers rather than implying the paper has already been fully read.

## Scripts

Use the scripts from the repository root:

```bash
scripts/add_arxiv_paper.sh 2308.08155 AutoGen "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
scripts/add_arxiv_paper.sh --no-source 2308.08155 AutoGen "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
scripts/add_arxiv_paper.sh --refresh-metadata --no-source 2308.08155 AutoGen
scripts/sync_seed_papers.sh
scripts/sync_seed_papers.sh --execute --limit 10
scripts/audit_papers.sh
```

`scripts/add_arxiv_paper.sh` fetches arXiv API metadata politely: it serializes metadata requests with a local lock, waits at least 3 seconds between API calls, caches XML responses under `.cache/arxiv/`, and backs off on `429`/`503` responses. Use `--no-metadata` when you only want local stubs and downloads. Use `--refresh-metadata` to rewrite `metadata.yaml` from the cache or API, and add `--refresh-cache` only when you need to force a new arXiv API request.

`scripts/sync_seed_papers.sh` reads `docs/seeds.md` and finds missing arXiv-backed seed folders. It defaults to dry-run, `--no-source`, and `--no-metadata` so large seed-set syncs do not hammer arXiv's API.

The root `add_paper.sh` wrapper is kept for compatibility and forwards to `scripts/add_arxiv_paper.sh`.
