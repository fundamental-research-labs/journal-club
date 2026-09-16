# ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
**arXiv:** 2210.03629
**Venue:** ICLR 2023
**Date:** October 2022 arXiv; local ICLR version dated March 2023

## Problem
LLMs can produce chain-of-thought reasoning, and they can also be prompted or trained to act in external environments, but these capabilities were often treated separately. Reason-only prompting can hallucinate or propagate errors because it is not grounded in external observations, while action-only agents can lose track of goals, fail to plan, or repeat invalid actions in long-horizon environments.

## Method
ReAct augments an agent's action space with free-form language "thoughts" and prompts a frozen LLM to generate interleaved trajectories of thoughts, task-specific actions, and observations. On HotpotQA and FEVER, the agent uses a small Wikipedia API with `search`, `lookup`, and `finish` actions; on ALFWorld and WebShop, thoughts appear more sparsely to decompose goals, track subgoals, choose search strategies, and connect observations to actions. The main experiments use few-shot prompts with PaLM-540B, with additional GPT-3 and finetuning experiments in the appendix/main analysis.

## Key Findings
- On HotpotQA and FEVER, ReAct beats the action-only baseline, and hybrid ReAct/CoT-SC strategies perform best among the prompting methods in Table 1.
- Human trajectory analysis on HotpotQA finds ReAct is more grounded than CoT, with fewer hallucinated successful traces and no hallucination-labeled failures in the sampled ReAct failures, but more reasoning and search-result errors.
- On ALFWorld and WebShop, sparse reasoning improves interactive decision making: the best ReAct ALFWorld trial reaches 71% overall success versus 45% for Act and 37% for BUTLER, and WebShop success rises from 30.1% for Act to 40.0% for ReAct.
- ReAct-style finetuning on generated trajectories is reported as especially helpful for smaller PaLM models on HotpotQA, suggesting that reasoning-action traces are useful training data beyond in-context prompting.
- The paper emphasizes interpretability and controllability because thoughts, actions, and observations expose why the model acted and can be edited by a human in the loop.

## Tags
`language-agents`, `reasoning`, `acting`, `tool-use`, `chain-of-thought`, `few-shot-prompting`, `interactive-decision-making`, `knowledge-intensive-qa`, `web-navigation`

## Connections
- Extends chain-of-thought prompting by grounding reasoning in external observations and actions.
- Prefigures later tool-use and web-agent benchmarks such as Mind2Web, WebArena, VisualWebArena, WebVoyager, and BrowserGym.
- Connects to AgentBench and AgentBoard as an early template for evaluating LLM agents through trajectories rather than isolated answers.
- Contrasts with pure action-generation approaches and with embodied planners such as SayCan or Inner Monologue by making internal reasoning flexible, explicit, and interleaved with feedback.
