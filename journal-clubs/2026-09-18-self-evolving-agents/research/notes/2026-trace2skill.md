# Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills

## Source and access

Key: `2026-trace2skill`. [Primary v5](https://arxiv.org/html/2603.25158v5); [register](../sources.md#2026-trace2skill). First 2026-03-26; version 2026-06-04. Read September 16, 2026: methods, main results, relevant appendices. [Retained original](../originals/2026-trace2skill/2026-trace2skill-paper-v5.pdf); CC BY 4.0.

## Question and methods

Parallel analysts distill local lessons from success/failure trajectories, then consolidate skill patches (§2). Distinguishes deepening human skills from creating skills from weak or empty seeds.

## Results and evidence

§3: SpreadsheetBench-Verified splits 400 examples into 200 evolution/200 held-out test; spreadsheet results average three seeds. Math uses 400 DAPO evolution/100 test and 30 AIME problems at avg@8. Table 2 includes regressions: 122B-authored Combined changes same-model AIME by −1.2 points. DocVQA uses 50 evolution/5,299 test examples (§3.5).

## Appraisal and limitations

Coordinator: valuable transfer companion to WikiSkill, with explicit task/model shifts and dispersion in appendices. Repeated AIME attempts do not create independent questions; many contrasts complicate broad improvement claims. The limitations section identifies only 32 sampled validation questions for costly patch selection. Reserve rather than another top-ten skill slot.

## Discussion and follow-up

When should success versus failure traces be trusted? How should patch selection balance validation expense, negative transfer, and independence of final evaluation?

Results above are author-reported; appraisal is coordinator interpretation. No experiments reproduced. [Screening detail](../workers/citation-screening-skills.md).

[Prominent citations and their roles](../prominent-citations.md#2026-trace2skill)
