# Complete Literature import

Copied all 5,463 tracked files from [gyyang/Literature](https://github.com/gyyang/Literature) at revision `faf6d2c7b982e5dfcedda018d0a0cca2d40229e2` into [`literature/`](literature/README.md). The source main branch still pointed to this revision when checked for this import on September 16, 2026.

The original directory structure, file contents, executable permissions, `.gitattributes`, and `.gitignore` files are preserved. Git LFS files contain downloaded content, not pointer text. The complete per-file inventory, sizes, source Git object IDs, and SHA-256 hashes are in [full-import-manifest.json](full-import-manifest.json).

This includes the 27-page review PDF and editable Quarto manuscript, bibliography and figures, all 98 paper folders, slides, literature graph webapp, corpus scripts, field maps, review audits, manuscript plans, and industry references. This is a working-tree copy, not a transfer of Git history. The source repository remains unchanged. Untracked caches, installed dependencies, temporary builds, and `.git/` are not copied. The review PDF was tracked in the source and is included.

The earlier selective import remains beside `literature/` for continuity; use `literature/` for future work on the complete corpus and tooling. May 4 is the source repository's creation date, not a claim that every imported file existed that day. The review PDF itself is dated May 8, 2026.

## Running the tools

From the journal-club repository root, first change to the imported workspace. Commands in the original README that say “repository root” mean this directory:

```sh
cd journal-clubs/2026-05-04-multi-agent-systems/literature
```

Review manuscript: install Quarto with its Typst support and use Node.js/npm for the watch script. The original README's `.cache/quarto-local/...` installation was machine-local and is not included.

```sh
npm run pdf:build
npm run pdf:dev
```

These are alternatives: the first renders once; the second watches for changes. The existing PDF can be read without installing Quarto.

Paper acquisition and corpus checks use Bash, Python 3, and the command-line download/archive utilities used by the original scripts. Consult acquisition help before downloading:

```sh
bash scripts/add_arxiv_paper.sh --help
bash scripts/audit_papers.sh
python3 scripts/build_webapp_data.py
```

The graph data builder writes `webapp/src/data/graph-data.json`. The field-map and corpus-sync scripts remain in `scripts/`; their commands and options are documented in the original README and script help. Acquisition and field-map generation can make network requests and modify the corpus.

The webapp uses Node.js and pnpm 10.11.0, as specified in its package manifest:

```sh
cd webapp
pnpm install --frozen-lockfile
pnpm dev
# Or type-check and build:
pnpm build
```

Git LFS is needed when committing or checking out the imported binary assets. The imported attributes retain the source's LFS rules. Nothing has been committed, pushed, or published by this import.

## Validation

- Every copied file was checked against its source Git blob, or its LFS SHA-256 object ID, and against the destination bytes. Executable modes were checked.
- Python, Bash, and Node tooling passed syntax checks.
- The webapp passed TypeScript checks and a production build in the temporary source checkout using its frozen lockfile. Vite reported a bundle-size warning; dependencies and build output were not imported.
- The existing review PDF was readable by Poppler and reported 27 pages. Pages 1, 10, and 27 were rendered and visually inspected; no obvious clipping or overlap was observed on those pages. This was a spot check, not a complete page-by-page review.
- Quarto was unavailable locally, so the manuscript was not rebuilt. The existing tracked PDF was preserved byte for byte.

This import preserves the original research and its existing limitations; it is not a new claim-level review or a publication-rights audit. The earlier session import's CAID discrepancy remains documented in [IMPORT.md](IMPORT.md).
