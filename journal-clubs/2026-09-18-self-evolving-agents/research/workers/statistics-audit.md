# Statistics audit: Hyperagents and EvoHarnessBench

**Run date:** 2026-09-16. Primary artifacts inspected read-only. Hyperagents repository was cloned from the paper’s cited URL and pinned to commit `59a68f672dfb92c74aeb7e61535d776fb36e172d` (repository HEAD at retrieval; commit timestamp 2026-04-14 in Git metadata). The paper text was inspected from `/tmp/self-evolving-audit/hyperagents.txt` and `hyperagents-pdf.txt`. EvoHarnessBench paper text was inspected from `/tmp/self-evolving-audit/evoharnessbench.txt`; its first-party project page was checked for result-table metadata.

## Hyperagents: what the paper says

The paper’s experimental-protocol paragraph (paper text line 133; PDF text pp. 4–5, around lines 401–405) says each method is run **five times**, reports medians with 95% bootstrap confidence intervals from **1,000 resamples**, and assesses significance with the Wilcoxon signed-rank test. The paragraph does not specify whether the bootstrap resamples runs, task-level scores, or another nested unit, nor does it state the Wilcoxon alternative, exact method, zero-difference handling, or multiplicity correction.

The paper’s results repeatedly describe “5 repeated runs” as the unit behind displayed intervals (e.g., paper text lines 152, 159, 163; PDF pp. 8–9). For the math accumulation experiment, the paper reports a DGM-H + transfer median 0.640 with CI 0.550–0.720 versus fresh initialization 0.610 with CI 0.510–0.680 and says the endpoint comparison is not statistically significant (paper text around lines 231–234; PDF p. 12). This is consistent with an underpowered five-run comparison; it is not evidence that the reported CI is a task-level interval unless code establishes that.

## Hyperagents: released analysis code

The cited repository is [`facebookresearch/Hyperagents`](https://github.com/facebookresearch/Hyperagents), pinned above. The relevant file is [`analysis/analysis_utils.py`](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/analysis/analysis_utils.py).

- `compute_bootstrap_ci` (repository lines 7–39) converts the input to an array, computes `np.median(data)`, then draws a `(1000, len(data))` index array using `np.random.RandomState(42)`. It computes the median of each resample and takes the 2.5th and 97.5th percentiles. Thus, when the input is the five method/run scores passed by the plotting code, the CI is a **run-level percentile bootstrap of five observations**, not a task-level or hierarchical bootstrap. The fixed seed is used for every call.
- `plot_testevals.py` lines 511–518 calls that function on `arr`; `plot_comparison.py` lines 120–152 similarly resamples the run-level values after interpolation onto a common x-grid. The code does not show a task bootstrap in these plotting utilities.
- `save_significance_tests` (repository lines 42–133) documents a one-sided hypothesis that the first method is greater than the second. In bootstrap/median mode, equal-length arrays are passed to `scipy.stats.wilcoxon(scores1, scores2, alternative='greater')`; unequal lengths use `scipy.stats.mannwhitneyu(..., alternative='greater')`. It explicitly labels the equal-length case as paired data. The code therefore resolves the paper’s ambiguity: the intended alternative is **greater**, and the released code uses SciPy’s default Wilcoxon method/options apart from `alternative='greater'` (no explicit `method`, continuity correction, or multiplicity correction is supplied).
- The code’s bootstrap count is unrelated to the Wilcoxon sample size: 1,000 is the number of resampled medians, while `n=5` remains the number of independent run-level observations used by the test. The code does not pool bootstrap replicates into the significance test.

## Interpreting the n=5 concern

There is no contradiction to accuse from the primary code. With five nonzero paired differences, the exact two-sided signed-rank test’s smallest attainable p-value is 0.0625; the one-sided `alternative='greater'` test can attain 0.03125 when all five differences have the favorable sign. The repository’s explicit one-sided call therefore explains how some reported `p < 0.05` claims can occur. This is a directional test and should be described as such; the paper’s generic phrase “Wilcoxon signed-rank test” omits that material detail.

The code also permits ties/zero differences through SciPy defaults and does not disclose in the paper whether any comparisons had fewer nonzero pairs. Exact p-values, asymptotic behavior, and zero handling are delegated to the installed SciPy version; the repository does not pin the statistical-library version in the inspected file. Claims should therefore retain the authors’ directional p-values only with the run pairing, one-sided alternative, and software-version caveat.

The CIs should not be read as independent evidence of generalization: a five-run percentile bootstrap can display a narrow interval when run scores repeat or are discrete, and it does not account for task sampling, adaptive checkpoint selection, or nested evaluations. In Hyperagents, “best generated agent” selection is based on validation score before held-out testing (paper text lines 148–163), so the test score is a run-level endpoint after an adaptive search process.

## EvoHarnessBench: uncertainty and repeats

The primary paper text reports a deterministic benchmark construction: **17** multi-stage streams, **802** unique tasks, and **1,510** axis-specific evaluation examples (paper text lines 82, 98, 164–165). It defines adaptation and held-out evaluation splits at each stage (paper text lines 164–165), which is a useful leakage control. Tables 2–7 show cells formatted as `x ± y`; the paper text extracted for this audit does not state near those tables whether `y` is a standard deviation, standard error, confidence interval, or the number of repeated runs.

The official first-party project page, [EvoHarnessBench](https://mas-orchestra.salesforceresearch.ai/evoharness/), clarifies the table convention: `±` is the **population standard deviation over repeated runs, not a standard error or confidence interval**, and published rows use **three runs**. It also states that Overall pools task counts rather than averaging EOG/ALE percentages. This makes the uncertainty display descriptive rather than inferential; with three repeats, no paper-level confidence interval or significance test should be inferred from the bars.

The paper’s main text does not expose the per-run values, random seeds, or a statistical comparison procedure in the inspected artifact. The project page says the SDK aggregates repeats and returns leaderboard JSON, but the public page was not a code checkout and no benchmark repository/statistics script was located in this bounded pass. Treat `x ± y` as three-run population SD unless the authors’ released SDK or supplementary artifact confirms otherwise. Task-level denominators are much larger (e.g., EOG 454 and ALE 63 in Table 2), but they are not independent repetitions of the full adaptive system and must not be substituted for run-level uncertainty.

## Practical handoff

1. Hyperagents’ reported `p < 0.05` results are technically possible because the released code uses a **one-sided paired Wilcoxon (`alternative='greater'`)** on five run-level scores; do not label this an inconsistency. The paper should ideally state this explicitly.
2. Hyperagents’ 95% intervals are fixed-seed, percentile bootstraps of the supplied run arrays (usually n=5), not task or hierarchical intervals. They quantify endpoint variation under the run sample only.
3. EvoHarnessBench reports three-run population SD (`±`), not CI/SE; its 802-task benchmark size does not imply 802 independent replications. Report the three-run limitation and avoid inferential language.
4. For either family, the strongest replication request is per-run/per-task score release, fixed seeds and API/model versions, paired task rows, and a preregistered primary comparison with multiplicity handling across the many methods, stages, axes, and transfer metrics.

## Access and gaps

Hyperagents code is publicly available under the repository’s license (license text not separately audited here); no local copy is retained in the journal-club session. EvoHarnessBench’s paper is an arXiv preprint (arXiv:2609.04280; [paper](https://arxiv.org/abs/2609.04280)); the project page is first-party and was read for the uncertainty convention. No EvoHarnessBench source checkout or independent rerun was found in this pass. No files other than this worker note were edited.
