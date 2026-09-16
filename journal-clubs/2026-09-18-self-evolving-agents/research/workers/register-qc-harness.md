# Harness register QC and final-shortlist challenge

Checked September 16, 2026 against `research/sources.json`, cached primary PDFs, arXiv API metadata, lane screening reports, and substantive notes. No shared register edits were made.

## Register corrections and consistency findings

### Definite metadata corrections

1. **`harnessdev` has the wrong title.** The register says **“HarnessDev: Benchmarking Autonomous Agent Harness Development.”** The arXiv API and v1 PDF title page give the exact title **“HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?”** The registered dates are otherwise correct for arXiv: first/latest **2026-09-01**, **v1**. The manuscript itself prints “Date: September 2, 2026”; retain September 1 as the arXiv publication date and record the manuscript date separately only if useful.
2. **`library-drift` has the wrong title.** The register says **“Library Drift: Accumulation and Lifecycle Management of Agent Skills.”** The arXiv API and v3 PDF title page give **“Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries.”** The dates/version are correct: first **2026-05-19**, latest **2026-07-29**, **v3**. The PDF reports acceptance to the ICML 2026 Workshop on Failure Modes in Agentic AI (FAGEN@ICML 2026); `type: preprint` is defensible but could be made more informative.
3. **`2026-darwinx` has resolvable version metadata.** It is currently `latest_version_date: unknown`, `version: unknown`. Primary arXiv metadata identifies **v1**, first/latest **2026-07-31**. Its provisional access status should remain unchanged.
4. **Final-shortlist dispositions are stale for two records.** The tentative final ten includes `harnessdev` and `hyperagents`, but both remain `reserve` in `sources.json`; the other eight tentative selections are `shortlist-candidate`. If disposition is intended to reflect the final coordinator shortlist, update these two during the final merge. If it records lane-local screening only, document that distinction because the mixed semantics will mislead downstream automation.

### Version provenance that is correct but could be made safer

- AHE, HGM, DGM, Evo-Harness, and AlphaEvolve have correct version/date fields after correction: AHE v4 (2026-05-18), HGM v3 (2025-10-29), DGM v3 (2026-03-12), Evo-Harness v2 (2026-08-30), AlphaEvolve v1 (2025-06-16).
- Their `pdf_url` values are sometimes unversioned even though `version` says the exact read version. Unversioned arXiv URLs currently resolve correctly but can change after a revision. Prefer versioned PDF URLs for evidence supporting notes: `...2604.25850v4`, `...2510.21614v3`, `...2505.22954v3`, `...2608.15071v2`, and `...2506.13131v1`.
- HarnessDev and Library Drift already use versioned abstract/PDF URLs. Their license strings were not independently re-derived in this QC; preserve only if the coordinator has an artifact-specific license check.

### Duplication and family normalization

- **No exact duplicate title or canonical URL exists** in the 126-entry register.
- Three similarly named families are distinct and should not be merged:
  - **Evo-Bench** (`2026-evo-bench`) selects tasks sensitive to harness quality and evaluates autonomous harness optimization with disjoint validation/evaluation sets.
  - **EvoHarnessBench** (`evoharnessbench`) tests agents as externally supplied tools, skills, and specialists grow across staged streams.
  - **Evo-Harness** (`2026-evo-harness`) compiles online execution contexts into persistent skill guidance.
  Add one-line `mechanism_family` values because title similarity invites accidental deduplication.
- **DGM, SICA, HGM, and Hyperagents are separate papers in one research lineage, not independent replications.** The register gives each its own `family`; only Hyperagents currently has `related_lineage`. Add the same related-lineage marker to all four, or normalize an evidence-family field, so synthesis does not count them as four independent confirmations.
- **Library Drift and the Ratchet repository/paper are one family.** The current register has only the paper record, so there is no duplicate now. Keep any later Ratchet code/project entry as a companion rather than a new candidate.
- AHE, HarnessDev, the harness-evaluation critique, DarwinX, and Evo-Bench share some benchmarks and conceptual surface but are independent author/project families. They should stay separate, with benchmark reuse treated as correlated evidence rather than deduplication.

## Independent challenge to the tentative final ten

Tentative list: WikiSkill; harness-evaluation critique; GEPA; SEAL; Hyperagents; AgentStream; R-Zero; HarnessDev; FinEvo-Bench; Shopify Sidekick.

### Judgment

**Keep the ten. Do not reverse the earlier Dream-RSI→R-Zero decision.** R-Zero adds the otherwise missing autonomous curriculum/weight-update branch and the most useful within-system collapse evidence; Hyperagents already carries the “improve the improver” role that Dream-RSI would duplicate.

No available substitution is unambiguously stronger across evidence and coverage:

- **HGM for HarnessDev** would improve explicit CPU-hour accounting and fitness-proxy teaching, but would make the set more dependent on the DGM/Hyperagents lineage and remove HarnessDev's independent six-creator, nine-lineage, 630-held-out-task view of harness construction and evolution.
- **ACE for GEPA** would improve online-playbook and latency/token coverage, but AgentStream already tests ACE under isolated/sequential/interleaved conditions. GEPA better anchors the prompt-evolution-versus-RL comparison.
- **EvoHarnessBench for AgentStream** would add changing-interface coverage, but AgentStream is broader across methods, models, and task order. Use EvoHarnessBench as a companion, not a replacement.
- **Library Drift for WikiSkill or AgentStream** would add an excellent retirement failure, but its one model and 40 selected evaluation tasks are narrower. Its harsh-retirement −0.019 result belongs in discussion/figures.
- **Reef for Shopify** would improve artifact inspectability and feedback-version attribution, but its efficacy result is a same-task 22/60 versus 21/60 comparison. Shopify uniquely covers a full production loop spanning harness, data, weights, deployment, and serving economics; keep its weak public efficacy evidence visible.
- **NemoClaw for Shopify** would give a more inspectable 186-question practitioner benchmark, but duplicates the selected memory/skill axis and loses the broader production-learning pipeline.

### Remaining conceptual gaps

The ten are balanced, but the final narrative should explicitly acknowledge four omissions rather than imply full coverage:

1. **Changing interfaces and externally expanding harnesses.** AgentStream changes task order/distribution, not the available tool/skill/agent catalog. Use EvoHarnessBench as a companion example.
2. **Lifecycle governance.** WikiSkill shows persistent knowledge and a regression; it does not deeply test retirement, routing drift, or stale-skill removal. Use Library Drift's retirement ablation.
3. **Evaluator integrity and specification gaming.** The harness critique tests budget and held-out transfer, but the ten contain no dedicated evaluator-tampering family. At minimum mention the DGM detection-marker removal example or the separately screened reward-hacking evidence when discussing fixed evaluators.
4. **Embodied evolution and macro/theoretical interpretation.** No selected family covers physical/embodied transfer or asks when narrow benchmark loops imply broad acceleration. SHAPER and the Economics of RSI are reserves for those roles; neither warrants displacing a core empirical family in a 45-minute topic-wide reading list.

The most useful companion packet is therefore **EvoHarnessBench + Library Drift + one evaluator-integrity example**, with HGM, Dream-RSI, ACE, Reef, NemoClaw, and Economics of RSI as role-specific reserves.
