# AgentStream

[Paper v1](https://arxiv.org/html/2608.00155v1). Dong Yan et al.; July 31, 2026 preprint. Accessed September 16; framework, setup, main results read. Family: AgentStream.

**Question/method.** Do context, memory, skills, and harness updates help across task streams? ACE, A-Mem, ReasoningBank, AutoSkill, and an integrated harness run with three models in isolated, sequential, and interleaved conditions (§§3–4).

**Reported evidence.** Six benchmarks × 50 tasks = 300 distinct tasks; three ordering seeds reuse those tasks. Table 1: GPT-5.4 vanilla averages 45.8; A-Mem interleaved 50.4 (+4.6 points), but AutoSkill isolated 42.8 (−3.0). Claude Opus 4.7 vanilla 63.9; ACE isolated 67.0, interleaved 61.9. Domain-level variability is printed; no macro confidence interval accompanies these comparisons. Appendix A is the cost-analysis target.

**Authors' claim.** Model capability, method, and stream organization condition gains.

**Interpretation/limits.** A useful factorial evaluation, not a causal demonstration that model scale determines learning. Shared tasks and order seeds are not independent datasets. Native benchmark scores differ in meaning. Table 2 aggregates 45 observations per scenario despite 15 model–method combinations; inspect seed aggregation before quoting its positive-rate headline. Use directly identifiable Table 1 comparisons meanwhile.

**Inspect/discuss.** Table 1 and per-seed Tables 11–13. Can retained experience improve one domain while hurting another?
