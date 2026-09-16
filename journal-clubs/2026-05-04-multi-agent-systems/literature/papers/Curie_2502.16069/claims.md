# Claims

## Claim 1
**Claim:** Rigorous automated experimentation needs explicit support for methodical procedure, reliability, and interpretability, not just prompt-driven agent workflows.

**Evidence:** The paper defines these three principles in its background section and designs Curie's Experimental Rigor Engine around them: Inter-ARM for methodical control, Intra-ARM for reliability, and the Experiment Knowledge Module for interpretability.

**Caveats/Scope:** This is an architectural claim grounded in the authors' framing of scientific experimentation; the implementation and evaluation focus on computer-science tasks.

**Source pointers:** `paper.pdf`, Sections 2.2 and 3.1; Figure 3.

## Claim 2
**Claim:** Stepwise intra-agent validation can reduce common failure modes in AI-run experiments before errors propagate.

**Evidence:** Intra-ARM validates experiment setups against the plan, variables, input/output handling, placeholders, and documentation, then executes setups in clean environments with reproducibility checks before accepting results.

**Caveats/Scope:** The paper describes two validators in detail and presents them as extensible; effectiveness depends on the coverage and correctness of the enforced validation policies.

**Source pointers:** `paper.pdf`, Section 3.2; Figures 4 and 5.

## Claim 3
**Claim:** Curie's inter-agent coordination model turns experimental plans into controlled, schedulable partitions rather than free-form agent conversations.

**Evidence:** Inter-ARM partitions experimental plans by independent-variable subsets, enforces permissible state transitions between Architect, Technician, and validation stages, and schedules partitions using priority, state, and agent availability.

**Caveats/Scope:** The scheduler described is relatively simple, and the paper does not isolate scheduling quality from the broader framework in a separate ablation.

**Source pointers:** `paper.pdf`, Section 3.3; Figure 6.

## Claim 4
**Claim:** Curie introduces a benchmark aimed at full experimental workflows rather than one-shot problem solving.

**Evidence:** The Experimentation Benchmark contains 46 tasks across four computer-science domains and asks agents to formulate experiments, use contextual scaffolding, execute setups, and compare against ground-truth design and result expectations.

**Caveats/Scope:** The benchmark is limited to computer science and to tasks whose ground truth can be derived from influential papers, official benchmarks, or open-source projects.

**Source pointers:** `paper.pdf`, Section 4; Table 1; Appendix D.

## Claim 5
**Claim:** Curie outperforms OpenHands and Microsoft Magentic-One on the authors' benchmark under a shared GPT-4o backbone.

**Evidence:** Table 2 reports weighted averages of 97.9 design, 78.1 execution setup, 73.4 implementation alignment, and 36.1 conclusion correctness for Curie, versus 83.6/32.4/40.2/10.5 for OpenHands and 82.9/6.8/35.2/2.3 for Magentic-One. The evaluation runs each task five times and averages the results.

**Caveats/Scope:** Some metrics rely on an LLM judge, although the authors manually assess implementation alignment and cross-check judge assessments against expert annotations. Results are for the tested benchmark, prompts, GPT-4o, and baseline implementations.

**Source pointers:** `paper.pdf`, Section 5 and Section 5.1; Table 2.

## Claim 6
**Claim:** Structured experiment memory is a core mechanism for making agent-run experiments auditable and recoverable.

**Evidence:** The Experiment Knowledge Module records plans, execution status, results, provenance, and a DAG-like history of changes, while tiered write access restricts what Architects and Technicians can modify.

**Caveats/Scope:** The paper motivates this module through LLM recall and write-consistency problems, but the provided results do not separately quantify the module's contribution apart from the whole Curie system.

**Source pointers:** `paper.pdf`, Section 3.4; Figure 7.
