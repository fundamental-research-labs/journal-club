---
name: journal-club-research
description: Research a journal club topic broadly, organize a traceable source corpus, and identify emerging directions and strong evidence. Use for initial literature discovery, research updates, or targeted evidence gaps from analysis and presentation.
---

# Journal Club Research

Build an evidence base that lets a later analyst form and challenge a thesis.
Default to a topic-wide investigation; a paper is evidence within the field, not
necessarily the unit of organization.

Read [the shared workflow](references/workflow.md) before working. Follow repository
instructions and reuse the existing session and source identifiers.

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
forward. Log queries, search dates, coverage, and gaps in `research/search-log.md`.
Avoid using the emerging thesis as the only vocabulary for discovery.

## Read and organize

Use `research/sources.md` as the source register and `research/notes/<source-id>.md`
for substantive reading notes; use the fields in the shared workflow. Read relevant
full texts before describing findings. Mark abstract-only or partial access explicitly.
Link sources rather than retaining downloads unless redistribution is permitted.

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

Finish when the major approaches, recent developments, and credible challenges are
covered and another search pass is yielding little decision-relevant information.
State coverage limitations. For a targeted follow-up, answer the specific request,
update affected records, and identify which claims may need revision. Update the
shared workflow state and hand off to analysis within the user's requested scope.
