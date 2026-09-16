# Multi-agent Architecture Search via Agentic Supernet

**Authors:** Guibin Zhang, Luyang Niu, Junfeng Fang, Kun Wang, Lei Bai, Xiang Wang
**arXiv:** 2502.04180
**Venue:** ICML 2025
**Date:** February 2025

## Problem
Existing methods for automating multi-agent system design search for a single, static, one-size-fits-all architecture. This fails to dynamically allocate inference resources based on query difficulty and domain, wasting compute on easy queries and underperforming on hard or cross-domain tasks.

## Method
MaAS introduces the "agentic supernet," a probabilistic distribution over multi-agent architectures inspired by neural architecture search (NAS) supernets like DARTS. Instead of finding one optimal system, MaAS optimizes a distribution of systems. A controller network (MoE-style, using lightweight embeddings) samples a query-dependent multi-agent architecture from the supernet at inference time. The supernet is a cascaded multi-layer DAG where each layer has a probability distribution over agentic operators (CoT, Debate, Self-Refine, ReAct, Ensemble, Self-Consistency, Testing, and an early-exit operator). The number of active operators per layer and the depth of the pipeline are both query-dependent. Training jointly updates the distribution parameters (via Monte Carlo gradient estimation) and the operators themselves (via LLM-based textual gradients for prompt and structure refinement), with a cost penalty term to encourage token efficiency.

## Key Findings
- Outperforms 14 baselines across 6 benchmarks (GSM8K, MATH, MultiArith, HumanEval, MBPP, GAIA) by 0.54%-16.89% on average, achieving 83.59% average accuracy on the first five benchmarks with gpt-4o-mini
- On GAIA (tool use), achieves 20.69% average accuracy vs. 16.34% for the best baseline (AgentSquare)
- Uses only 6-45% of the inference cost of existing handcrafted or automated multi-agent systems
- On MATH: training costs $3.38 (vs. AFlow's $22.50, a 6.8x reduction) and inference costs $0.42 (vs. AFlow's $1.66), while achieving higher accuracy (51.82% vs. 51.28%)
- Training wall-clock time is 53 minutes vs. 184 minutes for AFlow and 508 minutes for DyLAN
- Transfers well across LLM backbones (gpt-4o-mini, Qwen-2.5-72b, llama-3.1-70b) and across datasets (e.g., MATH-trained supernet achieves 92.80% on GSM8K)
- Generalizes inductively to unseen operators not seen during training (e.g., Debate operator)
- Ablation shows textual gradient is the most critical component; removing early-exit or cost constraint mainly increases inference cost without large accuracy changes

## Tags
`multi-agent-systems`, `automated-agent-design`, `architecture-search`, `neural-architecture-search`, `resource-efficiency`, `query-adaptive`, `agentic-supernet`

## Connections
- Directly relevant to **AgentScalingDiversity**: both study how to compose multiple agents, but MaAS automates the architecture search rather than studying scaling laws of fixed designs
- Contrasts with **SingleAgentOutperforms**: MaAS shows multi-agent systems can beat single agents when the architecture is adaptively selected per query, which may reconcile findings where static multi-agent setups underperform
- Relates to **WhyMultiAgentFail**: MaAS's query-dependent resource allocation addresses the failure mode of applying overly complex multi-agent pipelines to simple queries
- Connects to **ScienceOfScaling**: both consider how to efficiently allocate compute, but MaAS does so at the architecture level rather than model scale
- Relevant to **CooperBench** and **DELEGATE-52**: MaAS could be evaluated on these collaboration benchmarks to test whether adaptive architecture search improves cooperative task performance
- Complements **SlopCodeBench**: MaAS includes code generation benchmarks (HumanEval, MBPP) and its resource-efficiency findings are relevant to understanding cost vs. quality tradeoffs in agentic code generation
- Related to **CAID** and **MemMA**: MaAS's operator set could potentially incorporate memory-augmented or identity-aware agents as additional operators in the supernet
