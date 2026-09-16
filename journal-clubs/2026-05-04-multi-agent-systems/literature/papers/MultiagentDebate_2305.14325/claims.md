# Claims

## Claim 1
**Claim:** Multiagent debate improves reasoning accuracy over single-agent generation, reflection, and majority voting on the evaluated reasoning tasks.

**Evidence:** Table 1 reports higher scores for multi-agent debate on arithmetic, grade-school math, and chess move prediction. For example, debate reaches 81.8% on arithmetic versus 67.0% for a single agent, 85.0% on GSM8K versus 77.0%, and a higher Stockfish pawn-score measure on chess move prediction than the single-agent and majority baselines.

**Caveats/Scope:** The main results use `gpt-3.5-turbo-0301`, selected task subsets, and mostly three agents with two debate rounds. The method also spends more inference compute than a single agent.

**Source pointers:** Section 3.1; Table 1; Appendix A.2 evaluation details.

## Claim 2
**Claim:** Multiagent debate improves factual-answer quality on the paper's evaluated factuality tasks.

**Evidence:** Table 2 reports gains for debate on biographies, MMLU, and chess move validity. Debate improves biographies from 66.0 to 73.8, MMLU from 63.9 to 71.1, and chess move validity from 29.3 to 45.2 relative to the single-agent baseline, while reflection is mixed or worse on some factual tasks.

**Caveats/Scope:** The biography evaluation is model-judged against Wikipedia-derived bullet facts and may miss incorrect generated details not covered by the ground-truth bullets. MMLU and chess validity are evaluated on selected subsets rather than the full datasets.

**Source pointers:** Section 3.2; Table 2; Appendix A.2 biography, MMLU, and chess-validity details.

## Claim 3
**Claim:** Debate is not merely amplifying a pre-existing correct vote; agents can sometimes revise from initially wrong answers to a correct consensus.

**Evidence:** The paper's qualitative examples show arithmetic, GSM8K, and mixed ChatGPT/Bard debates where all shown agents initially make mistakes but later converge to the correct answer after seeing other agents' reasoning. Table 1 also shows debate outperforming simple majority voting on the reasoning tasks.

**Caveats/Scope:** The all-wrong-to-correct behavior is demonstrated qualitatively, not reported as a separate aggregate rate. The appendix also includes examples where debates converge to incorrect answers.

**Source pointers:** Introduction; Section 3.1 qualitative results; Figures 4, 5, and 11; Appendix A.1.

## Claim 4
**Claim:** The number of agents, number of rounds, prompt wording, and summarization strategy materially affect debate performance and convergence.

**Evidence:** Section 3.3 reports arithmetic performance increasing with more agents and with more rounds in the tested range, with little additional benefit above four rounds. It also reports that longer prompts can slow convergence but improve final correctness, while summarizing other agents' responses helps when many agents would otherwise exceed context limits.

**Caveats/Scope:** These analyses are concentrated on arithmetic and prompt-controlled debate settings, so the same trends should not be assumed for every task or model.

**Source pointers:** Section 3.3; Figures 10, 12, 13, and 14.

## Claim 5
**Claim:** Debate can be run across different model providers, not only multiple copies of the same model.

**Evidence:** In a 20-problem GSM8K comparison, Bard alone solves 11, ChatGPT alone solves 14, and joint ChatGPT/Bard debate solves 17. Figure 11 illustrates a case where both models start with incorrect answers but the debate leads ChatGPT to a correct final answer.

**Caveats/Scope:** This heterogeneous-model result is a small exploratory experiment, not the main benchmark suite.

**Source pointers:** Section 3.3 "Utilizing Different Language Models"; Figure 11.
