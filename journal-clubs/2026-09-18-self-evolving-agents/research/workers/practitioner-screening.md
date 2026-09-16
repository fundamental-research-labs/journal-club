# Practitioner screening: self-evolving agents

**Tier 2 run/cutoff:** September 16, 2026 (America/Los_Angeles). **Scope:**
every candidate in `practitioner-discovery.md`, plus the requested autoresearch,
Reef, and NVIDIA NemoClaw comparators and one additional evidence-bearing
first-party practitioner post. H/M/L/U mean high/medium/low/unknown. Scores judge
this journal club's topic and audience, not general project quality. Evidence
strength concerns support for the specific improvement claim; all company and
project performance claims below are owner-reported unless explicitly described
otherwise. No project was installed or executed.

## Priority and close comparators

### Shopify Sidekick continual-learning loop — shortlist candidate

- **Relevance: H** — production loop changes harness code, training trajectories,
  model weights, and learned prompt tokens from production failures.
- **Evidence: M** — the full first-party article specifies rubric calibration,
  replay/repair, SFT then GRPO, daily updates, and a 350-request/minute load test;
  it omits the task count, baseline model identity, holdout protocol, judge
  agreement, uncertainty, ablations, raw traces, and code. Quality and operational
  gains remain Shopify-reported.
- **Novelty: H** — unusually complete production account spanning discrete harness
  search, parameter updates, and serving optimization in one loop.
- **Teaching: H** — exposes editable state, fixed/learned evaluators, data selection,
  update cadence, deployment economics, and several places leakage or drift can enter.
- **Coverage: H** — fills the production weight-update and serving-economics gap that
  autoresearch and Reef only partly cover.
- **Primary read:** Cody Mazza-Anthony and Andrew McNamara, [“Sidekick's continual
  learning loop”](https://shopify.engineering/sidekicks-continual-learning-loop),
  published August 5, 2026; full article read September 16. Detailed notes:
  [2026-shopify-sidekick.md](../notes/2026-shopify-sidekick.md).
- **Acquisition:** canonical HTML only. Shopify's page supplies no reuse license;
  public access does not establish redistribution permission. No code, data, or raw
  logs were located.

### NVIDIA NemoClaw memory-driven Chief of Staff — shortlist candidate

- **Relevance: H** — retained structured memory, corrections, a preference policy,
  and ordered ingestion directly instantiate experience changing later behavior.
- **Evidence: M** — 186 deterministically graded questions, same base model, public
  synthetic corpus, answers, verdicts, and reports provide inspectable measurements.
  Evidence is weakened by one corpus/model, transformed pre-publication answers,
  no repetitions or intervals, and the missing self-model adapter and memory.
- **Novelty: M** — memory systems are common, but the evidence/judgment separation,
  correction ledger, deterministic grader, and explicit regressions are distinctive.
- **Teaching: H** — the +8.1-point aggregate coexists with worse abstention and
  single-hop results; it cleanly teaches averages, small slices, provenance, and cost.
- **Coverage: H** — strongest practitioner artifact in this pool for inspectable
  memory evaluation and regression evidence.
- **Pinned artifacts:** NVIDIA/nemoclaw-community commit
  [`718eb6d`](https://github.com/NVIDIA/nemoclaw-community/tree/718eb6d8e49bad20a27f36065a205a204e699589),
  September 16, 2026; inspected the recipe README, benchmark README, results README,
  and published result files, not executed. Detailed notes:
  [2026-nemoclaw-memory.md](../notes/2026-nemoclaw-memory.md).
- **Acquisition:** repository is Apache-2.0. The coordinator may retain a small
  pinned README/result artifact under that license; this worker retained no copy.

### Reef — shortlist candidate

- **Relevance: H** — connects inference receipts and delayed feedback to versioned
  harness or weight updates and deployment.
- **Evidence: M** — the Apache-2.0 repository now contains auditable recipe outputs.
  Its meta-harness result uses 30 tasks × 2 repeats: baseline 20/60, selected
  iteration 23/60, then a fresh same-task comparison of 22/60 versus 21/60. The
  authors correctly state this is not a held-out task evaluation; raw campaign
  histories remain internal.
- **Novelty: H** — focuses on attribution and release infrastructure around multiple
  learning recipes rather than presenting a single optimizer as the whole system.
- **Teaching: H** — natural comparison with autoresearch: both expose propose,
  evaluate, retain; Reef adds receipts, delayed feedback, candidate versioning, and
  a deployment boundary.
- **Coverage: H** — fills the serving-to-learning infrastructure layer.
- **Pinned artifacts:** Human-Agent-Society/reef commit
  [`401db36`](https://github.com/Human-Agent-Society/reef/tree/401db3670d34b1b5a77989234272e0bee4b90ce8),
  September 16, 2026; inspected README, Apache-2.0 LICENSE, and
  [`recipes/meta_harness/RESULTS.md`](https://github.com/Human-Agent-Society/reef/blob/401db3670d34b1b5a77989234272e0bee4b90ce8/recipes/meta_harness/RESULTS.md).
- **Acquisition:** Apache-2.0; no local copy retained by this worker.

### Karpathy autoresearch — reserve / essential comparator

- **Relevance: H** — canonical minimal loop edits one training file, evaluates a
  fixed metric under a fixed-duration run, and retains or rejects the edit.
- **Evidence: L** — the repository establishes the mechanism and experiment
  contract but provides no controlled population estimate of improvement and was
  not reproduced here.
- **Novelty: M** — influential, sharply bounded implementation; many later projects
  now copy the pattern.
- **Teaching: H** — clearest artifact for separating the improving trained model,
  editable training program, fixed evaluator, and non-improving agent policy.
- **Coverage: H** — supplies the baseline vocabulary needed to compare Sidekick,
  Reef, ArcFusion, and BetterForAll.
- **Pinned artifact:** karpathy/autoresearch commit
  [`228791f`](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117),
  March 26, 2026; README inspected. The README declares MIT, but the pinned tree has
  no standalone LICENSE file; retain only after the coordinator confirms the
  intended licensing basis.

### Prolific autoresearch human-in-the-loop experiment — shortlist candidate

- **Relevance: H** — directly tests an autoresearch loop's metric, reproducibility,
  search myopia, and the value of a human meta-level intervention.
- **Evidence: M** — first-party post reports 45 executed autonomous experiments,
  five trained/untrained conditions, 1,507 blind pairwise judgments from 305
  participants, Wilson 95% intervals, and downloadable annotations. It is one
  stochastic run on one 360M model/task/dataset/scaffold; the meta-prompt was not
  ablated.
- **Novelty: H** — rare practitioner counterevidence where the loop's transient
  metric peak failed to reproduce and a five-minute “take stock” prompt found a
  better search direction.
- **Teaching: H** — distinguishes metric optimization, human preference, capability,
  and agency. Autonomous recipes' ~52% wins over base had intervals overlapping
  chance; conversational recipes reached 66.4% [57.6, 74.2] and 59.7%
  [50.9, 67.9].
- **Coverage: H** — fills the requested accessible researcher-post/talk-like artifact
  with actual methods and evidence, while providing counterevidence to smooth
  compounding narratives.
- **Primary read:** Nora Petrova and Viviana Márquez / Prolific,
  [“When does autoresearch need a human?”](https://huggingface.co/blog/ProlificAI/autoresearch-hitl-experiment),
  May 21, 2026; full post read. The linked annotation dataset is public but its
  repository license was not verified in this pass. Canonical links only.

## Other discovery candidates

### ArcFusion self-improving document parser — reserve

- **Relevance: H** — deterministic harness drives versioned prompt updates on a
  production document parser.
- **Evidence: M** — full article provides intervention tables with 3–5 repeats,
  prompt versions, costs, and metric revisions. It explicitly says there is no
  formal holdout, ground truth changed during development, and the claimed 99.8%
  is a five-run average on an undisclosed set. No data, code, intervals, or
  independent replication is available.
- **Novelty: M** — useful applied case, though fixed-suite prompt optimization is a
  familiar mechanism.
- **Teaching: H** — unusually candid examples: changing the metric moved apparent
  accuracy 97.9%→94.3% with no prompt change; compression and checklists regressed;
  model aliases changed failures; the headline 86%→99.8% remains at overfit risk.
- **Coverage: M** — adds small-model prompt optimization and metric-design failure
  modes but overlaps autoresearch's loop structure.
- **Primary read:** Napat Dollapavijit / ArcFusion,
  [article](https://www.arcfusion.ai/blog/the-agent-that-learns), April 30, 2026;
  full article read. Footer says all rights reserved; no local copy or public code.

### BetterForAll self-improving-agents — reserve

- **Relevance: H** — implements deterministic, feedback, self-rewriting, and
  adversarial arena loops with stored results.
- **Evidence: L** — code, logs, checkpoints, tests, and claimed cross-validation are
  inspectable, but this independent project was not executed or audited end to end;
  some tasks use LLM judges and growing adversarial tests, complicating comparability.
- **Novelty: M** — the four-level progression and fixed-versus-evolving benchmark
  contrast are useful, but mechanisms derive from known approaches.
- **Teaching: H** — compact hands-on illustration of how changing the evaluator can
  reveal false confidence and how “self-improvement” changes meaning across levels.
- **Coverage: M** — adds an adversarial evolving-test perspective, with substantial
  overlap with harness/meta-agent papers.
- **Pinned artifact:** BetterForAll/self-improving-agents commit
  [`5f78237`](https://github.com/BetterForAll/self-improving-agents/tree/5f7823732d87c515ed7842d06bc3c2613ed0445b),
  April 9, 2026; README/tree inspected, no execution. MIT license; no local copy retained.

### Postsyntax Agent Improvement Loop — reserve

- **Relevance: M** — production failures become persistent regression cases across
  prompt, retrieval, tool sequence, and workflow state.
- **Evidence: L** — full essay specifies an operational design but presents examples
  and assertions, not a deployment sample, measured change, code, or evaluation.
- **Novelty: L** — regression-from-incidents is sound but inherited from established
  software practice.
- **Teaching: H** — a strong negative-control reminder: retaining changes without a
  growing regression suite can reintroduce yesterday's failures.
- **Coverage: M** — covers evaluation-corpus evolution rather than agent-state
  evolution; useful operational complement.
- **Primary read:** Rafay A., [essay](https://postsyntax.substack.com/p/the-agent-improvement-loop-turning),
  July 1, 2026; full public HTML read. No reuse license; canonical link only.

### Hyperstruck experience/failure series — watchlist

- **Relevance: H** — covers forgetting, provenance, deduplication, tool renaming,
  false success, and secret leakage in retained agent experience.
- **Evidence: U** — the index, dates, and summaries were inspected, but individual
  posts and any underlying measurements were not audited; even the index criticizes
  prominent claims for publishing no number.
- **Novelty: M** — unusually broad lifecycle and security failure taxonomy.
- **Teaching: M** — good prompts for discussion, but claims must remain leads until
  full posts and artifacts are read.
- **Coverage: H** — fills forgetting, provenance, privacy, and false-success gaps.
- **Primary access:** [blog index](https://hyperstruck.com/blog/), posts dated May 15
  through September 10, 2026. Footer says all rights reserved; canonical links only.

### ClosedLoop AI blog — watchlist

- **Relevance: M** — failure clustering and drift appear aligned with production
  feedback loops.
- **Evidence: U** — only the first-party index/marketing-level summaries were
  accessible; no measured artifact was verified.
- **Novelty: U** — unassessable without substantive posts.
- **Teaching: L** — insufficient inspected detail for a defensible slide or claim.
- **Coverage: L** — overlaps better-inspected Postsyntax and RememberLoop material.
- **Access:** [blog index](https://closedloopai.co/blog/), accessed September 16;
  publication dates and licensing basis not verified. No copy retained.

### RememberLoop REFLECT account — reserve

- **Relevance: M** — a scheduled second-look process inspects traces, errors, and
  background-job state and produces a durable human-readable note.
- **Evidence: L** — full essay includes a firsthand incident: over 100 “model not
  found” errors over three days and a reflection job itself failing for eight nights.
  These are author-reported anecdotes with no logs or controlled comparison.
- **Novelty: M** — reframes improvement as detecting silent degradation rather than
  increasing capability.
- **Teaching: H** — memorable counterexample to assuming fluent output means a
  healthy learning loop; also demonstrates that monitors need monitoring.
- **Coverage: M** — adds operational degradation detection absent from benchmark
  papers.
- **Primary read:** Sriram Natarajan,
  [essay](https://blog.rememberloop.com/p/how-to-build-continuously-improving),
  June 15, 2026; full post read. No reuse license; canonical link only.

### Zeltrex “The Living Agent” / GODEGEN — excluded

- **Relevance: H** — claims persistent identity, evolutionary parameters, memory,
  constrained code self-modification, multi-day autonomy, and distillation.
- **Evidence: L** — the 14-page first-party PDF is internally inconsistent: the
  abstract reports 80/100 and 11 leading dimensions; §4 reports 104/125 and 16;
  Table 2 shows 20 visible dimensions totaling 80. It reports 280+ tasks, 10+ days,
  24% merge rate, and 363/363 tests but no external benchmark, statistical support,
  task-level logs, or independently auditable corpus. It admits the distillation
  pipeline was not trained and evolutionary claims lack statistical significance.
- **Novelty: H** — broad combination of claimed update surfaces.
- **Teaching: M** — useful only as an evidence-audit exercise about self-scored
  capability matrices, shifting denominators, future components, and marketing claims.
- **Coverage: M** — touches long-running production evolution, but stronger sources
  cover each component with clearer evidence.
- **Primary read:** Vasyl Golubenko / TOV ZELTREX,
  [PDF](https://zeltrex.com/papers/the-living-agent-2026.pdf), March 2026; full-text
  relevant sections read. No license statement established; no local copy retained.

### Self-improving-agent survey and Awesome list — excluded as practitioner evidence

- **Relevance: H** — broad taxonomy and discovery map are directly on topic.
- **Evidence: M** — useful secondary synthesis, but not independent evidence for the
  practitioner systems it lists; primary claims must be followed to originals.
- **Novelty: L** — consolidates rather than contributes a practitioner mechanism.
- **Teaching: M** — useful vocabulary and citation expansion, less useful than a
  primary artifact for the session's evidence questions.
- **Coverage: L** — existing academic discovery lanes already cover its major families.
- **Pinned list artifact:** selfimproving-agent/Awesome-Self-Improving-Agents commit
  [`99ce397`](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents/tree/99ce3979185536c1efb57b5c6935244b56f1dfec),
  repository updated September 11, 2026; MIT license. Survey first submitted July 14,
  2026. No local copy retained.

## Comparative judgment

The strongest teaching set is **autoresearch → Reef → Sidekick**: a bounded local
experiment contract, infrastructure that attributes production feedback and versions
candidate artifacts, then a production account that also updates weights and serving
state. NemoClaw supplies the clearest inspectable memory comparison, while Prolific
supplies the strongest counterexample to treating local metric ascent as reliable or
autonomous research progress. ArcFusion is the best reserve because it candidly shows
how metric definitions, stochasticity, prompt length, checkpoint aliases, and missing
holdouts can dominate a self-improvement story.

No practitioner family here independently establishes durable compounding improvement
under changing future tasks. The strongest artifacts establish mechanisms and bounded
measurements. Shopify's claims lack public evaluation artifacts; Reef's fresh comparison
reuses the same task set; NemoClaw lacks the evaluated self-model implementation;
Prolific and ArcFusion each report a single case study; all performance claims remain
owner-reported unless independently corroborated later.
