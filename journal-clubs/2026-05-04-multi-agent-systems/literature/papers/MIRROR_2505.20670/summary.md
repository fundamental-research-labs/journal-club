# MIRROR: Multi-agent Intra- and Inter-Reflection for Optimized Reasoning in Tool Learning

**Authors:** Zikang Guo, Benfeng Xu, Xiaorui Wang, Zhendong Mao
**arXiv:** 2505.20670
**Venue:** Preprint
**Date:** June 2025

## Problem
LLM tool-use agents often fail on complex, multi-step tasks because tool selection, parameterization, and plan decomposition errors propagate through the trajectory. Existing reflection methods mainly operate after execution, so agents learn from bad outcomes but do not prevent preventable bad actions before they are run or handed to another agent.

## Method
MIRROR is a three-agent tool-learning framework with a Planner Agent, Tool Agent, and Answer Agent. Its core addition is intra-reflection: each agent scores and revises its own output before passing it downstream or executing a tool. The framework also keeps inter-reflection through task-local memory: short-term memory helps the Tool Agent recover from local tool/parameter failures, while long-term memory records whole task trajectories so the Planner Agent can revise poor decompositions across rounds.

## Key Findings
- On StableToolBench, MIRROR is the best average method reported for each tested LLM core (GPT-3.5 Turbo, Claude 3 Haiku, Qwen2.5-72B, and GPT-4o), with the paper reporting average Pass Rate gains over the next best method from 2.5 to 7.0 points.
- On TravelPlanner, MIRROR improves Delivery Rate plus commonsense and hard-constraint pass rates over ReAct across the tested LLM cores, but Final Pass Rate remains very low.
- Ablations with GPT-4o Mini on StableToolBench show that removing Planner, Tool, or Answer intra-reflection each lowers average Pass Rate, and removing all reflection drops average Pass Rate from 85.7 to 77.8.
- The reflection budget has a trade-off: the paper reports five inter-reflection rounds as the best tested setting, while fewer rounds underperform and more rounds increase tokens while reducing Pass Rate.

## Tags
`multi-agent`, `tool-learning`, `LLM-agents`, `reflection`, `intra-reflection`, `inter-reflection`, `planning`, `StableToolBench`, `TravelPlanner`

## Connections
- Extends **Reflexion**-style post-execution learning by adding pre-execution self-evaluation inside each agent.
- Evaluates against planning and tool-use baselines such as ReAct, DFSDT, ToolLlama-2, ToolGen, and Smurfs.
- Directly relevant to **StableToolBench/ToolBench** and **TravelPlanner** as benchmarks for executable tool use and constrained real-world planning.
- Connects to multi-agent orchestration systems such as AutoGen and MetaGPT, but focuses on reflection-gated handoffs rather than general conversational collaboration.
