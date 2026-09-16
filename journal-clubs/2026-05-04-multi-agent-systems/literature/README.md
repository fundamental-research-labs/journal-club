<div align="center">

# Multi-Agent Literature

This repository tracks papers, notes, reviews, and manuscript work for a<br>
high-quality literature review on LLM-driven multi-agent systems.

The current review thesis is:

> Multi-agent LLMs matter because they are how we scale test-time compute beyond
> one agent's context window, memory, and serial reasoning path. They are useful
> when separately stateful attempts are coordinated into verifiable artifacts
> and reliable work.

</div>

---

## Writing Philosophy

The review should be **opinionated fact**. It should be fair to the evidence,
but it should not hide behind neutral cataloguing. Among the facts, there must
be a conviction that cuts through the noise and fog.

The central conviction is plain:

> Multi-agent LLMs matter because they are how we scale test-time compute beyond
> one agent's context window, memory, and serial reasoning path.

A single agent can think longer, but only up to a point. Multi-agent systems can
think wider: many attempts, tools, memories, branches, experiments, and checks.
In principle, this can scale far beyond one context window. Human society is the
proof that intelligence scales through divided labor. It is also the warning:
scale only works when communication, records, rules, tools, and verification
keep independent work from dissolving into confusion.

Prefer plain language. Do not use big words when simple words tell the truth
more directly.

Separate drafting guidance from manuscript prose. Agents may receive reasoning
about why a paragraph should take a certain shape, but the manuscript should
not repeat that reasoning as meta-commentary. Do not write explanatory caveats
about the authors' intent, such as "By X, this review does not mean Y." Avoid
front-loading definitions unless a term is genuinely ambiguous and the
definition is needed at that moment. Prefer prose that makes the meaning clear
through use. Avoid editorial asides, process notes, and defensive framing. Put
the claim itself in the text; keep the rationale for agents, comments, review
notes, or evidence ledgers.

Keep the main text readable as a story. It should explain the review's
judgment in a way that an expert can follow without stopping at every paragraph
to inspect the bookkeeping. Use prose, short conceptual boxes, and canonical
case studies for the main argument.

Use supplementary tables, evidence logs, and review notes for the audit trail:
claim/evidence ledgers, evidence-type labels, strength judgments, caveats, and
paper-by-paper derivations. Skeptical readers should be able to see how the
review reached its opinions, but that machinery should not interrupt the main
text unless it sharpens the story.

---

## Main Entry Points

<table>
  <tr>
    <td><code>manuscript/multi-agent-review-draft/</code></td>
    <td>working Quarto manuscript.</td>
  </tr>
  <tr>
    <td><code>manuscript/multi-agent-review-draft/README.md</code></td>
    <td>agent-facing manuscript operating guide.</td>
  </tr>
  <tr>
    <td><code>overview/multi-agent-field-narrative.md</code></td>
    <td>compact narrative spine.</td>
  </tr>
  <tr>
    <td><code>docs/best-review-article-qualities.md</code></td>
    <td>quality standard for the review.</td>
  </tr>
  <tr>
    <td><code>docs/review-rubric.md</code></td>
    <td>rubric for paper-level review.</td>
  </tr>
  <tr>
    <td><code>executive-summary.md</code></td>
    <td>short journal-club synthesis of core recent papers.</td>
  </tr>
</table>

---

## Repository Map

```text
papers/              Reviewed/core paper folders with notes, claims, PDFs, and source when useful
papers_extra/        Generated broad-triage PDFs/source; not reviewed by default
docs/                Rubrics, field maps, candidate lists, audits, and paper reviews
overview/            High-level narrative drafts
manuscript/          Full review manuscript projects
slides/              Presentation materials
webapp/              React + TypeScript literature graph explorer
scripts/             Corpus sync, field-map, and audit scripts
```

---

## Corpus Contracts

`papers/` is the maintained reviewed corpus. Each paper folder should contain:

```text
metadata.yaml
summary.md
notes.md
claims.md
paper.pdf
```

Use `papers/` for active seeds, top-100 selections, and papers reviewed deeply
enough that local notes and claims are useful. See `papers/README.md` for the
full contract.

`papers_extra/` is the broad acquisition and triage area. It is useful when
agents need PDFs or arXiv source for candidate inspection, but papers there
should not be treated as reviewed. See `docs/papers-extra.md` and
`papers_extra/README.md`.

---

## Field Maps And Reviews

<table>
  <tr>
    <td><code>docs/candidates.md</code></td>
    <td>curated 400-paper candidate universe.</td>
  </tr>
  <tr>
    <td><code>docs/field-map-1000.md</code>, <code>.csv</code>, <code>.yaml</code></td>
    <td>broader 1000-paper landscape map.</td>
  </tr>
  <tr>
    <td><code>docs/paper-reviews.md</code></td>
    <td>detailed reviews for selected core papers.</td>
  </tr>
  <tr>
    <td><code>docs/sample-50-review-audit.md</code></td>
    <td>compact audit of 50 papers.</td>
  </tr>
  <tr>
    <td><code>docs/field-map-50-subagent-review-audit.md</code></td>
    <td>audit of 50 field-map papers.</td>
  </tr>
  <tr>
    <td><code>docs/review-stability.md</code></td>
    <td>rating stability checks for paper reviews.</td>
  </tr>
  <tr>
    <td><code>docs/taxonomy.yaml</code></td>
    <td>controlled taxonomy used by the webapp tree view.</td>
  </tr>
</table>

---

## Manuscript Workflow

Before editing the manuscript, read:

1. `docs/best-review-article-qualities.md`
2. `overview/multi-agent-field-narrative.md`
3. `manuscript/multi-agent-review-draft/README.md`
4. `manuscript/multi-agent-review-draft/index.qmd`
5. `manuscript/multi-agent-review-draft/sections/*.qmd`
6. `manuscript/multi-agent-review-draft/section-review-evidence.md`

Render the current manuscript from the repository root:

```bash
quarto render manuscript/multi-agent-review-draft/index.qmd --to typst
```

For a TypeScript-app-style edit loop that rebuilds the PDF whenever manuscript
sources change:

```bash
npm run pdf:dev
```

The output is `manuscript/multi-agent-review-draft/build/index.pdf`.

If global Quarto is unavailable in this workspace, use the local command
documented in `manuscript/multi-agent-review-draft/README.md`.

---

## Useful Scripts

```bash
scripts/add_arxiv_paper.sh 2308.08155 AutoGen "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
scripts/sync_seed_papers.sh
scripts/sync_papers_extra.py --execute --rank-max 400
scripts/audit_papers.sh
python3 scripts/build_field_map_1000.py
scripts/build_webapp_data.py
```

Most acquisition scripts default to dry-run or conservative behavior. Check the
script help or the relevant README before bulk downloads.
