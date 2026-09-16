---
marp: true
theme: default
paginate: true
style: |
  section { font-size: 24px; }
  h1 { font-size: 36px; color: #2d3436; }
  h2 { font-size: 28px; color: #636e72; }
---

# CAID: Effective Strategies for Asynchronous Software Engineering Agents
**Jiayi Geng, Graham Neubig** -- Carnegie Mellon University (Mar 2026)

- **Problem:** Multi-agent SWE fails because concurrent edits interfere, dependencies break silently, and merging partial progress is hard
- **Core idea:** Borrow human SWE collaboration primitives -- git worktree for isolation, git merge for integration, dependency graphs for scheduling -- and build a manager/engineer multi-agent system around them
- **Architecture:** A central Manager builds a dependency-aware task graph, delegates to N Engineer agents running in parallel git worktrees. Engineers self-verify with tests, commit, and the Manager merges back to main. Structured JSON communication (no free-form chat)
- **Key insight:** Branch-and-merge is *the* coordination mechanism. Soft isolation (shared workspace + instructions to stay apart) is not enough -- physical worktree isolation is necessary, especially for open-ended tasks

---

# Key Results

| Benchmark | Model | Single-Agent | CAID | Delta |
|---|---|---|---|---|
| PaperBench | Claude 4.5 Sonnet | 57.2% | 63.3% | **+6.1** |
| PaperBench | MiniMax 2.5 | 10.4% | 36.7% | **+26.3** |
| Commit0-Lite | Claude 4.5 Sonnet | 53.1% | 59.1% | **+6.0** |
| Commit0-Lite | MiniMax 2.5 | 42.3% | 57.0% | **+14.7** |

- Doubling single-agent iterations (100 -> 200) yields marginal or even *negative* gains; CAID's gains are 5-10x larger
- **Worktree isolation matters:** On PaperBench, soft isolation (55.5%) is *worse* than single-agent (57.2%), while worktree isolation reaches 63.3%
- **Scaling parallelism:** More engineers is not always better -- 4 engineers optimal for Commit0, 2 for PaperBench. Beyond that, delegation errors and integration overhead dominate
- **Fallback strategy is wasteful:** Running single-agent first then CAID adds cost/time but barely improves over just running CAID directly

---

# Open Questions & Discussion

- **Cost scales super-linearly:** CAID with Claude 4.5 costs $9.3 vs $3.3 for single-agent on PaperBench (2.8x) for a +6.1pt gain. Wall-clock time does not decrease despite parallel execution due to sequential merge gates
- **Manager is the bottleneck:** Which tasks get delegated first determines success. In minitorch, assigning autodiff.py early yields 34.3% vs 8.7% without it. But delegation quality is entirely prompt-engineered, not learned
- **Only tested on SWE tasks** where git provides natural isolation/merge infrastructure. How does this generalize to non-code shared artifacts (documents, designs, research)?
- **Practical relevance:** This is essentially what tools like Claude Code with worktrees already do. The contribution is the *systematic evaluation* showing that SWE primitives are the right abstraction for multi-agent coordination, not ad-hoc communication protocols
