# Mind2Web: Towards a Generalist Agent for the Web

**Authors:** Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Samuel Stevens, Boshi Wang, Huan Sun, Yu Su
**arXiv:** 2306.06070
**Venue:** NeurIPS 2023 Datasets and Benchmarks Track
**Date:** December 2023

## Problem
Web agents need to execute high-level natural-language instructions on real, dynamic websites, but earlier datasets were often simulated, limited to a small set of sites, or framed around low-level step-by-step instructions. The paper targets generalization to unseen websites and even unseen domains while preserving the complexity of real web pages.

## Method
Mind2Web is a dataset of crowdsourced high-level tasks, action sequences, webpage snapshots, and traces from real websites. The authors collect tasks across 137 websites and 31 domains, verify demonstrations, and define cross-task, cross-website, and cross-domain evaluation splits. They also introduce MindAct, a two-stage baseline: a fine-tuned DeBERTa ranker filters thousands of DOM elements into candidates, then a language model predicts the target element and operation using a multiple-choice action-prediction formulation.

## Key Findings
- Mind2Web contains 2,350 retained tasks over 137 real-world websites in 31 domains, with high-level instructions, an average of 1,135 page elements, and an average of 7.3 actions per task.
- The candidate generator reaches high Recall@50 across the three splits, making it practical to present a much smaller candidate set to the action-prediction model.
- MindAct's multiple-choice formulation substantially outperforms direct element generation and a pure classification baseline, but full-task success remains low because one wrong step fails the whole task.
- Performance is best on cross-task evaluation and notably weaker on unseen websites and unseen domains, suggesting that grounding actions in unfamiliar page structures is still the main bottleneck.
- GPT-4 shows promise in the same multiple-choice format, but the paper evaluates it on a budget-limited subset and flags operational cost as a concern.

## Tags
`web-agents`, `browser-automation`, `grounded-language`, `benchmarks`, `html`, `dom-grounding`, `llm-agents`, `datasets`

## Connections
- Useful companion to **WebArena**, **WorkArena**, and **OSWorld** when distinguishing offline action-prediction benchmarks from live or interactive agent environments.
- Related to tool-use and grounded-language papers because Mind2Web turns websites into a natural-language-controlled action environment rather than a simple retrieval tool.
- The candidate-ranking plus LLM-prediction design is an early pattern for handling web pages that are too large to fit directly into an LLM context.
