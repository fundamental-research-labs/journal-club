# Claims

## Claim 1: Multi-agent systems are not uniformly better than single agents.

**Evidence:** The paper reports large task-dependent variation, from strong gains on decomposable Finance Agent tasks to severe degradation on sequential PlanCraft tasks.

**Caveats/Scope:** The result is based on the paper's selected benchmarks, architectures, model families, and equalized compute setup.

**Source pointers:** `summary.md`; `source/0-abstract.tex`; `source/4-experiments_results.tex`

## Claim 2: Architecture-task alignment is the central predictor of whether coordination helps.

**Evidence:** Finance Agent benefits from parallel information gathering and synthesis, while PlanCraft's sequential dependency structure makes decomposition wasteful.

**Caveats/Scope:** The paper studies canonical architectures, not every possible orchestration protocol.

**Source pointers:** `source/4-experiments_results.tex`; `summary.md`

## Claim 3: High single-agent baselines leave little room for multi-agent improvement.

**Evidence:** The scaling analysis identifies a capability-saturation pattern, with SWE-bench Verified showing slight degradation for all multi-agent variants when single-agent baselines are already strong.

**Caveats/Scope:** The reported threshold is empirical and should be treated as a decision heuristic within similar task regimes.

**Source pointers:** `source/4-experiments_results.tex`; `summary.md`

## Claim 4: Coordination overhead and tool complexity jointly limit multi-agent scaling.

**Evidence:** The model includes efficiency, overhead, tool count, message density, and error amplification; the paper emphasizes that tool-heavy tasks suffer disproportionately from multi-agent inefficiency.

**Caveats/Scope:** Some overhead interactions are framed as directional under conservative clustered inference.

**Source pointers:** `source/4-experiments_results.tex`; `source/5-limitation_future_work.tex`

## Claim 5: Centralized verification can reduce error propagation relative to less structured coordination.

**Evidence:** Architectures without centralized verification are described as amplifying trace-level errors more than centralized coordination.

**Caveats/Scope:** Verification helps but does not overcome mismatched task structure or excessive coordination cost.

**Source pointers:** `source/0-abstract.tex`; `source/4-experiments_results.tex`
