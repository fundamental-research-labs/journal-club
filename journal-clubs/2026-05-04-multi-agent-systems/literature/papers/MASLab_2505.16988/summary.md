# MASLab: A Unified and Comprehensive Codebase for LLM-based Multi-Agent Systems

**Authors:** Rui Ye, Keduan Huang, Qimin Wu, Yuzhu Cai, Tian Jin, Xianghe Pang, Xiangrui Liu, Jiaqi Su, Chen Qian, Bohan Tang, Kaiqu Liang, Jiaao Chen, Yue Hu, Zhenfei Yin, Rongye Shi, Bo An, Yang Gao, Wenjun Wu, Lei Bai, Siheng Chen
**arXiv:** 2505.16988
**Venue:** Preprint
**Date:** May 2025

## Problem
LLM-based multi-agent systems have many isolated implementations, which makes replication expensive and comparisons fragile. Different repositories often use different preprocessing, prompts, tool wrappers, configurations, and evaluation protocols, so measured differences can reflect implementation choices rather than the MAS method itself.

## Method
MASLab is a unified research codebase for LLM-based MAS. It re-implements 24 methods listed in Table 1, including single-agent baselines, general MAS methods, coding-specific systems, math/science systems, and tool-augmented agents. Each method is represented as a shared Python class/inference-function pattern, with common data preprocessing, model/tool resources, non-algorithmic configurations, and evaluation protocols. The authors manually validate integrated methods by comparing intermediate and final outputs against official implementations where possible. They then use the codebase to run broad experiments over 10+ benchmarks and 8 LLM backbones.

## Key Findings
- MASLab's main contribution is infrastructure: a single codebase that supports fairer comparisons across more than 20 MAS methods by aligning inputs, configurations, tools, and evaluation.
- Evaluation protocol choice can substantially change method rankings. On MATH, MAV ranks first under the authors' LLM two-step evaluator but drops to tenth under a DyLAN-style rule-based evaluator; AgentVerse shifts from 79.0 to 25.6 accuracy under different protocols.
- LLM-based evaluation agrees much more closely with human checks in the paper's MATH audit than rule-based matching: Table 4 reports 98%+ agreement for LLM two-step and xVerify, versus 65.65% for the best rule-based protocol shown.
- Across broad benchmarks, no single general MAS dominates every domain or backend. MAS-GPT and LLM-Debate are strong overall in the reported landscape, but backend model choice changes rankings.
- Tool-augmented MAS is important on GAIA. In the paper's setup, MASLab-ReAct improves over single-agent baselines and matches or beats OWL-Roleplaying while using fewer tokens in Table 5.
- Scaling analyses show that more inference compute and larger backend models often help, but failures from strict output formats and tool use remain major reliability bottlenecks.

## Tags
`multi-agent`, `agent-frameworks`, `benchmarking`, `evaluation-protocols`, `reproducibility`, `tool-use`, `agent-infrastructure`

## Connections
- Complements papers such as **AutoGen**, **CAMEL**, **AgentVerse**, **ChatDev**, **MetaGPT**, **GPTSwarm**, **AFlow**, and **MAS-GPT** by putting many of those methods into one comparative implementation layer.
- Useful context for **CooperBench** and **CAID**: MASLab studies broad MAS evaluation infrastructure, while those papers focus on cooperative coding failures and branch-and-merge coordination for software agents.
- Relevant whenever citing benchmark results for MAS methods, because it shows that evaluation protocol and backend model choices can change the apparent ranking of methods.
