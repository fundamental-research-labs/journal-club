# TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks

**Authors:** Frank F. Xu, Yufan Song, Boxuan Li, Yuxuan Tang, Kritanjali Jain, Mengxue Bao, Zora Z. Wang, Xuhui Zhou, Zhitong Guo, Murong Cao, Mingyang Yang, Hao Yang Lu, Amaad Martin, Zhe Su, Leander Melroy Maben, Raj Mehta, Wayne Chi, Lawrence Jang, Yiqing Xie, Shuyan Zhou, Graham Neubig
**arXiv:** 2412.14161
**Venue:** Preprint
**Date:** September 2025

## Problem
Claims about AI agents automating professional work need benchmarks that look more like real digital workplaces than single-app web tasks or pure coding tasks. The paper targets the gap between broad automation claims and existing evaluations by asking whether LLM agents can perform consequential software-company work involving web apps, code, documents, terminal use, and communication with colleagues.

## Method
TheAgentCompany is a self-hosted simulated software company. Agents work in a local Docker workspace and an intranet composed of GitLab, ownCloud, Plane, and RocketChat, with simulated colleagues implemented through Sotopia. The benchmark contains 175 curated tasks across software engineering, project management, data science, administration, HR, finance, and other work categories. Each task has an intent, checkpoints, initialization/finalization logic, and evaluators that support both full completion and partial-credit scoring. Baselines use OpenHands CodeAct with Browsing and OWL RolePlay over closed and open-weight model backbones.

## Key Findings
- The best reported baseline, OpenHands with Gemini-2.5-Pro, completes 30.3% of tasks and reaches a 39.3% partial-completion score, showing nontrivial but far from complete workplace automation.
- Frontier closed models lead the benchmark, while open-weight models trail substantially in the reported runs.
- RocketChat and ownCloud tasks are especially difficult, suggesting that social interaction and complex workplace web UIs remain major bottlenecks.
- Software-engineering and project-management tasks are easier for the tested agents than data-science, administrative, and finance tasks, despite those latter categories often seeming less specialized to humans.
- Common failures include missing social implications in colleague messages, getting stuck in browser interfaces, and inventing fake shortcuts when the agent cannot find the right path.
- The benchmark is deliberately scoped: it uses relatively concrete, automatically evaluable tasks, does not report human performance, and evaluates only two agent scaffolds.

## Tags
`agent-benchmark`, `workplace-automation`, `web-agents`, `LLM-agents`, `simulated-company`, `OpenHands`, `checkpoint-evaluation`, `human-agent-interaction`

## Connections
- Extends the direction of WebArena, VisualWebArena, OSWorld, and WorkArena toward a self-hosted multi-application workplace environment.
- Complements SWE-bench and DevBench by including software-engineering work but embedding it inside broader company workflows.
- Related to Sotopia through its use of simulated colleagues for workplace communication.
- Useful counterweight for claims about near-term labor automation: it shows that some well-scoped digital tasks are solvable, but long-horizon and communication-heavy tasks remain difficult.
- Relevant to multi-agent coding and collaboration papers such as CooperBench and CAID because it provides another environment where coordination, communication, and tool use determine agent success.
