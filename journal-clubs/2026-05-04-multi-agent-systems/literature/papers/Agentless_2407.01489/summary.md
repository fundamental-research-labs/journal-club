# Agentless: Demystifying LLM-based Software Engineering Agents

**Authors:** Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang
**arXiv:** 2407.01489
**Venue:** Preprint
**Date:** October 2024

## Problem
Autonomous LLM software agents are usually built around iterative tool use, environment feedback, and model-driven planning. The paper asks whether this complexity is necessary for repository-level issue resolution, given that current LLM agents can misuse tools, drift through long action traces, and amplify early mistakes.

## Method
Agentless replaces open-ended agent control with a fixed three-phase pipeline. First, hierarchical localization narrows an issue from repository structure and retrieval to suspicious files, related classes/functions, and final edit locations. Second, repair prompts GPT-4o to generate multiple Search/Replace patches from localized snippets. Third, patch validation generates reproduction tests, runs existing regression tests, filters candidate patches, and uses normalized majority voting to choose the final submission.

## Key Findings
- On SWE-bench Lite, Agentless resolves 96 of 300 tasks (32.00%) at an average reported inference cost of $0.70, which the paper reports as the best open-source result in its comparison table, though not the top result overall once closed-source/commercial systems are included.
- The localization ablation supports the staged design: combining prompt-based and embedding-based file retrieval contains the ground-truth file more often than either alone, and skeleton-based related-element localization is cheaper and more effective than passing complete files.
- Repair improves when the method keeps multiple sampled edit-location sets separate and generates candidate patches for each; the paper reports a plateau around 40 patch samples and an oracle-style upper bound of 126 solvable tasks if any generated patch could be selected.
- Patch validation matters: majority voting alone resolves fewer tasks, regression filtering helps modestly, and adding generated reproduction tests gives the reported final 96 fixes. The generated tests are useful but noisy, so the system falls back to regression results when needed.
- The paper manually audits SWE-bench Lite and identifies tasks with insufficient information, exact ground-truth patches in the issue text, or misleading solution hints; it constructs SWE-bench Lite-S by filtering those cases.

## Tags
`software-engineering-agents`, `agentless`, `SWE-bench`, `automated-program-repair`, `fault-localization`, `patch-generation`, `test-generation`, `patch-validation`, `repository-level-coding`

## Connections
- Directly tied to **SWE-bench**: Agentless is evaluated on SWE-bench Lite and argues that benchmark artifacts can affect leaderboard interpretation.
- A counterpoint to autonomous coding agents such as **SWE-agent**, **OpenDevin**, **AutoCodeRover**, and **Aider**: it fixes the control flow in advance rather than letting an LLM plan tool actions.
- Useful as a single-pipeline baseline for later multi-agent coding work such as **CooperBench** and **CAID**, where coordination costs and branch/worktree mechanics become central.
- Related to **AgentCoder** through generated tests and iterative repair, but Agentless targets repository-level GitHub issues rather than function-level coding tasks.
- Connects to **SWE-bench Verified** and later live/multilingual SWE benchmarks by motivating more careful benchmark filtering and issue validation.
