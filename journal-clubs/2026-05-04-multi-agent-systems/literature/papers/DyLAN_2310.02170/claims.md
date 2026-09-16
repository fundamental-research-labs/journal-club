# Claims

## Claim 1: DyLAN treats multi-agent collaboration as a dynamic temporal network rather than a fixed chat protocol.

**Evidence:** The paper defines temporal feed-forward networks (T-FFNs), where layers are time steps, nodes are agents, and edges are communication channels. Figure 1 and Figure 2 show the two-stage DyLAN workflow and the way agent team reformation changes the active communication structure.

**Caveats/Scope:** This is a framework-level formulation; the concrete behavior still depends on the candidate agent prompts, tools, LLM ranker, and task-specific post-processing.

**Source pointers:** Abstract; Section 3.1; Section 3.2; Figure 1; Figure 2; Table 1

## Claim 2: Agent Importance Score provides an unsupervised way to select task-relevant agents.

**Evidence:** During Team Optimization, agents rate predecessor responses, scores are propagated backward through the T-FFN, and per-agent scores are summed across time steps. The top-scoring agents form the optimized team. Table 7 shows selected role compositions for MMLU subjects, and Table 13 reports Agent Importance Score outperforming random and human-prior selection on the evaluated GR and CG settings.

**Caveats/Scope:** The metric evaluates behavior in a preliminary trial, not inherent agent quality. It can fail when the candidate pool is badly mismatched to the task, and the paper's Shapley-style validation is limited by combinatorial cost.

**Source pointers:** Section 3.4; Algorithm 2; Appendix B.2; Table 7; Table 13; Appendix C.6

## Claim 3: Dynamic team optimization improves both performance and inference cost in the tested settings.

**Evidence:** Table 5 reports performance gains with fewer second-stage API calls after optimization for code generation, decision-making, and general reasoning. Figure 3 shows that optimized teams of two to four agents can outperform the unoptimized seven-agent DyLAN setting on MMLU while reducing API calls.

**Caveats/Scope:** The main result tables mostly report Task Solving cost after Team Optimization, so the upfront optimization cost is not fully reflected in the headline API-call counts. Benefits depend on reusing or amortizing the selected team.

**Source pointers:** Section 4.2; Section 4.3; Table 5; Figure 3; Appendix C.1

## Claim 4: DyLAN outperforms several single-agent and multi-agent baselines across diverse tasks.

**Evidence:** Table 2 reports gains on HumanEval code generation and WebShop decision-making; Table 3 reports higher MATH accuracy than single execution, LLM-Blender, LLM Debate, and PHP under the corresponding prompt settings; Table 4 reports higher MMLU accuracy than single execution, LLM-Blender, and LLM Debate.

**Caveats/Scope:** Experiments use selected benchmarks, mostly GPT-3.5-family backbones with an additional GPT-4 code-generation check in the appendix. MMLU is down-sampled, WebShop uses 50 test environments, and API calls are only a coarse efficiency proxy.

**Source pointers:** Section 4.1; Section 4.2; Table 2; Table 3; Table 4; Appendix C.2

## Claim 5: Agent team reformation and early stopping play different roles.

**Evidence:** The ablation in Table 6 shows that removing early stopping increases API calls substantially, while removing agent team reformation hurts task performance more. The paper argues that reformation filters temporary mistakes and hallucinations, while early stopping mainly saves compute once answers converge.

**Caveats/Scope:** Early stopping relies on task-specific consistency checks: exact matching for classification and decision-making, and BLEU thresholds for open-ended generation. The authors note that BLEU may be a weak fit for code consistency.

**Source pointers:** Section 3.3.2; Section 4.3; Table 6; Appendix A; Appendix B.1
