# Claims

## Claim 1
**Claim:** An environment-first collection pipeline can scale execution-backed SWE training data more efficiently than task-first SWE-bench-style collection.

**Evidence:** SWE-smith builds a repository execution environment first, then synthesizes many bugs within it. The paper reports 50,137 task instances from 128 Python repositories and 295 GB of environment storage, while estimating that a comparable SWE-bench-style 50k-instance collection would require 50-150 TB.

**Caveats/Scope:** The collection is Python-centric and depends on reusable repository-level environments; the storage comparison is an estimate against SWE-bench-style per-task images.

**Source pointers:** `paper.pdf`, Abstract; Section 2; Section 2.2; Table 1; Table 2; Appendix C.1

## Claim 2
**Claim:** Synthetic bugs can be made into executable SWE tasks by filtering candidate patches through existing tests.

**Evidence:** SWE-smith generates candidates with LM modification, LM rewrite, procedural AST edits, patch combination, and PR mirroring, then keeps only patches that break one or more existing passing tests. Table 1 reports validated instances and yield rates by strategy.

**Caveats/Scope:** These are synthetic regressions, not necessarily bugs that occurred in real maintenance workflows; fidelity to real issues remains a stated limitation for evaluation use.

**Source pointers:** `paper.pdf`, Section 2.1; Figure 2; Table 1; Appendix B; Appendix C.2; Appendix D

## Claim 3
**Claim:** SWE-smith trajectories can materially improve an open-weight SWE agent in the authors' evaluation setup.

**Evidence:** The authors generate expert trajectories with SWE-agent and Claude 3.7 Sonnet, train Qwen 2.5 Coder Instruct models, and report SWE-agent-LM-32B at 40.2% Pass@1 on SWE-bench Verified after training on 5,016 trajectories.

**Caveats/Scope:** Results use SWE-agent, Qwen 2.5 Coder Instruct 32B, rejection-sampling fine-tuning, a 75-step inference cap, and single-attempt evaluation without verifiers or inference-time scaling.

**Source pointers:** `paper.pdf`, Section 3; Section 4; Table 3; Appendix F.1; Appendix F.3

## Claim 4
**Claim:** The type of synthetic task and the issue text both affect downstream training quality.

**Evidence:** In ablations, PR Mirror trajectories produce the strongest student model among the tested bug strategies, while LM Rewrite and Procedural Modification are close; LM-generated issue text is empirically comparable to original issue text for PR Mirror tasks.

**Caveats/Scope:** The ablations train Qwen 2.5 7B student models with capped trajectory counts, so the exact ranking may change with model scale, agent scaffold, or training recipe.

**Source pointers:** `paper.pdf`, Section 4.1; Table 4; Table 5; Appendix D

## Claim 5
**Claim:** Repository diversity improves general SWE-agent performance, while repository-specific training can produce useful specialists.

**Evidence:** With 700 procedural-modification trajectories, performance rises as the number of represented repositories increases. Separate SymPy experiments show target-repository gains for both single-repository fine-tuning and specialist-stage fine-tuning, with smaller drops on general SWE-bench Verified without SymPy.

**Caveats/Scope:** The diversity result is based on procedural tasks and fixed 700-trajectory samples; the specialization case study is limited to SymPy and a small target evaluation subset.

**Source pointers:** `paper.pdf`, Section 4.1; Figure 4; Figure 5

## Claim 6
**Claim:** SWE-agent-LM-32B is efficient when it solves tasks but has identifiable failure modes around localization and repeated actions.

**Evidence:** On SWE-bench Verified, solved tasks use fewer average steps than Claude 3.7 Sonnet in the paper's comparison, but more than 25% of unsuccessful SWE-agent-LM-32B trajectories contain repetitive action sequences of length at least 10, and many failures are associated with runtime or cost limits before useful edits.

**Caveats/Scope:** This analysis is specific to SWE-agent-LM-32B inside SWE-agent and may change with scaffold-level mitigations, stronger search tools, or different stopping limits.

**Source pointers:** `paper.pdf`, Section 4.2; Figure 6; Figure 7; Figure 8; Appendix F.5
