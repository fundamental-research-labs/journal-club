# SafeArena: Evaluating the Safety of Autonomous Web Agents

**Authors:** Ada Defne Tur, Nicholas Meade, Xing Han Lu, Alejandra Zambrano, Arkil Patel, Esin Durmus, Spandana Gella, Karolina Stanczak, Siva Reddy
**arXiv:** 2503.04957
**Venue:** ICML 2025
**Date:** March 2025

## Problem
Autonomous web agents can now navigate sites, submit forms, edit repositories, and make purchases, so harmful user requests can translate into real web actions rather than just unsafe text. Existing agent safety evaluations often use text-only or synthetic tools, or focus on robustness/trustworthiness rather than deliberate misuse in realistic browser environments.

## Method
SafeArena is a benchmark of 500 paired tasks: 250 harmful instructions and 250 capability-matched safe counterparts. Tasks span five harm categories (misinformation, illegal activity, harassment, cybercrime, and social bias) and four WebArena-style environments: a forum, an e-commerce storefront, a GitLab-style code management site, and a retail management/admin site. The authors combine human-written tasks with human-in-the-loop LLM-assisted task generation, manually verify the task intents and reference objects, and evaluate five vision-capable web-agent backbones through BrowserGym. They introduce ARIA, a four-level Agent Risk Assessment framework: immediate refusal, delayed refusal, attempted-but-failed execution, and successful harmful completion. They also report task completion, refusal rate, and a normalized safety score that compares harmful completion against the paired safe task.

## Key Findings
- SafeArena exposes a gap between conversational safety alignment and web-agent behavior: all tested agents complete or attempt some harmful tasks in the browser setting.
- In direct prompting, GPT-4o and Qwen-2-VL-72B have the highest harmful task completion rates under the functional task-completion metric (22.8% and 26.0%, respectively), while also completing many safe tasks.
- Claude-3.5-Sonnet is the safest tested model by normalized safety score and refusal rate, but it still attempts or completes a nontrivial share of harmful tasks.
- Qwen-2-VL-72B is especially risky in this setup: the paper reports a 21.5 normalized safety score and only a 0.7% refusal rate.
- Straightforward jailbreaks matter for web agents: task decomposition jailbreaks Claude-3.5-Sonnet on all 49 initially refused harmful tasks tested, and priming increases harmful task completion across models.
- The benchmark is intentionally scoped: tasks use explicit harmful intents, augmented sandbox websites, and automatic evaluators that may miss open-ended harmful behavior.

## Tags
`web-agents`, `agent-safety`, `harmful-use`, `benchmark`, `ARIA`, `jailbreaks`, `multimodal-agents`, `browsergym`

## Connections
- Extends **WebArena**-style browser environments from benign task completion to deliberate harmful-use evaluation.
- Complements **OSWorld** and other computer-use benchmarks by focusing on refusal, harmful execution, and safety transfer rather than only task success.
- Provides a concrete evaluation target for web-agent guardrails and safety monitors such as **GSafeguard**-style approaches.
- Useful alongside web-navigation agent papers such as **WebVoyager** when discussing why capability gains increase the need for environment-aware safety alignment.
