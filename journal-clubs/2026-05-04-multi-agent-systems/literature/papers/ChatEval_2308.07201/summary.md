# ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate

**Authors:** Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu, Zhiyuan Liu, Jie Fu, Wei Xue, Shanghang Zhang
**arXiv:** 2308.07201
**Venue:** Preprint
**Date:** August 2023

## Problem
Human evaluation of generated text is expensive, slow, and variable, while traditional automatic metrics often correlate poorly with human preferences on open-ended generation. Single LLM-as-a-judge prompting helps, but the paper argues that a single evaluator can still miss the diversity and deliberation present in human annotation processes.

## Method
ChatEval casts several LLMs as a referee team that discusses candidate responses before producing an evaluation. Each agent receives a role/persona prompt and sees prior messages according to one of three communication strategies: one-by-one, simultaneous-talk, or simultaneous-talk-with-summarizer. The final decision is extracted by majority vote for pairwise comparison tasks or by averaging scores for scoring tasks. Experiments use homogeneous GPT-family groups with position calibration and compare against single-agent evaluators, FairEval, G-EVAL, and traditional metrics on FairEval open-ended QA and Topical-Chat dialogue response evaluation.

## Key Findings
- Multi-agent debate improves over single-agent evaluation on FairEval for both ChatGPT and GPT-4, and the best reported ChatEval setting slightly exceeds FairEval's reported MEC+BPC baselines.
- On Topical-Chat, ChatEval improves average correlation with human judgments over the corresponding single-agent GPT-4 evaluator and over G-EVAL-4, while ChatGPT gains are smaller and mixed by dimension.
- Diverse role prompts matter: replacing personas with the same generic annotator role removes the FairEval gain over the single-agent baseline in the reported ablation.
- Communication structure matters: one-by-one discussion performs best among the tested strategies on FairEval, while simultaneous variants show higher accuracy than the naive single-agent setting in the ChatGPT analysis.
- More roles help only up to a point, and additional discussion turns do not show a clear monotonic benefit, suggesting context growth and repeated debate can limit returns.

## Tags
`LLM-as-a-judge`, `multi-agent`, `debate`, `text-evaluation`, `NLG-evaluation`, `role-prompting`, `agent-communication`

## Connections
- Early example of using multi-agent debate not for task solving directly, but as an evaluator architecture for generated text.
- Complements single-agent LLM evaluator work such as FairEval and G-EVAL by adding deliberation, role diversity, and communication protocols.
- Useful contrast point for later multi-agent coding/cooperation papers: ChatEval reports gains from structured debate in evaluation, while papers like CooperBench stress that communication can also introduce coordination failures in coding settings.
