# AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents

**Authors:** Chang Ma*, Junlei Zhang*, Zhihao Zhu*, Cheng Yang*, Yujiu Yang, Yaohui Jin, Zhenzhong Lan, Lingpeng Kong, Junxian He
**arXiv:** 2401.13178
**Venue:** NeurIPS 2024 Datasets and Benchmarks Track
**Date:** December 2024 (local PDF is arXiv v2 dated 2024-12-23)

## Problem
LLM agents are usually evaluated with final success rates on isolated task families, which hides partial progress and makes it hard to compare agent behavior across diverse multi-turn, partially observable settings. Existing benchmarks often lack some combination of task diversity, multi-round interaction, partial observability, fine-grained progress metrics, and analytical tooling.

## Method
AgentBoard unifies nine text-based environments across embodied AI, games, web tasks, and tool-use tasks under a simple reflex-agent interaction loop. It adapts or curates tasks so agents must interact over multiple turns in mostly partially observable environments, then evaluates both success rate and a fine-grained progress rate based on human-annotated subgoals or continuous state matching. The accompanying open-source framework includes analysis for progress over steps, hard/easy cases, grounding accuracy, long-range interaction, sub-skills, trajectories, and a WandB-based visualization panel.

## Key Findings
- AgentBoard contains 1,013 environments across nine tasks: AlfWorld, ScienceWorld, BabyAI, Jericho, PDDL, WebShop, WebArena, Tool-Query, and Tool-Operation.
- The proposed progress rate is more discriminative than success rate when many agents fail to complete tasks; the authors validate it against human ratings with Pearson correlations above 0.95 across evaluated tasks.
- GPT-4 is the strongest evaluated model in Table 3, with average progress/success of 70.0/47.9, while proprietary models generally outperform the tested open-weight models.
- Open-weight agents often make limited early progress but struggle with long-range interaction; the paper reports that many open-weight models stop improving after only a few steps in several tasks.
- Analytical breakdowns suggest that agent performance depends on multiple abilities, including grounding, planning, memory, world modeling, self-reflection, and spatial navigation, not just instruction following.
- The benchmark still depends on human-authored progress annotations and mostly simulated environments, which the authors identify as scalability and realism limitations.

## Tags
`LLM-agents`, `agent-benchmark`, `multi-turn-evaluation`, `partial-observability`, `progress-rate`, `analytical-evaluation`, `tool-use`, `web-agents`, `embodied-agents`

## Connections
- Complements **AgentBench** and **MINT** by emphasizing partially observable multi-round tasks plus progress metrics and analytical tooling.
- Useful alongside **WebArena**, **WebShop**, **AlfWorld**, **ScienceWorld**, and **BabyAI** as a unifying evaluation layer rather than a single-environment benchmark.
- Relevant to papers on multi-agent and coding-agent evaluation because it argues that final success rate alone can hide meaningful partial progress and process failures.
- Connects to agent-skills work on grounding, memory, planning, world modeling, self-reflection, and navigation by providing task-level sub-skill analysis.
