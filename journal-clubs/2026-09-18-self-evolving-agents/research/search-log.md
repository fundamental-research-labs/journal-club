# Search log

> The opening sections preserve the earlier September 16 pass. The autonomous refinement and final audit below supersede their acquisition counts, review depths, and unresolved statistical questions.


**Preparation/access date:** September 16, 2026. Existing September 18 session reused; 45-minute format preserved. Research update only. Queries below are representative exact strings used, grouped by purpose; results are discovery leads until followed to primary sources.

| Pass | Queries / direct follow-up | Outcome |
| --- | --- | --- |
| Existing corpus | Session README, reading list, research notes, practitioner sources | Found partial readings and missing evaluation details; retained foundational map |
| Broad recent work | `self evolving agents September 2026 MetaRSI WikiSkill AgentStream`; `self improving agents harness evolution evaluation 2026`; `self evolving agents memory skills autoresearch researcher 2026 blog` | Revisited core papers; identified additional embodied and evaluation leads |
| September evaluation | `"HarnessDev" agent arxiv`; `"self-evolving" "September" "2026" agent benchmark` | Added HarnessDev and EvoHarnessBench; inspected primary methods/results |
| Practitioner and failure modes | `"self evolving" agent September 2026 blog github` | Found Reef, Ratchet/Library Drift, and Sepo; primary follow-up for first two |
| Social search | `"self improving" agent September 2026 site:x.com`; `site:x.com "Reef" "self-improvement"`; `site:x.com "Hyperagents"` | Limited useful original coverage; direct Karpathy announcement retrieval failed |
| Weight updates / latest releases | `self evolving agents weight updates continual learning September 2026`; `"ScienceBuddy" agent self evolving`; `"SoL-Pi" research` | Verified ScienceBuddy Sep 15 paper and source repository; inspected Reef announcement and SoL-Pi README |
| Evidence audit | arXiv abstract histories and versioned HTML for WikiSkill, AgentStream, harness critique, Hyperagents, MetaRSI, HarnessDev, EvoHarnessBench, Library Drift, ScienceBuddy | Extracted setup, split counts, effect sizes, uncertainty qualifications, and exact table/section locators |
| Artifact dates | GitHub latest-commit API for Reef, ScienceBuddy, SoL-Pi, autoresearch | Pinned hashes and commit dates in notes; commit dates not mislabeled publication dates |

## Access and selection decisions

- Followed secondary indexes to arXiv, author repositories, and first-party articles; secondary summaries are not evidence for findings.
- Primary HTML was read through the web tool and direct HTTP text extraction. Temporary retrieved text stayed outside the repository; only original notes and links are delivered.
- Reef's article failed in the web reader but direct HTTP retrieval succeeded. X announcement retrieval failed; no inaccessible post claims were adopted.
- Rechecked current versions: harness critique v2 August 27; MetaRSI v2 September 9; EvoHarnessBench v2 September 10; Library Drift v3 July 29. Hyperagents still lists March v1. ScienceBuddy is September 15 v1.
- Foundation coverage relies on the preserved initial reading list; GEPA's earlier full-text access limitation remains. This update does not silently promote inherited abstracts into reviewed evidence.
- Code and implementation guides were read as research, not installed or executed. Product screenshots and demo descriptions were not counted as benchmark replications.

## Numerical cautions found

- HarnessDev's 34/64 is directional agreement between feedback and held-out changes, not a count of proven generalizing improvements.
- The harness critique's displayed evolution average differs slightly from recomputing its rounded component cells; preserve the reported value and precision caveat.
- Library Drift's rolling gain is not late-window performance minus the round-zero baseline.
- AgentStream's 45-observation scenario aggregates need a clearer seed-denominator interpretation before use; direct Table 1 comparisons are safer.
- ScienceBuddy's three-cycle description conflicts with its two-cycle heading. Its 895-task inventory and 288 adaptation conversations are not established evaluation denominators.

## Stopping rule and gaps

Broad discovery identified the main update surfaces and new September work; follow-up shifted to inspecting experimental claims rather than expanding an unbounded reading list. The final targeted checks materially clarified version dates, metrics, and source limitations. This is sufficient for a qualified research-stage handoff, not saturation of all literature. No exhaustive-recall claim is made. Remaining specialized domains, social threads, talks, replication, and quantitative appendix checks are recorded in the source register and workflow queue.


## Autonomous refinement run — September 16, 2026, 19:34 UTC

User authorized approximately one hour of autonomous research. Existing twelve substantive notes, source register, landscape, reading list, practitioner register, and workflow were inspected before searching. Preserve the 45-minute session assumption and existing descriptive keys. Scope: strengthen and rank the existing corpus; widen neglected mechanisms and competing evidence rather than repeat completed discovery.

Budget: five bounded parallel discovery lanes (memory/skills/context; weights/self-play; harness/workflow; practitioner artifacts; evaluation/counterevidence), each roughly 12–18 queries plus citation expansion and a two-expansion no-new-evidence stopping rule. Discovery uses gpt-5.6-luna at low reasoning per skill; screening will use gpt-5.6-sol at medium reasoning; coordinator verifies final selections. This is an update, so fewer than the initial-discovery default of ten lanes; no numerical candidate quota.

Coordinator priorities: audit outstanding MetaRSI/ScienceBuddy/statistics questions, verify shortlist primary texts, acquire originals where licensing allows, create the missing ranked shortlist, and update the handoff. Existing human edits to root AGENTS.md are preserved. No slides or experimental reproduction planned. Research cutoff remains September 16, 2026; recent queries overlap existing coverage.

## Autonomous refinement: completed discovery and screening

This run supersedes the earlier snapshot's twelve-note count, GEPA full-text access limitation, and “no retained originals” statement. Existing keys and source families were preserved; new records extend the same corpus. No external messages, publication, or experiment execution occurred.

### Scope and delegation actually used

Five bounded discovery lanes used **gpt-5.6-luna, low reasoning**. Six screening lanes used **gpt-5.6-sol, medium reasoning**, including an additional frontier screen prompted by discoveries rather than a new broad search. The primary coordinator reconciled records, verified final selections, audited statistics/artifacts, and wrote the final selection and landscape. This follows the research skill's tiered delegation; workers did not recursively delegate.

| Lane | Discovery / follow-up | Screening and substantive reading |
| --- | --- | --- |
| Memory, skills, context | [Discovery](workers/memory-discovery.md); [survey-map audit](workers/survey-map-audit.md) | [Screening](workers/memory-screening.md): GEPA, ACE, MemRL, SelfMem, VISTA, Backfires, Ground Truth First; existing WikiSkill/AgentStream/Library Drift deepened |
| Weight adaptation and self-play | [Discovery](workers/weights-discovery.md); [2026 update](workers/weights-2026-update.md) | [Screening](workers/weights-screening.md): SEAL, Absolute Zero, R-Zero, TTRL; synthetic-data failure literature retained as background leads |
| Harness and improver code | [Discovery](workers/harness-discovery.md); [foundational additions](workers/foundational-rsi-additions.json) | [Screening](workers/harness-screening.md): DGM, HGM, AlphaEvolve, Agentic Harness Engineering, Evo-Harness; Reflexion/Voyager/STOP notes added |
| Evaluation and counterevidence | [Discovery](workers/evaluation-discovery.md); [statistical audit](workers/statistics-audit.md) | [Screening](workers/evaluation-screening.md): FinEvo, SEA-Eval, SHAPER, RHA/RHB; quantitative checks on existing harness/stream sources |
| Original practitioner work | [Discovery](workers/practitioner-discovery.md); [talks/social audit](workers/talks-social-audit.md) | [Screening](workers/practitioner-screening.md): Shopify/NemoClaw deep reading; Reef original measurement/artifact audit |
| Frontier gap follow-up | Targeted papers from the 2026 update, not a sixth broad discovery lane | [Frontier screen](workers/frontier-screening.md): SIA, Escher-Loop, Economics of RSI; coordinator Dream-RSI review; [Agent-World / world-knowledge follow-up](workers/frontier-gap-update.json) |

The linked discovery reports retain actual query strings, dates, source expansion, and access limits. Searches covered arXiv, conference/primary paper pages, author/lab sites, technical blogs, GitHub code/results, X/Twitter, and original talk/project leads. Search snippets and secondary summaries were used to locate originals, not to substantiate findings. No social post inaccessible in the reader was quoted or used as evidence.

### How the selection changed

The first shortlist sketch centered on recent harness/memory work and included Dream-RSI. A [cross-batch challenge](workers/shortlist-challenge.md) identified autonomous curricula as a missing branch. **R-Zero replaced Dream-RSI**, with Absolute Zero as a distinct companion study; Hyperagents already occupied the meta-improvement slot. This is grouping for reading economy, not conflating two experiments into one evidence family.

GEPA and SEAL were promoted after primary PDF review, replacing inherited abstract-only status. Shopify was selected for production-loop coverage, with **low public causal-efficacy evidence** explicitly recorded; NemoClaw and Reef are artifact-focused alternatives. The newest ScienceBuddy/MetaRSI claims remain reserves because the coordinator's release audit did not establish historical denominator/budget provenance. Further full reading of Agent-World and World Knowledge Exploration filled the environment/curriculum gap without displacing the final ten.

The final set is ten priorities, 34 reviewed reserves, 25 screened reserves, 53 watchlist records, three companion records, and seven exclusions: **132 records**, not 132 full-text reviews. There are **43 substantive note files**; some notes cover a closely related companion source. The structured register preserves rejected leads and relationships for future targeted updates.

### Coordinator primary-source verification

- Inspected current arXiv title/author/version/license metadata for 85 modern-ID records, plus STOP separately. One additional metadata request (the reliability-position lead) returned HTTP 406; it remains a watchlist item. Corrected seeded HarnessDev and Library Drift titles; retained first-submission versus revision distinctions, including Hyperagents' March v1 despite an August date in the manuscript.
- Read/verified the final ten's relevant primary methods/results and selected appendices; Shopify is a full first-party engineering article. Primary-source links and locators remain in notes. Rendered and visually inspected GEPA Table 1, SEAL ARC/setup, WikiSkill Table 1, the harness critique's held-out table, and R-Zero Appendix Table 6/7. Worker full-text readings supplement, rather than replace, coordinator checks of selected claims.
- **AgentStream:** reconstructed Tables 11–13 and Table 2 with a retained [standard-library script](check-agentstream-aggregates.py). Means 1.3667/0.7511/0.8978 pp and sample SDs of three seed means 0.8025/0.4834/0.3411 match printed precision. There are 45 shared-task cells/scenario; positive/negative/tie counts are 34/11/0, 28/16/1, 28/17/0. Main aggregate accuracy and single-run cost data are kept separate.
- **Hyperagents:** inspected pinned `analysis_utils.py`; bootstrap units are run-array entries, 1,000 resamples, median percentile endpoints. Tests are one-sided; equal-length arrays use paired Wilcoxon, unequal-length arrays Mann–Whitney. Pair alignment and multiplicity caveats remain. Figure 4's transferred math endpoint is nonsignificant.
- **EvoHarnessBench:** first-party project schema defines population SD over three runs, pooled task-count overall scores, and summed agent durations. Paper inventory, axis examples, and live-gallery counts are not assumed interchangeable.
- **ScienceBuddy:** retained MIT-licensed guides/config and inspected repository tree. Released 715/90/90 task-ID split has 20 Train–Val and 18 Train–Test overlapping material groups; maintained training schedule differs from the paper. No historical run ledger was located. Do not infer paper denominators from this recipe.
- **MetaRSI:** Appendix F supplies accounting conventions and 100 GPQA IDs, but the inspected official project/repository did not expose the actual per-variant realized-cost and sealed-split ledger needed to verify matching independently.
- **FinEvo:** corrected draft “775 deliverables” to **775 input files**, and verified same-backbone paired reset controls. The human-judge ICC calibrates one run; it does not measure adaptation uncertainty or independent-evaluator transfer.
- **R-Zero:** visually confirmed main-table/prose disagreements and the separately scoped Qwen3-4B collapse analysis. Retrospective GPT-4o/Gemini pseudo-label audits are not causal isolation of the failure mechanism.
- **GEPA:** preserved the printed 48.91 GRPO aggregate; displayed two-decimal cells average 48.9667, a discrepancy too large to be explained solely by rounding those cells. No invented correction. “Fewer rollouts” remains distinct from lower total compute.
- **Practitioners:** inspected retained Reef results/README and NemoClaw report JSON. Reef's 22/60 vs 21/60 comparison reuses search tasks. NemoClaw summaries imply 169/186 vs 154/186 correct, but reports mark one trial, transformed/regraded answers, cost-incomparability, a dirty benchmark revision, and different historical/published document counts. The evaluated self-model adapter/memory is absent.

### Acquisition and access

Retained **24 unmodified licensed PDFs and 12 small repository artifacts**, about 50 MB total. Canonical arXiv licenses provide the paper permission basis; MIT/Apache-2.0 repository licenses accompany code/docs. [Manifest](originals/manifest.json) and [originals guide](originals/README.md) record versions, URLs, restrictions, hashes, and failed/restricted copies. ArXiv non-exclusive papers were read temporarily and linked rather than retained without redistribution permission. Several endpoint failures were resolved using already-downloaded official bytes after exact version-stamp checks; no alternate source was silently substituted.

X/Twitter content and a SEAL video lead remained inaccessible or unauthenticated. No video was watched. A description listing paper authors is not proof of an author talk; that lead is excluded. Institutional/project pages are companions, not independent confirmations.

### Final quality checks and stopping rationale

Independent final checks are in [evaluation QC](workers/final-qc-evaluation.md), [weight/self-play QC](workers/final-qc-weights.md), and [register QC](workers/register-qc-harness.md). Corrections were propagated to the shortlist and landscape. All ten selections have primary-source notes and explicit limitations. The source register distinguishes reviewed evidence from metadata leads and preserves immutable source identifiers.

The final verification pass checks local authored links, source keys, shortlist membership, manifest sizes/hashes, and readability of all retained PDFs. Original partial README links are excluded from authored-link validation because they intentionally point to the full upstream repository. AgentStream arithmetic is rerunnable with `python3 research/check-agentstream-aggregates.py` from the session directory (Python standard library and network access only).

The two final targeted challenges—selection redundancy and environment/curriculum coverage—added useful qualifications but no reason to change the final ten. Remaining gaps require new empirical releases, independent replication, or a different session emphasis. Broad discovery therefore stopped within the authorized hour; unsupported claims were narrowed rather than extending the search indefinitely. No exhaustive-recall or experimental-reproduction claim is made.

**Final check outcome:** 511 authored relative file links resolved; 132 unique source keys and ten shortlist records checked; all 36 retained-original files matched recorded bytes/SHA-256; all 24 PDFs passed `pdfinfo`; no unregistered original files found. `git diff --check` passed. The AgentStream audit again reproduced the reported rounded aggregates. Existing unrelated root `AGENTS.md` changes were left untouched.

## Requested format and commit follow-up — September 16, 2026

Standardized all 43 notes to a shared five-section layout, retaining the original substantive blocks and every existing Markdown link. Added source-specific discussion questions where missing. Verified the section sequence for every note, 511 authored relative links, and retained-original hashes/readability. Commit scope is the session directory; the pre-existing root `AGENTS.md` modification is excluded. No new discovery or ranking changes.
