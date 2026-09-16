# MLGym: A New Framework and Benchmark for Advancing AI Research Agents

**Authors:** Deepak Nathani, Lovish Madaan, Nicholas Roberts, Nikolay Bashlykov, Ajay Menon, Vincent Moens, Amar Budhiraja, Despoina Magka, Vladislav Vorotilov, Gaurav Chaurasia, Dieuwke Hupkes, Ricardo Silveira Cabral, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach, William Yang Wang, Roberta Raileanu
**arXiv:** 2502.14499
**Venue:** Preprint
**Date:** February 21, 2025

## Problem
AI research agents need evaluations that go beyond code repair, Kaggle-style submissions, or narrow ML engineering tasks. Existing agent benchmarks do not provide a unified Gym-style environment for training/evaluating agents on open-ended machine learning research workflows with diverse artifacts, task metrics, datasets, and experimental feedback.

## Method
MLGym defines a Gymnasium-compatible environment where an LLM agent interacts with a dockerized shell workspace, task code, datasets, read-only evaluation scripts, validation/submit commands, and optional tools such as literature search and memory. MLGym-Bench instantiates the framework with 13 Level-1 "baseline improvement" tasks across data science, 3-SAT, game theory, computer vision, NLP, and reinforcement learning. The experiments evaluate a SWE-Agent-style scaffold with five frontier backbone models and aggregate heterogeneous task results using performance profiles and Area Under the Performance Profile (AUP), separating Best Attempt@4 from Best Submission@4.

## Key Findings
- The paper positions MLGym as the first Gym environment for AI research agents, with explicit abstractions for agents, environments, datasets, tasks, tools, and flexible evaluation artifacts.
- MLGym-Bench covers open-ended ML research tasks where agents must inspect code/data, train or tune models, run experiments, validate results, and submit task-specific artifacts rather than one uniform answer format.
- OpenAI o1-preview has the strongest aggregate AUP@4 in the reported setup, while Gemini-1.5-Pro and Claude-3.5-Sonnet are close behind; Gemini is reported as the best cost/performance tradeoff.
- Current frontier agents often improve provided baselines, but the authors characterize the gains as mostly hyperparameter or implementation improvements rather than novel hypotheses, algorithms, or architectures.
- Reliability remains uneven: models differ in invalid submissions, failures, incomplete runs, and their ability to preserve the best intermediate attempt as the final submission.

## Tags
`AI-research-agents`, `ML-benchmarks`, `Gym-environment`, `LLM-agents`, `automated-experimentation`, `performance-profiles`, `baseline-improvement`, `SWE-Agent`

## Connections
- Extends the SWE-Agent style of shell-based code editing/evaluation from software engineering into broader machine learning research workflows.
- Contrasts with MLE-Bench, SWE-Bench/SWE-Agent, MLAgentBench, RE-Bench, and ScienceAgentBench by emphasizing Gym compatibility, algorithmic tasks, flexible artifacts, and open-ended research tasks.
- Useful alongside agent-coordination papers such as CooperBench and CAID: MLGym evaluates research-agent capability under a single-agent scaffold, while those papers examine whether multiple coding agents can coordinate effectively.
- Relevant to discussions of automated science because it operationalizes "AI research agent" progress as reproducible task performance rather than subjective paper-idea quality.
