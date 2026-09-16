# GPTSwarm: Language Agents as Optimizable Graphs

**Authors:** Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, Jurgen Schmidhuber
**arXiv:** 2402.16823
**Venue:** ICML 2024
**Date:** August 2024

## Problem
LLM agent systems often rely on hand-designed prompt structures, tool-use flows, and multi-agent communication patterns. This makes Chain-of-Thought, Tree-of-Thought, Reflexion, tool agents, and role-based multi-agent systems hard to compare, reuse, and improve automatically.

## Method
GPTSwarm represents each language agent as a directed computational graph: nodes are operations such as LLM calls, tool use, API calls, or file/web analysis, and edges define information flow. Multiple agents compose into a larger swarm graph, where inter-agent edges are communication channels. The paper proposes two optimizers: edge optimization, which learns a distribution over feasible DAG connections with REINFORCE, and node optimization, which iteratively updates node-level prompts from input-output histories.

## Key Findings
- The graph formalism can express individual agents, multi-agent swarms, and common prompting methods such as Chain-of-Thought, Tree-of-Thought, Reflexion, and self-consistency.
- On adversarial MMLU swarms, edge optimization filters harmful agents and recovers performance toward the direct-answer baseline; Appendix D reports GPTSwarm at 0.8301 accuracy versus 0.5751 for Multiagent Debate in the same 3 truthful/3 adversarial setup.
- On Mini Crosswords, edge optimization improves average accuracy from 0.465 (+/- 0.0509) for the initial distribution to 0.575 (+/- 0.0275); evaluating an optimized distribution with GPT-4-Turbo reaches 0.800 (+/- 0.0616) in the paper's setup.
- On HumanEval, node-level prompt optimization improves a ReAct-style coding agent from 0.76 without optimization to 0.88 (+/- 0.007).
- On GAIA, a 7-agent Tree-of-Thought swarm with self-consistency averages 18.45 across levels, outperforming the reported GPT-4-Turbo, AutoGPT, and GPT-4-with-plugins baselines in the paper's comparison, though it remains far below human performance.

## Tags
`language-agents`, `multi-agent`, `computational-graphs`, `agent-orchestration`, `prompt-optimization`, `REINFORCE`, `DAGs`, `tool-use`, `MMLU`, `HumanEval`, `GAIA`

## Connections
- Complements graph-structured prompting work such as Graph of Thoughts by extending graphs beyond prompting schemes to include tool use, node operations, and swarms of agents.
- Related to AutoGen, CAMEL, ChatDev, MetaGPT, and other role-based multi-agent systems, but focuses on automatically optimizing communication topology rather than only hand-designing roles or dialogue protocols.
- Useful background for later work on agent coordination and scaling: it treats communication edges as an optimization target, while many benchmarks show that naive multi-agent communication can hurt performance.
- Connects to OPRO, DSPy-style prompt/program optimization, and broader meta-learning for LLM inference pipelines through its node-level prompt optimizer.
