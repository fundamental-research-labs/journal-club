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

Stable descriptive source keys provide the chain:
`2026-agent-memory-evaluation` source → `C001` claim → slide number/title.
Never recycle an ID after removing an item. Slides may be renumbered; refresh their
mapping in the storyboard. Keep URLs and result locators alongside IDs so readers
can inspect the underlying evidence without knowing the workflow.

On a return to an earlier stage, do a targeted pass, update the affected evidence,
and propagate substantive changes through thesis, claims, storyboard, and deck.
Mark dependent artifacts stale until updated. After a thesis is formed or materially
revised, audit its field coverage and strongest counterevidence; reopen discovery
when that audit reveals thin support or omitted approaches, or the user requests it.

Stop iterating when the requested artifacts meet their stage checks and no unresolved
gap would materially alter the central conclusion. Narrow unsupported claims instead
of searching forever. If two consecutive targeted passes add no decision-relevant
evidence, record the limitation and proceed with qualified claims or report a blocked
prerequisite. Respect explicit user budgets; do not imply completion when a required
artifact or verification remains unavailable.

## Research folders and filenames

Use this layout for new sessions; create directories and files only as content exists:

```text
journal-clubs/YYYY-MM-DD-short-topic/     # undated-short-topic if unscheduled
  README.md                             # scope and links to current materials
  workflow.md                           # queue, revisions, downstream status
  research/
    sources.md                          # all candidates and acquisition status
    search-log.md                       # dated searches, coverage, run changes
    shortlist.md                        # current ranked selection and alternatives
    landscape.md                        # synthesis organized by topic
    originals/
      2026-agent-memory-evaluation/
        2026-agent-memory-evaluation-paper-v2.pdf
        2026-agent-memory-evaluation-supplement-v2.pdf
      2026-agent-memory-field-notes/
        2026-agent-memory-field-notes-page-captured-2026-09-16.html
    notes/
      2026-agent-memory-evaluation.md
      2026-agent-memory-field-notes.md
```

Use descriptive lowercase kebab-case source keys: `<publication-year>-<short-title>`
(e.g. `2026-agent-memory-evaluation`); use `undated` when the publication year is unknown.
Examples here illustrate naming only, not actual sources. Do not assign opaque numbered
source names. Keep titles recognizable, omit filler words, and avoid spaces and
punctuation other than hyphens. Resolve collisions with an author/organization or a
meaningful artifact qualifier, rather than a sequence number. Once assigned, keep a
key stable across ranking changes and source revisions; correct it only when needed
and update all affected links.

One original-source directory belongs to one source key. Companion sources have their
own descriptive keys and share an evidence-family field in the register. Use the same
key for the directory and reading-note filename so their relationship is obvious.
Where other workflow instructions say source ID, use this descriptive key.

Name retained files `<source-key>-<artifact>-<version-or-capture>.ext`. Artifact names
include `paper`, `supplement`, `page`, `slides`, `transcript`, and `code`. Use the
source's actual version (`v2`, `release-1.2`, or `commit-abc1234`) when available;
otherwise use `retrieved-YYYY-MM-DD`. Use `captured-YYYY-MM-DD` for web snapshots or
print exports. Add a descriptive suffix if multiple artifacts would collide; never
overwrite a different version. The extension must match the actual format. Preserve
original bytes for downloads; clearly identify generated captures and derived files.

Link originals and notes relatively from the register, and link each note back to
its original file and canonical URL. In `research/sources.md`, for example, use
`originals/2026-agent-memory-evaluation/2026-agent-memory-evaluation-paper-v2.pdf` and `notes/2026-agent-memory-evaluation.md`.
Do not create empty source folders for failed downloads. Existing sessions may keep
their established layout: document the mapping in the README, preserve IDs and links,
and avoid duplicating or mass-renaming prior materials just to match this convention.

## Source records

`research/sources.md` is a compact index. Each entry includes source ID, title,
authors/organization, stable URL/DOI, source type, publication and version dates,
access date, access depth, evidence family, and a relative link to reading notes.
Distinguish preprints, peer-reviewed work, code, blogs, threads, talks, and demos.
Track relevant release/commit versions for changing artifacts. Mark unknown fields.
Also record original-copy status (saved, unavailable, retention-restricted, or pending),
relative file links, download URL, retrieval/capture date, retained version, and
license/permission basis. For missing copies, record the reason and locations tried.
For multiple saved versions, identify the one supporting the current reading notes.

For tiered research, also track discovery run/date, topic tags, screening disposition
(pending, shortlisted, reserve, or excluded), and a brief selection/exclusion reason.
Access depth is separate from disposition: shortlisted sources may be provisional.
Discovery-only entries may omit a notes link until substantive reading occurs. Keep
screened-out candidates and family relationships for incremental reruns.
`research/shortlist.md` holds the current ranked selection (about 10 evidence families
by default), not the size of the thesis evidence base. For broad topics, aim for
roughly 50 relevant reviewed references in the evidence base as a breadth diagnostic,
with field-appropriate exceptions explained; this is not a thesis citation quota.
The essay selects sources for their explanatory and argumentative value. Record
consequential evidence considered but kept in supporting records, with its role and
reason for omission from the essay. Track discovery, reviewed-family, thesis-use,
and shortlist counts separately in a thesis coverage audit; never pad with companions
or unread leads. Dated search-log entries preserve material ranking changes and coverage.

`research/notes/2026-agent-memory-evaluation.md` records:
- Source title/ID, canonical URL, local-original link if retained, exact version read,
  reading date, and access depth; state any missing copy or incomplete capture.
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
- Status: usable, provisional, or unsupported; downstream slide references when a presentation exists.

Use only usable claims as unqualified factual takeaways. Provisional claims may be
presented with visible qualification. Unsupported claims belong in an explicitly
framed hypothesis or open question, not in the deck as established findings.

## Stage handoffs

- Research → analysis: source register, ranked shortlist, retained originals with
  acquisition limitations, reading notes, landscape, search log with run changes,
  and gaps.
- Analysis → presentation: thesis, claim ledger, unresolved qualifications. Presentation develops
  the narrative and slide sequence in its storyboard.
- Presentation → completion: storyboard, editable source, final deck/exports,
  figure provenance when relevant, visual/factual review, and current README links.

A handoff states what is ready, what remains uncertain, and what should happen next.
Existing equivalent files can fulfill these roles; these names are defaults rather
than a migration requirement.
