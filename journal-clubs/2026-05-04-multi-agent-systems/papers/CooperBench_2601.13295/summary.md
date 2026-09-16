# CooperBench: Why Coding Agents Cannot be Your Teammates Yet

**Authors:** Arpandeep Khatua*, Hao Zhu*, Peter Tran, Arya Prabhudesai, Frederic Sadrieh, Johann K. Lieberwirth, Xinkai Yu, Yicheng Fu, Michael J. Ryan, Jiaxin Pei, Diyi Yang
**arXiv:** 2601.13295
**Venue:** Preprint
**Date:** January 2025

## Problem
Current AI coding agents have strong individual capabilities, but it is unclear whether they can effectively cooperate when working together on shared codebases. The paper asks: does adding a second agent help or hurt when two features must be implemented on the same repository?

## Method
CooperBench is a benchmark of 652 collaborative coding tasks across 12 open-source repositories in Python, TypeScript, Go, and Rust. Each task assigns two agents different features that are logically compatible but may conflict at the code level (77.3% of tasks have conflicting ground-truth solutions). Agents work in isolated Docker containers and communicate via a real-time text message channel. After execution, patches are merged with git and evaluated against expert-written unit tests. The key comparison is "Coop" (two agents, one feature each) vs. "Solo" (one agent implements both features). Five models were evaluated: GPT-5, Claude Sonnet 4.5, MiniMax-M2, Qwen3-Coder-30B, and Qwen3-30B-Instruct.

## Key Findings
- **The curse of coordination:** GPT-5 and Claude Sonnet 4.5 agents achieve only ~25% success in Coop mode, roughly 50% lower than the Solo baseline where one agent does both tasks.
- **Communication does not improve success:** Despite agents spending up to 20% of their action budget on messaging, adding a communication channel produces no statistically significant improvement in task success rate.
- **Communication does reduce merge conflicts:** Merge conflict rates drop significantly when agents can communicate, but avoiding conflicts alone does not ensure correct implementations (spatial vs. semantic coordination gap).
- **Mid-difficulty tasks suffer most:** The coordination gap is largest for medium-difficulty tasks; easy tasks leave room for coordination overhead, and hard tasks fail regardless.
- **More agents makes it worse:** Scaling from 2 to 3 to 4 agents on a subset of tasks drops success from 68.6% to 46.5% to 30.0%.
- **Three root causes of failure:** (1) communication channels jammed with vague, repetitive, or inaccurate messages; (2) agents deviate from their own commitments; (3) agents hold incorrect expectations about partner state and plans.
- **Emergent coordination behaviors:** Rare but notable successes involve role division, resource division (line-level ownership), and negotiation where agents converge on a plan before acting.
- **Trust paradox:** Models trained to verify claims struggle in cooperative settings where they must trust unverifiable partner assertions about code on a separate branch.

## Tags
`multi-agent`, `cooperation`, `coordination`, `benchmark`, `coding-agents`, `communication`, `social-intelligence`

## Connections
- Directly related to **WhyMultiAgentFail**: both identify coordination overhead as a key bottleneck in multi-agent systems. CooperBench provides empirical evidence in the coding domain while WhyMultiAgentFail addresses the question more broadly.
- Related to **SingleAgentOutperforms**: CooperBench's "curse of coordination" finding (solo > coop) aligns with findings that single agents can outperform multi-agent setups.
- Relevant to **AgentScalingDiversity**: CooperBench shows that scaling agents (2 to 4) hurts performance, complementing work on how agent diversity and scaling interact.
- Related to **SlopCodeBench**: both benchmark coding agents, but CooperBench focuses on cooperative coding rather than individual code quality.
- Related to **DELEGATE-52** and **MaAS**: these propose multi-agent architectures, while CooperBench reveals fundamental coordination limitations that such architectures must overcome.
- Related to **ScienceOfScaling**: CooperBench's finding that more agents degrade performance provides a concrete counterpoint to scaling-based approaches.
