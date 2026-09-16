# Research handoff

**Updated September 16, 2026. Stage: research ready for analysis, with explicit source limitations.** Scope is the existing September 18 topic-wide journal club. The user authorized approximately one hour of autonomous research; this does not request a final analysis thesis, slides, or external publication.

## Current materials

- [Ranked shortlist](research/shortlist.md): ten priority resources and reasoned alternatives.
- [Landscape](research/landscape.md): topic questions, update surfaces, positive/negative evidence, and discussion prompts.
- [Source register](research/sources.md) / [structured records](research/sources.json): candidate decisions, exact access depth, versions, and acquisition status.
- [Reading notes](research/notes/), [originals guide](research/originals/README.md), and [acquisition manifest](research/originals/manifest.json): primary-source evidence and reproducibility limits.
- [Search log](research/search-log.md): queries, lane reports, ranking changes, and audit outcomes.

The session README and reading/practitioner routes now point to the same current corpus. Initial research notes remain historical context and are visibly superseded. No claim ledger, storyboard, or deck exists, so no downstream slide edits are outstanding.

## What changed

The initial twelve detailed notes were expanded to 43 substantive notes, covering prompt/context search, weights, self-play, improver code, environment/curriculum generation, evaluator integrity, and first-party production systems. The current register includes 132 resource/candidate records; watchlist and excluded entries are not represented as fully reviewed studies.

The selected ten deliberately include controlled positive examples, budget/reset controls, task-stream regressions, late self-play deterioration, and a production account. R-Zero displaced the provisional Dream-RSI slot to avoid underrepresenting autonomous curricula; Dream-RSI remains the first meta-improvement alternative. Follow-up reading of Agent-World and World Knowledge Exploration added mechanism coverage without changing the selected ten.

Several earlier gaps were resolved: AgentStream aggregate/seed interpretation, Hyperagents bootstrap/test methods, and EvoHarnessBench population SDs. Other claims were narrowed: ScienceBuddy's released recipe cannot establish historical paper denominators; MetaRSI conventions cannot substitute for actual ledgers. FinEvo's 775 count was corrected to input files. R-Zero and GEPA numerical source inconsistencies are recorded rather than silently reconciled.

## Work queue

These are conditional analysis/presentation follow-ups, not barriers to using the qualified research set.

| Key / requesting stage | Affected source and precise question | Why it matters / acceptance criterion | Owner / status |
| --- | --- | --- | --- |
| `sciencebuddy-historical-eval` / analysis | Which tasks, seeds, and total resources produced each paper curve, given the different released schedule and overlapping source materials? | Obtain matching run/split ledger before estimating uncertainty or claiming independent held-out performance. Current recipe is separately documented. | Research; open, claim narrowed |
| `metarsi-actual-ledgers` / analysis | Are per-variant resource budgets and sealed splits released for the reported composition comparison? | Verify actual experiment records, not merely Appendix F conventions or a general harness README. | Research; open, claim provisional |
| `rzero-aggregate-conflict` / presentation | Which code/checkpoint aggregation resolves v4 table/prose disagreements? | Do not chart disputed abstract aggregates; the separately audited Appendix Table 6 collapse result is usable with its model/scope. | Research; open, avoid disputed aggregates |
| `gepa-table-arithmetic` / presentation | Why does the six-cell GRPO mean differ from the printed aggregate? | Preserve the author-reported value with a note; no corrected result asserted without underlying data. | Research; open, minor source inconsistency |
| `agentstream-statistics` / presentation | What are the 45 cells and the ± quantities? | Tables 11–13 reproduce the mean and sample SD of three seed-level means; script and interpretation retained. No CI label. | Research; resolved |
| `hyperagents-statistics` / presentation | What is bootstrapped and why can n=5 yield p<.05? | Five run-level values, 1,000 bootstrap resamples; source code uses one-sided tests. Pairing/multiplicity limits recorded. | Research; resolved |
| `evoharnessbench-statistics` / presentation | Are displayed intervals SD, SE, or CI? | First-party project defines population SD over three runs; task/example and agent-hour units recorded. | Research; resolved |
| `practitioner-reproduction` / analysis | Can public artifacts independently reproduce the reported benefit? | Reef/NemoClaw small artifacts retained; missing adapter/memory, single-run data, and lack of held-out tasks remain visible. Training/reproduction would be a separate task. | Analysis/research; qualified, no reproduction attempted |
| `social-talk-access` / presentation | Is there an original accessible talk or thread worth quoting/showing? | Establish authorship and inspect full content or transcript with timestamp before using a claim. Current inaccessible/unverified leads are excluded as evidence. | Research; optional gap |
| `september-cutoff` / presentation | Has relevant work or a revision appeared after September 16? | Refresh selected source versions before September 18 if preparing materials then; record changed claims. | Research; future refresh |

## Verification and limits

Primary methods/results and selected appendices were read to the depths stated in each note. Multiple screening lanes were reconciled by the coordinator; final evaluation and weight/self-play claims received an additional independent check. Current arXiv bibliographic/version/license metadata was checked for the substantive paper corpus and many screened leads. Exact review scope remains source-specific.

Licensed original PDFs were checked for PDF readability and linked to immutable download versions; SHA-256 hashes and file sizes are recorded. Selected GEPA, SEAL, WikiSkill, harness-critique, and R-Zero tables were rendered and visually inspected. AgentStream aggregate arithmetic was reconstructed with a retained standard-library Python script. Before handoff, 511 authored relative file links resolved, 132 unique keys and ten shortlist records were checked, all 36 original-file hashes/sizes matched, and all 24 PDFs passed readability checks. `git diff --check` passed.

No training experiments, deployed systems, or benchmark evaluations were reproduced. No video was watched, and inaccessible social content was not inferred. This is broad, bounded research rather than an exhaustive systematic review. It supports qualified claims about specific adaptation mechanisms and their limits; it does not establish unlimited, domain-general, accelerating recursive improvement.

## Note-format and commit follow-up

All 43 reading notes now use the same five sections: Source and access; Question and methods; Results and evidence; Appraisal and limitations; Discussion and follow-up. Source-specific tables, numerical qualifications, citations, and audit findings are preserved. Discussion questions were added where absent. The formatting pass did not reopen research or change the shortlist.
