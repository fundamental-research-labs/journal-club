# Claims

## Claim 1
**Claim:** ACC-Collab treats LLM collaboration as a learned actor-critic behavior rather than an emergent property of prompted off-the-shelf agents.

**Evidence:** The method defines a two-agent team with an actor responsible for answers and a critic responsible for feedback, then alternates training the critic and actor to maximize the final answer correctness after iterative discussion.

**Caveats/Scope:** The framework is specialized to two-agent actor-critic collaboration, not arbitrary multi-agent organizations or open-ended tool-using agents.

**Source pointers:** `paper.pdf`, Abstract; Sec. 3; Sec. 4.1

## Claim 2
**Claim:** Guided collaborative trajectories provide the paper's main mechanism for generating useful preference data for both agents.

**Evidence:** The trajectory-generation algorithm compares natural deliberation with prompts guided toward and away from the ground-truth answer, estimates which intermediate responses improve final accuracy, and keeps pairs whose improvement exceeds a threshold before training with DPO.

**Caveats/Scope:** This depends on tasks where correct and incorrect answers can be identified and used for guidance; the authors leave learned reward functions and broader task settings for future work.

**Source pointers:** `paper.pdf`, Algorithm 1; Sec. 4.2-Sec. 4.5; Appendix C.1

## Claim 3
**Claim:** On the tested QA benchmarks, ACC-Collab generally outperforms prompt-only and training-based multi-agent baselines after five deliberation rounds.

**Evidence:** Table 1 compares SoM, Persona, DebateTune, SFT, DebateGPT, ACC-Collab, and ACC-Collab+ across BoolQ, MMLU, BBH, SCIQ, and ARC for Llama-3, Mistral, and Gemma-2. ACC-Collab variants are the top entries in nearly all rows, including all Llama-3 and Mistral rows.

**Caveats/Scope:** The result is not uniform: Gemma-2 on MMLU is a clear counterexample. The benchmarks are QA-style tasks, and all results are reported on the paper's train/validation/test partitions.

**Source pointers:** `paper.pdf`, Sec. 5; Sec. 5.1; Table 1

## Claim 4
**Claim:** ACC-Collab improves the benefit of multi-round deliberation, not only the final static model accuracy.

**Evidence:** Figure 2 measures percent improvement from round 0 to round 4 and shows ACC-Collab+ with the highest average improvement across the five datasets for each tested base model family. Figure 3 also shows ACC-Collab variants maintaining strong per-round accuracy on BoolQ and SCIQ.

**Caveats/Scope:** Figure 2 reports averaged percent improvements without a table of exact values, so the claim is comparative rather than a precise numeric effect size.

**Source pointers:** `paper.pdf`, Sec. 5.2; Figure 2; Figure 3

## Claim 5
**Claim:** Training changes critic behavior toward more substantive disagreement and feedback.

**Evidence:** The paper contrasts an untrained critic that agrees with an incorrect actor answer against a trained critic that challenges the answer and gives more detailed feedback; Appendix C.2 provides additional critic-response examples. Table 2 further shows that trained actors and critics can improve team accuracy when paired with trained or untrained partners.

**Caveats/Scope:** The behavioral evidence is mostly qualitative, and the paper states that trained actor responses do not show an obvious qualitative change despite improved accuracy.

**Source pointers:** `paper.pdf`, Sec. 5.3; Sec. 5.4; Table 2; Figure 4; Appendix C.2
