# OpenHands: An Open Platform for AI Software Developers as Generalist Agents

**Authors:** Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, Graham Neubig
**arXiv:** 2407.16741
**Venue:** ICLR 2025
**Date:** April 2025

## Problem
AI agents that write code, operate shells, browse the web, and modify real repositories need more than prompting recipes: they need a safe runtime, durable action history, reusable tool interfaces, agent implementations, human oversight, and evaluation infrastructure. Existing frameworks cover parts of this stack, but the paper argues that research on software-using generalist agents needs an open, integrated platform.

## Method
OpenHands, formerly OpenDevin, is built around an event stream that records actions and observations, an agent abstraction that maps state to executable actions, and a Docker-sandboxed runtime exposing bash, IPython, and a Playwright browser. It adds an AgentSkills library for reusable editing and document tools, an `AgentDelegateAction` for routing subtasks to specialized agents, an agent hub with CodeActAgent, BrowsingAgent, GPTSwarm, and micro agents, and benchmark integrations for software engineering, web browsing, and miscellaneous assistance tasks.

## Key Findings
- The platform integrates 15 established benchmarks spanning software engineering, web tasks, and general assistance.
- In the paper's selected results, the same CodeActAgent family is evaluated across SWE-Bench Lite, WebArena, GPQA, and other tasks, supporting the platform's generalist-agent framing rather than a single-benchmark specialist story.
- OpenHands reports competitive but not universally best results: for example, CodeActAgent v1.8 reaches 26.0% on SWE-Bench Lite with Claude 3.5 Sonnet, 22.0% with GPT-4o, and delegated web browsing reaches 15.3% on WebArena with Claude 3.5 Sonnet.
- The platform is positioned as a community artifact: the paper reports an MIT license, more than 2.1K contributions, over 188 contributors, and a quality-control system based on integration tests and mocked LLM responses.
- The authors explicitly leave open limitations around stronger agents, long-file editing, richer multimodality, improved web browsing, and reducing hand-crafted workflows.

## Tags
`software-engineering-agents`, `agent-frameworks`, `tool-use`, `sandboxed-execution`, `event-stream`, `web-agents`, `multi-agent-delegation`, `agent-evaluation`, `open-source`

## Connections
- Closely related to **SWE-agent** and **SWE-Bench**: OpenHands generalizes software-agent interfaces and evaluates on SWE-Bench Lite while retaining bash, code execution, and repository editing as central primitives.
- Complements **WebArena**, **VisualWebArena**, **WorkArena**, and **BrowserGym** as a platform that can host browser agents and web-task evaluations.
- Provides infrastructure used or referenced by later software-agent coordination work such as **CAID**, where OpenHands supplies the agent substrate for branch-and-merge multi-agent coding.
- Useful context for **CooperBench**, **WhyMultiAgentFail**, and **SingleAgentOutperforms** because it exposes multi-agent delegation as a platform mechanism without claiming that multi-agent coordination is solved.
- Sits near **AutoGen**, **AgentScope**, and other agent frameworks, but emphasizes a software-developer-like runtime with sandboxed bash, Python, browser control, UI, and benchmark integrations.
