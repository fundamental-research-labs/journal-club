# Claims

## Claim 1: Single-shot pass-rate benchmarks miss iterative code degradation.

**Evidence:** SlopCodeBench carries each agent's own workspace forward across evolving checkpoints, exposing future costs of early architectural choices that still pass current tests.

**Caveats/Scope:** The paper reports the Python track even though the benchmark design is language-agnostic.

**Source pointers:** `summary.md`; `source/main.tex`; `source/sections/introduction.tex`; `source/sections/benchmark.tex`

## Claim 2: Current coding agents fail to solve full long-horizon benchmark problems end-to-end.

**Evidence:** The paper reports that no evaluated agent solves any of the 20 problems end-to-end; the performance table gives checkpoint, isolated, core, and partial solve rates.

**Caveats/Scope:** This is for the evaluated set of 11 models, harnesses, and benchmark problems.

**Source pointers:** `source/main.tex`; `source/figures/performance_table.tex`; `source/sections/results/overall.tex`

## Claim 3: Agent code quality deteriorates over repeated self-extension.

**Evidence:** The results show structural erosion and verbosity rising in most trajectories, with high-complexity functions accumulating more decision-point load over time.

**Caveats/Scope:** The metrics are static approximations of maintainability, not direct human-maintenance measurements.

**Source pointers:** `source/sections/results/quality_accumulation.tex`; `source/sections/benchmark.tex`; `summary.md`

## Claim 4: Agent-generated code diverges from maintained human repositories over time.

**Evidence:** The calibration section compares agent trajectories to maintained Python repositories and finds agent metrics climb while human repository metrics plateau.

**Caveats/Scope:** The human repositories are a calibration panel, not matched human solutions to the same tasks.

**Source pointers:** `source/sections/results/agent_vs_human.tex`; `summary.md`

## Claim 5: Quality-aware prompts improve starting quality but do not stop degradation.

**Evidence:** Anti-slop and plan-first prompts lower initial verbosity and erosion, but the degradation slopes remain largely parallel and pass rates do not consistently improve.

**Caveats/Scope:** The prompt intervention study covers selected models and prompt strategies, so stronger tooling or training interventions remain open.

**Source pointers:** `source/sections/results/compounding.tex`; `source/sections/conclusion.tex`; `summary.md`
