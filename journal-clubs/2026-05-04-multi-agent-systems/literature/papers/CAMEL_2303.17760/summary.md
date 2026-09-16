# CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society

**Authors:** Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem
**arXiv:** 2303.17760
**Venue:** NeurIPS 2023
**Date:** November 2023

## Problem
Chat-based LLMs can solve complex tasks, but practical success often depends on a human steering the conversation with domain-specific prompts. CAMEL asks whether another communicative agent can take over that steering role so LLM agents can cooperate autonomously with minimal human input.

## Method
The paper proposes a role-playing framework with an AI user, an AI assistant, and a task-specifier agent. Given an initial idea and role assignment, the task specifier turns the idea into a concrete task; the AI user decomposes the task into instructions; and the AI assistant returns instruction-following solutions until a termination condition is met. The framework relies on "inception prompting" at setup time to fix roles, define communication protocols, discourage role flipping and unsafe behavior, and provide an end-of-task token. The authors use this setup to generate AI Society and Code conversational datasets, plus Math and Science question-answer datasets, and fine-tune LLaMA-7B variants on the generated data.

## Key Findings
- Role-playing enables autonomous multi-turn task solving and synthetic instruction-data generation, but it exposes failure modes such as role flipping, repeated instructions, flake replies, and infinite conversational loops.
- The AI Society generation process uses 50 assistant roles, 50 user roles, and 10 tasks per role pair, yielding 25,000 conversations; the appendix also documents Code, Math, and Science data generation.
- In the paper's agent evaluation, CAMEL conversation-derived solutions outperform gpt-3.5-turbo single-shot solutions in human evaluation on AI Society and GPT-4 evaluation on AI Society and Code.
- Fine-tuning LLaMA-7B on progressively added CAMEL datasets improves judged performance on the newly added domains, and the final CAMEL-7B improves over base LLaMA-7B and Vicuna-7B on HumanEval/HumanEval+ pass@k in the reported experiments.
- The authors explicitly caution that generated data may contain false information, harmful-agent simulations create misuse risk, and evaluation is hard because tasks are diverse and often require domain expertise.

## Tags
`multi-agent`, `communicative-agents`, `role-playing`, `inception-prompting`, `instruction-data`, `synthetic-data`, `LLM-agents`, `agent-cooperation`, `AI-society`

## Connections
- Early foundation for LLM-based agent societies and role-conditioned multi-agent frameworks.
- Relevant to later agent frameworks that use role assignment, task decomposition, and autonomous chat loops.
- Useful counterpoint for benchmark papers on multi-agent failure: CAMEL proposes prompt protocols and termination conditions, while later work often tests whether such coordination holds up in harder environments.
- Connects synthetic instruction-data generation with multi-agent simulation, rather than relying only on single-model self-instruct pipelines.
