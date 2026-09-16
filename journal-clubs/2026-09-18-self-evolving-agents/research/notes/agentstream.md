# AgentStream

## Source and access

**Source key:** `agentstream`.

**Originals and source links:** [register](../sources.md#agentstream); [canonical source](https://arxiv.org/abs/2608.00155v1). retention-restricted. [Manifest](../originals/manifest.json).

[Paper v1](https://arxiv.org/html/2608.00155v1). Dong Yan et al.; July 31, 2026 preprint. Accessed September 16; framework, setup, main results read. Family: AgentStream.

**Acquisition:** [original PDF](https://arxiv.org/pdf/2608.00155v1) not retained: arXiv HTML identifies the perpetual non-exclusive license, which does not grant general redistribution rights. HTML read directly; temporary text is outside the repository.

## Question and methods

Do context, memory, skills, and harness updates help across task streams? ACE, A-Mem, ReasoningBank, AutoSkill, and an integrated harness run with three models in isolated, sequential, and interleaved conditions (§§3–4).

## Results and evidence

### Reported evidence

Six benchmarks × 50 tasks = 300 distinct tasks; three ordering seeds reuse those tasks. Table 1: GPT-5.4 vanilla averages 45.8; A-Mem interleaved 50.4 (+4.6 points), but AutoSkill isolated 42.8 (−3.0). Claude Opus 4.7 vanilla 63.9; ACE isolated 67.0, interleaved 61.9. Domain-level variability is printed; no macro confidence interval accompanies these comparisons. Appendix A/Table 7 costs are audited below.

### Reconstructed aggregation and costs — September 16

A [small standard-library audit script](../check-agentstream-aggregates.py) reads the primary v1 HTML Tables 11–13 and subtracts each model’s vanilla macro average. It exactly recovers Table 2 to its printed precision:

| Scenario | Cells | Positive / negative / ties | Mean gain (pp) | Sample SD of three seed means (pp) |
| --- | ---: | --- | ---: | ---: |
| Isolated | 45 | 34 / 11 / 0 | 1.37 | 0.80 |
| Sequential | 45 | 28 / 16 / 1 | 0.75 | 0.48 |
| Interleaved | 45 | 28 / 17 / 0 | 0.90 | 0.34 |

**Derivation, not an author statement about code:** 3 models × 5 methods × 3 ordering seeds = 45 cells. The printed ± values are reproduced by taking the sample SD of the three per-seed means over 15 model–method pairs. They are not the SD of 45 cells, a confidence interval, or uncertainty over new task datasets. The sequential row's missing 45th positive/negative is a tie in the rounded per-seed table. Percentages should use these counts: 34/45 is 75.56%, and 28/45 is 62.22%; the paper prose’s 75.7/62.3 percentages differ slightly. Do not silently copy those rounded prose values. Unrounded underlying values were not available, so near-zero ties remain subject to rounding.

Appendix A/Table 7 gives **single-evaluation** cost figures, distinct from the three-seed main table: GPT-5.4 vanilla $0.297/task; A-Mem interleaved $1.893/task, 6.37×, with that run’s +5.6-point gain and 8.8 versus 9.5 agent steps. The main-table gain is +4.6; do not mix the +5.6 single-run cost row with the aggregate score. This illustrates that fewer action steps can coexist with substantially more total API cost. Pricing and account details are experiment-specific.

## Appraisal and limitations

### Authors' claim

Model capability, method, and stream organization condition gains.

### Interpretation and limitations

A useful factorial evaluation, not a causal demonstration that model scale determines learning. Shared tasks and order seeds are not independent datasets. Native benchmark scores differ in meaning. Table 2 aggregation was reconstructed in the follow-up below; its 45 cells are model–method–order-seed combinations, not independent datasets.

## Discussion and follow-up

Table 1 and per-seed Tables 11–13. Can retained experience improve one domain while hurting another?
