# Claims

## Claim 1
**Claim:** Multi-agent debate can improve LLM-as-a-judge alignment with human preferences over a matched single-agent evaluator.

**Evidence:** On FairEval, ChatEval's multi-agent setting improves reported accuracy over the single-agent setting for both ChatGPT and GPT-4. On Topical-Chat, the multi-agent GPT-4 setting improves average Spearman and Kendall-Tau correlations over the single-agent GPT-4 setting.

**Caveats/Scope:** The experiments use GPT-family models, homogeneous agent groups, and two evaluation benchmarks; the gains are not uniformly large across all model/dimension combinations.

**Source pointers:** `paper.pdf`, Abstract; Sec. 3.4; Sec. 3.5; Table 1; Table 2

## Claim 2
**Claim:** Persona diversity is a necessary component of the reported ChatEval gains.

**Evidence:** In the FairEval ablation, a multi-agent system with the same generic annotator prompt for every agent matches the single-agent accuracy and has lower kappa than the diverse-role ChatEval variant.

**Caveats/Scope:** This ablation is reported for ChatGPT on FairEval with one-by-one communication, two agents, and two discussion turns; other persona designs or tasks may behave differently.

**Source pointers:** `paper.pdf`, Sec. 2; Sec. 4.1; Table 3; Appendix A

## Claim 3
**Claim:** The communication protocol changes evaluation quality.

**Evidence:** The paper compares one-by-one, simultaneous-talk, and simultaneous-talk-with-summarizer strategies. In the FairEval analysis, one-by-one achieves the strongest reported accuracy and kappa, while the simultaneous variants are lower but still report higher accuracy than the single-agent baseline.

**Caveats/Scope:** The protocol comparison uses ChatGPT, FairEval, three agents, two discussion turns, and the authors' prompt/history construction; it is not a full search over debate protocols.

**Source pointers:** `paper.pdf`, Sec. 2; Sec. 4.2; Table 4; Appendix B

## Claim 4
**Claim:** Scaling debate length or agent count has diminishing returns.

**Evidence:** The role-number analysis improves up to three or four roles before declining in accuracy at five roles, while the discussion-turn analysis shows no clear upward trend as turns increase.

**Caveats/Scope:** The plots are based on FairEval with ChatGPT and the one-by-one strategy, so they should be read as configuration guidance rather than a general scaling law.

**Source pointers:** `paper.pdf`, Sec. 4.3; Figure 3

## Claim 5
**Claim:** ChatEval is intended to mimic a deliberative evaluation process, not just produce a scalar score.

**Evidence:** The qualitative example shows agents opening with a preference, raising alternative considerations, maintaining or revising stances, and reaching a final judgment that matches the human annotation for a hard-to-distinguish pair of answers.

**Caveats/Scope:** This is a qualitative case study, so it illustrates possible behavior rather than proving that all debates are reliable or human-like.

**Source pointers:** `paper.pdf`, Sec. 4.4; Table 5
