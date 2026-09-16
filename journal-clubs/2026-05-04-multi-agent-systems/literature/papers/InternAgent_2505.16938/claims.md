# Claims

## Claim 1: InternAgent frames autonomous scientific research as a closed-loop multi-agent pipeline from idea to verification.

**Evidence:** Section 2 and Figure 2 define three linked capabilities: self-evolving idea generation with human-interactive feedback, idea-to-methodology construction, and evolutionary experimental planning and execution. The introduction and conclusion emphasize completing the loop from hypothesis generation to code implementation and experimental validation.

**Caveats/Scope:** This is a system-design claim. The paper demonstrates the loop through selected benchmark tasks rather than proving general autonomous discovery across all scientific settings.

**Source pointers:** `paper.pdf`, Sec. 1, Sec. 2, Fig. 2, Sec. 6

## Claim 2: InternAgent is evaluated across a broad suite of 12 AI and science tasks.

**Evidence:** Section 3.1 lists tasks in reaction yield prediction, molecular dynamics, power flow estimation, time series forecasting, perturbation-response transcription prediction, enhancer activity prediction, sentiment classification, 2D image classification, 3D point cloud classification, semantic segmentation, point cloud autonomous driving, and vision-language model fine-tuning. Tables 1-4 report task-specific metrics and experiment statistics.

**Caveats/Scope:** The tasks are broad but still author-selected, use heterogeneous metrics, and often compare against task-specific baselines rather than a single standardized autonomous-research benchmark.

**Source pointers:** `paper.pdf`, Sec. 3.1, Tables 1-4

## Claim 3: In the reported experiments, InternAgent improves task performance over baselines and outperforms DOLPHIN where DOLPHIN is applicable.

**Evidence:** Tables 1 and 2 report higher max and average performance for InternAgent than the baseline on all 12 tasks. On tasks where DOLPHIN results are reported, InternAgent's max and average scores are generally higher; the text highlights AutoRYP as an example where InternAgent's max R2 exceeds DOLPHIN's.

**Caveats/Scope:** These are paper-reported results, not an independent replication. Metrics differ by task, and the paper reports successful/improving ideas separately from all generated ideas, so task-level gains should be read with the execution statistics in Tables 3 and 4.

**Source pointers:** `paper.pdf`, Sec. 3.2, Tables 1-4

## Claim 4: InternAgent supports repository-level experiments that previous auto-research systems in the comparison do not handle.

**Evidence:** The paper states that DOLPHIN only supports single-file experiments and marks DOLPHIN as not applicable for project-level tasks such as Auto2DSeg, AutoPCDet, and AutoVLM. InternAgent reports executable and improving runs on those tasks, with Auto2DSeg improving the DeepLabV3Plus baseline in Table 2.

**Caveats/Scope:** Repository-level support is shown on selected codebases, not as a general software engineering benchmark. The success rates in Table 4 indicate that not every generated idea runs or improves performance.

**Source pointers:** `paper.pdf`, Sec. 2.3, Sec. 3.2, Tables 2 and 4

## Claim 5: Adaptive evolution improves performance and execution outcomes in the authors' ablation.

**Evidence:** Table 8 compares InternAgent with and without adaptive evolution on AutoRYP, Auto2DCls, and AutoSenCls. The full system reports higher max and average metrics and more improving/successful ideas across those tasks.

**Caveats/Scope:** The ablation covers only three tasks and focuses on the adaptive evolution module, so it does not isolate every component of the full multi-agent pipeline.

**Source pointers:** `paper.pdf`, Sec. 3.3, Table 8

## Claim 6: Expert reviewers rate InternAgent-generated ideas higher than AI-Scientist-V2 ideas in the paper's human evaluation.

**Evidence:** Table 10 reports average scores from five qualified reviewers over 20 ideas per method on four tasks. InternAgent receives higher soundness, contribution, and overall scores than AI-Scientist-V2 in reaction yield prediction, 2D semantic segmentation, 2D image classification, and point cloud autonomous driving.

**Caveats/Scope:** The evaluation is subjective and limited to four tasks. The paper provides reviewer qualification criteria in Appendix B, but the result should still be treated as an internal expert assessment unless externally replicated.

**Source pointers:** `paper.pdf`, Sec. 4.2, Table 10, Appendix B.1-B.2
