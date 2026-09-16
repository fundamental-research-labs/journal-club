# SWE-bench Goes Live!

**Authors:** Linghao Zhang, Shilin He, Chaoyun Zhang, Yu Kang, Bowen Li, Chengxing Xie, Junhao Wang, Maoquan Wang, Yufan Huang, Shengyu Fu, Elsie Nallipogu, Qingwei Lin, Yingnong Dang, Saravan Rajmohan, Dongmei Zhang
**arXiv:** 2505.23419
**Venue:** Preprint
**Date:** June 2025

## Problem
SWE-bench and related issue-resolution benchmarks are valuable but static, manually curated, and limited to relatively few repositories. This makes them vulnerable to data contamination and weakens their usefulness for evaluating whether newer code models can solve fresh, repository-level GitHub issues.

## Method
SWE-bench-Live keeps the SWE-bench issue-resolution task but rebuilds the benchmark pipeline around recent real GitHub issue/PR pairs and per-instance executable environments. Its initial release contains 1,319 tasks from issues created between January 1, 2024 and April 20, 2025 across 93 open-source Python repositories. The paper introduces REPOLAUNCH, an agentic Docker environment setup pipeline that identifies setup files, chooses a base image, installs/builds the repository, verifies tests, handles dependency version drift with a time-aware package proxy, and packages a reusable image. Candidate tasks are retained only when test logs show stable FAIL_TO_PASS behavior after the gold PR patch without breaking PASS_TO_PASS tests.

## Key Findings
- SWE-bench-Live is broader and fresher than prior real issue-resolution benchmarks in the comparison table: 1,319 real tasks across 93 repositories with automatic curation.
- The full benchmark top result reported in the paper is OpenHands with Claude 3.7 Sonnet at 19.25% resolved, with 85.89% patch apply rate and 48.29% file-level localization success.
- Under the same OpenHands/Claude 3.7 Sonnet setup, the authors report 43.20% resolved on SWE-bench Verified, more than twice the SWE-bench-Live result.
- On the Lite subset, the best resolved rates are clustered around the high teens across OpenHands, SWE-agent, and Agentless combinations, suggesting broad difficulty rather than one framework failure.
- Difficulty rises sharply with patch and repository scope: one-file patches under five changed lines are solved about 48% of the time, while patches touching at least three files or over 100 lines fall below 10%.
- Recency alone does not explain the difficulty; OpenHands/Claude 3.7 Sonnet has no clear success-rate trend across 2024Q1-2025Q1 issue creation periods.

## Tags
`swe-bench-live`, `swe-bench`, `coding-agents`, `issue-resolution`, `live-benchmark`, `repository-level-benchmark`, `docker-environments`, `test-based-evaluation`, `data-contamination`

## Connections
- Extends the SWE-bench family by focusing on continuously refreshed, real GitHub issues rather than a fixed static set.
- Complements SWE-bench Verified, Multi-SWE-bench, SWE-Gym, and SWE-smith by emphasizing freshness, repository diversity, and automated environment setup.
- Related to LiveCodeBench's contamination-resistant evaluation goal, but in repository-level bug fixing rather than algorithmic programming tasks.
- Useful alongside CooperBench and other coding-agent evaluations as evidence that realistic repository tasks remain difficult even when patches can be applied and localized.
- REPOLAUNCH connects to agentic software engineering infrastructure: environment setup, build repair, test discovery, and reproducible Docker packaging.
