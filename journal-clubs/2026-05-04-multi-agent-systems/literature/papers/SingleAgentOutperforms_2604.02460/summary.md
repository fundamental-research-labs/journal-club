# Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

**Authors:** Dat Tran, Douwe Kiela (Stanford University)
**arXiv:** 2604.02460
**Venue:** COLM 2026 (preprint)
**Date:** April 2025

## Problem
Multi-agent LLM systems (MAS) often report strong results, but these comparisons are confounded by unequal test-time computation -- MAS use more tokens through multiple agent calls. When computation is normalized, it is unclear whether MAS have any inherent architectural advantage over single-agent systems (SAS) for reasoning tasks.

## Method
The authors provide an information-theoretic argument using the Data Processing Inequality: inter-agent messages are a lossy function of the full context, so MAS cannot exceed SAS in information about the answer under a fixed budget. They then run controlled experiments holding thinking-token budgets equal (100 to 10,000 tokens) across SAS and five MAS architectures (Sequential, Subtask-parallel, Parallel-roles, Debate, Ensemble). They test on two multi-hop QA benchmarks (FRAMES and MuSiQue 4-hop) with three model families (Qwen3-30B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash/Pro). They also run context degradation experiments (deletion, masking, substitution, distractors) to identify when MAS becomes competitive.

## Key Findings
- SAS matches or outperforms all MAS variants across models and datasets when thinking tokens are held constant (except at trivially small budgets like 100 tokens).
- SAS uses fewer thinking tokens than MAS while achieving equal or better accuracy.
- Debate is the most consistently strong MAS variant; Parallel-roles is the next best.
- Performance gains from more thinking tokens plateau around 1,000-2,000 tokens; beyond that, models may over-explore or overthink.
- Context degradation experiments confirm the theory: when context is corrupted (especially via substitution or masking at 70% levels), Sequential MAS catches up to or surpasses SAS, because structured decomposition compensates for degraded single-pass reasoning.
- Deep paraphrasing of benchmark questions improved model performance (Gemini SAS went from 0.331 to 0.358), suggesting original benchmarks may suffer from memorization artifacts.
- Error analysis shows SAS succeeds by staying close to question constraints, while MAS succeeds through broader exploration but often loses correct answers at the finalization/aggregation step.
- The SAS advantage holds across multiple Gemini model generations (2-Flash-Lite through 3-Pro-Preview), ruling out version-specific artifacts.

## Tags
`single-vs-multi-agent`, `compute-budget`, `multi-hop-reasoning`, `test-time-compute`, `information-theory`, `context-degradation`, `benchmark-evaluation`

## Connections
- Directly supports **WhyMultiAgentFail**: both papers identify coordination overhead and information loss as key failure modes of multi-agent systems; this paper adds formal information-theoretic grounding via DPI.
- Complements **ScienceOfScaling**: that paper studies scaling laws for multi-agent systems, while this paper shows that scaling via more agents is less efficient than giving the same compute to a single agent.
- Relates to **AgentScalingDiversity**: both study how to allocate compute across agents; this paper argues the single-agent allocation is optimal under fixed budgets for reasoning tasks.
- Contrasts with **MaAS** and **DELEGATE-52**: those papers propose multi-agent orchestration frameworks; this paper suggests their gains may come from extra compute rather than architectural benefits.
- Relevant to **CooperBench** and **MemMA**: cooperative benchmarks and memory-augmented multi-agent designs may still show MAS benefits in domains beyond multi-hop QA (e.g., tool use, long-horizon tasks) that this paper explicitly scopes out.
- Context degradation findings connect to **CAID**: understanding when single-agent context utilization breaks down helps identify the regime where multi-agent designs add genuine value.
- Echoes findings from **AI_Scientists_Dont_Reason**: both papers challenge optimistic claims about agentic LLM capabilities by applying more rigorous evaluation controls.
- The benchmark memorization findings (paraphrasing ablation) are relevant to **SlopCodeBench**, which also examines evaluation rigor for agent benchmarks.
