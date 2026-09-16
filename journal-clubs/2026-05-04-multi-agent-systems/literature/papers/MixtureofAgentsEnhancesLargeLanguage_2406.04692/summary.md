# Mixture-of-Agents Enhances Large Language Model Capabilities

**Authors:** Junlin Wang, Jue Wang, Ben Athiwaratkun, Ce Zhang, James Zou
**arXiv:** 2406.04692
**Venue:** Preprint
**Date:** June 2024

## Problem
LLMs have different strengths, but using them together is nontrivial: simple reranking can only select an existing answer, and retraining or model fusion can be costly or inaccessible. The paper asks whether multiple off-the-shelf LLMs can be composed through prompting so that their combined response is better than any one model's standalone output.

## Method
Mixture-of-Agents (MoA) is a layered, prompt-only ensemble. In the first layer, several proposer models independently answer the user prompt. Later layers receive the prompt plus prior model outputs and use an aggregate-and-synthesize instruction to produce refined responses. The default open-source MoA uses Qwen1.5-110B-Chat, Qwen1.5-72B-Chat, WizardLM-8x22B, LLaMA-3-70B-Instruct, Mixtral-8x22B-v0.1, and dbrx-instruct across three layers, with Qwen1.5-110B-Chat as the final aggregator. Variants include MoA-Lite with fewer layers and MoA w/ GPT-4o as the final aggregator.

## Key Findings
- On AlpacaEval 2.0, the open-source MoA reports a 65.1% length-controlled win rate versus 57.5% for GPT-4 Omni in the paper's June 2024 comparison; MoA w/ GPT-4o reports 65.7%.
- On MT-Bench, MoA w/ GPT-4o and open-source MoA score 9.40 and 9.25 respectively, above the listed GPT-4 Omni score of 9.19.
- On FLASK, MoA improves several dimensions over the Qwen1.5-110B-Chat aggregator and outperforms GPT-4 Omni on some dimensions, though it is weaker on conciseness.
- MoA outperforms an LLM-ranker baseline, suggesting that aggregation is not merely selecting a proposer output.
- Diverse proposers help: in the two-layer Qwen1.5-110B-Chat aggregation setup, six different proposers score higher than six samples from one proposer.
- The main limitation is latency: iterative full-response aggregation delays time to first token, so thinner or chunk-wise variants may be needed for interactive use.

## Tags
`multi-agent`, `LLM-ensemble`, `mixture-of-agents`, `aggregation`, `proposer-aggregator`, `AlpacaEval`, `MT-Bench`, `FLASK`, `open-source-LLMs`

## Connections
- Related to model-ensemble and routing work such as LLM-Blender, FrugalGPT, and mixture-of-experts, but MoA composes complete LLMs through prompting instead of training routers, fusion models, or internal expert layers.
- Complements multi-agent debate and discussion papers by using a structured, feed-forward proposer/aggregator pipeline rather than free-form deliberation.
- Relevant to **CooperBench** and **CAID** as a positive multi-agent result, but in response synthesis rather than shared-codebase collaboration.
- Useful counterpoint to claims that a single strong agent is enough: this paper shows gains from multiple models, while its limitations clarify that the gains come with added inference cost and latency.
