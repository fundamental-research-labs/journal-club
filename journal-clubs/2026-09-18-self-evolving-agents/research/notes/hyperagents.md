# Hyperagents

## Source and access

**Source key:** `hyperagents`.

**Originals and source links:** [register](../sources.md#hyperagents); [canonical source](https://arxiv.org/abs/2603.19461v1). Retained unmodified: [hyperagents-paper-v1.pdf](../originals/hyperagents/hyperagents-paper-v1.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

[Paper v1](https://arxiv.org/html/2603.19461v1). Jenny Zhang et al.; first submitted March 19, 2026; preprint. arXiv lists one version despite an August manuscript date in the initial session notes. Accessed September 16; §§3–5 read selectively. Family: DGM/Hyperagents; related systems are not independent replications.

## Question and methods

Can the process generating agent changes itself improve? Task and meta agents share editable code. Main experiments retain handcrafted parent selection (§3). Transfer experiments freeze the meta agent and measure improvement@50 (§5.2).

## Results and evidence

### Reported evidence

Five coding runs, 80 iterations, 50 training tasks: full Polyglot performance 0.084→0.267 (reported CI 0.231–0.280; includes training tasks). In math grading after 200 iterations, transferred versus fresh initialization scores 0.640 (CI 0.550–0.720) versus 0.610 (0.510–0.680); authors explicitly report p>0.05 (§5.3). §5 specifies medians over five runs, 95% bootstrap confidence intervals from 1,000 resamples, and Wilcoxon signed-rank tests. The code-level follow-up below confirms run-array resampling and one-sided tests.

### Statistical implementation audit — September 16

Coordinator inspected [`analysis/analysis_utils.py`](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/analysis/analysis_utils.py), commit `59a68f6` (April 14). `compute_bootstrap_ci` resamples the supplied run-score array 1,000 times with seed 42, computes each median, and takes percentile endpoints. The plotting audit identifies five-run arrays. These CIs quantify run variability, not task sampling or a hierarchical population. `save_significance_tests` uses **one-sided** paired Wilcoxon (`alternative='greater'`) for equal-length arrays and one-sided Mann–Whitney for unequal lengths. Thus p<.05 is possible with five nonzero favorable paired differences; the two-sided minimum-p objection does not apply. The script assumes pairing from equal length rather than proving seed alignment, and no multiplicity correction is present in that routine. The Figure 4 endpoint remains nonsignificant as stated by the authors.

The [detailed audit](../workers/statistics-audit.md) supplies implementation locators. No statistical or experimental rerun was performed. The stronger claim of indefinitely compounding improvement remains unsupported by these finite experiments.

## Appraisal and limitations

### Authors' claim

Meta-level strategies transfer and can accumulate across runs.

### Interpretation and limitations

More direct evidence about improving the improver than editing skills alone. Finite experiments do not establish unbounded acceleration. Initial zero scores in some domains reflect formatting failures; compare strong initialized controls. Complete resource normalization remains unaudited; the statistical implementation was inspected as documented below.

## Discussion and follow-up

Figures 3–4: transferred improvement process versus ordinary task warm-start.
