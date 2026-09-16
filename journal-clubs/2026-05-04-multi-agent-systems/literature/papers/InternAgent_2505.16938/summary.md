# InternAgent: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification

**Authors:** InternAgent Team; Bo Zhang; Shiyang Feng; Xiangchao Yan; Jiakang Yuan; Runmin Ma; Yusong Hu; Zhiyin Yu; Xiaohan He; Songtao Huang; Shaowei Hou; Zheng Nie; Zhilong Wang; Jinyao Liu; Tianshuo Peng; Peng Ye; Dongzhan Zhou; Shufei Zhang; Xiaosong Wang; Yilan Zhang; Meng Li; Zhongying Tu; Xiangyu Yue; Wanli Ouyang; Bowen Zhou; Lei Bai
**arXiv:** 2505.16938
**Venue:** Preprint
**Date:** July 2025

## Problem
Autonomous scientific research systems need to do more than generate plausible hypotheses: they must find relevant prior work, propose effective and novel methods, implement those methods in real code, run experiments, and feed results back into the next research step. The paper argues that existing systems struggle with proposal quality and closed-loop validation, especially across heterogeneous scientific and AI tasks and repository-level codebases.

## Method
InternAgent is a closed-loop multi-agent framework with three main stages. First, self-evolving idea generation combines a Survey Agent for literature search, a Code Review Agent for baseline code understanding, an Idea Innovation Agent for idea generation/evolution, an Assessment Agent for scoring coherence, credibility, verifiability, novelty, and alignment, human or agent feedback, and an Orchestration Agent. Second, a Method Development Agent turns concise ideas into detailed, implementable methodologies and refines them with critiques and literature. Third, evolutionary experimental planning and execution uses Aider for simpler code changes, OpenHands for repository-level changes, exception-guided debugging, and adaptive multi-round experiment planning based on measured results.

## Key Findings
- The paper evaluates InternAgent on 12 tasks spanning chemistry, molecular dynamics, power flow, time series, genomics, NLP, image classification, point clouds, segmentation, autonomous driving, and vision-language model fine-tuning.
- In the reported tables, InternAgent improves over the baselines on all 12 tasks and outperforms DOLPHIN on the tasks where DOLPHIN is applicable.
- The framework supports several project-level code tasks where DOLPHIN is reported as not applicable, including Auto2DSeg, AutoPCDet, and AutoVLM.
- The adaptive evolution ablation improves max and average results on AutoRYP, Auto2DCls, and AutoSenCls compared with the same system without adaptive evolution.
- Expert idea review in four task areas rates InternAgent ideas higher than AI-Scientist-V2 on soundness, contribution, and overall score.

## Tags
`autonomous-scientific-research`, `multi-agent`, `AI4Science`, `closed-loop-agents`, `idea-generation`, `agentic-coding`, `experiment-automation`, `human-in-the-loop`, `OpenHands`, `Aider`

## Connections
- Extends the AI Scientist / AI-Scientist-V2 line from idea generation and experiment automation toward broader AI and science tasks with explicit codebase review and adaptive execution.
- Directly compares with DOLPHIN, AI-Researcher, and AI-Scientist-V2 as neighboring closed-loop auto-research systems.
- Useful alongside CAID and CooperBench when discussing why multi-agent workflows need isolation, planning, code comprehension, and feedback rather than simple agent parallelism.
- Relevant to AI4Science and human-AI collaboration discussions because it couples literature search, human feedback, code generation, and empirical validation.
