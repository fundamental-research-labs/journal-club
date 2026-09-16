# MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents

**Authors:** Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Zhe Wang, Zhenhailong Wang, Cheng Qian, Xiangru Tang, Heng Ji, Jiaxuan You
**arXiv:** 2503.01935
**Venue:** Preprint
**Date:** March 2025

## Problem
Most agent benchmarks evaluate isolated agents or narrow task families, leaving a gap for settings where LLM agents must coordinate, divide labor, negotiate, or compete under changing state and partial information.

## Method
MultiAgentBench is implemented through MARBLE, a multi-agent coordination framework with an agent graph, coordination engine, cognitive module, shared/individual memory, environment tools, and evaluators. The benchmark covers six interactive scenarios: research proposal generation, Minecraft building, database anomaly diagnosis, coding, bargaining, and Werewolf. It evaluates both mutual-goal and conflicting-goal teams using milestone KPI tracking, final task scores, and coordination scores derived from communication and planning behavior. Experiments compare five models and study star, tree, graph, and chain coordination protocols plus planning strategies such as vanilla prompting, chain-of-thought, group discussion, and cognitive evolving planning.

## Key Findings
- gpt-4o-mini has the strongest overall task-score profile among the five evaluated models, but the paper emphasizes that task ability and coordination ability do not always move together.
- Coordination metrics are useful but not sufficient: a model can communicate or plan well while still failing execution-heavy tasks such as Minecraft.
- In the research scenario, graph-style coordination performs strongly among the tested protocols, while cognitive evolving planning improves coordination relative to the other planning prompts.
- Ablations suggest that more interaction or more agents is not automatically better; excessive iterations and larger teams can add coordination overhead.
- The authors report qualitative "aha-moments" such as strategic information sharing, trust-polarized collaboration, and role-driven strategy changes in social and research settings.

## Tags
`multi-agent`, `LLM-agents`, `benchmark`, `coordination`, `collaboration`, `competition`, `agent-evaluation`, `MARBLE`

## Connections
- Extends single-agent evaluation lines such as AgentBench by making inter-agent communication, planning, and competitive dynamics part of the measured behavior.
- Complements coding-agent collaboration benchmarks such as CooperBench by broadening beyond software tasks to research, games, database diagnosis, bargaining, and social deduction.
- Related to AutoGen-style multi-agent conversation frameworks and graph-based coordination work such as GPTSwarm, but framed primarily as an evaluation benchmark.
- Useful context for papers arguing about whether multi-agent systems help: it shows both potential coordination benefits and clear coordination-overhead failure modes.
