# AutoAgent: A Fully-Automated and Zero-Code Framework for LLM Agents

**Authors:** Jiabin Tang, Tianyu Fan, Chao Huang
**arXiv:** 2502.05957
**Venue:** Preprint
**Date:** October 2025 (arXiv v3; PDF header date 9 Oct 2025)

## Problem
Most LLM-agent frameworks still assume developer skill: users must write code, wire APIs, design prompts, and compose workflows. AutoAgent asks whether agent development can be made natural-language-driven, so non-programmers can create customized agents, tools, and multi-agent workflows without manual coding.

## Method
AutoAgent is framed as an "Agent Operating System" with four parts: Agentic System Utilities, an LLM-powered Actionable Engine, a Self-Managing File System, and Self-Play Agent Customization. The system includes an orchestrator plus specialized web, coding, and local-file agents; supports both direct tool-use and XML-style transformed tool-use; converts local files into queryable vector databases; and uses profiling/editor agents to generate, validate, debug, and run tools, agents, and event-driven workflows from natural-language requirements.

## Key Findings
- On GAIA validation, AutoAgent reports 55.15 average success, outperforming the listed open-source systems in Table 1 while remaining below the closed-source h2oGPTe Agent v1.6.8 overall.
- On MultiHop-RAG, AutoAgent reports 73.51% accuracy and 14.20% error, compared with LangChain agentic RAG at 62.83% accuracy and 20.50% error under the paper's gpt-4o-mini/text-embedding-3-small setup.
- Open-ended demonstrations show AutoAgent generating a DaVinci image agent, a two-agent Financial Agent, and a majority-voting math workflow from natural-language prompts.
- The generated majority-voting workflow reports 75.6 pass@1 on MATH-500, modestly above the best single model reported in Table 3 (DeepSeek-v3 at 74.2).
- Important caveat: the paper does not present a user study of non-programmers, and the open-ended creation results are mainly qualitative case studies.

## Tags
`LLM agents`, `agent frameworks`, `zero-code`, `multi-agent systems`, `tool use`, `workflow generation`, `agentic RAG`, `GAIA`, `MultiHop-RAG`

## Connections
- Extends the LangChain, AutoGen, CAMEL, MetaGPT, and OpenAgent framework line by focusing on automated creation of agents and workflows rather than developer-facing orchestration APIs.
- Useful alongside GAIA/generalist-agent work because AutoAgent evaluates a modular web-code-file agent stack on everyday multi-skill tasks.
- Connects to agentic RAG systems by treating file ingestion, vector storage, retrieval, and answer generation as agent-accessible system utilities.
- Complements multi-agent coordination papers: its emphasis is automatic construction and orchestration, while separate benchmark work is needed to test whether generated agent teams reliably coordinate under harder shared-state settings.
