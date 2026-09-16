# Effective Strategies for Asynchronous Software Engineering Agents

**Authors:** Jiayi Geng, Graham Neubig
**arXiv:** 2603.21489
**Venue:** Preprint
**Date:** March 2025

## Problem
Long-horizon software engineering tasks (e.g., implementing full Python libraries or reproducing research papers) are difficult for single agents due to context saturation and sequential execution bottlenecks. Existing multi-agent approaches split roles but fail at true parallel execution because concurrent edits interfere, dependencies are hard to synchronize, and merging partial work into a coherent codebase is error-prone.

## Method
CAID (Centralized Asynchronous Isolated Delegation) is a multi-agent coordination paradigm that borrows directly from human software engineering workflows. A central manager agent analyzes the codebase, builds a dependency graph, and decomposes work into parallelizable task groups. It delegates these to engineer agents via structured JSON specifications. Each engineer works in its own isolated `git worktree` (separate branch and directory), implements its tasks, runs self-verification tests, and commits. The manager merges engineer branches back into main via `git merge`, resolving conflicts explicitly. The cycle repeats over multiple rounds until all tasks are done or limits are reached. Built on the OpenHands agent SDK.

## Key Findings
- On PaperBench, CAID improves over single-agent baselines by up to 26.3 percentage points absolute (MiniMax 2.5: 10.4% to 36.7%; Claude 4.5 Sonnet: 57.2% to 63.3%)
- On Commit0-Lite, improvements of 6.0 pp for Claude 4.5 Sonnet (53.1% to 59.1%) and strong performance with MiniMax 2.5 (57.0%)
- Doubling a single agent's iteration budget (100 to 200) yields only marginal or even negative gains, showing the bottleneck is architectural, not computational
- Running single-agent first then falling back to multi-agent wastes runtime and cost with minimal performance gain over just running multi-agent directly
- Git worktree isolation is essential: "soft isolation" (instruction-only separation in a shared workspace) hurts performance on open-ended tasks like PaperBench (drops below single-agent)
- More engineers is not always better -- optimal parallelism depends on task modularity and the manager's delegation capacity (4 engineers best for Commit0, 2 for PaperBench)
- The manager's ability to identify and assign high-impact dependencies is critical; delegating the wrong modules first can drastically reduce pass rates

## Tags
`multi-agent`, `software-engineering`, `coordination`, `git-worktree`, `branch-and-merge`, `task-decomposition`, `parallel-execution`, `long-horizon`, `async-agents`

## Connections
- Directly addresses failures identified in **WhyMultiAgentFail** -- unstructured communication is the primary breakdown mode; CAID replaces free-form dialogue with structured JSON and git-based integration
- Responds to **CooperBench** findings that naive two-agent parallel coding on a shared repo degrades success by 30%; CAID's worktree isolation is designed to prevent exactly this
- Contrasts with **SingleAgentOutperforms** -- while that paper argues single agents beat multi-agent setups, CAID shows multi-agent wins when coordination uses proper SWE primitives (isolation + merge + tests)
- Complementary to **AgentScalingDiversity** on scaling laws: CAID finds that adding more agents has diminishing/negative returns without matching task modularity, echoing diversity-scaling tradeoffs
- Related to **DELEGATE-52** on task delegation -- CAID's manager must correctly identify high-impact dependencies for delegation to succeed
- Overlaps with **MaAS** on multi-agent-as-a-service architectures; CAID provides a concrete coordination paradigm that could plug into such frameworks
- Relevant to **ScienceOfScaling** -- CAID's analysis of parallelism vs. coordination cost mirrors scaling efficiency concerns
- **SlopCodeBench** evaluates code quality; CAID's self-verification and test-gated merge directly targets code correctness in multi-agent settings
- **MemMA** addresses memory in multi-agent systems; CAID uses LLMSummarizingCondenser for the manager's context, a related but simpler approach to the memory problem
