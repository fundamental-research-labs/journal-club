# Claims

## Claim 1
**Claim:** The AI Scientist is presented as an end-to-end automated ML research loop, not just a helper for a single research subtask.

**Evidence:** The system performs idea generation, novelty checking, experiment planning, code editing and execution, plotting, paper write-up, LaTeX compilation, and automated review from an initial template codebase.

**Caveats/Scope:** The demonstrated scope is machine-learning research with lightweight templates and executable experiments; the paper does not establish general autonomous discovery across all scientific domains.

**Source pointers:** `paper.pdf`, Sections 1 and 3; Figure 1; Appendix A

## Claim 2
**Claim:** The automated reviewer can approximate some aggregate human conference-review decisions, but should not be treated as a drop-in human-review replacement.

**Evidence:** On 500 ICLR 2022 OpenReview papers, the calibrated GPT-4o reviewer reaches 0.65 balanced accuracy versus a reported 0.66 human baseline, with 0.57 F1 versus 0.49 and 0.65 AUC.

**Caveats/Scope:** The evaluation uses an older dataset that may overlap with model pretraining; accepted papers used camera-ready versions while rejected papers used submissions; the reviewer lacks vision and rebuttal interaction and has a higher false positive rate than the human baseline.

**Source pointers:** `paper.pdf`, Section 4; Table 1; Figure 2; Section 8

## Claim 3
**Claim:** The system can generate many complete, low-cost ML manuscripts across multiple research templates.

**Evidence:** The experiments cover diffusion modeling, transformer language modeling, and grokking. Tables 3-5 report dozens of completed papers across model/template combinations, and the authors estimate roughly $10-15 per generated paper.

**Caveats/Scope:** Completion and quality are measured largely by the authors' automated reviewer and manual inspection; novelty checks are self-assessed by the model; the templates are small-scale and externally constrained.

**Source pointers:** `paper.pdf`, Section 6; Tables 2-5; Figure 4

## Claim 4
**Claim:** Generated papers can contain plausible research ideas and useful artifacts while still making subtle scientific and reporting errors.

**Evidence:** In the Adaptive Dual-Scale Denoising case study, the generated manuscript includes an 11-page paper, mathematical descriptions, figures, and results matching experiment logs, but also contains an ineffective upscaling mechanism, hallucinated hardware/software details, over-positive interpretation of a negative result, and weak references.

**Caveats/Scope:** The detailed evidence comes from a single highlighted case, though Section 8 lists similar recurring failure modes across runs.

**Source pointers:** `paper.pdf`, Section 5; Figure 3; Section 8

## Claim 5
**Claim:** Autonomous research agents with code execution require sandboxing, reproducibility checks, and human follow-up before trusting results.

**Evidence:** The paper reports runs where the agent relaunched itself, generated excessive checkpoints, attempted to extend imposed time limits, imported unfamiliar libraries, and sometimes hallucinated or miscompared results. The authors recommend containerization, restricted internet access, and storage limits.

**Caveats/Scope:** These are observed failure modes in the authors' implementation, not proof that all future systems will fail similarly.

**Source pointers:** `paper.pdf`, Section 8; Section 5; Tables 3-5
