# Claims

## Claim 1
**Claim:** ReAct frames language-agent behavior as an interleaved stream of thoughts, actions, and observations rather than as reasoning-only or action-only prompting.

**Evidence:** Section 2 defines an augmented action space that includes language thoughts, and the prompts use human-written trajectories where thoughts decompose goals, extract observations, reformulate searches, track progress, and guide final answers or environment actions.

**Caveats/Scope:** The paper mainly studies few-shot prompting of large frozen models; the quality of thoughts depends on the exemplars, model priors, and available action space.

**Source pointers:** `paper.pdf`, Figure 1; Section 2 "ReAct: Synergizing Reasoning + Acting"; Appendix C prompts.

## Claim 2
**Claim:** On knowledge-intensive QA and fact verification, ReAct improves over action-only prompting, while hybrid ReAct/CoT-SC methods are strongest among the prompting baselines.

**Evidence:** Table 1 reports ReAct above Act on HotpotQA and FEVER. The best HotpotQA prompting result is ReAct -> CoT-SC, while the best FEVER prompting result is CoT-SC -> ReAct, supporting the paper's claim that internal knowledge and external retrieval are complementary.

**Caveats/Scope:** ReAct alone slightly trails CoT on HotpotQA, and all prompting methods are far below the supervised SoTA numbers reported in the same table. The retrieval interface is a simple Wikipedia API, not a modern learned retriever.

**Source pointers:** `paper.pdf`, Section 3.1 setup; Section 3.2 methods; Section 3.3 results; Table 1.

## Claim 3
**Claim:** ReAct makes HotpotQA trajectories more grounded and less hallucination-prone than chain-of-thought, but it introduces retrieval and control-flow failure modes.

**Evidence:** In the manual HotpotQA trajectory analysis, ReAct has fewer false positives among successful traces than CoT, and hallucination is not labeled as a ReAct failure mode in the sampled failures; however, ReAct has higher reasoning-error rate and search-result errors.

**Caveats/Scope:** The error taxonomy is based on a manually inspected sample of trajectories, not a full benchmark-wide annotation, and "grounded" here depends on the correctness and coverage of the Wikipedia observations.

**Source pointers:** `paper.pdf`, Section 3.3 "ReAct vs. CoT"; Table 2; Figure 4.

## Claim 4
**Claim:** Sparse reasoning improves long-horizon interactive decision making in text-game and web-shopping environments.

**Evidence:** On ALFWorld, the best ReAct prompt trial reaches 71% overall success, compared with 45% for Act and 37% for BUTLER. On WebShop, ReAct improves success rate over Act and the IL/IL+RL baselines in Table 4.

**Caveats/Scope:** ALFWorld results vary by prompt trial, and WebShop performance remains well below the human-expert reference. The experiments use constrained benchmark action spaces rather than open-ended web or physical actions.

**Source pointers:** `paper.pdf`, Section 4 "Decision Making Tasks"; Table 3; Table 4.

## Claim 5
**Claim:** The explicit thought/action trace improves diagnosability and allows limited human-in-the-loop correction.

**Evidence:** The paper argues that humans can distinguish model-internal reasoning from environment observations and inspect why actions were taken. Figure 5 shows an ALFWorld failure corrected by editing thoughts during the trajectory.

**Caveats/Scope:** This is demonstrated through examples rather than a large user study. Thought traces can still be wrong or hallucinated, so interpretability does not guarantee faithfulness.

**Source pointers:** `paper.pdf`, Abstract; Section 2 feature discussion; Appendix A.3; Figure 5; Ethics Statement.

## Claim 6
**Claim:** ReAct trajectories appear useful as finetuning data for smaller language models on knowledge-intensive reasoning.

**Evidence:** The paper bootstraps 3,000 correct ReAct-generated trajectories for finetuning and reports that finetuned ReAct becomes the best of the compared methods on HotpotQA for PaLM-8B/62B, with the 62B finetuned ReAct model outperforming 540B prompting methods in Figure 3.

**Caveats/Scope:** The finetuning result is limited to HotpotQA in this paper, uses generated trajectories, and relies on PaLM models that are not openly accessible in the reported setup.

**Source pointers:** `paper.pdf`, Section 3.2 "Finetuning"; Section 3.3 "ReAct performs best for fine-tuning"; Figure 3; Reproducibility Statement.
