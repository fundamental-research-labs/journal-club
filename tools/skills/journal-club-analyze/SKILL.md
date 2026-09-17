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
Check the originals directory and acquisition manifest before accessing sources
online. Reopen the retained primary originals for pivotal claims and ambiguous
measurements, using the exact versions supporting the reading notes. Extract or
render local PDFs as needed; “reopen primary sources” does not mean search the web.

Reuse the research stage's documented cutoff and freshness checks. An analysis
request does not by itself require another discovery or latest-version search.
Use targeted online access when a needed original is missing, unreadable, or
incomplete, a material question cannot be resolved locally, or a freshness update
is requested or required by the session date. For missing originals, consult the
acquisition record and open its canonical/versioned URL before broad search;
preserve recorded retention restrictions. Record the specific gap and any new
evidence without silently replacing the version already reviewed.

If research is absent, request or perform research according to the authorized
scope; do not create an authoritative thesis from titles or abstracts alone.

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

Write `analysis/thesis.md` with the clarity and explanatory care of excellent science
writing. Assume a curious reader with the session's stated background, not a
specialist in every subfield. Build an evidence-backed argument the reader can
understand on the first pass: what the problem is, how the approaches work, what
the experiments show, and what remains unknown. Preserve scholarly rigor without
using conference-paper prose as the style target. Do not invent experiments,
contributions, anecdotes, or scenes to make the writing more engaging.

Start with a concrete problem or a source-backed example before introducing an
abstract category. Explain mechanisms through actors and actions: what the agent
changes, how it chooses a change, and what happens next. Prefer familiar words and
active verbs to noun clusters and compressed labels. For example, replace
“positive persistence controls” with “agents did better when they kept what they
had learned than when their memory was reset.” Introduce technical terms after
explaining the idea, and retain them when they add precision. Use analogies only
when they clarify a mechanism, and make their limits clear.

Give each paragraph a main job and each sentence a manageable amount of new
information. Vary sentence length naturally; avoid both dense qualification chains
and a choppy series of slogans. Explain why a result matters before adding the next
paper or number. Make uncertainty concrete—what was not tested, what comparison is
missing, or which other explanation fits—instead of relying on vague hedges.

Use connected paragraphs with informative topic sentences, concrete subjects, and
explicit transitions. Define unfamiliar terms when first needed. Organize related
work around conceptual relationships, assumptions, and disagreements; explain what
comparisons establish rather than listing papers in sequence. Use a few descriptive
headings when helpful, without imposing a fixed template or length. Avoid a briefing
format built from a bold thesis slogan, numbered argument cards, chronology tables,
confidence labels, or competing-thesis matrices.

Integrate the strongest competing explanation, limitations, and practical or
research implications into the argument. Distinguish reported findings from your
interpretation through attribution and calibrated prose, rather than separate
“established/emerging/interpretive” bins. Keep decisive numbers and qualifications
that affect their meaning; leave exhaustive audit detail in the evidence records.
Cite primary sources near the claims, with result locators where relevant. Keep
claim-ID traceability in `claims.md` or a compact supporting map, so the thesis can
be read independently of internal workflow labels.

Keep source-access audits and readiness status in the workflow record. The thesis
should explain the field to a reader, not narrate the analysis process.
Presentation narrative, slide sequencing, visuals, and discussion facilitation
belong to the presentation skill. Analysis hands off the thesis, claim ledger,
and unresolved qualifications; do not create a storyline or presentation outline.

Create `analysis/claims.md` using the shared claim format. Label analyst inference,
opinion, and prediction explicitly, but still show the evidence and assumptions
behind them. Avoid false balance: give alternatives attention proportional to their
plausibility and evidence. Do not hide uncertainty to make the story cleaner.

## Iterate and finish

Send missing evidence, conflicting results, or uncertain provenance back to research
with a precise question and an explanation of which conclusion it could change.
Revise affected claims and the thesis after the response. Retain rejected theses
briefly when their rejection explains an important tradeoff; do not accumulate a
transcript of every draft.

Before finishing, read the thesis as continuous prose from the intended reader's
perspective. Can they explain the central claim and how the main mechanisms work
without the claim ledger or presentation outline? Revise sentences that need a
second reading, abstract subjects, unexplained jargon, abrupt transitions, and
paragraphs that merely enumerate sources. Then check the rewrite against the
evidence: simpler language must preserve populations, comparators, units, causal
limits, and the distinction between a reported result and your interpretation.

The analysis is ready when the central argument is traceable, serious objections
are addressed, confidence matches the evidence, and remaining gaps are either
resolved or explicitly narrow the conclusion. Update workflow state. Hand off to
presentation only within the requested scope.
