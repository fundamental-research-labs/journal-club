# Shared journal club workflow

This contract connects research, analysis, and presentation. Read it for any of the
three stages. Reuse existing session materials; adapt existing filenames rather
than duplicating an established corpus. Keep the three skills together when moving
or installing them because analysis and presentation reference this file.

## Scope and iteration

A request for one stage authorizes that stage and its necessary supporting work;
it does not automatically request a full deck. An end-to-end journal club request
runs research → analysis → presentation and targeted returns to earlier stages.
Do not ask for approval at routine handoffs already covered by the request.

Use `journal-clubs/YYYY-MM-DD-short-topic/`, or `undated-short-topic/` when no session
date is known. Start with its README: topic, audience, duration, date, preparation
cutoff, scope assumptions, selected sources, and relative links to current materials.
Create files as they acquire useful content, not as empty scaffolding.

Keep `workflow.md` in the session with:
- Current stage, revision date, inputs used, and readiness for the next stage.
- A short work queue: ID, requesting stage, affected source/claim/slide IDs, precise
  question, why it matters, owner stage, acceptance criterion, and status.
- Material revisions: what changed, why, and downstream artifacts requiring updates.
- Remaining limitations and completion checks.

Stable IDs provide the chain: `S001` source → `C001` claim → slide number/title.
Never recycle an ID after removing an item. Slides may be renumbered; refresh their
mapping in the storyboard. Keep URLs and result locators alongside IDs so readers
can inspect the underlying evidence without knowing the workflow.

On a return to an earlier stage, do a targeted pass, update the affected evidence,
and propagate substantive changes through claims, storyline, storyboard, and deck.
Mark dependent artifacts stale until updated. Reopen broad discovery only when the
scope changes or the gap reveals a missed approach.

Stop iterating when the requested artifacts meet their stage checks and no unresolved
gap would materially alter the central conclusion. Narrow unsupported claims instead
of searching forever. If two consecutive targeted passes add no decision-relevant
evidence, record the limitation and proceed with qualified claims or report a blocked
prerequisite. Respect explicit user budgets; do not imply completion when a required
artifact or verification remains unavailable.

## Source records

`research/sources.md` is a compact index. Each entry includes source ID, title,
authors/organization, stable URL/DOI, source type, publication and version dates,
access date, access depth, evidence family, and a relative link to reading notes.
Distinguish preprints, peer-reviewed work, code, blogs, threads, talks, and demos.
Track relevant release/commit versions for changing artifacts. Mark unknown fields.

`research/notes/S001.md` records:
- Research question and why the source matters to this topic.
- Methods, population/task/data, evaluation setup, comparators, and resource budget.
- Specific findings with numbers, units, sample sizes, uncertainty, and exact page,
  section, figure, table, timestamp, or code locators as applicable.
- Authors' claims, reported evidence, and analyst interpretation in separate prose.
- Strengths, limitations, confounds, independence, and reproducibility information.
- Access limitations, contradictory evidence, and candidate figures or datasets.

Use a concise record for an opinion or proposal; do not fabricate experimental
fields that do not apply. Index inaccessible discoveries but never treat them as
reviewed support. Avoid copying long copyrighted passages.

## Claim records

`analysis/claims.md` records for each claim:
- Stable ID and precise wording, including the applicable conditions and population.
- Type: reported finding, synthesis/inference, opinion, or prediction.
- Supporting source IDs, URLs, and exact result locators.
- Contradicting evidence and the strongest alternative explanation.
- Comparability caveats and whether sources are independent.
- Confidence (high/moderate/low) with a short evidence-based rationale; confidence
  is an analytic judgment, not a statistical probability.
- What would falsify, narrow, or materially change the claim.
- Status: usable, provisional, or unsupported; downstream storyline/slide references.

Use only usable claims as unqualified factual takeaways. Provisional claims may be
presented with visible qualification. Unsupported claims belong in an explicitly
framed hypothesis or open question, not in the deck as established findings.

## Stage handoffs

- Research → analysis: source register, reading notes, landscape, search log, gaps.
- Analysis → presentation: thesis, claim ledger, storyline, unresolved qualifications.
- Presentation → completion: storyboard, editable source, final deck/exports,
  figure provenance when relevant, visual/factual review, and current README links.

A handoff states what is ready, what remains uncertain, and what should happen next.
Existing equivalent files can fulfill these roles; these names are defaults rather
than a migration requirement.
