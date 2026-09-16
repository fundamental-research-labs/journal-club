# Claims

## Claim 1: MACNET turns large agent teams into a DAG-structured refinement process.

**Claim:** The paper's core method is to assign actor agents to graph nodes, critic agents to directed edges, and execute local refinement interactions in topological order.

**Evidence:** Section 2 defines MACNET as a directed acyclic graph, assigns actors to nodes and critics to edges, and specifies dual-agent interactions where critics request refinements and actors emit updated artifacts.

**Caveats/Scope:** This is a framework design claim, not a proof that every DAG or role assignment will improve collaboration.

**Source pointers:** `paper.pdf` Section 2.1-2.2; Figures 1-4; Equations 1-4.

## Claim 2: Artifact-only propagation is the paper's main scalability mechanism.

**Claim:** MACNET controls context growth by propagating only the final artifact from an interaction rather than the full dialogue history.

**Evidence:** Section 2.3 contrasts retaining full interaction histories with retaining artifacts only, and Equation 5 derives quadratic sink-agent token growth without memory control versus linear growth with the mechanism in the mesh case.

**Caveats/Scope:** The quadratic-to-linear comparison is a theoretical token-complexity analysis; the paper does not isolate every practical latency or quality effect of memory control.

**Source pointers:** `paper.pdf` Section 2.3; Equation 5.

## Claim 3: MACNET variants outperform the evaluated baselines on aggregate quality.

**Claim:** Across the four benchmark families, the MACNET variants achieve higher average "Quality" scores than the listed single-agent and multi-agent baselines.

**Evidence:** Table 1 reports aggregate Quality scores above the baselines for MACNET-random, MACNET-mesh, MACNET-star, MACNET-chain, and MACNET-tree; the strongest listed baseline is AgentVerse.

**Caveats/Scope:** Performance is task-dependent. MACNET-chain is not best on HumanEval, and the experiments use the paper's selected datasets, topology sizes, prompts, and GPT-3.5-based interactive reasoning setup.

**Source pointers:** `paper.pdf` Section 3.1; Table 1.

## Claim 4: Topology choice materially changes collaboration quality and efficiency.

**Claim:** No single topology dominates all tasks, but irregular random topologies can provide a strong effectiveness-efficiency tradeoff.

**Evidence:** Section 3.2 compares density, shape, and direction. Table 1 shows different topologies leading different datasets, and the text reports random topologies outperforming regular alternatives in aggregate while using about 51.92% less time than mesh topologies.

**Caveats/Scope:** The comparison covers six representative topology families, not an exhaustive search over all DAGs; the random topology result may depend on construction details and task mix.

**Source pointers:** `paper.pdf` Section 3.2; Table 1; Figures 5-6.

## Claim 5: Scaling collaboration follows a saturating logistic-style trend in these experiments.

**Claim:** Increasing the MACNET node count initially yields slow gains, then faster gains, and finally saturation rather than indefinite improvement.

**Evidence:** Section 3.3 scales node counts from 2^0 to 2^6 and fits the observed performance trend with a sigmoid-variant function. Figure 7 shows this pattern across the studied topologies, and the paper says dense settings can involve more than a thousand node-and-edge agents.

**Caveats/Scope:** This is an empirical fit over the paper's datasets and topology families; the authors explicitly note that future scaling laws should account for additional factors such as profiles, tools, protocols, and routing.

**Source pointers:** `paper.pdf` Section 3.3; Figure 7; Equation 6.

## Claim 6: The proposed mechanism for collaborative emergence is broader refinement coverage.

**Claim:** Larger agent networks may improve artifacts because they surface more critique/refinement aspects and extend artifact generation.

**Evidence:** Section 3.4 analyzes software-development interactions, grouping critique aspects into error and non-error categories. Figure 8 shows more interaction aspects at larger scales, and the text reports a 93.10% likelihood that actors implement critic-suggested refinements.

**Caveats/Scope:** This is a mechanistic hypothesis supported by interaction analysis, not a causal ablation proving that aspect diversity alone drives the performance curve. Longer artifacts may also interact with length-sensitive metrics.

**Source pointers:** `paper.pdf` Section 3.4; Figure 8; Equation 7.
