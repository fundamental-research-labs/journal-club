# SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution

**Authors:** Yuxiang Wei, Olivier Duchenne, Jade Copet, Quentin Carbonneaux, Lingming Zhang, Daniel Fried, Gabriel Synnaeve, Rishabh Singh, Sida I. Wang
**arXiv:** 2502.18449
**Venue:** NeurIPS 2025
**Date:** December 2025

## Problem
Open-source models lag proprietary systems on real-world software engineering tasks such as SWE-bench, and most prior training approaches rely on supervised fine-tuning or proprietary teacher models. RL has improved reasoning in math and competitive coding, but repository-level issue fixing lacks cheap executable rewards and stable environments.

## Method
SWE-RL trains Llama-3.3-70B-Instruct on open-source software evolution data from GitHub pull requests. Each RL item contains an issue, full-file code context, and an oracle patch. The model reasons and emits search/replace edits; malformed outputs receive -1 reward, while valid patches are scored by `difflib.SequenceMatcher` similarity to the oracle patch and optimized with GRPO. Evaluation uses Agentless Mini, a simplified Agentless-derived pipeline for file localization, repair sampling, reproduction/regression test selection, and reranking.

## Key Findings
- Llama3-SWE-RL-70B reaches 41.0% pass@1 on SWE-bench Verified with Agentless Mini, above the paper's listed <=100B open-model baselines and the authors' Llama3-SWE-SFT-70B baseline.
- In a repair-only oracle-localization comparison, the RL model improves repair performance over both the base Llama-3.3-70B-Instruct model and the SFT baseline, despite similar format accuracy to SFT.
- Scaling repair samples and reproduction tests improves Agentless Mini reranking, but gains plateau after moderate sample counts.
- Out-of-domain evaluations suggest SWE-RL improves reasoning beyond issue fixing, especially on code reasoning and math, while the SFT baseline often degrades relative to the base model.
- A continuous patch-similarity reward outperforms an exact-match discrete reward, matching the paper's argument that real-world patches have many partially correct or functionally equivalent forms.

## Tags
`software-engineering`, `reinforcement-learning`, `code-repair`, `SWE-bench`, `software-evolution`, `GRPO`, `reasoning-models`, `open-source-LLMs`

## Connections
- Extends DeepSeek-R1-style rule-based RL from math and competitive coding into repository-level software engineering.
- Closely tied to SWE-bench Verified and useful when discussing trained open models for GitHub issue resolution.
- Contrasts with SWE-Gym, SWE-Fixer, and Lingma-SWE-GPT-style supervised approaches by emphasizing RL on public PR data rather than proprietary-teacher distillation.
- Complements scaffold work such as Agentless: the paper's gains depend on both model training and the Agentless Mini pipeline used for localization, testing, and reranking.
