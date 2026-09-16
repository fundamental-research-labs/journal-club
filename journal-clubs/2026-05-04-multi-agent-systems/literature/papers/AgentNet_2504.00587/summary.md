# AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems

**Authors:** Yingxuan Yang, Huacan Chai, Shuai Shao, Yuanyi Song, Siyuan Qi, Renting Rui, Weinan Zhang
**arXiv:** 2504.00587
**Venue:** Preprint
**Date:** May 2025

## Problem
Most LLM-based multi-agent systems use a central controller, static workflow, or fixed agent roles. The paper argues that these designs create scalability bottlenecks, single points of failure, weak adaptation to changing task demands, and privacy barriers for cross-organization collaboration where agents may hold proprietary data or capabilities.

## Method
AgentNet models the system as a decentralized directed graph of agents. Each agent has a router that decides whether to forward, split, or execute a task, and an executor that performs task steps. Routing is based on task requirements, agent capability vectors, and evolving edge weights; weak edges are pruned so the network topology changes over time while preserving DAG-style task flow. Each router and executor also keeps a fixed-size local memory of successful trajectory fragments, retrieves relevant fragments with a RAG-style mechanism for new tasks, and prunes low-value memories, allowing agents to specialize without explicit role assignment.

## Key Findings
- In the reported 3-agent experiments on MATH, BBH, and API-Bank, AgentNet is competitive with or stronger than the listed single-agent and multi-agent baselines across DeepSeek-V3, GPT-4o-mini, and Qwen-turbo, especially on BBH and API-Bank.
- Router ablations on BBH show that learned decentralized routing outperforms random routing variants and a global-router comparison in the reported setup.
- Removing the evolution phase lowers GPT-4o-mini performance on MATH, API-Bank, and BBH, supporting the importance of adaptive memory and specialization.
- Heterogeneous-agent results are mixed: diversity hurts or does not help in the 3-agent setting, but helps in the 5-agent BBH setting.
- Scaling analysis shows incremental gains with more agents and larger executor pools, with diminishing returns rather than unbounded improvement.

## Tags
`multi-agent`, `decentralized-agents`, `LLM-agents`, `task-routing`, `DAG-routing`, `RAG-memory`, `agent-specialization`, `evolutionary-coordination`, `privacy-preserving-collaboration`

## Connections
- Complements **CAID**: both target scalable multi-agent coordination, but CAID uses a central manager and software-engineering worktree isolation while AgentNet removes the central orchestrator and learns task routing over an evolving agent graph.
- Provides a constructive counterpoint to **CooperBench**: instead of free-form cooperating agents, AgentNet makes routing, specialization, and task decomposition explicit; its evidence is from reasoning and API-use benchmarks rather than collaborative coding.
- Related to AutoGen, MetaGPT, GPTSwarm, AFLOW, and MorphAgent as nearby LLM multi-agent frameworks and baselines; AgentNet's distinguishing emphasis is decentralized routing plus per-agent retrieval memories.
- Relevant to privacy-preserving or cross-organization agent collaboration, though the privacy claim is mostly architectural and is not stress-tested with real sensitive data.
