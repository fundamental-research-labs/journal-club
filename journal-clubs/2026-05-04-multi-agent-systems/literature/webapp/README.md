# Literature Webapp

React + TypeScript app for navigating the local multi-agent paper corpus.

Regenerate graph data after adding paper metadata or bibliography files:

```bash
scripts/build_webapp_data.py
```

Run the app locally:

```bash
cd webapp
pnpm install
pnpm dev
```

Production build:

```bash
pnpm build
```

The app uses Vite, React, TypeScript, Tailwind CSS, and Zustand. Generated graph
data lives at `src/data/graph-data.json`.

The tree y-axis is driven by the controlled taxonomy in `../docs/taxonomy.yaml`.
The data builder prefers explicit `classification` metadata, then curated
`docs/seeds.md` sub-areas, then topic/title inference as a visible fallback.
