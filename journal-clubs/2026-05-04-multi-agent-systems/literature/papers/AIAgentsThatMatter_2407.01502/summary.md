# AI Agents That Matter

**Authors:** Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, Arvind Narayanan
**arXiv:** 2407.01502
**Venue:** Preprint
**Date:** July 2024

## Problem
AI agent progress is mostly reported through benchmark accuracy, but agent systems are expensive, stochastic, benchmark-sensitive, and often evaluated with inconsistent procedures. The paper argues that current practices can make costly or brittle agents look like genuine advances, especially when benchmarks lack proper holdouts or when model-evaluation benchmarks are reused for downstream procurement decisions.

## Method
The authors analyze agent evaluation practice through empirical reproductions and case studies. They re-evaluate HumanEval coding agents against simple retry, warming, and model-escalation baselines while plotting cost-accuracy Pareto frontiers; modify DSPy with Optuna for joint cost/accuracy optimization on HotPotQA; compare model-vs-downstream interpretations of NovelQA; survey 17 agent benchmarks for holdout adequacy; and document standardization/reproducibility issues in HumanEval and WebArena evaluations.

## Key Findings
- Accuracy-only leaderboards are misleading for agents because repeated model calls and simple retry policies can improve accuracy while hiding large inference-cost differences.
- On HumanEval, simple baselines offer Pareto improvements or close matches against several complex SOTA-style agent architectures, undercutting claims that planning/reflection/debugging alone explain the gains.
- Joint cost/accuracy optimization is a practical design target: in the HotPotQA/DSPy case study, the authors report substantially lower variable cost with similar retrieval accuracy.
- Model developers and downstream developers need different evaluation axes; downstream users need dollar costs and token counts, not only proxies such as parameter count.
- Many agent benchmarks lack holdouts at the right level of generality, which enables brittle shortcuts; the WebArena/STeP case study shows how task-specific hardcoded policies can inflate apparent real-world capability.
- Agent evaluations need stronger standardization because benchmark subsets, missing tests, environment rate limits, and evaluation bugs make reported results hard to compare or reproduce.

## Tags
`agent-evaluation`, `benchmarks`, `cost-control`, `pareto-frontier`, `reproducibility`, `holdouts`, `benchmark-overfitting`, `downstream-evaluation`, `HumanEval`, `WebArena`, `HotPotQA`

## Connections
- Complements **WorkArena**, **WebArena**, **Mind2Web**, and other web-agent benchmarks by spelling out how benchmark generality and holdout design affect what leaderboard accuracy means.
- Useful counterweight to agent-architecture papers such as **Reflexion**, **LATS**, **LDB**, and SWE-style agents: it asks whether improvements survive simple cost-controlled baselines.
- Connects to coding-agent benchmark work such as **CooperBench** and **CAID** by emphasizing reproducible evaluation, strong solo/simple baselines, and cost as a first-class metric.
- Relates to **tau-bench** and other downstream agent benchmarks because it separates model-evaluation goals from deployment/procurement evaluation goals.
