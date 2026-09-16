# Claims

## Claim 1: Language agents can be represented as optimizable computational graphs.

**Evidence:** The paper defines an agent as a directed computational graph with nodes for operations and edges for information flow, then defines a swarm as a composite graph connecting multiple agent graphs. Figure 1 illustrates nodes, agent graphs, swarm graphs, communication edges, and optimization targets.

**Caveats/Scope:** The formal execution model in the main text focuses on DAGs and string inputs/outputs, even though the authors argue the framework can generalize to multimodal data and broader operations.

**Source pointers:** `paper.pdf`, Abstract; Figure 1; Sections 2.1-2.2

## Claim 2: Inter-agent communication topology can be optimized as a distribution over feasible DAG edges.

**Evidence:** GPTSwarm parameterizes potential inter-agent edges, samples feasible DAGs, evaluates utility, and updates edge probabilities with REINFORCE. The MMLU adversarial experiments use this mechanism to reduce the influence of deliberately harmful agents and recover toward the direct-answer baseline.

**Caveats/Scope:** Edge optimization is evaluated on selected benchmark setups; it does not prove that learned communication topology will generalize across arbitrary agent systems or tasks without task-specific utility signals.

**Source pointers:** `paper.pdf`, Sections 2.3 and 3.1; Figure 2; Appendix E.1 / Table 4

## Claim 3: GPTSwarm is more cost-efficient than compared MMLU multi-agent optimization baselines, though not the highest-accuracy one in Appendix D.

**Evidence:** Appendix D reports the 3 truthful/3 adversarial MMLU comparison: GPTSwarm inference reaches 0.8301 accuracy after USD 5.32 optimization cost and USD 1.82 inference cost, while DyLAN reaches 0.8366 accuracy but uses USD 105.93 optimization cost and USD 14.99 inference cost; Multiagent Debate is 0.5751 accuracy.

**Caveats/Scope:** This is one adversarial MMLU setup with specific prompts, models, and cost assumptions. DyLAN is slightly more accurate in the table, so the claim is about cost/performance tradeoff rather than absolute accuracy.

**Source pointers:** `paper.pdf`, Appendix D.1 / Table 3

## Claim 4: Edge optimization improves Mini Crosswords performance beyond random or manually aggregated alternatives in the paper's setup.

**Evidence:** Section 3.2 reports an increase from 0.465 (+/- 0.0509) for the initial edge distribution to 0.575 (+/- 0.0275) after ten REINFORCE iterations. Best-of-three aggregation across the three agents scores 0.320 (+/- 0.0415), and a same-edge-count random distribution scores 0.510 (+/- 0.0552).

**Caveats/Scope:** The experiment uses a 20-problem Mini Crosswords subset and reports averages over three runs; the GPT-4-Turbo result is evaluated on one randomly selected optimized distribution because of API cost.

**Source pointers:** `paper.pdf`, Section 3.2; Figures 3-4; Appendix D.2

## Claim 5: Node-level prompt optimization can improve a coding agent without changing its high-level architecture.

**Evidence:** On HumanEval, the paper optimizes prompts inside a ReAct-style agent using node histories and execution feedback. The reported online learning result improves from 0.76 without optimization to 0.88 (+/- 0.007), with most gains occurring in the first five iterations.

**Caveats/Scope:** The result is for the authors' HumanEval setup and node optimizer; it is not a general claim that prompt optimization alone solves program synthesis or coding-agent reliability.

**Source pointers:** `paper.pdf`, Section 3.3; Figure 5; Appendix E.3

## Claim 6: Modular swarms help on GAIA primarily through composition of tools and self-consistency, not through the paper's graph optimizers.

**Evidence:** The GAIA experiments build swarms from DirectAnswer, query generation, web search, file analysis, combined-answer, and Tree-of-Thought components. Table 1 reports GPTSwarm at 18.45 average versus GPT-4-Turbo at 9.70 and AutoGPT at 4.85; Table 2 shows the 7xTOT self-consistency swarm at 30.56 (+/- 3.25) on Level 1.

**Caveats/Scope:** The authors explicitly state that the GAIA experiments include neither edge-based nor node-level optimization. Performance remains far below the human Level 1 result reported in Table 2, and web access is limited to direct downloads and Google search.

**Source pointers:** `paper.pdf`, Section 3.4; Tables 1-2; Figure 6
