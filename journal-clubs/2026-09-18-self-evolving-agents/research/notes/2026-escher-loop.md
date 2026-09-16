# Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization

## Source and access

**Source key:** `2026-escher-loop`.

**Originals and source links:** [register](../sources.md#2026-escher-loop); [canonical source](https://arxiv.org/abs/2604.23472). retention-restricted. [Manifest](../originals/manifest.json).

**Canonical source:** [arXiv:2604.23472](https://arxiv.org/abs/2604.23472); [PDF v2](https://arxiv.org/pdf/2604.23472v2); [code](https://github.com/scaling-group/escher-loop)

**Authors:** Ziyang Liu, Xinyan Guo, Xuchen Wei, Han Hao, Liu Yang

**Version read:** v2, May 27, 2026 (v1 April 25)

**Reading/access:** September 16, 2026; full primary PDF including methods, results, ablations, and Appendix A. Code linked but not audited; experiments not reproduced.

**Original-copy status:** temporary PDF inspected and validated; not retained. ArXiv records its non-exclusive distribution license, which is not a general redistribution license.

## Question and methods

### Question and mechanism

Escher-Loop asks whether the optimizer used in LLM program evolution can itself become an object of evolution. It maintains a Task Agent population of executable solution programs and an Optimizer Agent population. In this implementation, an optimizer is a program that constructs prompts for a fixed Gemini 3 Flash model (§§2.1–2.2). An optimizer transforms scored task programs into a new candidate; a lead optimizer can likewise rewrite sampled optimizer programs (Algorithm 1).

New task programs receive an absolute task score. Optimizers sampled on the same task context receive pairwise win/loss outcomes from those scores, which update an Elo rating. The same evaluations therefore drive task search and optimizer selection without a separate optimizer benchmark (§2.3). The state being improved is task code and optimizer prompting logic; the LLM weights do not change.

### Evaluation design

The paper evaluates three fixed AlphaEvolve-style mathematical optimization instances: Kissing Number in dimension 11, Circle Packing for 26 circles, and Heilbronn Triangle for 11 points (§3; Appendix C). OpenEvolve is the static handcrafted optimizer baseline. Each method receives 10M equivalent tokens per task, where `T_eq = output tokens + 0.25 × input tokens`, based on relative API pricing (§3; Appendix A.1).

Requests use Gemini 3 Flash Preview: 80% low thinking and 20% default dynamic thinking; downstream generation temperature 0.7 and optimizer evolution temperature 1.0. Optimizer population size is capped at 50, Elo starts at 1200 with K=32, and the archive uses rank-based softmax sampling (Appendix A.2–A.4).

Figures 2–3 show multiple independent trajectories but do not tabulate main-comparison means, dispersions, or the exact run count in their captions/text. The mechanism ablations on Kissing Number and Circle Packing are explicitly repeated three times (Table 1).

## Results and evidence

Under the 10M-token budget, the paper reports that Escher-Loop reaches the highest observed best-so-far score in all three tasks (Fig. 2). A single best evolved optimizer often improves over OpenEvolve on Kissing Number and Circle Packing but underperforms it on Heilbronn Triangle and never reaches the full loop's peak (Fig. 3, §3.2). This is evidence that one selected prompt program does not fully explain the population system; it is not a held-out transfer test because the isolated trajectories use the same three task instances that generated the optimizer population.

Three-run ablations report:

| Task/method | Best@10M mean | AUC@10M mean | AUC SD |
| --- | ---: | ---: | ---: |
| Kissing Number, OpenEvolve baseline | 0.786 | 0.674 | 0.067 |
| Kissing Number, static 50-optimizer pool | 0.568 | 0.408 | 0.181 |
| Kissing Number, fixed Elo | 0.811 | 0.772 | 0.074 |
| Kissing Number, random Elo update | 0.739 | 0.721 | 0.016 |
| Kissing Number, Escher-Loop | 0.963 | 0.876 | 0.032 |
| Circle Packing, OpenEvolve baseline | 0.961 | 0.956 | 0.008 |
| Circle Packing, static 50-optimizer pool | **0.988** | **0.966** | 0.009 |
| Circle Packing, Escher-Loop | 0.987 | **0.966** | 0.009 |

Table 1 is important because it narrows the claim: Escher-Loop clearly dominates the tested ablations on Kissing Number, while on Circle Packing the static pool has a slightly higher mean peak and ties AUC to printed precision. The paper appropriately describes Circle Packing as close rather than a clean win (§3.3).

## Appraisal and limitations

### Controls, uncertainty, and limits

- **Compute control:** equivalent-token matching is better than raw iteration matching, but it normalizes by an assumed input/output price ratio. It does not match wall time, API latency, hidden provider compute, or dollar prices if routing conditions change.
- **Replications:** the ablations use n=3; AUC standard deviation is reported, but no confidence intervals or hypothesis tests. Best@10M variability is omitted even though best-of-search endpoints are selection-sensitive.
- **Task split:** there is no train/validation/test division or unseen task family. Each loop repeatedly optimizes the same fixed instance and evaluator. The paper states that cross-domain transfer remains future work (Conclusion).
- **Baseline breadth:** the principal baseline is OpenEvolve. The ablations are informative, but there is no comparison against additional contemporary agent/program optimizers, an equal-cost ensemble of independently designed prompts, or weight-training methods.
- **Dynamic benchmark:** Elo comparisons share sampled task contexts, reducing the paper's stated nonstationarity problem. Elo is also used for sampling, so evidence collection is adaptive: high-rated optimizers are sampled more and weak ones can be removed (Appendix B). Ratings are operational selection scores, not independently calibrated general optimizer ability.
- **Contamination:** formal benchmark/code familiarity in Gemini 3 Flash is not assessed. Fixed evaluators make objective measurement strong but can reward task-specific search heuristics.
- **Reproducibility:** code is linked and final task programs are printed. Provider model preview behavior, API routing, and full run artifacts were not independently checked in this lane.

### Authors' claim

Mutual evolution of task and optimizer populations raises performance ceilings because optimizers adapt their strategies as task programs improve.

### Evidence-supported narrow claim

On three fixed geometry optimization instances and a 10M-equivalent-token budget, the system's best observed trajectories exceed the static OpenEvolve trajectories; three-run ablations show a substantial advantage on Kissing Number, with mixed/near-tied evidence on Circle Packing.

### Interpretation

Escher-Loop is the strongest new empirical example in this batch of changing the improvement procedure itself. It demonstrates recursive rewriting at the artifact level, not recursive model-weight improvement or general optimizer growth. The right teaching contrast is “meta-optimization on fixed verifiable instances” versus “transferable improvement ability.”

## Discussion and follow-up

### Useful figures

Figure 1 for the two populations and feedback; Table 1 for the mechanism audit. Pair any Figure 2 peak-performance slide with the fixed-instance and best-of-search qualifications.
