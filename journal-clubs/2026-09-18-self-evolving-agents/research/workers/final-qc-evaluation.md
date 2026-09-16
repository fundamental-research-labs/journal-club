# Final QC: evaluation claims in shortlist and landscape

**Reviewed:** 2026-09-16. Files reviewed read-only: `research/shortlist.md` and `research/landscape.md`, checked against the detailed notes and the previously inspected primary sources for AgentStream, FinEvo-Bench, HarnessDev, and *Rethinking the Evaluation of Harness Evolution for Agents*. No final document was edited.

## Required correction outside the final documents

- `research/workers/evaluation-screening.md`, FinEvo verification paragraph: corrected **“775 deliverables”** to **“775 input files”** and added that a complete run produces 120 task outputs. The candidate JSON did not contain the erroneous denominator. The detailed FinEvo note and both final documents already use the corrected interpretation.

## Findings for the final documents

### No blocking numerical or date errors found

- **FinEvo-Bench:** `shortlist.md` correctly states 120 tasks, 20 scenes, three shuffled streams, four scaffolds using the same Qwen3.7-Max backbone, state reset before each control task, score gains of 9.33–19.37 points, and exclusion of judge tokens. Its explicit statement that 775 denotes input files is correct. `landscape.md` correctly describes the paired stateful/reset control and the one-expert/120-output judge calibration. The main effects still lack across-run intervals or paired tests, and both files say so or avoid inferential wording.
- **AgentStream:** the +1.37/+0.75/+0.90 point means and the 28-positive/17-negative interleaved counts match the reconstructed Tables 11–13 audit. The 45 cells reuse the same 300 tasks across three order seeds and are not independent datasets; both files preserve that boundary. The $0.297→$1.893 cost claim is correctly isolated as a single Table 7 evaluation and is not fused with the three-seed +4.6-point aggregate.
- **HarnessDev:** 189 feedback tasks = 100 SWE-Pro + 89 Terminal-Bench; the held-out evaluation contains 630 SWE-Pro tasks. The 34/64 quantity is directional agreement over adjacent version switches, not 34 successful transfers. Five of five self-runtime lineages and one of four fixed-runtime lineages improve at the declared version, with one trajectory per lineage. The shortlist and landscape state these distinctions correctly.
- **Harness-evolution critique:** 72.3 versus 67.4 is the paper's reported average for parallel sampling versus evolution; 68.3 versus 67.7 is evolved versus initial harness on the 34-task held-out test after a 45/10/34 split. The shortlist correctly notes two runs, the small held-out set, and that five-rollout matching is not full token, latency, or dollar parity. It does not claim statistical significance.
- **Dates/versions:** AgentStream v1 2026-07-31; FinEvo-Bench v1 2026-08-06; HarnessDev v1 2026-09-01; harness critique first submitted 2026-07-14 and v2 2026-08-27. These are internally consistent in the final documents.
- **Links:** all relative Markdown targets in `shortlist.md` and `landscape.md` resolve locally. The reviewed arXiv/DOI targets are syntactically consistent with the source notes; no bad link was found.

## Optional wording refinements

These are precision improvements rather than factual corrections.

1. **`shortlist.md`, AgentStream row:** “Mean paired gains” could be read as a task-level paired statistical estimate. More exact wording would be: **“Mean differences from each model's vanilla macro average are +1.37/+0.75/+0.90 points for isolated/sequential/interleaved streams.”** The tasks are shared, but no paired-test uncertainty is reported.
2. **`shortlist.md`, harness-critique row:** after “reported averages favor sampling over evolution,” optionally add **“without confidence intervals or a demonstrated significance test in the reported table.”** The boundary column already communicates the two-run/small-test limitation, so this is not required.
3. **`landscape.md`, FinEvo feedback paragraph:** “That provides a useful control” refers to expert calibration of the judge, not an independent evaluator. If maximum explicitness is desired, replace it with **“That calibrates score agreement on one run without testing whether learning transfers to a separately designed evaluator.”** The next clause already conveys this meaning.

## QC conclusion

The final shortlist and landscape preserve the important denominators, distinguish descriptive variation from statistical uncertainty, and avoid inflated causal claims for the four focal sources. The only material denominator error found was confined to the worker screening report and has been corrected there.
