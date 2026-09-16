---
marp: true
theme: default
paginate: true
style: |
  section { font-size: 24px; }
  h1 { font-size: 36px; color: #2d3436; }
  h2 { font-size: 28px; color: #636e72; }
---

# SlopCodeBench: How Coding Agents Degrade Over Iterative Tasks
**Orlanski, Roy, Yun, Shin, Gu, Ge, Adila, Sala, Albarghouthi -- UW-Madison, WSU, MIT**

- **Problem**: Coding benchmarks evaluate single-shot solutions, but real development is iterative. Code can pass tests yet become progressively harder to extend -- existing benchmarks don't measure this
- **Benchmark**: 20 problems, 93 checkpoints. Agent builds initial solution, then repeatedly extends its own prior code as specs evolve (e.g., Python-only search tool --> multi-language --> AST patterns --> auto-fix). Specs prescribe only external behavior (CLI/API), not internal structure. Test suite is hidden
- **Two quality metrics**:
  - **Structural erosion**: fraction of complexity mass (CC x sqrt(SLOC)) in high-complexity functions (CC > 10)
  - **Verbosity**: fraction of redundant/duplicated code (137 AST-Grep rules + clone detection)
- **Key design**: Agent's own code carries forward between checkpoints -- bad architectural decisions at checkpoint 1 compound through all subsequent checkpoints

---

# Key Results

- **No agent solves any problem end-to-end** across 11 models. Best strict checkpoint solve rate: Opus 4.6 at 17.2%
- **Quality degrades steadily**: erosion rises in 80% of trajectories, verbosity in 89.8%
- **Agent code is 2.2x more verbose** than 48 maintained open-source Python repos (0.33 vs 0.15). Erosion: 0.68 vs 0.31
- **Humans stay flat, agents deteriorate**: tracking 20 repos over time, human erosion/verbosity plateau while agent metrics climb monotonically every checkpoint
- **Concrete example**: Opus 4.6's `main()` in circuit_eval grows from CC=29/84 lines to CC=285/1,099 lines over 8 checkpoints -- nine command branches repeat identical arg-parsing scaffolding
- **Prompt interventions fail to halt degradation**: "anti-slop" prompts cut initial verbosity by ~34% but the degradation *slope* is identical. Quality-aware prompting costs 48% more ($450 vs $304 for GPT 5.4) with zero improvement in pass rates (p > 0.05 on all subtypes)
- **Cost grows 2.9x** from first to last checkpoint, but extra spending doesn't improve correctness
- **Best models by cost-adjusted performance**: Opus 4.6 leads strict solve rate; GPT 5.4 has lowest erosion (0.515)

---

# Open Questions & Discussion

- **The "slop" problem is architectural, not cosmetic**: prompt pressure changes the intercept but not the slope. This suggests the failure is in how LLMs approach iterative modification -- they patch existing functions rather than refactoring
- **Training-time vs inference-time fix?** The paper leaves open whether training on iterative coding trajectories (not just single-shot solutions) could change the degradation dynamics
- **Relevance to multi-agent systems**: Any agent that maintains a codebase over time will hit this. The compounding of early design decisions is exactly what happens in long-running agent deployments -- the "technical debt" failure mode
- **Missing control**: No human developer baseline on the same tasks. The 48-repo comparison is informative but not apples-to-apples. Would a junior developer also degrade? Probably, but likely slower
- **Practical implication**: Pass-rate benchmarks (SWE-Bench, etc.) systematically miss extension robustness. If you're building a coding agent for production use, you need to measure quality trajectories, not just test pass rates
