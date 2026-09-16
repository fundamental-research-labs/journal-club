# Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration

## Source and access

**Source key:** `2026-spontaneous-world-knowledge`.

**Originals and source links:** [register](../sources.md#2026-spontaneous-world-knowledge); [canonical source](https://arxiv.org/abs/2604.18131). Retained unmodified: [2026-spontaneous-world-knowledge-paper-v1.pdf](../originals/2026-spontaneous-world-knowledge/2026-spontaneous-world-knowledge-paper-v1.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

**Canonical source:** [arXiv:2604.18131](https://arxiv.org/abs/2604.18131); [PDF v1](https://arxiv.org/pdf/2604.18131v1)

**Authors:** Qifan Zhang, Dongyang Ma, Tianqing Fang, Jia Li, Jing Tang, Nuo Chen, Haitao Mi, Yan Wang

**Version read:** v1, submitted April 20, 2026; latest version verified September 16, 2026

**Reading/access:** September 16, 2026; full primary PDF methods, experiments, tables, prompts, and input-processing appendix inspected. No code/data link was exposed on the arXiv page; experiments were not reproduced.

## Question and methods

The paper trains a web agent to explore a website before receiving a downstream question and to write a Markdown “World Knowledge” guidebook. At task time, that guidebook is loaded into context. The persistent learned change is a policy for planning, exploration, and summarization; adaptation to a particular website is stored as external text, not as a deployment-time weight update (§3).

The outcome reward for a guidebook is its improvement in downstream question accuracy relative to no guidebook. Training uses 600 labeled deep-search questions across 20 websites (§3.1). For SFT, Gemini-2.5-Pro generates three guidebook candidates per training environment; candidates are scored using Qwen3-30B-A3B on labeled questions, and the best full trajectory becomes imitation data (§3.2). Selected teacher trajectories average 374.8 steps and 3,322.4 observation/action tokens per step.

The authors then run two rounds of what they call Reinforcement-based Rejection Sampling: the trained policy generates `C` candidates, each is evaluated by the same downstream-utility reward, and the highest-scoring trajectories become further fine-tuning data (§3.3). `C`, the number of environments or trajectories retained per round, optimizer settings, epochs, and hardware are not reported. This is offline best-of-candidate fine-tuning, not online RL and not reward-free training. “Reward-free” refers only to inference on a new website.

At inference, the system first clusters a site's URLs by prefix and ranks pages by graph linkage; this preprocessing produces a structured entry file rather than exposing the raw homepage (§4.2; Appendix A). The agent may then spend up to 500 actions and 43,200 seconds (12 hours) generating the guidebook. Downstream answering is capped at 100 actions and 3,600 seconds (§4.1).

## Results and evidence

### Evaluation and findings

Evaluation uses subsets of WebWalker and WebVoyager totaling 1,427 questions. For WebWalker, the authors randomly choose ten websites from each of four domains: conference, game, organization, and education. WebVoyager uses Wolfram, Apple, Dictionary, and Coursera. Questions judged answerable from pretrained knowledge are removed (§4.1). The paper does not list the 20 training websites, all 40 selected WebWalker sites, item IDs, selection seed, or an explicit website-disjointness check between training and evaluation; consequently the “unseen environment” claim is not independently auditable from the paper.

WebWalker answers are judged by Qwen2.5-32B against ground truth. WebVoyager is judged by Gemini-2.5-Flash using the question, answer, and accessibility-tree trajectory (§4.1; Appendix C). No human agreement or evaluator-error analysis is reported.

Table 1 reports:

| Backbone | Condition | WebWalker average | WebVoyager average |
| --- | --- | ---: | ---: |
| Qwen3-30B-A3B | No world knowledge | 22.04% | 41.08% |
| Qwen3-30B-A3B | Gemini prompt-only guidebook | 29.85% | 55.92% |
| Qwen3-30B-A3B | Base-model prompt-only guidebook | 19.50% | 40.76% |
| Qwen3-30B-A3B | SFT policy | 38.17% | 51.50% |
| Qwen3-30B-A3B | RFT policy | 40.91% | 57.44% |
| Seed-OSS-36B | No world knowledge | 16.26% | 39.93% |
| Seed-OSS-36B | Gemini prompt-only guidebook | 31.33% | 56.82% |
| Seed-OSS-36B | Base-model prompt-only guidebook | 16.65% | 36.72% |
| Seed-OSS-36B | SFT policy | 28.57% | 56.00% |
| Seed-OSS-36B | RFT policy | 37.50% | 56.79% |

The absolute RFT-versus-no-guidebook differences are +18.87/+16.36 points for Qwen and +21.24/+16.86 points for Seed on WebWalker/WebVoyager. Calling this a generic “20% performance increase” hides benchmark and backbone variation and is ambiguous between percentage points and relative percent.

Table 2 reports that world knowledge reduces mean downstream execution steps from 24.28 to 20.05 for Qwen3-30B on the four WebWalker domains, about 17%. It does not count the much larger up-front guidebook-generation process, so this is task-execution efficiency after amortizing exploration, not end-to-end cost.

Figure 3 reports cross-model transfer of guidebooks, including selected Qwen3-14B versus unassisted Gemini-2.5-Flash domain comparisons. The figure does not establish equal total inference compute: the assisted model consumes a separately generated guidebook plus task-time inference. Figure 4 shows most gains arriving after SFT and the first rejection-sampling round, with marginal or fluctuating second-round results. Figure 5 shows guidebook-length gains plateauing and sometimes reversing at 32K–64K tokens.

## Appraisal and limitations

### Split, cost, and uncertainty audit

- **Environment split:** evaluation tasks are distinct benchmark subsets, but training/evaluation website identity is not disclosed sufficiently to verify environment-level separation. Removing questions answerable from pretrained knowledge is a model-dependent selection step with no reported blinded protocol.
- **Selection reuse:** training guidebooks and RFT trajectories are explicitly selected on labeled downstream task success. This is valid meta-training but means the method learns from external rewards and task labels; it is only inference-time reward-free.
- **Comparators:** no-guidebook, prompt-only base, and strong Gemini teacher guidebooks are useful controls. There is no random/retrieval summary baseline, equal-token browsing baseline, amortized-cost comparison, or test of guidebook persistence under website drift.
- **Uncertainty:** guidebook generation uses nonzero temperature, yet no seeds, independent generations, standard deviations, confidence intervals, or significance tests are reported. Task-answer decoding at temperature zero does not remove variation in the generated guidebook.
- **Compute/cost:** the paper reports action/time caps and average teacher-trajectory size but no training hardware, token totals, candidate count `C`, epochs, learning rate, wall time, dollar cost, or end-to-end inference cost. At the reported mean, one teacher trajectory contains roughly 1.25 million observation/action tokens before accounting for the three candidates and downstream reward evaluations.
- **Evaluator reliability:** both benchmarks rely on LLM judges, and no human validation or judge sensitivity analysis is reported. Gemini-2.5 appears both as SFT teacher and WebVoyager judge, though the evaluated policy outputs rather than its training trajectories are judged.
- **Editable state:** the website-specific artifact is contextual Markdown. It is regenerated for each environment and is not shown to accumulate across environments or tasks; this is proactive context construction, not continual memory or recursive improvement.

### Authors' claim

Outcome-reward training instills an intrinsic “meta-evolution” capability that autonomously adapts to unseen environments without rewards at inference, and the generated knowledge can outperform scale.

### Evidence-supported narrow claim

On the authors' selected WebWalker/WebVoyager subsets, policies trained to construct guidebooks obtain substantially higher judged task success than the same backbones without guidebooks, and the guidebooks can help other models. The controls also show that merely prompting the untrained base model to construct a guidebook can hurt.

### Interpretation

This is a useful learned exploration-and-compression method, but “self-evolution” overstates the persistent change at deployment: the output is a long context document, generated through a learned fixed policy, and the policy itself does not update from deployment experience. Missing environment-split disclosure, stochastic uncertainty, amortized resource accounting, and reproducibility details limit the strength of the result.

## Discussion and follow-up

### Shortlist decision

**reviewed reserve, below Agent-World**. It does not merit replacing a current top-ten family. The corpus already has stronger persistent-memory and task-stream evidence; use this as an adjacent example showing that proactive environment mapping can improve web agents and that poor self-generated context can degrade them.

### Useful visuals

Figure 2 for training-versus-inference separation and Table 1 for the strongest control comparison. Label the guidebook as external context and include its generation budget if shown.
