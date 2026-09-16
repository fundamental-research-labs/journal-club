# AgentCoder: Multi-Agent Code Generation with Effective Testing and Self-optimisation

**Authors:** Dong Huang, Jie M. Zhang, Michael Luck, Qingwen Bu, Yuhao Qing, Heming Cui
**arXiv:** 2312.13010
**Venue:** Preprint
**Date:** May 2024

## Problem
LLM code generation often improves when generated code is tested and repaired, but useful tests are hard to obtain. Single-agent self-refinement can couple code and test generation in one conversation, making tests biased toward the generated code, while broader multi-agent software-development frameworks can spend many tokens on role coordination without reliable executable feedback.

## Method
AgentCoder uses three specialized agents. A programmer agent generates and refines code with chain-of-thought-style programming instructions. A test designer agent independently writes basic, edge, and large-scale test cases from the task requirements without seeing the generated solution. A test executor agent is a Python-scripted local executor that combines code and tests, runs them, and returns syntax/runtime/assertion feedback to the programmer until the code passes the generated tests or the iteration budget is exhausted. The paper evaluates pass@1 on HumanEval, HumanEval-ET, MBPP, and MBPP-ET with several LLM backbones and compares against zero-shot LLMs plus LLM-based code-generation optimization baselines.

## Key Findings
- AgentCoder reports the strongest end-to-end pass@1 results in its comparison table: with GPT-4 it reaches 96.3 on HumanEval, 86.0 on HumanEval-ET, 91.8 on MBPP, and 91.8 on MBPP-ET.
- With GPT-3.5-turbo, AgentCoder's mean pass@1 is 84.1 across the four datasets, above the listed optimization baselines; the largest gains are on the enhanced-test variants.
- Ablations show that the full three-agent loop matters: programmer-only, programmer-plus-test-designer, and programmer-plus-test-executor variants all trail the complete AgentCoder setup.
- More repair iterations help within the tested budget: pass@1 rises from one to five iterations on all four GPT-3.5-turbo datasets.
- The independent test designer produces more accurate and higher-coverage tests than the compared single-prompt/test-generation baselines, and the paper's single-agent-vs-multi-agent ablation supports separating code generation from test design.
- The appendix reports lower response-token use for AgentCoder than the compared multi-agent frameworks on the GPT-4 HumanEval/MBPP setting.

## Tags
`multi-agent`, `code-generation`, `software-engineering-agents`, `automated-testing`, `test-generation`, `iterative-refinement`, `pass@1`, `HumanEval`, `MBPP`

## Connections
- Related to **CodeCoT** and other test-driven self-refinement methods, but separates code and test generation into different agents to reduce test bias.
- Contrasts with heavier multi-agent coding frameworks such as **MetaGPT**, **ChatDev**, and **AgentVerse** by using only three roles and a script-based executor.
- Useful predecessor for later repository-level coding-agent work such as **SWEagent**, **CAID**, and **CooperBench**, though AgentCoder evaluates mostly function-level Python coding benchmarks rather than collaborative edits in large repositories.
- Complements **SingleAgentOutperforms** and **WhyMultiAgentFail** by showing a case where role separation helps, while keeping the coordination channel narrow and grounded in executable tests.
