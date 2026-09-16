# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

## Source and access

Key: `2026-skillopt`. [Primary v2](https://arxiv.org/html/2605.23904v2); [register](../sources.md#2026-skillopt). First 2026-05-22; version 2026-05-25. Read September 16, 2026: methods, main results, relevant appendices. No original retained: arXiv non-exclusive distribution license does not grant general redistribution.

## Question and methods

A frozen target executes tasks while an offline optimizer edits one skill document. Bounded patches, selection gating, rejected-edit feedback, and slower epoch updates regulate changes (§3). WikiSkill and SHAPER cite this comparator.

## Results and evidence

§4/Table 1 covers 52 model–benchmark–harness cells. Reported GPT-5.5 direct-chat six-benchmark average: 58.8→82.3 (+23.5 percentage points). Deterministic split seed is 42; test is disjoint from selection. Main results lack independent-run intervals. Table 6 reports large, benchmark-dependent training-token budgets.

## Appraisal and limitations

Coordinator: important direct baseline, with useful transfer and optimizer ablations, but reported dominance is not an uncertainty estimate. Identical scorers/splits do not establish equal optimization resources. Keep as a close reserve: adding another skill method would reduce the selected set’s production, weight-update, or counterevidence coverage. This differs from the screener’s conditional proposal to replace Shopify.

## Discussion and follow-up

How much does bounded editing add beyond a validation gate? Does a persistent skill retain value under a new task distribution and a matched lifetime token budget?

Results above are author-reported; appraisal is coordinator interpretation. No experiments reproduced. [Screening detail](../workers/citation-screening-skills.md).
