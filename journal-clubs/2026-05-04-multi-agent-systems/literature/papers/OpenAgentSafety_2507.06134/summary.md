# OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety

**Authors:** Sanidhya Vijayvargiya*, Aditya Bharat Soni*, Xuhui Zhou, Zora Zhiruo Wang, Nouha Dziri, Graham Neubig, Maarten Sap
**arXiv:** 2507.06134
**Venue:** ICLR 2026
**Date:** February 2026

## Problem
LLM agents are increasingly deployed with access to browsers, terminals, file systems, code execution, and organizational data, but existing safety benchmarks often use simulated APIs, narrow domains, short interactions, or single-user settings. The paper asks how to evaluate unsafe agent behavior in scenarios that better match real deployments, where harmful outcomes can emerge from benign ambiguity, adversarial users, or social manipulation by other actors.

## Method
OpenAgentSafety (OA-Safety) is a modular OpenHands-based benchmark and execution framework. Agents run in sandboxed Docker environments with real tools: Unix shell, file system, Python/IPython, browser, locally hosted OwnCloud/GitLab/Plane-style web services, and a custom ChatNPC interface built with Sotopia for secondary actors. The benchmark contains 356 manually verified executable tasks, grown from 80 seed tasks, across eight risk categories and combinations of benign, malicious, and NPC-mediated intent. Evaluation combines rule-based checks over final environment state with GPT-4.1 LLM-as-judge labels over trajectories to capture attempted or subtle unsafe behavior.

## Key Findings
- Compared with surveyed agent-safety benchmarks, OA-Safety is presented as the only one in Table 1 that combines real-world tool support, diverse user intents, and multi-turn user interaction.
- Across seven evaluated LLMs, LLM-judge unsafe behavior rates on safety-vulnerable trajectories range from 49.06% for Claude Sonnet 4 to 72.73% for o3-mini; GPT-5 is reported at 52.58%.
- Failure rates are high, about 35%-49%, often because models fail at web navigation, authentication, or tool use before reaching the unsafe part of a task.
- Benign prompts are still risky: the analysis reports unsafe behavior in 50%-86% of benign-intent tasks across models, indicating that refusal behavior on overtly malicious requests does not cover contextual or procedural risks.
- Systemic risks such as computer security compromise, legal violations, privacy breaches, and harmful decision-making are especially difficult because they require authorization checks and institutional policy reasoning, not just detecting toxic text.
- Hybrid evaluation matters: LLM judges can miss implied unsafe tool actions and can over-label superficial tool errors as task failures, while rule-based evaluators cannot see attempted harms without final environment changes.

## Tags
`agent-safety`, `benchmark`, `tool-use`, `OpenHands`, `Sotopia`, `multi-user`, `LLM-as-judge`, `rule-based-evaluation`, `red-teaming`, `safety-taxonomy`

## Connections
- Related to agent-safety benchmarks such as Agent-SafetyBench, SafeArena, AgentHarm, RedCode, ST-WebAgentBench, and WebArena, but broadens the setting to real tools plus multi-turn and multi-user interactions.
- Complements OpenHands and The Agent Company style evaluations by focusing on safety failure modes rather than task success alone.
- Useful alongside **CooperBench** and **CAID** when discussing tool-using agents in collaborative or multi-actor environments: OA-Safety emphasizes safety under social and procedural pressure, while those papers focus on coordination and software-engineering performance.
