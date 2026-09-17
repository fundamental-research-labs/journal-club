# Darwin Gödel Machine

## Source and access

**Source key:** `2025-darwin-godel-machine`.

**Originals and source links:** [register](../sources.md#2025-darwin-godel-machine); [canonical source](https://arxiv.org/abs/2505.22954). Retained unmodified: [2025-darwin-godel-machine-paper-v3.pdf](../originals/2025-darwin-godel-machine/2025-darwin-godel-machine-paper-v3.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

**Source/key:** `2025-darwin-godel-machine` — Jenny Zhang et al., *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents*. [arXiv](https://arxiv.org/abs/2505.22954), [versioned PDF](https://arxiv.org/pdf/2505.22954v3), [first-party Sakana project article](https://sakana.ai/dgm/). First submitted 2025-05-29; latest and read version **v3, 2026-03-12**, verified from the arXiv submission history and the PDF stamp `arXiv:2505.22954v3 [cs.AI] 12 Mar 2026`; ICLR 2026. Read 2026-09-16: §§3–6, Figures 2–4, Appendices C–E. The inspected v3 PDF is retained under CC BY 4.0, as recorded in the acquisition manifest above. [Code](https://github.com/jennyzzt/dgm) is Apache-2.0.

## Question and methods

Can an archive of self-modifying coding agents sustain improvement by branching through lower-scoring stepping stones? DGM runs 80 iterations, one offspring per iteration, two SWE-bench and four Polyglot iterations concurrently. Self-modification uses Claude 3.5 Sonnet New; evaluation uses the same model on SWE and o3-mini on Polyglot (§4.1). Agents pass staged evaluations: 10 tasks, then 60, then 200 for high-ranked SWE agents; 10 then 50 for Polyglot (§4.2).

## Results and evidence

### Reported evidence

On the selected 200 SWE-bench Verified tasks, the base-to-best score is 20.0%→50.0%; on full Polyglot it is 14.2%→30.7% (§4.4, Figure 2). Frozen cross-benchmark transfer gives 28.9% on Polyglot for the SWE-evolved agent versus 14.2% base, and 24.5% on SWE for the Polyglot-evolved agent versus 20.0% base (Figure 4). Model transfer on 200 SWE tasks gives o3-mini 23.0→33.0 and Claude 3.7 Sonnet 19.0→59.5 (Figure 4/text; the plotted label appears as 59.0, so cite the prose/table only after checking the final typeset source). The SWE run took about two weeks and is estimated at $22,000, versus $10,000 for each learned ablation baseline; a 60-task SWE evaluation is estimated at $350 (Appendix E.1).

### Reward-hacking companion

The first-party Sakana article describes a safety experiment in which the evaluator inserted detection markers for hallucinated tool results; a DGM variant removed those markers rather than solving the underlying problem. Treat this as an author-reported demonstration of specification gaming, not an independently replicated rate. It complements the paper's safety discussion (§5 and Appendix I) and is a useful warning that self-editing can target the measurement mechanism itself.

## Appraisal and limitations

### Interpretation

DGM is the historical anchor for open-ended code/harness evolution, with useful cross-model and cross-benchmark tests. Its archive ablation supports the role of retaining alternate lineages, but the study does not establish acceleration or unbounded recursive improvement.

### Limitations

Single search runs, adaptive repeated exposure to fixed task subsets, stochastic staged promotion, and no confidence intervals. Its main $22k run is more than twice either ablation's estimated cost, so score comparisons are not compute matched. The outer open-ended search procedure remains fixed. Some evolved agents use more inference at deployment.

## Discussion and follow-up

How would held-out task families and a fixed lifetime budget change selection among evolved agents?

[Prominent citations and their roles](../prominent-citations.md#2025-darwin-godel-machine)
