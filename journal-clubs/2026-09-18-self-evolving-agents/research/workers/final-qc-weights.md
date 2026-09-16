# Final QC: weights, self-play, and GEPA statements

Checked September 16, 2026 against the primary PDFs and substantive notes. This is a bounded factual QC of `research/shortlist.md` and `research/landscape.md`; the shared files were not edited.

## Exact changes recommended

### 1. Scope SEAL's “two outer rounds” to knowledge incorporation

In the shortlist SEAL boundary, change:

> Only two outer RL rounds; improvement can erase earlier knowledge.

to:

> The knowledge-incorporation experiment uses two outer ReSTEM rounds; sequential self-edits measurably degrade earlier-task performance.

Reason: §4.2/Appendix B specifies two ReSTEM rounds for SQuAD knowledge incorporation. The inspected ARC section specifies 15 sampled edits per training task and five per evaluation task, but does not support applying the “two rounds” statement to ARC or to SEAL as a whole. Figure 6 shows gradual forgetting; “degrade” is more exact than “erase,” since the paper explicitly says prior performance declines without complete collapse.

### 2. Make the SEAL 72.5% unit explicit

The shortlist's “72.5% of evaluated configurations” is directionally correct but less precise than the paper. Prefer:

> On eight selected ARC evaluation tasks, 29 of 40 sampled self-edit attempts succeed (**72.5%**; five independently applied edits per task).

Reason: §4.1 evaluates five generated self-edits on each of eight selected tasks, yielding 40 edit attempts. The percentage is a self-edit success rate, not task accuracy and not full-ARC performance. The paper gives 72.5%; `29/40` is the exact count implied by that design and percentage, although the paper does not print “29/40” verbatim. The current boundary column correctly states 11 training tasks, eight evaluation tasks, and 40 attempts. The landscape's “eight selected test tasks” statement is correct.

### 3. Label GEPA aggregates as reported Table 1 values

In the shortlist GEPA row, change:

> Six-task Qwen aggregate: **54.85 GEPA vs 48.91 GRPO**

to:

> Six-task Qwen aggregate reported in Table 1: **54.85 GEPA vs 48.91 GRPO**

Reason: rendered primary Table 1 reports those exact aggregates across HotpotQA, IFBench, HoVer, PUPA, AIME-2025, and LiveBench-Math. GEPA's displayed task cells average to 54.845, which rounds to 54.85. GRPO's displayed two-decimal cells average to about 48.97, not 48.91; the reported aggregate therefore appears to use unrounded underlying scores or contains a small source inconsistency. Preserve 48.91 as the paper's reported aggregate, rather than presenting it as exactly reconstructible from displayed cells. The six-task scope, GEPA's five-of-six wins, AIME 32 versus 38 loss, and task-specific 1,839–7,051 versus 24,000 rollout counts are confirmed.

### 4. Add the retrospective model-judge qualifier to R-Zero label quality

The shortlist and landscape already correctly say declining label quality is associated with, but does not causally isolate, collapse. For maximal precision, extend the shortlist boundary to:

> Retrospective model-judge audits show declining pseudo-label quality, but that association does not isolate the cause of collapse.

Reason: Table 5 uses three sets of 200 generated questions (steps 15/30/45) and treats GPT-4o as a perfect oracle, reporting pseudo-label accuracy 79%→69%→63%. Appendix Table 7 uses a separate Gemini-labeled late-stage audit and finds different model sizes begin deteriorating at different estimated label-accuracy levels. The paper itself concludes label noise is not the sole cause. The shared landscape states this interpretation accurately.

### 5. Scope the R-Zero peak/drop to the exact analysis

The shortlist's values are correct. A slightly stronger wording would be:

> In the Qwen3-4B two-model analysis, average math performance peaks at **49.12 after step 45** and falls to **46.52 at step 60** (Appendix Table 6).

Reason: Appendix Table 6 compares two-model R-Zero with a shared-parameter Single-R-Zero configuration. The 49.12→46.52 sequence is the two-model Qwen3-4B analysis, not an aggregate over all four main model families. The present text says “two-role math performance,” which is substantively correct; adding the model and metric prevents broader interpretation.

## Confirmed without change

- **Versions and venues:** GEPA was first posted July 25, 2025, current inspected arXiv v2 is February 14, 2026, and the PDF says “Accepted at ICLR 2026 (Oral).” SEAL was first posted June 12, 2025, v2 is September 18, 2025, and it appears in NeurIPS 2025 proceedings. R-Zero was first posted August 7, 2025, v4 is February 13, 2026, and the PDF says “Published as a conference paper at ICLR 2026.” The shortlist dates/venues are correct.
- **SEAL mechanism:** describing SEAL as generating synthetic update data plus optimization instructions that change weights is accurate. Its external optimizer, task/evaluator, and update stack remain fixed, as the landscape indicates.
- **R-Zero mechanism:** alternating Challenger/Solver updates, majority-vote pseudo-labeling, and fixed filtering/reward rules are accurately represented. Pairing it with Absolute Zero as an executable-reward companion is appropriate; they are related but not independent replications under identical conditions.
- **R-Zero source inconsistencies:** the shortlist properly warns that main-table averages conflict with prose. Visual inspection of v4 confirms Table 1 Qwen3-8B math 48.64→53.72 versus prose 49.18→54.69, and Table 2 general 31.98→34.50 versus prose claiming +5.13. These are source inconsistencies, not text-extraction errors.
- **GEPA cost qualification:** the landscape correctly says fewer rollouts do not establish lower total compute. GEPA includes reflection and extensive validation evaluation; Table 1 rollout counts are not matched token, accelerator-time, wall-clock, or dollar budgets.

## QC disposition

No weight/self-play/GEPA statement requires a ranking change. The shared documents are usable after the wording corrections above. The most material correction is scoping SEAL's two-round statement to knowledge incorporation; the others improve units, provenance, and generalization boundaries.
