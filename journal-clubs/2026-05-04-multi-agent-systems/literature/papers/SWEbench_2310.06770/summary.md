# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**Authors:** Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan
**arXiv:** 2310.06770
**Venue:** ICLR 2024
**Date:** October 2023

## Problem
Existing code-generation benchmarks mostly test short, self-contained programming tasks, while real software maintenance requires finding relevant code in large repositories, understanding issue reports, editing multiple locations, and preserving existing behavior. SWE-bench asks whether language models can resolve real GitHub issues under executable repository-level evaluation.

## Method
The benchmark is built from merged pull requests in 12 popular Python repositories. Candidate tasks are PRs that resolve GitHub issues and add tests; execution filtering keeps instances where applying the PR changes at least one test from failing to passing and avoids unusable environments. Each task gives a model the issue text and codebase snapshot, asks it to generate a patch, then applies that patch and runs the associated tests. The paper also defines SWE-bench Lite, a 300-instance subset, and trains SWE-Llama models on a separate 19,000-instance issue-PR corpus from disjoint repositories.

## Key Findings
- SWE-bench contains 2,294 task instances across 12 Python repositories, with average codebases of hundreds of thousands of lines and reference fixes that often edit multiple functions or files.
- Baseline language models perform poorly: in the local PDF's BM25 setting, all full-benchmark resolve rates are below 4%, with Claude 3 Opus at 3.79% and Claude 2 around 2%.
- Retrieval and localization are major bottlenecks: increasing BM25 context improves oracle-file recall but can lower task resolution, and oracle/collapsed-oracle settings improve results.
- SWE-Llama shows that supervised fine-tuning on issue-to-patch data is possible, but performance is sensitive to context distribution and remains low under BM25 retrieval.
- Model patches tend to be shorter and narrower than human reference patches, often fixing the immediate symptom without matching the broader structural changes made by maintainers.

## Tags
`swe-bench`, `coding-agents`, `software-engineering`, `program-repair`, `github-issues`, `patch-generation`, `execution-based-evaluation`, `long-context`

## Connections
- Foundational benchmark for later software-engineering agent work that reports SWE-bench or SWE-bench Lite results.
- Complements **CooperBench** by focusing on solo issue resolution and executable patch quality, while CooperBench studies multi-agent coordination failures.
- Provides a target setting for approaches like **CAID**, where repository-scale issue resolution may benefit from explicit task decomposition, isolated edits, and test-based integration.
- Connects to automated program repair and bug localization work, but preserves more of the real repository context than small function-level coding benchmarks.
