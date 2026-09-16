# More Agents Is All You Need

**Authors:** Junyou Li, Qin Zhang, Yangbin Yu, Qiang Fu, Deheng Ye
**arXiv:** 2402.05120
**Venue:** Transactions on Machine Learning Research
**Date:** October 2024

## Problem
Prior work improves LLM reasoning with self-consistency, prompting, or multi-agent collaboration, but it is unclear how much benefit comes from complex coordination versus simply sampling more independent agent outputs. The paper asks whether LLM performance reliably scales with the number of instantiated agents and when that scaling is most useful.

## Method
Agent Forest repeatedly queries a single LLM or an existing LLM method/framework to collect multiple candidate answers, then selects the most representative answer by voting. For closed-form tasks this is frequency or mathematical equivalence voting; for code generation the paper uses pairwise BLEU similarity among generated programs. Experiments evaluate Llama2-13B, Llama2-70B, and GPT-3.5-Turbo on GSM8K, MATH, MMLU, chess state tracking, and HumanEval, with GPT-4 used as a single-query comparison. The method is also layered on CoT, Zero-Shot CoT, SPP, Debate, and Reflection.

## Key Findings
- Accuracy generally increases with ensemble size across the evaluated non-GPT-4 backbones and five tasks; Table 2 reports improvements from single query to an ensemble size of 40.
- Smaller-model ensembles can sometimes beat larger single-query baselines, for example Llama2-13B with Agent Forest on GSM8K exceeds single-query Llama2-70B in Table 2.
- Agent Forest usually improves existing prompting and collaboration methods when added on top, but the paper reports failures for Debate with Llama2 on HumanEval due to noisy synthesized code.
- Gains are larger for weaker models and harder tasks in the GSM8K/MATH comparison, while controlled experiments show a more nuanced pattern: gains rise then fall with inherent difficulty, increase with reasoning-chain length, and improve as the prior probability of the correct answer increases.
- The main tradeoff is inference cost: token usage grows with the number of samples, so Agent Forest exchanges additional calls for higher accuracy.

## Tags
`multi-agent`, `agent-forest`, `llm-ensembling`, `self-consistency`, `inference-time-scaling`, `majority-voting`, `reasoning`, `code-generation`

## Connections
- Extends the self-consistency idea beyond chain-of-thought prompting by treating repeated LLM calls or repeated executions of a method as an agent ensemble.
- Provides a simple baseline for multi-agent papers: before attributing gains to communication or role structure, compare against independent sampling plus voting.
- Complements coordination-focused multi-agent work by showing that "more agents" can mean non-interacting replicas, not necessarily collaborative agents.
- Relevant to inference-time compute scaling and cost-aware model selection, since the paper explicitly trades additional token budget for accuracy.
