# FinEvo-Bench

## Source and access

**Source key:** `2026-finevo-bench`.

**Originals and source links:** [register](../sources.md#2026-finevo-bench); [canonical source](https://arxiv.org/abs/2608.06144v1). retention-restricted. [Manifest](../originals/manifest.json).

**Primary source:** Bo Deng et al., *FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows*, [arXiv:2608.06144v1](https://arxiv.org/abs/2608.06144v1), 2026-08-06.

**Version/access:** v1 PDF, read 2026-09-16; §§3–4, Tables 2–7, appendices A–C.

**Original:** see current acquisition record above. [Direct PDF](https://arxiv.org/pdf/2608.06144v1). ArXiv non-exclusive distribution license; no separate redistribution license found, so retain only under repository policy/permission.

## Question and methods

### Question and role

Does retaining feedback-derived experience improve later, related professional tasks beyond the same scaffold's state-reset performance? FinEvo-Bench provides the lane's clearest paired persistence control and adds compliance, report quality, resource cost, and professional-process recurrence.

### Methods and setting

The benchmark contains 120 real-case-grounded tasks organized as six distinct cases in each of 20 scenes across six financial domains, using 775 input files and requesting open-ended deliverables (§3; Figure 1). Cases in a scene share a professional process but differ in facts, files, calculations, and conclusions. Two domain experts draft and cross-review each 100-point scene rubric and apply it to all six cases (Appendix A, Tables 14–19).

Three independently shuffled global streams interleave all 120 tasks. Every evolving run starts without benchmark-derived experience, processes the stream sequentially, receives post-task problem/reason feedback, and may retain an abstraction. Its non-evolving pair resets state before every task while holding order, Qwen3.7-Max backbone, greedy temperature-0 decoding, and scoring fixed (§4.1, pp.4–5). Claude Code, Codex, Letta, and GenericAgent are each evaluated over three full evolving streams and three paired controls: 360 task executions per condition per scaffold.

A separate Claude Code scorer backed by Claude Opus 4.6 applies hidden rubrics. The agent sees a summary of deficiencies after completion but not the whole rubric or judge record. Execution and reflection tokens are recorded; judge cost is excluded.

## Results and evidence

### Findings

The scorer and one financial expert independently scored 120 outputs from one run: ICC(A,1)=0.95, 95% CI [0.93,0.97], mean absolute difference 1.6 and maximum 5 points (§4.2, p.5).

Table 3 (p.6), averaged over three streams:

| Scaffold | Evolved score | Compliance issues/task | Paired score gain | Compliance reduction | Total tokens/task (×10^4) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Claude Code | 89.47 | 0.11 | +17.89 | 0.44 | 76.50 |
| Codex | 91.17 | 0.11 | +19.37 | 0.44 | 68.75 |
| Letta | 91.65 | 0.09 | +17.82 | 0.39 | 50.43 |
| GenericAgent | 83.34 | 0.34 | +9.33 | 0.12 | 21.78 |

Late within-scene ranks 4–6 have score gains 6.10–8.70 points higher than ranks 1–3 and compliance reductions 0.02–0.10 higher (§4.3, Figure 3/Table 3). Later scene rank is also later in the global stream, so this does not isolate same-scene learning from general accumulated experience.

Table 5 (p.7), Claude Code carrier comparison: reset 71.58 score/0.55 issues; fixed expert skill 86.67/0.13; unrestricted evolution 89.47/0.11; memory only 90.42/0.09; skill only 93.71/0.05. Reflection tokens per task are 60.19×10^4 for unrestricted, 26.18×10^4 for memory, and 44.03×10^4 for skill. Table 6 reports rubric feedback beating a complete reference answer by +3.95 to +7.93 score points and −0.06 to −0.14 issues per task across scaffolds.

### Coordinator verification

Re-read primary §§3–4 and Tables 3–6 on September 16. Corrected the screening draft: **775 is the number of input files, not output deliverables** (§3.1). There are 120 task outputs per complete run. All four evaluated scaffolds use the same Qwen3.7-Max backbone; scaffold names do not identify their usual vendor models. Only the separate scorer uses Claude Opus 4.6.

## Appraisal and limitations

### Authors' claim, evidence, and interpretation

The authors attribute paired gains to retained experience because only persistence differs within a matched stream. That attribution is substantially stronger than an evolved-versus-unrelated-baseline comparison. The result demonstrates learning recurring benchmark procedures under repeated judge feedback. It does not establish open-world competence or a unique contribution from any individual stored memory, and the activated/non-activated subgroup comparison is selection-biased because the agent chooses when to retrieve.

### Strengths and limitations

Strengths: matched reset controls, common backbone, three independent permutations, explicit compliance outcomes, detailed task/rubric construction, and human calibration of the scorer. Limits: the paper reports mean main effects without across-run SD/CI or paired tests; one expert calibrates one run's outputs; scorer and feedback come from the same rubric ecosystem; all tasks share benchmark-authored recurring procedures; judge token cost is excluded; only Claude Code receives the carrier ablation; and the cross-scene diagnostic uses one 30-task stream.

## Discussion and follow-up

### Candidate figures

Table 3 with paired gain and cost, plus a simple diagram of the stateful/reset stream. Avoid implying that the skill-only ordering generalizes beyond Claude Code and this benchmark.

[Prominent citations and their roles](../prominent-citations.md#2026-finevo-bench)
