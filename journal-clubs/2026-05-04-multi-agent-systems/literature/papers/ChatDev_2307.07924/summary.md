# ChatDev: Communicative Agents for Software Development

**Authors:** Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, Maosong Sun
**arXiv:** 2307.07924
**Venue:** Preprint
**Date:** June 2024

## Problem
Software development requires coordinated work across requirements analysis, design, coding, review, and testing, but prior deep-learning approaches often optimize isolated waterfall phases with phase-specific models or prompts. The paper asks whether LLM-powered agents can use language itself as the shared coordination medium across the full prototype-development loop.

## Method
ChatDev is a chat-powered software-development framework built from role-specialized LLM agents. A "chat chain" decomposes development into sequential phases and subtasks: design, coding, code completion, code review, and system testing. Each subtask pairs an instructor-like agent with an assistant-like agent, using role prompts, short-term phase memory, and long-term cross-phase summaries so outputs from one step become inputs to the next. For review and testing, ChatDev adds communicative dehallucination: the assistant can ask for more specific information before producing a final code change, aiming to reduce incomplete, unexecutable, or requirement-mismatched code.

## Key Findings
- On the paper's Software Requirement Description Dataset, ChatDev reports higher average completeness, executability, consistency, and combined quality than GPT-Engineer and MetaGPT (Table 1).
- The largest reported gap is executability: ChatDev reaches 0.8800 versus 0.3583 for GPT-Engineer and 0.4145 for MetaGPT in the reported setup.
- Pairwise evaluations by GPT-4 and human judges prefer ChatDev outputs over both baselines in most comparisons (Table 2).
- Ablations indicate that later chat-chain phases improve quality, communicative dehallucination helps reduce coding hallucinations, and removing role prompts causes the largest quality drop (Table 4).
- Communication analysis suggests natural-language design discussions support system planning, while programming-language review and testing conversations drive optimization and debugging (Figures 3-5).
- The paper cautions that outputs remain closer to prototypes than production systems, depend on detailed requirements, and cost more tokens/time than single-agent baselines.

## Tags
`multi-agent`, `LLM-agents`, `software-development`, `code-generation`, `communicative-agents`, `chat-chain`, `dehallucination`, `agent-roles`, `waterfall-model`

## Connections
- Precedes and complements **MetaGPT**: both use role-specialized agents for software work, but ChatDev emphasizes multi-turn communicative refinement and dehallucination rather than standardized operating procedures alone.
- Related to **AutoGen** as an early example of programming LLM applications through structured multi-agent conversations.
- Useful historical contrast for later benchmark papers such as **CooperBench** and **CAID**, which examine when multi-agent coding coordination fails or needs stronger software-engineering primitives.
- Connects to code-generation and agent-orchestration work by treating natural language and programming language as a unified coordination substrate.
