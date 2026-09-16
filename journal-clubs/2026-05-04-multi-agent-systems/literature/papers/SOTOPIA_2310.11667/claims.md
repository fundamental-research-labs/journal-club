# Claims

## Claim 1: SOTOPIA turns social intelligence evaluation into an interactive, goal-driven task.

**Evidence:** The environment samples social scenarios, private goals, character profiles, and relationships, then runs multi-turn role-play episodes where agents can speak, use non-verbal communication, take physical actions, remain silent, or leave. The paper's task space includes 90 scenarios, 40 characters, 90 relationships, and 450 sampled tasks.

**Caveats/Scope:** The experiments focus on short dyadic episodes with fixed turn-taking; Appendix B notes that richer relationship types, larger scenario pools, multi-party interaction, and asynchronous dynamics remain future work.

**Source pointers:** `paper.pdf`, Sections 2.1-2.2; Section 4; Appendix B

## Claim 2: SOTOPIA-EVAL evaluates more than whether the explicit social goal was achieved.

**Evidence:** The evaluation framework scores each agent along seven dimensions: goal completion, believability, knowledge gain, secret keeping, relationship impact, social-rule compliance, and financial/material benefit. Several dimensions have negative ranges to represent harms such as leaking secrets or violating norms.

**Caveats/Scope:** These dimensions are designed by the authors from sociology, psychology, and economics literature; they are not a complete theory of social intelligence.

**Source pointers:** `paper.pdf`, Section 3

## Claim 3: GPT-4 is a usable but limited proxy for human evaluation in SOTOPIA.

**Evidence:** In the human-evaluation study, most GPT-4 scores fall near human scores, and Table 1 reports strong correlations for model outputs on goal completion, financial/material benefit, and relationship. The paper also reports weaker correlations for human role-play and cautions that GPT-4 tends to rate higher than humans on some dimensions.

**Caveats/Scope:** The authors explicitly warn about evaluator bias and note weaker alignment for dimensions such as secrets and social rules; the claim should not be generalized to all LLM judges or all social settings.

**Source pointers:** `paper.pdf`, Section 5; Figure 2; Table 1; Appendix G

## Claim 4: Stronger static benchmark performance does not guarantee stronger interactive social performance.

**Evidence:** Table 2 shows GPT-4 leading, followed by GPT-3.5, Llama-2-70b-chat, and MPT-30b-chat across most SOTOPIA dimensions. The paper emphasizes that Llama-2-70b-chat trails GPT-3.5 in SOTOPIA despite being competitive or better on some static benchmarks, and qualitative examples show failures to maintain persona, advance conversation, or respond actively.

**Caveats/Scope:** The result depends on the particular model versions, prompts, and SOTOPIA tasks tested in the paper.

**Source pointers:** `paper.pdf`, Section 4; Section 6; Table 2; Figures H.3-H.5

## Claim 5: Social interaction quality depends on the partner, not only the focal agent.

**Evidence:** The pairwise performance heatmap shows weaker partner models reduce the performance of other agents. The paper describes cases where communication collapses because one model fails to answer or cooperate, causing both sides to fail the task.

**Caveats/Scope:** Most SOTOPIA scenarios in the paper are fundamentally cooperative, so the partner-effect finding may differ in adversarial or non-cooperative task mixes.

**Source pointers:** `paper.pdf`, Section 6; Figure 3; Figure H.6

## Claim 6: Humans still outperform GPT-4 on the hardest social-goal tasks.

**Evidence:** On SOTOPIA-hard, Table 3 reports significantly higher goal-completion scores for humans than GPT-4 when compared against GPT-4 interacting with humans. The authors' qualitative analysis says humans tend to be more strategic in bargaining and more persistent in pursuing assigned goals.

**Caveats/Scope:** SOTOPIA-hard contains the top 20 challenging tasks selected for GPT-4, and the human study is smaller than the model-model simulation.

**Source pointers:** `paper.pdf`, Section 7; Table 3; Figures H.10-H.13
