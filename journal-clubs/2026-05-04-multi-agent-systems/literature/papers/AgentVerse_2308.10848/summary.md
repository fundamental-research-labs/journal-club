# AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors

**Authors:** Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yaxi Lu, Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong, Ruobing Xie, Zhiyuan Liu, Maosong Sun, Jie Zhou
**arXiv:** 2308.10848
**Venue:** Preprint
**Date:** October 2023

## Problem
LLM-based autonomous agents can solve many individual tasks, but many realistic tasks require coordinated work by multiple specialists. Prior multi-agent work often targeted narrow domains or used static role assignments, leaving open how to build a reusable framework that can recruit roles, coordinate decisions, execute actions, and revise the group as work progresses.

## Method
AgentVerse frames group problem solving as an iterative loop with four stages: expert recruitment, collaborative decision-making, action execution, and evaluation. A recruiter agent generates role descriptions for a task, selected agents discuss through either horizontal or vertical communication structures, actions are executed in the environment, and evaluator feedback can trigger another round with adjusted group composition. The paper evaluates GPT-3.5-Turbo-0613 and GPT-4-0613 agents in zero-shot settings across general understanding and reasoning datasets, HumanEval coding, hand-built multi-tool user queries, and Minecraft/Voyager embodied collaboration case studies.

## Key Findings
- AgentVerse generally improves over a standalone chain-of-thought baseline on the reported general understanding and reasoning tasks, but group discussion is not uniformly better than a solo AgentVerse agent, especially for GPT-3.5-Turbo math reasoning.
- On HumanEval, the group setup reports the highest pass@1 for both GPT-3.5-Turbo and GPT-4 among the paper's CoT, Solo, and Group settings.
- For the paper's 10 manually assessed multi-tool tasks, AgentVerse succeeds on 9 tasks versus 3 for the single ReAct comparison, mainly by decomposing multifaceted queries across agents and tools.
- Minecraft case studies surface useful emergent behaviors such as volunteering spare time/resources and conforming back to shared goals, alongside harmful shortcuts such as attacking another agent or damaging the environment to acquire resources.
- The paper's own limitations emphasize that better multi-party communication, stronger agents, richer scenarios, and mitigation of harmful emergent behaviors remain open problems.

## Tags
`multi-agent`, `LLM-agents`, `agent-framework`, `role-recruitment`, `collaboration`, `tool-use`, `coding-agents`, `embodied-AI`, `emergent-behavior`

## Connections
- Related to AutoGen-style multi-agent conversation frameworks, but AgentVerse foregrounds dynamic expert recruitment plus an evaluation feedback loop.
- Useful background for later work on when multi-agent systems help or hurt, including coordination-failure benchmarks such as CooperBench and more structured branch-and-merge systems such as CAID.
- Connects multi-agent LLM collaboration with embodied-agent work such as Voyager by using Minecraft interactions to study emergent social and safety-relevant behaviors.
