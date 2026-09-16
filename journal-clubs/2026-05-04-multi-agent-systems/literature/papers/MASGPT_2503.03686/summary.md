# MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems

**Authors:** Rui Ye, Shuo Tang, Rui Ge, Yaxin Du, Zhenfei Yin, Siheng Chen, Jing Shao
**arXiv:** 2503.03686
**Venue:** Preprint
**Date:** March 2025

## Problem
LLM-based multi-agent systems can outperform a single LLM on difficult tasks, but many systems depend on fixed human-designed roles and workflows or require repeated LLM calls to adapt the agent team to each query. This makes them costly, hard to generalize across domains, and inconvenient to deploy at scale.

## Method
MAS-GPT reframes MAS construction as a supervised generation task: given a user query, generate an executable Python `forward` function that defines agent prompts, LLM calls, and inter-agent information flow. The authors construct query-MAS training pairs by building query and MAS pools, evaluating query-MAS compatibility, selecting high-performing MAS designs with inter-consistency across similar queries, and refining pairs for query-specific intra-consistency. They then fine-tune Qwen2.5-Coder-32B-Instruct so MAS-GPT can generate a query-adaptive MAS in one inference; the generated MAS is then executed with a chosen MAS-driving LLM to answer the original query.

## Key Findings
- The constructed training set contains 11,442 query-MAS samples and 7,580 unique MAS variants after selection and refinement.
- With Llama-3-70B-Instruct as the MAS-driving model, MAS-GPT has the best average score in Table 2 across eight benchmarks, including math, coding, general QA, and science tasks.
- The approach also has the best average score with Qwen2.5-72B-Instruct and GPT-4o-mini MAS drivers in Table 3, suggesting the generated MAS are not tied to one underlying answer model.
- On AIME-2024, MAS-GPT improves over single o1-preview and DeepSeek-R1 inference in the paper's reported comparison, but this is a small 30-problem benchmark.
- Ablations show that inter-consistency selection, MAS adjustment, and reasoning-process refinement each contribute to performance; scaling experiments suggest more training data and larger base models improve MAS generation.

## Tags
`multi-agent`, `LLM-agents`, `agent-orchestration`, `MAS-generation`, `supervised-fine-tuning`, `synthetic-data`, `query-adaptive-agents`, `executable-code`

## Connections
- Related to **AutoGen**, **AgentVerse**, **MetaGPT**, and **ChatDev** as prior LLM-based MAS frameworks, but MAS-GPT focuses on generating a query-specific system rather than manually specifying a fixed workflow.
- Contrasts with adaptive MAS optimizers such as **DyLAN**, **GPTSwarm**, **ADAS**, and **AFlow** by moving per-query search into a trained generator, trading one-time training cost for lower inference-time construction cost.
- Relevant to papers on multi-agent scaling and coordination because it treats MAS topology and agent prompts as learned artifacts rather than hand-authored design choices.
- Useful background for benchmark discussions involving MATH, GSM8K, HumanEval, MMLU, GPQA, SciBench, and AIME-2024 in multi-agent LLM settings.
