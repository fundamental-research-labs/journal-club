# EvoSkill: Automated Skill Discovery for Multi-Agent Systems

## Source and access

Key: `2026-evoskill`. [Primary v1](https://arxiv.org/html/2603.02766v1); [register](../sources.md#2026-evoskill). First 2026-03-03; version 2026-03-03. Read September 16, 2026: methods, main results, relevant appendices. [Retained original](../originals/2026-evoskill/2026-evoskill-paper-v1.pdf); CC BY 4.0.

## Question and methods

Executor, failure-analysis proposer, and skill-builder agents evolve reusable folders (§2). OfficeQA uses 246 questions, 17 validation examples, and training sizes 12/24/36; each configuration evolves for 1.5 epochs (§3.1).

## Results and evidence

Table 1 exact-match baseline is 60.6%; merge is 68.1%, whereas Figure 2 and prose say 67.9%. Preserve this unresolved discrepancy. §3.3: transferred skill improves 43.5→48.8% on 128 sampled BrowseComp examples. §3.1.3 footnote explicitly says each configuration had a single evaluation run.

## Appraisal and limitations

Coordinator: concrete predecessor for WikiSkill’s persistent-wiki contrast, but small validation sets, one backbone/harness, single-run results, and merging across runs limit inference. Do not silently harmonize the OfficeQA numbers or interpret the 5.3-point transfer gain as statistically established. Reserve.

## Discussion and follow-up

Can skill merging be evaluated with a fixed selection budget and untouched test set? Would the transfer gain survive repeated runs and a larger task sample?

Results above are author-reported; appraisal is coordinator interpretation. No experiments reproduced. [Screening detail](../workers/citation-screening-skills.md).

[Prominent citations and their roles](../prominent-citations.md#2026-evoskill)
