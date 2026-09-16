# Notes

## Why It Matters
This is a methodological anchor for evaluating AI agents. Its central contribution is not a new agent architecture but a checklist for making agent results meaningful: compare against simple baselines, report cost alongside accuracy, separate model-evaluation from downstream-evaluation needs, design holdouts that block shortcuts, and standardize evaluation enough that reported gains can be reproduced.

## When To Cite
Cite it when arguing that agent benchmarks should report cost-accuracy Pareto curves, when adding simple retry/escalation baselines to agent evaluations, when discussing benchmark overfitting and holdout design for agents, or when distinguishing model-leaderboard results from downstream deployment decisions. It is also useful for critiques of web-agent and coding-agent leaderboards that rely on inconsistent benchmark subsets or fragile environment-dependent evaluations.

## Key Terms
AI agents; compound AI systems; agentic systems; cost-controlled evaluation; Pareto frontier; inference cost; fixed cost; variable cost; joint optimization; DSPy; Optuna; HumanEval; HotPotQA; NovelQA; retrieval-augmented generation; WebArena; STeP; benchmark shortcuts; benchmark overfitting; holdout generality; downstream evaluation; reproducibility; evaluation standardization.
