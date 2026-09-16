# Claims

## Claim 1
**Claim:** AgentBoard provides a broader analytical evaluation setup than earlier LLM-agent benchmarks by combining task diversity, multi-round interaction, partial observability, fine-grained progress metrics, and analytical evaluation.

**Evidence:** Table 1 compares AgentBoard with AgentBench, GAIA, MINT, API-Bank, ToolEval, and LLM-Eval across those criteria, marking AgentBoard as the only benchmark in the comparison with all five properties.

**Caveats/Scope:** The comparison is limited to the selected prior benchmarks and to the authors' characterization of their properties; it does not cover every later or domain-specific agent benchmark.

**Source pointers:** `paper.pdf`, Table 1; Section 2, "AgentBoard - Overview"

## Claim 2
**Claim:** Progress rate is intended to expose partial task completion that final success rate misses.

**Evidence:** Section 2.2 defines progress rate as the best state-to-goal match or subgoal completion rate over an interaction trajectory. Section 4.2 gives examples where models with similarly low success rates, such as Llama2-13b and Mistral-7b, are separated by substantially different progress rates.

**Caveats/Scope:** Progress rate quality depends on accurate state matching or subgoal labels, and the paper notes that human annotation is a scalability limitation.

**Source pointers:** `paper.pdf`, Section 2.2; Table 3; Section 4.2; Limitations

## Claim 3
**Claim:** The automatic progress-rate annotations track human judgments of agent progress closely in the evaluated tasks.

**Evidence:** The authors collect 60 trajectories per task from GPT-4, GPT-3.5-Turbo, and DeepSeek-67b, ask four authors to assign progress scores, and report Pearson correlations above 0.95 between human ratings and automatic progress rates across the tasks in Figure 3.

**Caveats/Scope:** The validation uses sampled trajectories and author raters; it supports the metric for these tasks but does not eliminate annotation subjectivity or guarantee transfer to new environments.

**Source pointers:** `paper.pdf`, Section 3.2; Figure 3; Appendix J; Table 13

## Claim 4
**Claim:** In the reported experiments, proprietary models outperform the tested open-weight models as general LLM agents.

**Evidence:** Table 3 ranks models by average success rate and shows GPT-4 at 70.0/47.9 average progress/success, followed by other proprietary systems before the strongest open-weight models. Section 4.2 explicitly states that proprietary models still outperform the best open-weight models.

**Caveats/Scope:** The result reflects the specific model versions, prompts, decoding choices, and AgentBoard tasks used in the paper; later models or stronger agent scaffolds could change the ranking.

**Source pointers:** `paper.pdf`, Table 3; Section 4.1; Section 4.2; Appendix I

## Claim 5
**Claim:** Agent performance drops on harder, more compositional examples, making hard/easy breakdowns important beyond average scores.

**Evidence:** Table 5 reports progress and success rates for easy and hard cases and shows drops for all listed models. The paper interprets hard examples as reflecting multiple-subgoal settings where even strong models such as GPT-4 struggle.

**Caveats/Scope:** Hardness is operationalized mainly by subgoal or condition counts, which may not capture all forms of task difficulty.

**Source pointers:** `paper.pdf`, Table 5; Section 4.3, "Performance breakdown for hard and easy examples"; Table 14

## Claim 6
**Claim:** Long-range interaction remains a major bottleneck, especially for many open-weight agents.

**Evidence:** Figure 4 plots progress rate over interaction steps, and Section 4.3 states that GPT-4 and Claude2 continue making progress over 30 steps in some tasks, while many open-weight models peak early and generally stop progressing after about six steps.

**Caveats/Scope:** The analysis is task-dependent: the paper also notes that some web and tool tasks plateau early even for strong models, suggesting later stages can be especially challenging.

**Source pointers:** `paper.pdf`, Figure 4; Section 4.3, "Long-Range Interaction"
