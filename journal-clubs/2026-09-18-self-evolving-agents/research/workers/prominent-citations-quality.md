# Prominent-citation quality audit

Audit date: 2026-09-16. This report records factual checks applied to the worker citation lanes. It is a quality record, not another source register or a field-wide citation ranking.

## Verification contract

For each selected edge, the audit requires: (1) a versioned seed artifact, preferably the retained PDF; (2) an `inspection_source` pointing to the artifact and extraction; (3) the cited identity resolved in the seed bibliography or an unambiguous first-party reference; (4) a locator in the seed body, not merely a bibliography entry; (5) a role supported by that local context; and (6) chronology compatible with the inspected seed version. The edge context reports the citing authors' characterization. It does not verify the cited work's findings.

The reproducible local workflow was:

```text
sources.json + originals/manifest.json
  -> resolve seed key, version, first date, and retained artifact
  -> pdftotext -layout on the retained PDF
  -> if absent, download the already-registered versioned arXiv PDF to /tmp
  -> inspect introduction, related work, method/baseline, limitations, and bibliography
  -> exact-title/author search in extracted text
  -> compare cited first date with the inspected seed version
  -> retain only context-supported edges and label cited-work access separately
```

Temporary meta-lane verification artifacts are under `/tmp/meta-citation-audit.7mmz3G/`. They include the versioned PDFs and `pdftotext` outputs for STOP v3, AFlow v4, Dream-RSI v1, MLEvolve v1, Escher-Loop v2, SICA v2, and Gödel Machines v5. Retained-source paths and temporary acquisition URLs are recorded per seed in `prominent-citations-meta.json`.

## Meta lane result

`prominent-citations-meta.json` was rebuilt from primary text: **14 seeds and 44 selected edges**, all with inspection provenance. Seed and non-null cited keys validate against `sources.json`.

The superseded output contained citation directions that the seed text cannot support. The following edges were rejected after full-text search and bibliography inspection:

- STOP → Darwin Gödel Machine and STOP → Self-Adapting Language Models. Both cited works postdate STOP and neither appears in STOP v3.
- Automated Design of Agentic Systems → AFlow. AFlow postdates ADAS v1 and does not occur in inspected ADAS v2.
- AFlow → GEPA. GEPA postdates the inspected AFlow v4 and is absent.
- AlphaEvolve → Darwin Gödel Machine. DGM predates AlphaEvolve by weeks, but the AlphaEvolve v1 text does not cite it; chronological possibility is not evidence of an edge.
- MLEvolve → EvoX. EvoX does not occur in MLEvolve v1; AlphaEvolve, MLE-bench, MLAgentBench, and OpenEvolve are the supported prominent relationships.
- Economics of RSI → AlphaEvolve or DGM. The paper's actual predecessors are economic growth and innovation-network models, especially Davidson et al. (2026), Davidson (2023), and Aghion et al. (2017).

Dream-RSI → DGM required a narrower correction rather than deletion. DGM occurs in the bibliography and is cited in §1 and §6 as a generic agent-self-improvement/harness example. The old locator “§6.2, lines 216–220” and direct-predecessor role were false. The corrected edge is `foundation`, with §1/§6 locators. The historical row in `citation-mining-meta.md` now matches the primary text.

The meta lane also fixes the invalid seed key `2026-hyperagents` to the registered key `hyperagents`. Aggregation should reject any year-prefixed aliases for `harness-evolution-evaluation`, `evoharnessbench`, `wikiskill`, `library-drift`, and `metarsi`.

## Consequential additions and disposition

| Work | Verified relationship | Reconciliation with the essay |
|---|---|---|
| Gödel Machines | Formal foundation for DGM/HGM/Hyperagents. A rewrite executes only after proving that switching has higher expected utility than continuing proof search, relative to encoded axioms, utility, resources, and search. | **Supporting only.** Use for the proof-gated ideal versus empirical DGM contrast; never count it as empirical self-evolving-agent evidence. |
| A Self-Improving Coding Agent (SICA) | Direct DGM competitor. SICA keeps an archive but Algorithm 1 always expands the best-scoring archived agent; DGM explicitly explores across archived variants. | **Supporting only, but consequential to the mechanism explanation.** One sentence prevents “archive” from being treated as equivalent to archive exploration and preserves DGM's stepping-stone distinction. |
| FunSearch | Direct predecessor of AlphaEvolve and code-search foundation for ADAS. AlphaEvolve explicitly calls itself a substantial enhancement. | **Supporting only** if the AlphaEvolve paragraph already explains inherited LLM-guided program evolution; otherwise integrate one lineage clause. |
| OpenEvolve | First-party implementation and tested baseline for EvoX, Escher-Loop, MLEvolve, and Dream-RSI. | **Supporting only.** Mention where implementation lineage or a rerun baseline matters; it is not independent peer-reviewed evidence by itself. |
| MLE-bench | Main 75-task evaluation substrate for MLEvolve. | **Supporting only / evaluation infrastructure.** It establishes what was tested, not that MLEvolve self-improves. |
| MLAgentBench | Earlier benchmark/system in the ML-engineering-agent lineage. | **Supporting only.** Safe to omit when MLE-bench already anchors the evaluation discussion. |
| Davidson et al. (2026) | Direct theoretical predecessor for the innovation-network equations in *The Economics of RSI*. | **Integrate only if the economics mechanism remains in the essay.** It is the relevant foundation; AlphaEvolve and DGM are not cited predecessors there. |

The fuller SICA/Gödel reading record is in `sica-goedel-primary-audit.md`.

## Cross-lane structural checks

At the last check, memory had 12 seeds/47 edges and evaluation had 13 seeds/48 edges; both parsed as JSON, all seeds had `inspection_source`, and all seed keys matched `sources.json`. The learning file was temporarily absent while its screener was replacing the original output, so it was not certified by this audit. Aggregation should rerun these mechanical checks after all four files settle:

1. `jq empty` on every lane file.
2. Every seed has `source_key`, versioned `url`, `inspection_source`, `sections_checked`, and explicit access limits.
3. Every seed key and non-null `cited_key` exists verbatim in `sources.json`.
4. No cited first-publication date is later than the exact inspected seed version date. A later seed revision can add an edge, but its inspection source must identify that revision.
5. A citation found only in the bibliography is not promoted without a body locator and role.

The reward-hacking note represents **two distinct full primary papers**, not one paper with two names: *RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents* (`2026-reward-hacking-agents`) and *Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use* (`2026-reward-hacking-benchmark`). They share one combined reading note but must count as two distinct reviewed papers/families in any full-paper count.

## Access limits

This audit verified seed citation contexts and cited identities. It did not re-read every cited work. Findings from a cited work remain unverified unless a substantive session note or the SICA/Gödel audit records a primary reading. Temporary PDFs were used only for verification and were not added to the repository. Citation recurrence remains a discovery and coverage signal, not a quality score or independent confirmation.
