# Claims

## Claim 1
**Claim:** Collab-Overcooked is designed to force collaboration rather than merely present tasks as collaborative.

**Evidence:** The benchmark splits the kitchen into resource-isolated sub-environments, gives Alice and Bob different action spaces, and uses asymmetric task knowledge so agents must communicate and exchange resources to complete tasks. Table 1 positions it as supporting forced collaboration and both end-to-end and process-oriented evaluation.

**Caveats/Scope:** The design is currently a two-agent grid-kitchen environment with sequential process-specific tasks; it does not prove the same mechanisms cover all real-world multi-agent settings.

**Source pointers:** `paper.pdf`, Abstract; Sec. 4.1; Table 1; Appendix A.1

## Claim 2
**Claim:** TES/ITES allow the paper to evaluate collaboration as a process, not just final task success.

**Evidence:** TES compares action trajectories to annotated Referential Action Trajectories while penalizing redundant actions; ITES measures the marginal contribution of a newly proposed collaborative action. PC, IC, and RC are derived from these scores to measure progress completeness, correct collaboration initiation, and correct response.

**Caveats/Scope:** The metrics depend on having reliable RATs. The authors note that exhaustive RAT enumeration becomes difficult in environments with very large state/action spaces.

**Source pointers:** `paper.pdf`, Sec. 3.2-3.3; Appendix B; Limitations

## Claim 3
**Claim:** Current LLM-MAS agents degrade substantially as collaboration complexity increases.

**Evidence:** Table 2 reports strong Level 1 performance for several models but much lower success rates at Level 5 and Level 6; for example, Claude Sonnet 4 remains strongest overall but falls from 100% SR at Levels 1-2 to 58% at Level 6, while many smaller/open models reach 0% SR on high-complexity levels.

**Caveats/Scope:** Results use the paper's shared baseline architecture, gamma = 1.5 time limit factor, beta = 0.95 TES setting, and 10 repetitions per task.

**Source pointers:** `paper.pdf`, Sec. 5.2; Sec. 5.3.1; Table 2

## Claim 4
**Claim:** Initiating collaboration is a stronger bottleneck than responding to collaboration for many evaluated models.

**Evidence:** The process-oriented analysis reports that most 14B+ models show higher RC than IC, and the authors interpret this as evidence that instruction-following makes response easier while recognizing when and how to ask for help remains difficult.

**Caveats/Scope:** IC and RC are ITES-based approximations of correct collaborative behavior, so the conclusion is tied to the benchmark's RAT annotations and request/response protocol.

**Source pointers:** `paper.pdf`, Sec. 5.3.2; Figure 3; Appendix B.2; Appendix C.4

## Claim 5
**Claim:** Collaboration failures are linked to attention misalignment and late-sequence degradation.

**Evidence:** The failure analysis finds that agents become more prone to premature or repetitive initiation in later collaborative steps. Attention analysis shows successful initiation correlates with attention to collaboration rules, while failed cases overemphasize recipe/task execution details. In the Qwen attention-intervention experiments, the paper reports 35% to 64% improvements on previously failed instances.

**Caveats/Scope:** Attention interventions are diagnostic experiments on selected Qwen models and task levels, not a complete training or deployment method.

**Source pointers:** `paper.pdf`, Sec. 5.3.4; Figure 5; Appendix C.3; Appendix C.4

## Claim 6
**Claim:** Human participants provide evidence that the benchmark's high-complexity tasks are tractable despite being hard for LLM agents.

**Evidence:** Human experiments with ten volunteers show comparatively stable SR, PC, IC, and RC across all six complexity levels under 10s, 15s, and 20s per-step time constraints, while the strongest open-source LLM baseline declines as task complexity increases.

**Caveats/Scope:** The human evaluation uses a small participant pool, paired trials, a human-computer interface, and verbal communication, so it is best read as a performance ceiling/context check rather than a broad human study.

**Source pointers:** `paper.pdf`, Sec. 5.3.3; Figure 4; Appendix C.2; Table 6
