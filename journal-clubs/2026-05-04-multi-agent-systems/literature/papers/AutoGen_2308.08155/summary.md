# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

**Authors:** Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Awadallah, Ryen W. White, Doug Burger, Chi Wang
**arXiv:** 2308.08155
**Venue:** Preprint
**Date:** October 2023

## Problem
LLM applications increasingly need agents that can reason, use tools, execute code, incorporate feedback, and coordinate with humans or other agents. Before AutoGen, much of this orchestration was either task-specific or locked into fixed interaction patterns, making it hard to reuse agents across domains or experiment with different collaboration structures.

## Method
AutoGen is an open-source framework that models LLM applications as multi-agent conversations. Its core abstraction is the conversable agent: an entity with a role, message history, and configurable capabilities backed by LLM calls, human input, tool execution, or combinations of these. The paper introduces "conversation programming," where developers define agents and then specify conversation-centric computation and conversation-driven control flow using natural language prompts, Python code, auto-reply functions, termination conditions, function calls, and group-chat managers. The paper demonstrates the framework through math problem solving, retrieval-augmented chat, ALFWorld decision making, OptiGuide multi-agent coding, dynamic group chat, and conversational chess.

## Key Findings
- Built-in AutoGen agents achieved the strongest reported MATH performance among the compared methods in the paper's experiments, including 69.48% accuracy on the full MATH test set versus 55.18% for vanilla GPT-4.
- Retrieval-augmented Chat's interactive retrieval improved Natural Questions results over the non-interactive variant and DPR in the reported setup (25.88 F1 / 66.65 recall versus 22.79 / 62.59 and 15.12 / 58.56).
- On ALFWorld, adding a grounding agent raised average task success from 54% for the two-agent AutoGen setup to 69%, helping avoid repetitive commonsense error loops.
- In the OptiGuide coding application, AutoGen reduced the core workflow code from over 430 lines to 100 lines and reduced user interaction burden by roughly 3x to 5x in the reported evaluations.
- A dynamic group-chat pilot on 12 tasks found that GroupChat with GPT-4 solved 11 tasks versus 9 for a two-agent chat, with fewer average LLM calls and no termination failures.

## Tags
`multi-agent`, `LLM-agents`, `conversation-programming`, `agent-frameworks`, `tool-use`, `code-execution`, `human-in-the-loop`, `RAG`, `AutoGen`

## Connections
- Foundational infrastructure paper for later multi-agent coding and orchestration work such as **CAID** and **CooperBench**: AutoGen proposes reusable abstractions, while later work probes when collaboration helps or fails.
- Useful contrast to papers arguing that naive multi-agent systems underperform single agents; AutoGen's main claim is that agent roles, tools, human control, and programmable conversation patterns are the coordination substrate.
- Connects to RAG, tool-use, and online decision-making agent literature by showing how the same conversation framework can wrap retrieval, code execution, environment feedback, and safeguards.
