<div align="center">

# Multi-Agent Review Draft

This folder contains the working manuscript for a literature review on
LLM-driven multi-agent systems. The target is not an annotated bibliography.
The target is a field-shaping synthesis: selective, evidence-backed,
historically causal, and useful for deciding when multi-agent systems help or
hurt.

Central thesis:

> Multi-agent LLMs matter because they are how we scale test-time compute beyond
> one agent's context window, memory, and serial reasoning path. Their central
> promise is not that many agents are intrinsically smarter than one agent, but
> that well-coordinated agents can multiply attempts, tools, memories, branches,
> critiques, experiments, and checks, then turn that extra work into reliable
> results people can steer, audit, and use.

</div>

---

## Writing Philosophy

The manuscript should be **opinionated fact**. It should be selective,
evidence-backed, and fair, but not timid. Among the facts, there must be a
conviction that cuts through the noise and fog.

The conviction for this review is:

> Multi-agent LLMs matter because they are how we scale test-time compute beyond
> one agent's context window, memory, and serial reasoning path.

A single agent can think longer, but only up to a point. Multi-agent systems can
think wider: many attempts, tools, memories, branches, experiments, and checks.
In principle, this can scale far beyond one context window. Human society is the
proof that intelligence scales through divided labor. It is also the warning:
scale only works when communication, records, rules, tools, and verification
keep independent work from dissolving into confusion.

Write this in plain language. Speak truth directly. Do not use big, vague words
when simple words are more accurate.

The main manuscript should be an understandable story, not a ledger. It should
carry readers through the historical argument and the positive theory in prose:
what changed, what failed, what survived, and what mature systems should look
like. Use conceptual boxes and a few canonical case studies when they help the
story.

Put the derivation machinery in supplementary material or evidence logs. A
claim/evidence ledger is useful for skeptical readers because it shows which
papers support each opinion, what kind of evidence they provide, how strong that
evidence is, and what caveats remain. That table belongs in a supplement or
`section-review-evidence.md` unless a compact version directly improves the
main narrative.

---

## Read First

Use this order before editing:

1. `../../docs/best-review-article-qualities.md` - quality bar for the review.
2. `../../overview/multi-agent-field-narrative.md` - preferred narrative direction.
3. `index.qmd` - canonical manuscript assembly and section order.
4. `sections/*.qmd` - canonical manuscript prose, one top-level section per file.
5. `section-review-evidence.md` - section critique and evidence packets.
6. `../../docs/paper-reviews.md` and `../../docs/sample-50-review-audit.md` - deeper paper-level judgments when needed.

---

## Source Of Truth

For manuscript text:

<table>
  <tr>
    <td><code>index.qmd</code></td>
    <td>defines manuscript metadata and ordered section includes.</td>
  </tr>
  <tr>
    <td><code>sections/*.qmd</code></td>
    <td>is canonical prose, with one file per top-level section.</td>
  </tr>
  <tr>
    <td><code>build/index.pdf</code></td>
    <td>is rendered output only.</td>
  </tr>
  <tr>
    <td><code>index.typ</code></td>
    <td>is generated output unless explicitly being debugged.</td>
  </tr>
</table>

For factual claims:

1. Primary paper PDF/source under `../../papers/<Paper>_<id>/`
2. `../../papers/<Paper>_<id>/claims.md`
3. `../../papers/<Paper>_<id>/summary.md` and `notes.md`
4. `section-review-evidence.md`
5. Existing manuscript prose

If these conflict, trust the primary paper or local `claims.md`, then update
the manuscript and evidence log.

Section filenames are semantic. Do not rename section files only because the
manuscript order changes; reorder the include list in `index.qmd` instead.

---

## Corpus Map

<table>
  <tr>
    <td><code>../../papers/</code></td>
    <td>contains reviewed/core papers with local notes and claims.</td>
  </tr>
  <tr>
    <td><code>../../papers_extra/</code></td>
    <td>contains broad triage artifacts, not reviewed papers.</td>
  </tr>
  <tr>
    <td><code>../../docs/candidates.md</code></td>
    <td>is the curated 400-paper candidate pool.</td>
  </tr>
  <tr>
    <td><code>../../docs/field-map-1000.*</code></td>
    <td>is the broad landscape map.</td>
  </tr>
  <tr>
    <td><code>papers_extra/</code></td>
    <td>Do not treat a paper in <code>papers_extra/</code> as reviewed unless it has been promoted or separately reviewed.</td>
  </tr>
</table>

---

## Editing Rules

Before adding a claim:

- Identify the supporting citation key.
- Check whether the paper has `claims.md`.
- Mark weak evidence as weak: demo, survey, subjective evaluation,
  model-judge result, uncontrolled comparison, or speculative trend.
- Do not make broad "multi-agent systems improve X" claims without budget,
  baseline, and verifier caveats.

Prefer edits that:

- sharpen causal transitions,
- distinguish strong evidence from demos,
- reduce citation piles,
- connect mechanisms to evidence,
- clarify when multi-agent systems hurt.

Readable citation style:

- Italicize exact paper titles when a sentence treats the title as the subject:
  `*Why Do Multi-Agent LLM Systems Fail?* [@whymultiagentfail] made...`
- Put the citation immediately after the title on first or important mentions.
- For long titles, prefer normal author-year narrative citation:
  `@singleagentoutperforms offer a particularly important control...`
- Leave system, benchmark, and method names in roman text unless the sentence is
  explicitly naming the paper rather than the system.

Avoid edits that:

- turn the review into a catalogue,
- add papers only because they exist,
- overclaim from surveys,
- bury the thesis under framework names,
- introduce unsupported capability claims.

---

## Evidence Standards

A strong multi-agent claim should answer:

- What is the mechanism: decomposition, diversity, verification, debate,
  memory, tool specialization, branch-and-merge, or architecture search?
- What is the comparison baseline?
- Is budget controlled: tokens, calls, dollars, latency, tools, context?
- Is the verifier credible?
- What failure modes or caveats remain?

When tracking evidence outside the main text, label the evidence type. For
example: controlled benchmark, budget-matched comparison, ablation, scaling
analysis, artifact-level validation, model-judge evaluation, human expert
evaluation, system demonstration, theoretical argument, or negative-control
failure study. These labels help readers distinguish solid claims from
promising but unsettled ones.

---

## Current Known Gaps

- The manuscript needs a supplementary claim/evidence ledger linking major
  claims to paper-level evidence without turning the main text into
  bookkeeping.
- Figure permissions must be checked before external submission; see
  `figure-provenance.yaml`.
- `Design Principles` should remain grounded in evidence, not become generic
  advice.
- `Future Directions` should avoid becoming a citation stack.
- Section-level status should be kept current in `section-review-evidence.md`
  or a future manuscript status file.

---

## Files

<table>
  <tr>
    <td><code>index.qmd</code></td>
    <td>canonical Quarto assembly file and ordered section list.</td>
  </tr>
  <tr>
    <td><code>sections/</code></td>
    <td>semantic section files included by <code>index.qmd</code>.</td>
  </tr>
  <tr>
    <td><code>_quarto.yml</code></td>
    <td>Quarto project/render settings.</td>
  </tr>
  <tr>
    <td><code>references.bib</code></td>
    <td>local bibliography for cited papers.</td>
  </tr>
  <tr>
    <td><code>figures/</code></td>
    <td>original synthesis figures and selected primary-paper figures used by the manuscript.</td>
  </tr>
  <tr>
    <td><code>figure-provenance.yaml</code></td>
    <td>provenance and reuse status for manuscript figure assets.</td>
  </tr>
  <tr>
    <td><code>section-review-evidence.md</code></td>
    <td>section-level critique, evidence packets, and planned manuscript changes.</td>
  </tr>
  <tr>
    <td><code>build/index.pdf</code></td>
    <td>rendered PDF.</td>
  </tr>
</table>

---

## Render

From the repository root, if Quarto is installed globally:

```bash
quarto render manuscript/multi-agent-review-draft/index.qmd --to typst
```

For a TypeScript-app-style watch loop that rebuilds `build/index.pdf` whenever
the manuscript sources or figure files change:

```bash
npm run pdf:dev
```

In this workspace, Quarto was extracted locally because the Homebrew cask
required sudo:

```bash
.cache/quarto-local/pkg/quarto-core.pkg/Payload/bin/quarto render manuscript/multi-agent-review-draft/index.qmd --to typst
```

The manuscript includes original synthesis figures and selected primary-paper
figures. Reproduced primary-paper panels should be permission-checked against
publisher, arXiv, or license terms before external submission.
