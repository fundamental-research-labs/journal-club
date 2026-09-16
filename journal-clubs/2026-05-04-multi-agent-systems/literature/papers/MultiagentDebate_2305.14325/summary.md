# Improving Factuality and Reasoning in Language Models through Multiagent Debate

**Authors:** Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, Igor Mordatch
**arXiv:** 2305.14325
**Venue:** Preprint
**Date:** May 2023

## Problem
LLMs can hallucinate facts and make brittle reasoning jumps even when prompted with chain-of-thought, reflection, or self-consistency methods. The paper asks whether multiple independent LLM instances can cross-check one another through iterative debate and converge on more reliable final answers without model internals.

## Method
The method instantiates multiple copies of a language model as agents. Each agent first answers the same query independently; in later rounds, each agent receives the other agents' responses in a consensus prompt and updates its own answer. The procedure is task-agnostic and black-box: it uses ordinary generations rather than likelihoods, gradients, or fine-tuning. Most experiments use `gpt-3.5-turbo-0301`, three agents, and two debate rounds, with analyses varying the number of agents, rounds, prompts, summarization, and mixed ChatGPT/Bard agents.

## Key Findings
- Debate improves reasoning over single-agent, reflection, and majority baselines on arithmetic, GSM8K, and chess move prediction in Table 1.
- Debate improves factuality on generated computer-scientist biographies, MMLU, and chess move validity in Table 2.
- The paper introduces a biography factuality benchmark with 524 computer scientists and model-judged agreement against Wikipedia-derived facts.
- More agents and more debate rounds improve arithmetic performance in the tested range, while prompt wording controls how quickly agents converge.
- Debate can recover from cases where all agents are initially wrong, but it can also converge confidently to an incorrect answer.
- The approach is more computationally expensive than single-pass prompting because it requires multiple generations across multiple rounds.

## Tags
`multi-agent`, `debate`, `llm-inference`, `factuality`, `reasoning`, `consensus`, `self-critique`, `black-box`

## Connections
- Early prompt-only template for multi-agent LLM inference: agents share candidate answers and critiques before a final answer.
- Complements self-consistency and majority voting by using language-model critique to revise answers, not just aggregate samples.
- Related to later mixture/ensemble agent work such as **MixtureofAgents**, but debate is iterative and bidirectional rather than a one-way aggregation layer.
- Relevant to **AgentScalingDiversity** because it studies agent count, rounds, prompt heterogeneity, and summarization as scaling knobs.
- Useful contrast for coordination-failure papers such as **CooperBench**: debate improves closed-form QA-style tasks, but the paper does not address shared-state collaboration or long-horizon software work.
