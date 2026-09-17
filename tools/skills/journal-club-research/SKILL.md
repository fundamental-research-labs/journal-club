---
name: journal-club-research
description: Research a journal club field with parallel discovery, primary-source screening, and thesis-driven coverage audits. Build a broad evidence base and a compact reading shortlist. Use for initial discovery, research updates, or re-research after analysis.
---

# Journal Club Research

Build an evidence base that lets a later analyst form and challenge a thesis.
Default to a topic-wide investigation; a paper is evidence within the field, not
necessarily the unit of organization.

Read [the shared workflow](references/workflow.md) before working. Follow repository
instructions and reuse the existing session and source identifiers.

## Resume before searching

Inspect the existing README, workflow queue, search log, source register, reading
notes, shortlist, landscape, and any existing thesis and claim ledger before
launching agents. Reuse equivalent existing filenames and stable IDs; do not create a parallel corpus because its layout differs.

Choose scope from the request and existing coverage:
- **Initial discovery:** build broad coverage when little research exists.
- **Refinement/update (default with an existing corpus):** search since the previous
  cutoff, fill gaps, screen promising pending candidates, and revisit weak or
  conflicting evidence. Preserve useful foundational coverage.
- **Thesis-driven coverage audit:** after analysis forms or materially revises a thesis,
  test its coverage against the broader field using the procedure below. Reuse the
  corpus; reopen discovery across missing approaches, not just recent dates.
- **Targeted follow-up:** resolve the queued question; widen only when it exposes
  a missed approach or the user changes scope.

Record the run date/cutoff, scope, prior coverage, open questions, and intended search
budget in `research/search-log.md`. On updates, overlap the previous cutoff slightly
for late-indexed sources and check important sources for revisions. Reuse completed
searches and notes unless changed scope, versions, or evidence warrants revisiting.

## Frame the search

Use the topic, audience, session date, and existing materials to establish scope.
Record the preparation date and assumptions in the session README. When unspecified,
assume a technically literate audience and a 30-minute talk plus discussion; adapt
when context indicates otherwise. Identify the field's central questions, competing
approaches, terminology, and adjacent fields before narrowing the search.

Search in complementary passes:
- Foundational work that explains the concepts, baselines, and historical limits.
- Recent primary work, including the latest available releases as of preparation.
  Start with the last 6–12 months, expanding for slower-moving fields. Verify first
  publication and latest version dates; do not equate a revision with a new result.
- Original practitioner work: researcher X/Twitter threads, technical blogs, project
  writeups, code releases, evaluations, talks, and demos. Follow interesting claims
  to first-party explanations, code, logs, or data. Record inaccessible material;
  search snippets and secondhand mentions are discovery leads, not reviewed evidence.
- Counterevidence, negative results, replications, critiques, and alternative methods.

Search with synonyms and competing framings, and follow citations backward and
forward. Run the recent-paper citation-mining pass below alongside keyword discovery.
Log queries, search dates, coverage, and gaps in `research/search-log.md`.
Avoid using the emerging thesis as the only vocabulary for discovery.

## Re-research from an existing thesis

Treat the thesis as a hypothesis to test, not a search filter. Read its actual
argument and claim ledger, then map each major claim to supporting evidence,
credible challenges, competing explanations, and omitted approaches. Search both
claim-specific terms and independent field terminology. A general claim about what
the field has not established requires broader checking than the examples cited.

For a broad, fast-moving topic such as self-evolving agents, expect roughly **50
substantively relevant, reviewed references in the evidence base**, adjusting to field size
and explicit user scope. This is a coverage diagnostic, not a quota or a requirement
for a short single-paper session. Distinguish four counts: discovery records,
reviewed evidence families, sources actually used in the thesis, and reading
priorities. A ten-source shortlist is a reading route, never a ceiling on research
or thesis references. Companion paper/blog/code artifacts count as one underlying
family for breadth; metadata leads and an unused bibliography do not count as
reviewed support. Sources can inform or challenge the analysis without appearing in
the essay; record their role and disposition in the coverage audit. The thesis has
no citation quota. If reviewed coverage is materially below the diagnostic, investigate
why and record consequential gaps before declaring the research sufficient.

Build `research/thesis-coverage.md` (or update an equivalent record) with:
- Thesis claim/question, current sources, strongest challenge or alternative,
  uncovered mechanism/population/evaluation, and the search that could change it.
- Selected references and their exact role: support, challenge, mechanism,
  foundation, or scope boundary. Link primary URLs and substantive reading notes.
- Actual before/after counts, deduplication basis, access limits, and disposition
  of important omissions; distinguish a missing citation from missing research.

Use complementary discovery lanes for omitted foundations and methods, strongest
positive/negative evidence, recent primary-paper citation neighborhoods, and original
practitioner work. Reconsider previously screened reserves and watchlist sources
against the thesis; ranking outside the ten is not grounds for exclusion. Read
primary methods/results for consequential additions before promoting them. Trace
selected backward/forward citation edges, but keep independent keyword discovery
to counter the thesis's vocabulary and citation-network biases.

Screen for the contribution to a specific argument, including evidence that would
force a narrower or different thesis. Stop when major coverage gaps are addressed
and further expansions add little decision-relevant evidence, or report the actual
budget/access limit; reaching 50 alone does not establish saturation. Do not add
marginal sources to make the count. Hand off concrete paragraph/claim revisions.
When the user requests applying the research fix to an existing thesis, integrate
the verified additions into connected, claim-cited prose and update traceability
within that scope. Otherwise mark affected analysis stale and queue the revision.
Select additions that change or clarify the argument; supporting records can retain
redundant examples and specialist detail. Do not remove consequential counterevidence
for narrative convenience. Neither a citation dump nor a sequence of paper reviews
demonstrates adequate research coverage.

## Tier 1: broad parallel discovery

Delegate complementary search lanes to inexpensive agents. Default to 10 agents,
each with a bounded lane for initial discovery, split by the passes above and topic
subareas; use fewer, narrower lanes on updates. Aim for roughly 200–300 distinct
candidate evidence families on a broad topic when the literature supports it, not
a quota to pad. Seek exhaustive
coverage of defined lanes, not a claim to have searched the entire internet. Stop a
lane after two query/citation expansions yield no meaningful new candidates, or when
its stated budget is reached.

Use explicit tiers when available: `gpt-5.6-luna` at low reasoning for discovery,
`gpt-5.6-sol` at medium reasoning for screening, and the coordinating agent for final
verification and synthesis. These are configurable workflow defaults, not assertions
about current pricing. Honor user model/budget choices and use available equivalents
if needed. If delegation or tier selection is unavailable, perform the same stages
with available tools and report the limitation; never imply agents ran when they did not.

Give each agent the topic, lane, date window, query/candidate budget, known sources,
output fields, and stopping condition. For model overrides, use `fork_turns="none"`
and supply this context explicitly rather than copying the full conversation. Agents
must not recursively delegate. Keep worker outputs separate; only the coordinator
merges the shared register, shortlist, and workflow state.

Discovery maximizes recall; it does not choose the top 10. Each agent returns:
- Title, canonical URL/DOI, authors/organization, source type, verifiable publication/
  version dates, discovery/access date, and access depth.
- Direct original-source download links when available (PDF, HTML, slides, code,
  or other artifacts), plus any known access or retention restrictions.
- Topic tags, why it might matter, and related paper/blog/code/thread family links.
- Clearly attributed preliminary claims or leads, with locators when read; snippets
  alone never become verified findings.
- Queries, coverage, inaccessible leads, and gaps, including lanes with no useful hits.

Merge candidates into `research/sources.md` using the shared source fields. Deduplicate
by DOI, canonical URL, title/authors, and version relationships before assigning new
IDs. Group companion artifacts into one evidence family; revisions normally retain
the same source ID, with older result/version provenance preserved in notes. Keep
low-ranked candidates with short reasons to avoid repeating their discovery later.
Discovery-only entries need no empty reading-note files.

### Mine recent papers for important prior work

Use several of the most recent relevant primary papers as seeds, spanning competing
approaches and author groups. Verify first-publication and version dates; a recent
revision alone does not make a paper a fresh seed. On updates, reuse the corpus and
target missing citation coverage rather than restarting broad discovery.

Assign disjoint seed sets to inexpensive discovery agents in parallel with each
other and keyword-search lanes. Read the seeds' introductions and related-work
sections, then resolve their bibliography entries. Prioritize works the authors
highlight as foundations, direct predecessors, strong baselines, competing methods,
or important limitations; do not merely copy entire reference lists. Give each lane
a seed/edge budget and the existing source register. Workers must not recursively
delegate or edit shared records.

For each useful citation edge, record the seed's canonical URL/version, section and
paragraph or page locator, cited work's title/canonical URL, its role in the seed's
argument, and the existing source key or proposed new candidate. Attribute the
characterization to the seed authors. Check the cited primary source's metadata and
record access depth; a seed's summary does not verify the cited work's findings.
Keep an auditable edge table in the lane report and link it from the search log.

Merge and deduplicate against all existing families before screening. Record both
new discoveries and important already-covered works, so the pass demonstrates
coverage rather than rewarding only novelty. Expand another citation generation
only for a consequential gap; stop after two expansions add no decision-relevant
sources or the stated budget is reached. Report budget exhaustion separately from
saturation. Citation frequency and repeated mentions are discovery signals, not
evidence quality or independent confirmation. Preserve keyword, practitioner, and
counterevidence searches to reduce citation-network and author-group bias.

## Tier 2: screen and prioritize

Give stronger screening agents the deduplicated candidates, existing shortlist,
audience, central questions, and a common rubric. Partition large pools into batches
so every new or materially changed candidate is screened. Reuse prior judgments for
unchanged sources, reconsidering them when scope or criteria change. Each screener
returns per-candidate judgments and reasons, strongest candidates, counterevidence,
and uncertain cases. Local discovery-lane rankings must not determine final selection.

Assess relevance, evidence strength, novelty, teaching/discussion value, and coverage
contribution separately as high/medium/low with reasons; use unknown when uninspected.
Consider independence and redundancy by family. Inspect primary material before judging
evidence strength; metadata-only screening stays provisional. Citation counts, venue,
recency, and source format are not substitutes for appraisal. Include substantive
practitioner work and foundations on their merits, without a paper-only or format quota.

The coordinator compares across batches, resolves inconsistent judgments, and builds
a provisional reading shortlist of about 10 evidence families, distinct from the
broader reviewed thesis evidence base and adapting to the request and
topic. Select a representative source and link companions for each. Cover the main
questions, competing approaches, and credible challenges; explain gaps rather than
padding the list. Retain close alternatives for replacements after verification.

## Tier 3: verify and finalize the shortlist

Verify the provisional shortlist against primary sources and substantive reading
notes before finalizing. Agent summaries are navigation aids, not sufficient evidence.
Downgrade or replace unsupported selections; keep inaccessible promising sources
visibly provisional or on the watchlist. Read additional consequential sources when
needed to resolve conflicts or gaps outside the shortlist.

Write `research/shortlist.md` with ranked source/family IDs, stable links, selection
reasons, rubric judgments, access/reading status, and each source's role in the session.
Distinguish established evidence from emerging ideas. Include close alternatives and
why they missed the cut. This is a reading priority list; retain a topic-wide landscape
rather than turning the session into successive paper reviews.

## Acquire originals and make reading notes

Use the folder layout and naming rules in the shared workflow. Actively try to save
an original-source copy for each shortlisted source and every additional source read
substantively; collect download links for the broader candidate pool during discovery.
Prioritize the provisional shortlist, then reserves and other consequential sources.
Do not delay screening to download every candidate, and do not equate a download
with having read it.

Prefer the publisher, author, official project, or primary repository. For papers,
try the original PDF and relevant supplements; if unavailable, try an author-hosted
or repository version and record which version was obtained. For blogs and threads,
save permitted HTML or an available author export; label print-to-PDF captures as
captures, not original PDFs. For talks, prefer slides and available transcripts;
for code, retain a relevant permitted release or small artifact with its commit/tag
rather than cloning large repositories by default. Record omissions in partial captures.

Follow repository retention rules: retain copies only when redistribution is permitted;
record the license/permission basis. Otherwise keep the canonical link, access status,
and original reading notes, with a precise reason no copy was saved. Public access
alone does not establish redistribution permission. Do not bypass access controls.
If an official download fails, try a reasonable alternate first-party location, then
record the failure and continue. Distinguish unavailable, retention-restricted, and
not-yet-attempted copies from successfully saved originals.

Check that each saved file opens, matches the source title/version, and is not an
error/login page. Link it from the source register and reading notes. On reruns, reuse
valid existing copies; save changed versions separately and identify the version read.
Before handoff, ensure each shortlisted source has substantive notes or an explicit
access limitation, and a verified local copy or a recorded reason it could not be kept.

## Reading standards

Use `research/sources.md` as the source register and `research/notes/<source-key>.md`
for substantive reading notes. Use descriptive year/title source keys, never opaque
numbered source names; follow the naming rules and fields in the shared workflow. Read relevant
full texts before describing findings. Mark abstract-only or partial access explicitly.
Keep canonical source links even when a local copy is available.

For each consequential source, extract the question, methods, experimental setting,
results, strengths, limitations, and exact result locators. Preserve sample sizes,
units, denominators, uncertainty, baselines, and compute or cost where relevant.
Distinguish author claims from measurements and your interpretation. Use “not
reported” for missing information; never fill gaps with plausible numbers.

Judge evidence by how well it supports a particular claim: controls, measurement
validity, comparison fairness, uncertainty, contamination, independence, replication,
and relevance to real use. Peer review and popularity are metadata, not substitutes
for this appraisal. A reproducible practitioner evaluation can be stronger than a
weak paper; a polished demo alone cannot establish general effectiveness. Group a
paper, its blog, and its launch thread as one underlying evidence family.

## Synthesize for analysis

Write `research/landscape.md` around questions and approaches, including:
- What the field is trying to solve, the main approaches, and their tradeoffs.
- Established results versus emerging signals, with dates and source IDs.
- The strongest evidence and the most consequential conflicts or missing tests.
- Candidate trends with concrete observations across time, independent support,
  and plausible alternatives such as benchmark changes or increased compute.
- Questions the analyst should resolve and useful figures or datasets to inspect.

Prioritize novelty and evidence quality separately. Include promising early ideas
without presenting proposals, anecdotes, or demos as established results. Do not
force a single thesis at this stage.

## Merge the run and hand off

Update records in place, preserving human annotations and useful prior notes. Append
a dated search-log summary: new/revised sources, ranking changes and reasons, resolved
and open gaps, coverage limitations, and actual models/lanes used. Distinguish newly
discovered older work from newly published research. Record unfinished or failed lanes
so a later run can resume them. Budget or access exhaustion is not search saturation.

Reconsider the shortlist against both retained and new evidence; do not replace it
wholesale with recent results. Update affected landscape sections, README links, and
workflow queue entries. Identify dependent claims/slides needing revision and mark
them stale; rebuilding a deck must remain within the user's requested scope. If no
meaningful change is found, record that outcome and preserve the existing materials
instead of cosmetically rewriting them.

Finish when the major approaches, recent developments, and credible challenges are
covered and another search pass is yielding little decision-relevant information.
State coverage limitations. For a targeted follow-up, answer the specific request,
update affected records, and identify which claims may need revision. Update the
shared workflow state and hand off to analysis within the user's requested scope.
