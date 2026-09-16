---
name: journal-club-analyze
description: Turn journal club research into defensible theses, trends, interpretations, and discussion questions. Use to synthesize evidence, challenge an argument, or revise analysis after new research or presentation feedback.
---

# Journal Club Analyze

Develop a point of view that earns its conclusions. The deliverable is an argument
about the field: what changed, why it matters, where it breaks, and what to do or
investigate next. A catalog of paper summaries is insufficient.

Read [the shared workflow](../journal-club-research/references/workflow.md), the
session README, research landscape, source register, and relevant reading notes.
Reopen primary sources for pivotal claims and ambiguous measurements. If research
is absent, request or perform research according to the authorized scope; do not
create an authoritative thesis from titles or abstracts alone.

## Build and challenge interpretations

Group evidence by research question, mechanism, and tradeoff. Compare like with like:
check task, dataset, split, metric definition, baseline, sample size, model version,
and resource budget before comparing results. Do not create pooled numbers or
rankings from incompatible evaluations. Identify shared datasets, authors, and
artifacts so repeated reporting is not mistaken for independent confirmation.

Develop a few materially different candidate theses when the evidence permits.
For each, consider supporting evidence, the strongest counterexample, alternative
explanations, applicability limits, and what would change your mind. Prefer the
thesis with the strongest explanatory value and consequences, not the boldest
wording. If the evidence cannot distinguish candidates, make that tension the
argument and identify the discriminating experiment.

A trend needs dated observations and an explanation of what is changing. Separate
adoption or attention from capability, benchmark progress from transfer, and
correlation from mechanism. Treat a single new release as an emerging signal unless
additional evidence supports a broader direction.

## Write the analysis

Create `analysis/thesis.md` with:
- A concise central thesis, its scope, and why the audience should care now.
- Supporting arguments arranged as a narrative, each linked to claim IDs.
- Established findings, emerging trends, and your interpretations clearly separated.
- Your reasoned position on consequential tradeoffs, with confidence and limits.
- The strongest competing explanation and evidence against your preferred view.
- Practical implications, unresolved questions, and tests that could settle them.
- Discussion questions that invite a decision, prediction, or disagreement and
  name the evidence that would inform it.

Create `analysis/claims.md` using the shared claim format. Label analyst inference,
opinion, and prediction explicitly, but still show the evidence and assumptions
behind them. Avoid false balance: give alternatives attention proportional to their
plausibility and evidence. Do not hide uncertainty to make the story cleaner.

Create `analysis/storyline.md` as the presentation handoff: audience and duration,
opening question, minimal conceptual background, argument sequence, decisive
results, counterargument, synthesis, and discussion. Suggest visual explanations
and trace each major beat to claim IDs. Keep paper-specific detail in supporting
material unless needed to understand the argument.

## Iterate and finish

Send missing evidence, conflicting results, or uncertain provenance back to research
with a precise question and an explanation of which conclusion it could change.
Revise affected claims and the storyline after the response. Retain rejected theses
briefly when their rejection explains an important tradeoff; do not accumulate a
transcript of every draft.

The analysis is ready when the central argument is traceable, serious objections
are addressed, confidence matches the evidence, and remaining gaps are either
resolved or explicitly narrow the conclusion. Update workflow state. Hand off to
presentation only within the requested scope.
