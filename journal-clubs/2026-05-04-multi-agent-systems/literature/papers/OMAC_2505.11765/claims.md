# Claims

## Claim 1
**Claim:** Multi-step LLM-based MAS can be organized around five optimization dimensions that cover both agent functionality and collaboration structure.

**Evidence:** Section 3.1 defines two functional dimensions, optimizing existing agents and constructing new agents, and three structural dimensions, candidate team selection, dynamic step-level participation, and communication-flow routing. Appendix B motivates this taxonomy by viewing MAS collaboration as an information-flow graph with agents as nodes and communications as edges.

**Caveats/Scope:** This is a conceptual coverage claim, not a formal proof that the five dimensions are exhaustive or optimal for every MAS architecture.

**Source pointers:** `paper.pdf`, Section 3.1; Appendix B; Appendix D.6

## Claim 2
**Claim:** The same optimization loop can be adapted to optimize any one of the five dimensions.

**Evidence:** Section 3.2 describes a dimension-agnostic loop: the Semantic Initializer generates candidate agents or controllers, the candidates are evaluated in the MAS on training data, positive-negative pairs are sampled from performance scores, and the Contrastive Comparator produces refined prompts or controllers. Figures 1 and 2 illustrate the workflow and a Fun-1 example.

**Caveats/Scope:** The loop depends on the reasoning quality of the underlying LLM and on representative supervised training feedback; it does not provide mathematical optimality guarantees.

**Source pointers:** `paper.pdf`, Section 3.2; Figures 1-2; Appendix D.1

## Claim 3
**Claim:** Single-dimension OMAC optimization improves reported performance over strong baselines on code generation, general reasoning, and arithmetic reasoning.

**Evidence:** Tables 1-3 report OMAC variants outperforming the cited baselines in the default GPT-3.5-turbo setup. Examples include HumanEval Pass@1 up to 89.25 versus DyLAN at 85.74, MMLU accuracy up to 74.22 versus DyLAN at 69.42, and MATH accuracy up to 35.17 versus DyLAN at 32.35.

**Caveats/Scope:** The main experiments use sampled benchmark subsets, DyLAN-derived default MAS configurations, and three-run averages; claims should be scoped to the reported evaluation setup.

**Source pointers:** `paper.pdf`, Section 4.1; Tables 1-3; Appendix C.1

## Claim 4
**Claim:** Iterative multi-dimension optimization can yield larger gains than optimizing a single dimension.

**Evidence:** Section 4.2 and Figures 4-6 report improved test performance when OMAC iteratively optimizes selected dimension pairs. Appendix D.2 states that, on arithmetic reasoning, the reported relative improvement rises from 2.9% to 9.6% when jointly optimizing Fun-1.1 and Fun-1.2.

**Caveats/Scope:** The paper selects dimensions based on single-dimension performance to control cost, so the result supports the proposed selection-and-iteration strategy rather than arbitrary joint optimization.

**Source pointers:** `paper.pdf`, Section 4.2; Figures 4-6; Appendix C.2.3; Appendix D.2

## Claim 5
**Claim:** Contrastive refinement contributes beyond simply sampling semantically diverse candidates.

**Evidence:** The OMAC-C ablation removes the Contrastive Comparator and keeps only Semantic Initializer candidate generation plus training-set selection. Tables 4, 8, and 9 show full OMAC outperforming OMAC-C across arithmetic reasoning, code generation, and general reasoning dimensions.

**Caveats/Scope:** OMAC-C still often improves over the strongest baseline, so the ablation supports both semantic initialization and contrastive refinement rather than attributing all gains to the comparator alone.

**Source pointers:** `paper.pdf`, Section 4.3; Table 4; Appendix C.2.2; Tables 8-9

## Claim 6
**Claim:** Structural optimization can reduce inference cost, but OMAC has nontrivial training cost.

**Evidence:** Appendix C.2.4 reports lower inference API-call and cost figures for structurally optimized OMAC variants on HumanEval and MATH, with combined Str-2+Str-3 variants using fewer calls than the listed multi-agent baselines. The same section notes that optimizing each HumanEval dimension requires around 1,400 API calls during training, and explores 50% training-data sampling as a cost reduction strategy.

**Caveats/Scope:** Cost numbers are tied to the benchmark setup, GPT-3.5-Turbo pricing assumptions, and the specific collaboration workflows; production cost may differ.

**Source pointers:** `paper.pdf`, Section 4.4; Appendix C.2.4; Tables 10-13
