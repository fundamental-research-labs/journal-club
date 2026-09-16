# Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, Shangding Gu
**arXiv:** 2602.03794
**Venue:** ICML 2026 (accepted)
**Date:** February 2025

## Problem
Scaling LLM-based multi-agent systems (MAS) by adding more agents shows strong diminishing returns when agents are homogeneous (same model, prompts, tools). Why does this happen, and why does agent diversity help?

## Method
The authors develop an information-theoretic framework showing that MAS performance is bounded by intrinsic task uncertainty H(Y|X), not by agent count. They derive architecture-agnostic bounds proving that improvements depend on the number of "effective channels" -- independent, non-redundant reasoning paths -- rather than raw agent calls. Homogeneous agents saturate early because their outputs are strongly correlated, while heterogeneous agents contribute complementary evidence. They introduce K*, a label-free metric based on the entropy effective rank of the cosine-similarity Gram matrix of agent output embeddings, to quantify effective channels without ground-truth labels. They decompose K* into K*_c (correct reasoning diversity) and K*_w (incorrect reasoning diversity) to show that not all diversity is beneficial -- only diversity among correct paths helps.

## Key Findings
- Homogeneous scaling shows clear diminishing returns: marginal gains collapse toward zero after N=4 agents across all 7 benchmarks
- 2 diverse agents (full diversity, L4) match or exceed 16 homogeneous agents (L1), an 8x reduction in agent count
- Four diversity layers tested: L1 (no diversity) < L2 (persona only) < L3 (model only) < L4 (model + persona), with L4 consistently best
- Heterogeneous configs outperform homogeneous by +4.4 to +8.6 points on average for Vote, and +3.3 to +6.6 for Debate
- K* correlates positively with accuracy; high K*_c / K*_w ratio (correct-path diversity dominates incorrect-path diversity) predicts strong performance
- Information recovery follows a geometric contraction curve: residual uncertainty decays as (1-alpha)^K, explaining the "fast-then-slow" scaling pattern
- Models tested: Qwen-2.5-7B, Llama-3.1-8B, Mistral-7B across GSM8K, ARC, Formal Logic, TruthfulQA, HellaSwag, WinoGrande, Pro Medicine
- Design guideline: homogeneous systems plateau at N~4; heterogeneous systems benefit up to N~8

## Tags
`multi-agent-scaling`, `diversity`, `information-theory`, `effective-channels`, `voting`, `debate`, `diminishing-returns`, `agent-heterogeneity`

## Connections
- **ScienceOfScaling**: Both study when scaling agent count helps. Kim et al. find diminishing returns beyond a single-agent performance threshold; this paper provides the information-theoretic explanation (bounded by effective channels, not agent count).
- **SingleAgentOutperforms**: Tran & Kiela argue single agents are more information-efficient under fixed token budgets. This paper reconciles that finding -- homogeneous multi-agent scaling is indeed wasteful, but diverse multi-agent setups can overcome the efficiency gap.
- **WhyMultiAgentFail**: Cemri et al. taxonomize MAS failure modes including inter-agent misalignment. This paper formalizes one root cause: correlated agent outputs (redundancy) as a source of diminishing returns.
- **MaAS**: Zhang et al. show optimal MAS topology is query-dependent. This paper's K* metric could serve as a signal for MaAS-style architecture selection by measuring effective channel diversity.
- **CAID**: Geng & Neubig show genuine multi-agent gains on architectural tasks with natural decomposition. This paper's framework explains why: tasks with decomposable structure naturally produce higher K* when agents work on different sub-problems.
- **CooperBench**: Both papers highlight that simply adding agents is not enough. CooperBench shows social intelligence bottlenecks; this paper shows information-theoretic bottlenecks from homogeneity.
- **AI_Scientists_Dont_Reason**: Rios-Garcia et al. find scaffold design explains only 1.5% of variance. This paper suggests that diversity across base models (not just scaffolding) is the key lever for multi-agent gains.
