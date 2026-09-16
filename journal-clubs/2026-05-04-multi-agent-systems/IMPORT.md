# Import record

Source: [gyyang/Literature at `faf6d2c7b982`](https://github.com/gyyang/Literature/blob/faf6d2c7b982e5dfcedda018d0a0cca2d40229e2/README.md). Imported September 16, 2026. Directory date uses repository creation, May 4, 2026, and does not assert a meeting date.

## Scope

Copied the HTML presentation, five Marp sources, executive summary, 16 referenced figures, and metadata/summary/notes/claims for the 11 indexed papers. Git LFS figures were downloaded and copied as actual PNG files. Source and destination hashes are recorded in [the manifest](import-manifest.json).

The source repository remains unchanged. Full paper PDFs, paper source trees, unused figures, manuscript, corpus tooling, triage records, and literature explorer were excluded. Acquisition/audit scripts assume a different corpus layout and were not needed to present this session.

## Changes and limitations

Paper metadata PDF/source paths now point to arXiv URLs because those files were not copied. All other imported files preserve source bytes. Figure credits and session navigation were added separately.

The executive summary reports a CAID PaperBench gain of **26.7%**, while the CAID mini-deck and local summary report **26.3 percentage points** (10.4% to 36.7%). This discrepancy is preserved and flagged rather than silently changing the archived material without a full primary-source review.

This is an archival migration, not a new literature review: research claims, publication status, and current paper versions have not been revalidated. Presentation image paths, PNG payloads, paper-note completeness, and manifest hashes are checked locally. Browser visual inspection could not be completed because the Browser runtime failed during initialization (`Cannot redefine property: process`).
