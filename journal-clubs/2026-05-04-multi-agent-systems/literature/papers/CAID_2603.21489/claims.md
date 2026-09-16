# Claims

## Claim 1
**Claim:** Branch-and-merge coordination improves long-horizon software-agent performance over a matched single-agent baseline.

**Evidence:** On PaperBench and Commit0-Lite, CAID improves scores across the evaluated models while keeping the underlying OpenHands agent substrate fixed.

**Caveats/Scope:** Results are for the tested models, benchmarks, iteration limits, and CAID configuration.

**Source pointers:** `summary.md`; `source/sec/abstract.tex`; `source/sec/main_results.tex`; `source/tables/main_results.tex`

## Claim 2
**Claim:** Simply increasing a single agent's iteration budget does not solve the long-horizon bottleneck.

**Evidence:** The paper compares single-agent runs with larger iteration limits and reports only marginal or sometimes negative gains, while CAID's gains are substantially larger.

**Caveats/Scope:** Iteration budgets are the compute control used here; other single-agent improvements are outside the tested setup.

**Source pointers:** `source/sec/main_results.tex`; `source/figs/single-agent-iter.tex`; `summary.md`

## Claim 3
**Claim:** Worktree isolation is a central mechanism for reliable multi-agent software collaboration.

**Evidence:** CAID gives each engineer an isolated `git worktree` and integrates through commits and merges; ablations show soft instruction-only isolation can underperform, especially on open-ended PaperBench tasks.

**Caveats/Scope:** Soft isolation can still help on more structured tasks, so isolation interacts with task structure and decomposition quality.

**Source pointers:** `source/sec/methods.tex`; `source/sec/analysis.tex`; `source/tables/ablation-isolation.tex`

## Claim 4
**Claim:** More engineer agents are not always better.

**Evidence:** The analysis finds different best parallelism levels across Commit0-Lite and PaperBench, with too many engineers increasing integration overhead and stressing the manager's delegation capacity.

**Caveats/Scope:** Optimal parallelism depends on task modularity, manager ability, and implementation budget.

**Source pointers:** `source/sec/analysis.tex`; `source/figs/nsubagents.tex`; `summary.md`

## Claim 5
**Claim:** Manager delegation quality can determine whether parallel execution pays off.

**Evidence:** A Commit0-Lite case study shows that assigning a critical dependency such as `autodiff.py` changes downstream progress, while missing that dependency limits pass rate despite multiple active engineers.

**Caveats/Scope:** This is a qualitative execution-trajectory analysis, not a universal rule for all repositories.

**Source pointers:** `source/sec/analysis.tex`; `source/figs/gantt_multi.tex`; `summary.md`
