# Two Heads are Better Than One: Test-time Scaling of Multi-agent Collaborative Reasoning

**Authors:** Can Jin, Hongwu Peng, Qixin Zhang, Yujin Tang, Dimitris N. Metaxas, Tong Che
**arXiv:** 2504.09772
**Venue:** Preprint
**Date:** August 2025

## Problem
Test-time scaling has improved single-agent reasoning, but the paper argues that scaling reasoning inside multi-agent systems is less understood. Fixed multi-agent setups can waste computation or under-coordinate because the right number of agents, discussion rounds, and token budgets vary by problem.

## Method
The authors build M500, a 500-example dataset of multi-agent collaborative reasoning traces. They sample difficult, diverse, interdisciplinary questions, generate AgentVerse traces with DeepSeek-R1 across roles such as expert recruiter, problem solvers, executor, and evaluator, and keep only traces that reach consensus, follow the required format, and produce correct answers. They fine-tune Qwen2.5-32B-Instruct on these ordered agent traces to produce M1-32B. At inference time, they add a CEO agent that monitors the question, current solution, feedback, and resource state, then decides whether to accept, refine, recruit agents, or adjust token budget.

## Key Findings
- In AgentVerse, M1-32B with the CEO agent improves over Qwen2.5 on the reported general understanding, math, and coding benchmarks, including GPQA-Diamond, AIME2024, MATH-500, HumanEval, and MBPP-Sanitized.
- Table 1 reports large gains on hard reasoning tasks: AIME2024 rises from 21.1 for Qwen2.5 to 62.2 for M1-32B with CEO, and MATH-500 rises from 84.4 to 95.8.
- M1-32B with CEO also outperforms s1.1-32B, a Simple-Scaling-style single-agent SFT baseline, across the evaluated AgentVerse tasks.
- The CEO agent gives consistent but modest gains over M1-32B without CEO across Table 1, supporting adaptive coordination on top of model-level collaborative training.
- The scaling analysis finds that more solver interaction and larger token budgets can help, but gains are task-dependent; too many problem solvers can hurt, and simply increasing total iterations does not improve performance.

## Tags
`multi-agent`, `test-time-scaling`, `collaborative-reasoning`, `supervised-fine-tuning`, `agent-orchestration`, `AgentVerse`, `M500`, `M1-32B`, `CEO-agent`

## Connections
- Complements **MixtureofAgentsEnhancesLargeLanguage_2406.04692** by focusing on trained collaborative reasoning traces and adaptive MAS control rather than only aggregating multiple model outputs.
- Related to **AgentScalingDiversity_2602.03794** because both examine when adding agents or changing agent scale helps versus when coordination overhead appears.
- Useful counterpoint to negative multi-agent coding results such as **CooperBench_2601.13295**: this paper reports gains in a structured AgentVerse reasoning setup, but not in shared-repository collaborative coding.
- Builds directly on Simple-Scaling-style reasoning SFT, but converts the training target from single-agent chains into ordered multi-agent traces.
