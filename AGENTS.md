# Working in this repository

This repository holds journal club research, presentations, and the shared agent
tooling used to create them. Prefer useful, reviewable materials and small changes
over elaborate infrastructure.

## Organization

- `journal-clubs/YYYY-MM-DD-short-topic/`: one directory per session. If the date
  is unknown, use `undated-short-topic` until it is scheduled.
- `tools/`: reusable scripts and agent tooling. Keep session-specific code with
  its session; promote it here only when reuse is useful.
- Within a session, start with a `README.md` recording the topic, session date
  (if known), selected papers, and links to the materials. Add research notes,
  slide sources, figures, and final deliverables as needed, not as empty scaffolding.

## Research and discussion

- Read the relevant papers before describing their findings. Prefer primary
  sources and verify bibliographic details, links, and substantive claims.
- Cite sources near the claims they support using stable URLs or DOIs. Record
  page, section, table, or figure references for specific results when available.
- Never invent citations, quotations, results, or missing details. State access
  limitations and distinguish full-text review from abstract-only review.
- Separate authors' claims, reported evidence, and your own interpretation.
  Preserve uncertainty; do not present association as causation.
- Cover the research question, methods, key results, strengths, limitations, and
  discussion questions. Include relevant sample sizes, effect sizes, and
  uncertainty rather than relying only on statistical significance.
- Adapt depth and terminology to the audience. Use available context and reasonable
  defaults; ask only when missing information materially affects the work.

## Materials and tooling

- Keep editable source files alongside final slides or documents. Use relative
  links and descriptive filenames; make the current deliverable easy to find.
- Make slides readable and focused. Attribute figures and data, and label adapted
  or illustrative graphics clearly. Put supporting detail in notes or appendices.
- Visually inspect generated slides, documents, and PDFs before delivery. Check
  citations, numerical consistency, links, and any analysis that supports conclusions.
  State any checks that could not be completed.
- Keep downloaded papers only when redistribution is permitted; otherwise record
  a source link. Do not commit credentials, private participant information, caches,
  or temporary build artifacts.
- Use existing tools and relevant available skills before adding dependencies.
  Document commands and dependencies for reusable scripts. Add tests where they
  protect meaningful behavior, not for prose or simple scaffolding.
- Preserve existing work. Avoid unrelated edits and do not publish or send
  materials externally unless requested.
