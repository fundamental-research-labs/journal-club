# WebArena: A Realistic Web Environment for Building Autonomous Agents

**Authors:** Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig
**arXiv:** 2307.13854
**Venue:** ICLR 2024
**Date:** July 2023

## Problem
Web-agent benchmarks before WebArena either simplified websites, used static snapshots, or evaluated action traces rather than whether the intended web task was actually completed. The paper asks how to build a realistic but reproducible environment for language-guided agents that must perform long-horizon everyday browser tasks.

## Method
WebArena is a self-hosted browser environment with fully functional sites modeled on common web domains: e-commerce, social forums, collaborative software development, and content management. It also includes tools and knowledge resources such as a map, calculator, scratchpad, offline Wikipedia, and site manuals. Agents interact through browser-like actions over observations such as HTML, screenshots, or accessibility trees. The benchmark contains 812 high-level natural-language intents generated from templates, with evaluation based on functional correctness: text-answer matching, LLM-assisted fuzzy matching, or programmatic checks over page state and backend data.

## Key Findings
- WebArena emphasizes dynamic interaction, realistic sites, diverse human-style tasks, and functional correctness, a combination the authors argue is missing from prior benchmarks.
- Human annotators complete 78.24% of a sampled task set, while the best reported GPT-4-based baseline reaches 14.41% end-to-end success.
- GPT-4 with chain-of-thought and an explicit unachievable-task hint reaches 11.70%; removing the hint improves overall success but weakens unachievable-task handling.
- The authors identify early stopping, weak exploration, observation bias, repeated invalid actions, and failures to interpret fine-grained page state as common model failure modes.
- Similar task templates are not solved consistently: GPT-4 achieves perfect success on only four of 61 templates that had at least one successful execution in the no-UA-hint analysis.

## Tags
`web-agents`, `browser-automation`, `autonomous-agents`, `agent-benchmark`, `functional-correctness`, `self-hosted-environment`, `accessibility-tree`, `long-horizon-tasks`

## Connections
- Predecessor to **VisualWebArena**, which extends the same line to visually grounded web tasks.
- Complements **Mind2Web** by using dynamic self-hosted websites rather than offline action-prediction traces.
- Used by later generalist-agent systems and platforms such as **OpenHands**, **Magentic-One**, and **BrowserGym** as a browser-agent benchmark.
- Related to **WebShop** and **MiniWoB++**, but stresses more realistic websites, cross-site tasks, user roles, and functional outcome checks.
