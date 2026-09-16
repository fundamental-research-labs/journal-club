# SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents

**Authors:** Xuhui Zhou*, Hao Zhu*, Leena Mathur, Ruohong Zhang, Zhengyang Qi, Haofei Yu, Louis-Philippe Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, Maarten Sap
**arXiv:** 2310.11667
**Venue:** ICLR 2024
**Date:** March 2024

## Problem
Social intelligence benchmarks for language agents are often static, narrow, or not goal-driven, so they miss the interactive tradeoffs that arise when agents must pursue private goals while maintaining relationships, norms, secrets, and material interests. The paper asks how to evaluate open-ended social interaction between language agents and humans in a systematic way.

## Method
SOTOPIA is a role-play environment for dyadic social episodes. It samples scenarios, private social goals, character profiles, relationships, and partner policies, then lets agents act through text-form speech, non-verbal communication, physical actions, silence, or leaving. The released task space in the paper uses 90 scenarios, 40 characters, 90 relationships, and 450 sampled tasks. SOTOPIA-EVAL scores each agent after an episode on seven dimensions: goal completion, believability, knowledge gain, secret keeping, relationship impact, social-rule compliance, and financial/material benefit. The experiments compare GPT-4, GPT-3.5, Llama-2-70b-chat, MPT-30b-chat, and human participants, with GPT-4 and humans also used as evaluators.

## Key Findings
- GPT-4 can approximate human evaluation on some SOTOPIA-EVAL dimensions, especially goal completion for model outputs, but the paper warns that LLM evaluation is weaker or biased on other dimensions and for human role-play.
- GPT-4 performs best among the tested model agents on most social dimensions, but all tested models still lose points for secret disclosure or social-rule violations.
- Interactive performance differs from static benchmark expectations: Llama-2-70b-chat trails GPT-3.5 in SOTOPIA despite stronger results on some static language benchmarks.
- Partner quality matters: weaker partner models can reduce the performance of otherwise stronger agents because the interaction itself breaks down.
- On SOTOPIA-hard, humans achieve significantly higher goal-completion scores than GPT-4 when interacting with humans, and qualitative examples suggest humans are often more strategic and persistent.

## Tags
`social-intelligence`, `language-agents`, `interactive-evaluation`, `multi-agent`, `role-play`, `LLM-as-judge`, `human-agent-interaction`, `social-commonsense`

## Connections
- Complements static social commonsense benchmarks by making social evaluation interactive, goal-oriented, and multi-dimensional.
- Useful alongside **CooperBench** as a non-coding domain where agent-agent interaction can fail because partner behavior and coordination quality matter.
- Related to generative-agent and social-simulation work, but focuses on systematic evaluation rather than only producing believable behavior.
- Relevant to LLM-as-judge research because it measures where GPT-4 aligns with human social-interaction judgments and where it should be used cautiously.
