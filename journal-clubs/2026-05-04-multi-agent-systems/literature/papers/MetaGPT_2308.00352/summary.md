# MetaGPT: Meta Programming for Multi-Agent Collaborative Framework

**Authors:** Sirui Hong, Mingchen Zhuge, Jiaqi Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, Jurgen Schmidhuber
**arXiv:** 2308.00352
**Venue:** ICLR 2024
**Date:** November 2024 (arXiv v7; ICLR 2024 conference paper)

## Problem
LLM-based multi-agent systems can solve simple dialogue tasks, but naive chaining and open-ended role-play can create inconsistent handoffs, irrelevant chatter, repeated instructions, and cascading hallucinations. The paper asks how to make multi-agent collaboration reliable enough for complex software-development workflows rather than isolated coding prompts.

## Method
MetaGPT models a software company with specialized agents: Product Manager, Architect, Project Manager, Engineer, and QA Engineer. It encodes standard operating procedures (SOPs) as prompt-driven handoffs: user requirements become a PRD, architecture artifacts, task assignments, code, tests, and final software. Communication is structured around documents, diagrams, schemas, a shared message pool, and role-specific subscriptions rather than free-form dialogue. Engineers also use executable feedback: after code generation, they run tests, inspect execution errors, and retry debugging up to a fixed limit.

## Key Findings
- With GPT-4 as the backend, MetaGPT reports 85.9% Pass@1 on HumanEval and 87.7% Pass@1 on MBPP, outperforming the compared code-generation baselines in Figure 4.
- On the SoftwareDev benchmark, MetaGPT receives higher executability scores and lower human revision cost than ChatDev in the main comparison; Appendix Table 4 reports 3.9 average executability for MetaGPT versus 2.1 for ChatDev and 1.0 for AutoGPT, LangChain, and AgentVerse on seven representative tasks.
- Role specialization matters: the role ablation shows engineer-only generation is weak, while adding Product Manager, Architect, and Project Manager improves executability and reduces human revisions.
- Executable feedback adds measurable gains beyond the base workflow, with reported Pass@1 improvements of 4.2 points on HumanEval and 5.4 points on MBPP, plus lower revision cost on SoftwareDev.
- The scope is not production-complete: the authors note limitations for specific UI/frontend scenarios, multimodal tools, user interruption/checkpointing, and satisfying diverse real-world requirements.

## Tags
`multi-agent`, `LLM-agents`, `software-engineering`, `agent-framework`, `SOP`, `structured-communication`, `code-generation`, `executable-feedback`, `role-specialization`, `MetaGPT`

## Connections
- Precedes and contrasts with **AutoGen**: AutoGen generalizes multi-agent conversation programming, while MetaGPT hard-codes a software-company workflow with standardized artifacts.
- Closely related to **ChatDev**: both use role-specialized software agents, but MetaGPT argues for SOP-style document handoffs and executable feedback instead of primarily chat-chain coordination.
- Relevant to **CAMEL** and **AgentVerse** as an example of moving from open-ended role play toward constrained, task-oriented multi-agent workflows.
- Useful background for later skepticism in **CooperBench** and later engineering patterns in **CAID**: MetaGPT shows early gains from structured coordination, while those later works study where multi-agent coding still fails and how stronger repository-level primitives help.
