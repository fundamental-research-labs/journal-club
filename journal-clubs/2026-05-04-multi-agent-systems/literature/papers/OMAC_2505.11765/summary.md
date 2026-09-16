# OMAC: A Holistic Optimization Framework for LLM-Based Multi-Agent Collaboration

**Authors:** Shijun Li, Hilaf Hasson, Joydeep Ghosh
**arXiv:** 2505.11765
**Venue:** Preprint
**Date:** May 2025 (local PDF v3 dated April 2026)

## Problem
LLM-based multi-agent systems often rely on hand-crafted agent prompts, fixed collaboration structures, or optimization methods that target only one part of the system. The paper asks how to systematically optimize both what agents do and how they collaborate in multi-step MAS workflows.

## Method
OMAC frames multi-agent collaboration as information flow over a graph and identifies five optimization dimensions: improving existing agents, constructing new agents, selecting the candidate team before collaboration, dynamically selecting agents at each step, and routing inter-agent communication. For any one dimension, a Semantic Initializer generates diverse candidate prompts or controllers, each candidate is evaluated on training tasks, and a Contrastive Comparator reasons over positive-negative performance pairs to produce refined candidates. For multiple dimensions, OMAC optimizes one dimension at a time while keeping the others fixed, then iterates.

## Key Findings
- In the reported GPT-3.5-turbo setup, single-dimension OMAC variants outperform the strongest baselines on HumanEval, MMLU, and MATH; best reported scores include 89.25 Pass@1 on HumanEval, 74.22 accuracy on MMLU, and 35.17 accuracy on MATH.
- The gains are not limited to one optimization type: both functional prompt/example optimization and structural controller optimization improve over the DyLAN default configuration in most reported settings.
- Multi-dimension optimization gives larger gains than optimizing a single dimension, with the arithmetic reasoning example rising from a 2.9% to a 9.6% relative improvement when jointly optimizing the two strongest functional dimensions.
- Ablations show that the Contrastive Comparator adds value beyond semantic initialization alone across arithmetic, code-generation, and general-reasoning settings.
- Structural optimization can reduce inference-time API calls and token cost by selecting fewer useful agents and routing only relevant context, though training still requires repeated full-system evaluations.

## Tags
`multi-agent`, `LLM-agents`, `agent-optimization`, `prompt-optimization`, `collaboration-structure`, `contrastive-reasoning`, `semantic-initialization`, `HumanEval`, `MMLU`, `MATH`

## Connections
- Directly extends DyLAN-style dynamic agent selection by using supervised task performance to optimize both functional and structural MAS components.
- Complements ADAS and AFlow: OMAC is another black-box MAS optimization approach, but emphasizes contrastive prompt/controller refinement rather than prompt evolution alone or MCTS workflow search.
- Related to structural-search work such as MaAS and G-Designer, while broadening the target from architecture alone to agent prompts, new-agent construction, team selection, stepwise participation, and communication routing.
- Useful context for CooperBench-style coordination failures: OMAC treats agent selection and communication routing as optimizable objects rather than assuming a fixed team topology.
- Adjacent to CAID-style engineering of multi-agent workflows, but focused on learned prompt/controller optimization for generic reasoning and coding benchmarks rather than git-based software engineering coordination.
