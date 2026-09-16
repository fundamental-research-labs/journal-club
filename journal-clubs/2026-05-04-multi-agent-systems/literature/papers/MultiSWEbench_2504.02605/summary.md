# Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving

**Authors:** ByteDance Seed
**arXiv:** 2504.02605
**Venue:** Preprint
**Date:** April 2025

## Problem
SWE-bench-style issue resolving has mostly measured Python repositories, leaving open whether LLM coding agents generalize to other software ecosystems with different build systems, runtime behavior, typing disciplines, and repository conventions.

## Method
Multi-SWE-bench builds a multilingual issue-resolving benchmark for Java, TypeScript, JavaScript, Go, Rust, C, and C++. The construction pipeline selects active GitHub repositories, crawls issue-linked merged pull requests, builds Dockerized execution environments, filters PRs using test-result transitions, and then applies dual manual annotation plus cross-review. The final benchmark contains 1,632 human-validated instances from 39 repositories, selected from 2,456 candidates by 68 expert annotators. The paper evaluates 9 LLMs with multilingual adaptations of Agentless, SWE-agent, and OpenHands, using resolved rate as the primary metric. It also introduces Multi-SWE-RL, an open-source community release of 4,723 containerized issue-resolving instances for RL-oriented training data.

## Key Findings
- Existing SWE agents generalize poorly beyond Python: Table 4 shows much lower resolved rates on the seven non-Python languages than on Python across methods and models.
- For Claude-3.7-Sonnet with MopenHands, resolved rate is 52.20% on Python but 21.88% on Java, 2.23% on TypeScript, 5.06% on JavaScript, 7.48% on Go, 15.90% on Rust, 8.59% on C, and 14.73% on C++.
- MopenHands is the strongest adapted method in most language-level comparisons, while MSWE-agent and MagentLess still win in some cases, so there is no universal workflow winner.
- Human-labeled difficulty, ground-truth patch length, and number of modified files strongly affect success; hard issues and long or cross-file patches remain difficult for all three methods.
- Multi-SWE-RL is larger than the benchmark but is not equivalently human-verified; it uses the same pipeline while excluding the final manual verification phase.

## Tags
`software-engineering-agents`, `issue-resolving`, `multilingual-benchmark`, `SWE-bench`, `automated-program-repair`, `coding-agents`, `RL-data`

## Connections
- Extends the SWE-bench/SWE-bench Verified line from Python issue resolving to multilingual repositories.
- Useful context for papers about coding-agent coordination because it supplies a harder, language-diverse evaluation surface.
- Complements Agentless, SWE-agent, and OpenHands by stress-testing their assumptions outside the Python-centric setting where they were developed.
- Related to RL-for-code-agent work through the Multi-SWE-RL companion dataset and community pipeline.
