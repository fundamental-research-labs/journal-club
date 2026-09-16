# A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration

**Authors:** Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, Diyi Yang
**arXiv:** 2310.02170
**Venue:** COLM 2024
**Date:** November 2024

## Problem
Many LLM-agent collaboration systems use a fixed team and static communication pattern, even though different tasks may need different expertise and different interaction structures. The paper asks whether dynamically selecting and reforming an agent team can improve task-solving quality and efficiency over single-agent, debate, and fixed multi-agent baselines.

## Method
DyLAN models collaboration as a temporal feed-forward network (T-FFN): each time step is a layer, nodes are agents, and edges are communications between agents across adjacent steps. It uses a two-stage process. In Team Optimization, candidate agents run a preliminary collaboration and compute an unsupervised Agent Importance Score from peer ratings propagated backward through the T-FFN. The top agents become the task-oriented team. In Task Solving, an LLM ranker performs agent team reformation by keeping higher-ranked responses active in later steps, and early stopping ends inference when more than two-thirds of agents converge on an answer.

## Key Findings
- DyLAN reports stronger results than tested baselines on HumanEval code generation, WebShop decision-making, MMLU general reasoning, and MATH arithmetic reasoning, while using a moderate number of API calls.
- Team optimization helps: Table 5 reports improved performance and lower second-stage API calls after selecting smaller teams, and Table 7 reports large subject-level gains on selected MMLU subjects.
- Agent team reformation is important for correctness, while early stopping mainly reduces API calls with little performance loss or slight improvement.
- Smaller optimized teams can outperform larger unoptimized teams on MMLU, suggesting that adding more agents is not enough without task-relevant selection.
- The authors validate Agent Importance Score against human-prior selection and simplified Shapley-style contribution estimates, but note that results still depend on the candidate-agent pool and evaluation setting.

## Tags
`multi-agent`, `LLM-agents`, `dynamic-teams`, `agent-selection`, `team-optimization`, `temporal-feed-forward-network`, `reasoning`, `code-generation`

## Connections
- Extends fixed multi-agent setups such as CAMEL and AgentVerse by adding dynamic team selection and reformation.
- Related to LLM Debate and ChatEval-style agent discussion, but DyLAN uses ranker-driven feed-forward communication rather than fixed debate rounds.
- Complements AutoGen-style multi-agent frameworks by focusing on how to choose and prune agents for a specific task.
- Relevant to CooperBench and other coordination-failure work: DyLAN argues that team composition and communication topology are first-class design variables, not incidental implementation choices.
