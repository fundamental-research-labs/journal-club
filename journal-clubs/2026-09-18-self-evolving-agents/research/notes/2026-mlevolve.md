# MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery

## Source and access

Key: `2026-mlevolve`. [Primary v1](https://arxiv.org/html/2606.06473v1); [register](../sources.md#2026-mlevolve). First 2026-06-04; version 2026-06-04. Read September 16, 2026: methods, main results, relevant appendices. No original retained: arXiv non-exclusive distribution license does not grant general redistribution.

## Question and methods

Can long-horizon ML engineering benefit from cross-branch experience? Progressive graph search, retrospective memory, and adaptive code generation combine under a fixed backbone (§3).

## Results and evidence

§4.1: 75 MLE-Bench tasks, up to 500 expansions and 12 hours per task; 21 vCPUs, 234 GB RAM, one H200. Table 1 reports 65.3±0.8% medal rate, mean±SEM over three seeds. Table 3: on 22 tasks, removing memory changes medal rate from 81.82 to 68.18%; no ablation interval is reported.

## Appraisal and limitations

Coordinator: substantive experience-reuse evidence, with heterogeneous leaderboard baselines using different models and runtime budgets. The smaller ablation helps isolate components but has limited uncertainty reporting. Search adaptation inside benchmark tasks does not establish persistent general improvement across deployment. Reserve for the ML-engineering route.

## Discussion and follow-up

Which improvement comes from memory, which from search scheduling, and which from backbone capability? What would a same-model, same-resource, cross-task reset control show?

Results above are author-reported; appraisal is coordinator interpretation. No experiments reproduced. [Screening detail](../workers/citation-screening-meta.md).

[Prominent citations and their roles](../prominent-citations.md#2026-mlevolve)
