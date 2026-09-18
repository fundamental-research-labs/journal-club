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

Read the [prominent-citation coverage check](../journal-club-research/references/prominent-citations.md)
and the session's per-source lists and aggregate. Before choosing anchors, review
recurring substantive citations, each anchor's direct predecessors and decisive
baselines, and the strongest challenges. Existing corpus coverage does not establish
essay coverage. If the lists are missing, build them for consequential sources within
scope and record remaining gaps; do not silently equate missing edges with no relevant
prior work. Read cited originals before adding substantive findings.

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

Before drafting, sketch the argument in a few sentences: the central claim, the
questions needed to establish it, and how each answer creates the next question.
Use this as a working outline, not a required deliverable or a slide sequence.
Choose anchor examples that deserve explanation and comparisons that could change
the conclusion. A mechanism taxonomy can support the argument, but should not
silently become its structure. Introduce another approach when it resolves a
problem, exposes a tradeoff, or challenges what the reader has just learned.

Write `analysis/thesis.md` with the clarity and explanatory care of excellent science
writing. Assume a curious reader with the session's stated background, not a
specialist in every subfield. Build an evidence-backed argument the reader can
understand on the first pass: what the problem is, how the approaches work, what
the experiments show, and what remains unknown. Preserve scholarly rigor without
using conference-paper prose as the style target. Do not invent experiments,
contributions, anecdotes, or scenes to make the writing more engaging.

Write the thesis as a standalone essay about the subject. Use the session context
to calibrate depth, but do not refer to “this journal club,” the audience's planned
discussion, or the act of preparing the materials. Introduce definitions through
their explanatory value, not as conventions chosen for an event. Let the opening
establish a question worth understanding and the ending develop what the evidence
means. A reader arriving without the README should have everything needed to follow
the argument. Keep preparation dates, handoff notes, and review bookkeeping in the
supporting records; include dates in the essay when they matter to the argument.

Give the reader a reason to care before asking them to learn a method. Open the
essay with the practical or intellectual problem and what resolving it would make
possible. At section openings, develop the unresolved question, consequence, or
tension left by the preceding reasoning. Establish why it matters before introducing
the paper that helps answer it. A concrete example can supply that motivation, but
a paper name followed by its mechanism is not itself a motivating opening. Avoid
generic importance claims and mechanical recaps; the connection should advance the
argument. For example, after explaining how an agent retains a procedure, motivate
the next section by asking whether learning it adds value beyond supplying good
instructions beforehand, then introduce the comparison that tests this.

Explain mechanisms through actors and actions: what the agent
changes, how it chooses a change, and what happens next. Prefer familiar words and
active verbs to noun clusters and compressed labels. For example, replace
“positive persistence controls” with “agents did better when they kept what they
had learned than when their memory was reset.” Introduce technical terms after
explaining the idea, and retain them when they add precision. Use analogies only
when they clarify a mechanism, and make their limits clear.

Develop consequential examples long enough for the reader to follow the decisions:
what happened, what the system retained or changed, why that choice could help,
and what evidence tests the explanation. Use documented details; label hypothetical
examples explicitly. Avoid compressing every method into a name, a feature, and a
caveat. An additional source earns space by changing the reasoning, not merely by
belonging to the same category. Keep representative positive evidence and the
strongest challenges even when they complicate the preferred argument.

Give each paragraph a main job and each sentence a manageable amount of new
information. Vary sentence length naturally; avoid both dense qualification chains
and a choppy series of slogans. Explain why a result matters before adding the next
paper or number. Make uncertainty concrete—what was not tested, what comparison is
missing, or which other explanation fits—instead of relying on vague hedges.

Make each sentence contribute a claim, mechanism, evidence, necessary connection,
or consequence. A sentence that merely announces importance, complexity, or an
upcoming example has not supplied the explanation. For example, replace “The
comparison becomes more interesting when the harness is reused” with “Reusing a
harness spreads its development cost across later tasks.” When recommending a
check, name what is compared and what outcome would change the conclusion; “memory
needs its own standards” leaves the reader to supply the analysis. Use only supported
details, and distinguish proposed tests from reported experiments. A generalization
can be meaningful without a number or citation in every sentence.

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

Check the thesis against the research coverage audit, not just the reading shortlist.
Assess breadth in the reviewed evidence base, not by a citation quota in the essay.
The coverage audit should show which important approaches and counterarguments
were considered, including sources retained only in supporting records and why.
A concise thesis can rest on broad research. Remove repetitive examples, not
consequential counterevidence; reopen research when a substantive gap could change
the conclusion. Integrate sources where they do argumentative work, without
padding or counting companion artifacts as independent evidence.
Reconcile prominent citations against the final prose after every material rewrite
or condensation. Record where consequential works do explanatory work, or a specific
reason and representative source for omitting them. Generic “additional comparator”
or shortlist rank is insufficient. Check that the reader can explain what each
anchor inherits, what it adds, and what its main comparison establishes. Keep these
checks in supporting records rather than turning the essay into a citation inventory.
If no thesis-driven audit exists, queue one; perform it when authorized by the request.

Send missing evidence, conflicting results, or uncertain provenance back to research
with a precise question and an explanation of which conclusion it could change.
Revise affected claims and the thesis after the response. Retain rejected theses
briefly when their rejection explains an important tradeoff; do not accumulate a
transcript of every draft.

Before finishing, read the section openings together, temporarily setting aside
paper names and citations. Can the reader explain what question each section takes
up, why its answer matters, and how the preceding section made it worth asking?
Repair missing motivation in the prose, not just in the heading or a transition
word. Then test the full structure: if several paragraphs can trade places without
affecting the reasoning, check whether they are a catalog that needs synthesis or pruning.
Do not force a linear dependency where a comparison genuinely requires parallel
cases. Consolidate recurring limitations around the conclusion they constrain;
keep source-specific qualifications beside the results whose meaning they change.

Audit sentences in context, especially paragraph openings, transitions, and endings.
If deleting one loses no information or necessary connection, remove it. If its
point is useful but could fit an unrelated topic with noun substitutions, specify
the actor, mechanism, comparison, condition, or consequence that makes it apply
here. Inspect repeated conclusions: retain a recap when it enables the next inference,
and otherwise cut it. Do not repair empty prose by adding jargon or unsupported
detail, or remove transitions that carry a real logical relationship. When asked
how widespread a prose issue is, review the entire essay and report an explicit
counting unit with representative before/after examples; keep the audit outside
the thesis and distinguish empty sentences from useful but underspecified ones.

Read the thesis as continuous prose from the intended reader's
perspective. Can they explain the central claim and how the main mechanisms work
without the claim ledger or presentation outline? Would the essay still read
naturally if shared on its own with someone unaware of the journal club? Revise
event-specific framing and process commentary along with sentences that need a
second reading, abstract subjects, unexplained jargon, abrupt transitions, and
paragraphs that merely enumerate sources. Then check the rewrite against the
evidence: simpler language must preserve populations, comparators, units, causal
limits, and the distinction between a reported result and your interpretation.

The analysis is ready when the central argument is traceable, serious objections
are addressed, confidence matches the evidence, and remaining gaps are either
resolved or explicitly narrow the conclusion. Update workflow state. Hand off to
presentation only within the requested scope.
