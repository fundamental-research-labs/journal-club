# AgentScope: A Flexible yet Robust Multi-Agent Platform

**Authors:** Dawei Gao, Zitao Li, Xuchen Pan, Weirui Kuang, Zhijian Ma, Bingchen Qian, Fei Wei, Wenhao Zhang, Yuexiang Xie, Daoyuan Chen, Liuyi Yao, Hongyi Peng, Zeyu Zhang, Lin Zhu, Chen Cheng, Hongzhu Shi, Yaliang Li, Bolin Ding, Jingren Zhou
**arXiv:** 2402.14034
**Venue:** Preprint
**Date:** May 2024

## Problem
Multi-agent LLM applications are harder to build than single-agent systems because developers must coordinate multiple agents, communication patterns, workflows, tools, multimodal data, external knowledge, and distributed deployments. The paper also emphasizes robustness problems: malformed LLM outputs, tool/API failures, hallucinations, and cascading errors can break an entire agent workflow.

## Method
AgentScope is a developer-oriented platform built around message exchange between agents. It defines core abstractions for messages, agents, services/tools, and workflows; adds pipeline and message-hub utilities for common interaction patterns; and provides built-in agents, service integrations, web/terminal/Gradio interfaces, a drag-and-drop workstation, and automatic prompt tuning. Robustness is handled through retry logic, rule-based output correction, custom parsers and fault handlers, agent-level critique patterns, and multi-agent logging. The platform also includes URL-based multimodal message handling, a ReAct-style service toolkit for tool use, configurable RAG agents with shared knowledge banks, and an actor-based distributed mode that can move local workflows to local or remote multi-process deployment with small configuration changes.

## Key Findings
- The paper's main contribution is a platform architecture, not a benchmark result: its evidence is primarily abstractions, modules, API examples, UI screenshots, and application walkthroughs.
- Message-based programming with pipelines and message hubs is presented as the core simplification for sequential, conditional, looped, and broadcast-style multi-agent workflows.
- AgentScope treats robustness as a platform concern with service/model retries, JSON-format repair, configurable parsing and fault handling, agent-level critique, and multi-agent logging.
- Multimodal data is passed through URL-bearing messages and lazy loading, while tools and RAG are packaged through service-toolkit and knowledge-bank abstractions.
- The actor-based distributed framework is designed to preserve a procedural workflow style while supporting automatic parallel execution and hybrid local/distributed agents.
- Demonstrations cover basic chat, group conversation, a werewolf game, distributed agents, RAG copilot, web search/retrieval, NL2SQL with tools, and the no-code workstation.

## Tags
`multi-agent`, `LLM-agents`, `agent-framework`, `message-passing`, `fault-tolerance`, `distributed-agents`, `tool-use`, `RAG`, `multimodal`, `workflow-orchestration`

## Connections
- Related to **AutoGen** and **MetaGPT** as an LLM multi-agent framework, but AgentScope emphasizes developer infrastructure: message-passing APIs, deployment modes, fault tolerance, UI/workstation support, and multimodal/tool/RAG modules.
- Useful context for papers on multi-agent coding and collaboration because it represents the kind of platform substrate those systems can build on, even though this paper does not evaluate coding-agent cooperation.
- Complements benchmark papers such as **CooperBench** and **MultiAgentBench** by describing a practical framework layer rather than a task suite.
- Connects to distributed agent orchestration work through its actor-based deployment model and placeholder mechanism for dynamic LLM-driven control flow.
