# Claims

## Claim 1: MultiAgentBench evaluates both cooperative and competitive LLM-agent behavior.
**Evidence:** The benchmark includes four mutual-goal task settings (research, Minecraft, database diagnosis, and coding) and two conflicting-goal social settings (bargaining and Werewolf). Each scenario defines agent roles, relationships, tools, and task-specific evaluation.

**Caveats/Scope:** The six scenarios are diverse but still curated and mostly have defined task objectives; the paper lists broader open-ended and ambiguous settings as future work.

**Source pointers:** `paper.pdf`, Sections 3.2 and 8; Appendices A.4-A.9.

## Claim 2: The evaluation separates final task success from coordination quality.
**Evidence:** Section 3.3 defines milestone-based KPI tracking, task scores, and a coordination score averaged from communication and planning scores. Appendix A.3 compares prompt-based coordination scoring with human annotations in the Werewolf setting and reports generally close scores.

**Caveats/Scope:** Several metrics depend on LLM-based judgment, and the human-alignment check is limited to one environment rather than all benchmark scenarios.

**Source pointers:** `paper.pdf`, Section 3.3; Appendix A.3; Figures 22-24.

## Claim 3: Strong coordination scores do not guarantee strong task performance.
**Evidence:** Table 1 shows cases where high coordination does not translate into high task score, such as Meta-Llama-3.1-70B in Minecraft, while the discussion argues that intrinsic model capability remains a primary driver of task success.

**Caveats/Scope:** Results are for the paper's five selected models, function-calling setup, communication limits, and scenario configurations.

**Source pointers:** `paper.pdf`, Section 4.2; Table 1; Appendix A.9 and Figure 21 for Minecraft execution issues.

## Claim 4: Coordination protocol and planning prompt choice materially affect performance in the research scenario.
**Evidence:** Section 4.3 reports that graph-based coordination performs strongly among star, tree, graph, and chain protocols in research tasks. Figure 6 reports that cognitive evolving planning has the best coordination score among the tested planning prompts, while group discussion performs poorly.

**Caveats/Scope:** This protocol/planning comparison is presented for the research scenario, so it should not be generalized to every task type without additional testing.

**Source pointers:** `paper.pdf`, Section 4.3; Figures 5 and 6.

## Claim 5: More iterations or more agents can introduce coordination overhead.
**Evidence:** The Minecraft iteration ablation shows scores improving initially and then degrading at higher iteration counts, while the research-agent-count ablation shows declining overall KPI as the number of agents increases even though coordination can improve from one to a small team.

**Caveats/Scope:** The iteration ablation uses a subset of Minecraft tasks, and the agent-count ablation uses selected research tasks; these are diagnostic rather than exhaustive scaling laws.

**Source pointers:** `paper.pdf`, Section 5; Figures 7 and 8.

## Claim 6: The benchmark surfaces qualitative emergent social behaviors.
**Evidence:** Section 6 identifies strategic information sharing, trust-polarized collaboration, and role-driven strategy iteration, with Werewolf and bargaining case studies showing agents selectively sharing information, forming or breaking trust, and changing role strategies over time.

**Caveats/Scope:** These are qualitative case-study observations, not a quantitative guarantee that such behaviors reliably emerge across all models or tasks.

**Source pointers:** `paper.pdf`, Section 6; Appendix A.5.6; Figures 14 and 15; Appendix A.8.
