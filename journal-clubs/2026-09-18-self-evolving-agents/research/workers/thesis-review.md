# Independent review of the expanded thesis

**Reviewed:** 2026-09-16. **Scope:** additions to
`analysis/thesis.md`, checked against `research/sources.json`, the substantive
reading notes, and the new thesis-coverage records. The original thirteen-source
core was not re-audited except where an added paragraph changed its interpretation.
No thesis or shared research file was edited.

## Corrections needed before treating the expansion as final

1. **Point Agentic Harness Engineering to the version that was actually read.**
   The citation in the “What the software does” paragraph links
   `2604.25850v1`, while the register and note say the latest and reviewed version
   is **v4 (2026-05-18)**. The reported Tables 2–3 numbers and the 0.4-point
   SWE-bench comparison come from the v4 audit. Change the thesis link to
   `https://arxiv.org/abs/2604.25850v4`. The token comparison should also retain
   the note's qualification that timeouts were excluded from mean tokens per
   trial; otherwise “uses fewer tokens” sounds like complete deployment-cost
   accounting.

2. **Do not summarize all three skill-transfer studies as uniformly
   “encouraging.”** EvoSkill reports one 128-item transfer sample with a single
   evaluation run; Trace2Skill includes a **−1.2-point same-model AIME cell**;
   SkillOpt's disjoint test results have no independent-run intervals and unequal
   optimization resources are unresolved. Replace the collective sentence with
   wording such as: “Each reports at least one positive held-out or cross-setting
   result, but the results are mixed: Trace2Skill also regresses in one AIME cell,
   and small selection sets, sparse repetition, and unmatched optimization
   budgets limit inference.” Put each citation immediately after its source-specific
   sentence so the negative Trace2Skill result is not hidden by the three-citation
   paragraph ending.

3. **Correct the Escher-Loop characterization.** The thesis says a static
   optimizer pool “nearly matches” the full loop on one task. On Circle Packing,
   the static pool actually has a slightly higher printed mean Best@10M
   (**0.988 vs 0.987**) and ties AUC to printed precision (**0.966 vs 0.966**).
   Say that it *matches the full loop on AUC and slightly exceeds its mean best
   score on one of the two ablation tasks*. This is a useful negative control, not
   merely a near miss.

4. **Narrow the Dream-RSI generalization.** “Dream-RSI reports better discovery
   results than a controller whose exploration policy stays fixed” suppresses its
   mixed task-level record. The within-model Lasso and kernel results are positive,
   but the three mathematics tasks include one small improvement, one regression,
   and one tie. Change this to “reports better quality/call tradeoffs on several
   tasks,” with the math regression and tie stated nearby. The existing replay-only
   guarantee caveat should remain.

5. **Keep three pending additions out of any completed-evidence count until their
   traceability is merged.** The essay has 58 link occurrences and **52 normalized
   unique primary URLs**; six sources are cited twice. That is a URL/use count, not
   52 independent confirmations. Companion URLs are not double-counted in the
   essay, but related lineages such as DGM/Hyperagents and shared benchmark/model
   ecosystems remain dependent evidence.

   - *Rethinking Continual Experience Internalization* is absent from the shared
     source register and shared notes at review time.
   - SkillsBench is still marked `watchlist`, `abstract and metadata only`, with
     acquisition pending in `sources.json`, despite the thesis making substantive
     §3–4 claims. An older full-reading note is explicitly marked superseded.
   - MemSkill is recorded as full-text screened but has no shared note; its new
     mechanism paragraph should remain provisional until the ongoing primary
     review is merged.

   These three are being screened separately; this review does not duplicate that
   work. After their results land, recount **reviewed evidence families used in the
   thesis**, separately from unique URLs and citation occurrences. Until then the
   defensible fully traceable count is below 52.

6. **Resolve two consequential omissions or state why they remain outside scope.**
   The expanded “Improving the search” section jumps from artifact search to 2026
   meta-optimization without the already screened 2024 workflow-search lineage.
   ADAS and AFlow have substantive local notes and show that code-defined workflow
   search can produce reusable fixed artifacts, some held-out transfer, and lower
   execution cost, while still failing the deployment-time accumulation test.
   They reinforce the thesis's static-design/extra-compute counterfactual and prevent
   the section from implying that this branch begins with AlphaEvolve or the 2026
   systems. One compact sentence citing either both or the stronger representative
   is enough.

   Anthropic's 2026 eval-engineering note is a second useful omission: repairing a
   brittle evaluation changed a reported agent score from 42% to 95% without a
   capability update. It would make the “score itself becomes the object of
   improvement” section concrete, but is less essential because RewardHackingAgents
   and RHB already support the trusted-measurement-boundary conclusion.

## Citation placement and comparability

- The essay remains readable as a standalone argument and preserves the important
  numeric caveats for WikiSkill, SEAL, FinEvo, HarnessDev, AgentStream, Hyperagents,
  and the economic calibration. No large structural rewrite is warranted.
- Several added paragraphs defer three or four source-specific citations to their
  last sentence. The highest-risk cases are the EvoSkill/Trace2Skill/SkillOpt
  paragraph, the AHE/Evo-Harness/SHAPER paragraph, and the
  EvoX/Escher-Loop/MLEvolve paragraph. Move each citation next to the sentence it
  supports; leave the final synthesis sentence uncited or cite all only when it is
  explicitly an analyst inference. This avoids making a source appear to support a
  neighboring source's design or limitation.
- Keep resource measures separate. Iterations (EvoX), task evaluations (HGM),
  equivalent tokens (Escher-Loop), calls (Dream-RSI), and runtime limits (MLEvolve)
  are not interchangeable budget controls. The thesis says this once, correctly;
  do not turn these studies into a ranked efficiency comparison downstream.
- Keep “the evidence for learning better ways to improve is ... still limited” as
  a scoped claim about **transferable improvement policies**. It is defensible after
  adding the recent positive systems because the reviewed tests remain finite,
  mostly fixed-task, and non-comparable. Avoid broadening it to scarcity of
  self-evolution studies generally; the expanded corpus plainly contains many.

## Net assessment

The expansion does not overturn the central thesis. It adds credible mechanisms,
mixed transfer evidence, and stronger counterexamples while preserving the core
claim that future-task value, retention, evaluator integrity, and lifetime cost are
the decisive tests. The version error, the two overly positive mixed-result
summaries, and the pending-source count are the necessary fixes. ADAS/AFlow are the
only reviewed omission likely to change the reader's historical and counterfactual
picture; the other uncovered areas (multi-agent topology search, wider embodied
systems, and long-horizon organizational deployment) remain acknowledged coverage
limits rather than evidence that would presently reverse the thesis.
