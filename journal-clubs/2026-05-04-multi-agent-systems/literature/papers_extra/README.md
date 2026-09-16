# Extra Papers Corpus

`papers_extra/` is for broad paper-artifact acquisition from field maps and
candidate lists. It is not the reviewed corpus.

Use `papers/` for active seeds, final top-100 selections, and papers with
reviewed notes or claims. Use `papers_extra/` when agents need local PDFs or
arXiv source trees for triage before promotion.

The generated files are ignored by git:

```text
papers_extra/multi-agent-triaged/manifest.csv
papers_extra/multi-agent-triaged/<rank>_<id>/paper.pdf
papers_extra/multi-agent-triaged/<rank>_<id>/source/
```

Populate it from the repo root:

```bash
python3 scripts/sync_papers_extra.py --execute --rank-max 400
```

See `docs/papers-extra.md` for the full workflow.
