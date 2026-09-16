# Claims

## Claim 1: Treating construction, retrieval, and utilization as isolated memory subroutines creates avoidable failures.

**Evidence:** The paper identifies strategic blindness on the forward path and sparse, delayed supervision on the backward path as coupled problems in memory-augmented agents.

**Caveats/Scope:** The diagnosis is developed for long-horizon memory agents, especially conversational QA settings.

**Source pointers:** `summary.md`; `source/0_abstract_v2.tex`; `source/4_method_v6.tex`

## Claim 2: MemMA coordinates memory through specialized planner-worker roles.

**Evidence:** The framework uses a Meta-Thinker, Memory Manager, Query Reasoner, and Answer Agent to separate strategic guidance from memory editing, retrieval refinement, and final answer generation.

**Caveats/Scope:** Role specialization adds orchestration overhead and is evaluated with fixed answer-agent settings.

**Source pointers:** `source/4_method_v6.tex`; `summary.md`

## Claim 3: Diagnosis-guided iterative retrieval is central to MemMA's gains.

**Evidence:** The Query Reasoner refines retrieval based on Meta-Thinker diagnoses of missing evidence, and ablations show the largest drop when iterative retrieval is removed.

**Caveats/Scope:** The paper uses bounded refinement budgets; additional iterations can risk drift.

**Source pointers:** `source/4_method_v6.tex`; `source/5_evaluation_v3.tex`; `summary.md`

## Claim 4: In-situ self-evolution repairs memory before errors propagate.

**Evidence:** After each session, MemMA synthesizes probe QA pairs, verifies the provisional memory, converts failed probes into repair proposals, and semantically consolidates repairs before committing memory.

**Caveats/Scope:** Probe quality and judge reliability affect repair quality.

**Source pointers:** `source/4_method_v6.tex`; `source/5_evaluation_v3.tex`; `summary.md`

## Claim 5: MemMA improves multiple storage backends, not just one memory implementation.

**Evidence:** Experiments instantiate MemMA over Single-Agent, A-Mem, and LightMem backends and report improved semantic accuracy for all three.

**Caveats/Scope:** Results are on LoCoMo with the paper's selected backbones and evaluation protocol.

**Source pointers:** `source/5_evaluation_v3.tex`; `summary.md`
