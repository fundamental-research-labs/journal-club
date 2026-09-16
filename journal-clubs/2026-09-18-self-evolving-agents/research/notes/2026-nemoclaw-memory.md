# NVIDIA NemoClaw memory-driven Chief of Staff

## Source and access

**Source key:** `2026-nemoclaw-memory`.

**Originals and source links:** [register](../sources.md#2026-nemoclaw-memory); [canonical source](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/). Retained unmodified: [2026-nemoclaw-memory-code-license-commit-718eb6d.txt](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-code-license-commit-718eb6d.txt); [2026-nemoclaw-memory-eval-readme-commit-718eb6d.md](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-eval-readme-commit-718eb6d.md); [2026-nemoclaw-memory-results-readme-commit-718eb6d.md](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-results-readme-commit-718eb6d.md); [2026-nemoclaw-memory-agentic-rag-report-commit-718eb6d.json](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-agentic-rag-report-commit-718eb6d.json); [2026-nemoclaw-memory-self-model-report-commit-718eb6d.json](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-self-model-report-commit-718eb6d.json). Repository-artifact license is recorded in the manifest; this does not license the paper or blog. [Manifest](../originals/manifest.json).

**Source/key:** `2026-nemoclaw-memory`. Xuan Wu, Alexia Huang, Yijie Lai, Joe Liu,
and Xiaowei Li / NVIDIA, [“Building a Memory-Driven Agent with NVIDIA
NemoClaw”](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/),
published September 4, 2026. Repository inspected at NVIDIA/nemoclaw-community
commit [`718eb6d`](https://github.com/NVIDIA/nemoclaw-community/tree/718eb6d8e49bad20a27f36065a205a204e699589),
authored September 16, 2026. Read September 16: article, recipe README, benchmark
README, reference-results README, and repository tree/result artifacts. No code was
executed. Repository license: Apache-2.0. Small unmodified evaluation and result
artifacts are retained locally under that license.
All measurements are NVIDIA-published and were not independently reproduced.

**Retained original artifacts (commit `718eb6d`, Apache-2.0):** - [Benchmark README](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-eval-readme-commit-718eb6d.md)
- [Reference-results README](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-results-readme-commit-718eb6d.md)
- [Agentic-RAG report](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-agentic-rag-report-commit-718eb6d.json)
- [Self-model report](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-self-model-report-commit-718eb6d.json)
- [Repository license](../originals/2026-nemoclaw-memory/2026-nemoclaw-memory-code-license-commit-718eb6d.txt)

Pinned raw URLs, byte counts, SHA-256 hashes, and license basis are recorded in
[`acquisition-practitioner.json`](../originals/acquisition-practitioner.json).

## Question and methods

### Question and design

Can a structured, inspectable memory layer outperform multi-round agentic retrieval
on questions requiring changed facts, temporal reasoning, disambiguation, and
multi-source synthesis? The Chief of Staff recipe separates:

- **Evidence:** source messages and documents.
- **Knowledge:** Markdown pages for people, projects, priorities, goals, concepts,
  and working patterns, with provenance, indexing, cross-references, and growth limits.
- **Judgment:** a SQLite ledger of obligations, rankings, corrections, and audit events.
- **Action:** governed execution through a separate policy/security boundary.

User corrections enter an append-only audit trail. Repeated corrections can update a
small readable preference policy that users may inspect, edit, or delete. Deterministic
code enforces tier size, overflow, and ranking order. This is retained-state learning,
not model-weight learning.

### Benchmark and comparators

The public `mnemo` Agent Memory Benchmark contains two fully synthetic corpora. Corpus
A has **425 documents**: 200 emails and 225 channel-days containing 559 messages from
April 16 through May 27, 2026. Corpus B has **173 documents**: 100 emails and 73
channel-days containing 383 messages from July 20 through September 24, 2027, in a
different domain and generated with a different model. Published comparison results
use **Corpus A only**.

Corpus A is ingested in two chronological halves so later documents supersede some
earlier claims. The **186 deterministically graded questions** comprise a 155-question
base set and 31 hard questions. Scoring has explicit normalization and no model judge;
the shipped questions always report zero deferred-to-judge cases.

The reference comparison uses NVIDIA Nemotron 3 Ultra for both systems:

- **Agentic RAG:** embeds documents and lets the model write queries over as many as
  three retrieval rounds. Its adapter ships publicly.
- **Self-model:** performs reasoning at ingest time and then answers from its produced
  memory. The published run reports 1,603 ingest calls and 182.8M ingest tokens, plus
  1,675 answering calls. Its adapter and resulting memory do **not** ship.

The benchmark README explicitly says the `ledger_rag` adapter does not score the
Chief of Staff recipe itself; it adds candidate selection and answer generation to a
ledger designed for triage and ranking. This prevents equating the product recipe,
benchmark adapter, and unpublished evaluated self-model.

## Results and evidence

### Reported results

| Slice | n | Agentic RAG | Self-model | Difference |
| --- | ---: | ---: | ---: | ---: |
| Overall accuracy | 186 | 82.8% | 90.9% | +8.1 pp |
| Hard questions | 31 | 67.7% | 87.1% | +19.4 pp |
| Changed facts / chain freshness | 5 | 60.0% | 100.0% | +40.0 pp |
| Point-in-time / as-of reasoning | 6 | 33.3% | 66.7% | +33.3 pp |
| Entity disambiguation | 15 | 66.7% | 86.7% | +20.0 pp |
| Multi-source synthesis | 73 | 87.7% | 94.5% | +6.8 pp |
| Abstention / faithful to corpus | 13 | 100.0% | 92.3% | −7.7 pp |
| Single-hop lookup | 30 | 86.7% | 83.3% | −3.3 pp |
| Citation coverage | 186 | 92.5% | 97.8% | +5.4 pp |

The repository publishes reports, scored answers, as-answered files, and per-question
verdicts for both runs. These are materially more inspectable than a blog-only table.
They do not include repeated runs, confidence intervals, the self-model adapter, or
the memory created during ingest. The two retained `report.json` files preserve the
model identifier, observed call counts, token accounting, benchmark fingerprints, and
the complete publication-transformation note supporting these qualifications.

### Coordinator artifact arithmetic and provenance check

The two retained reports were parsed directly. Their four-decimal overall accuracies uniquely imply **169/186 correct for the self-model and 154/186 for agentic RAG**, a net 15 questions (8.06 percentage points before rounding). This checks the published summaries; it does not rerun answers or independently validate grading. The summary reports alone do not identify paired wins/losses, so no paired significance test is inferred. Both reports mark `trial.of=1`, `accounting.comparable_on_cost=false`, and the benchmark revision as `dirty=true`. They record 425 ingested documents but a published fingerprint with 428 corpus documents; the current release and the historical run inventory should not be assumed identical. These details further support treating the renamed/regraded artifacts as a documented historical measurement, not a fresh reproduction on the published corpus.

## Appraisal and limitations

### Provenance and cost caveats

The stored answers predate publication-time renaming of 20 text identifiers and four
question IDs. The repository publishes the substitutions and both transformed and
as-answered files. Overall results against the published key rise from 80.1% to 82.8%
for agentic RAG and from 87.6% to 90.9% for the self-model after transformation. A
registrable domain was also replaced without publishing its original value. Transparent
documentation makes the transformation auditable, but a transformed result is weaker
than a fresh run on the released corpus.

Reported tokens are **169,852 ingest tokens and 14,509 tokens/question** for agentic
RAG versus **182,760,709 ingest tokens and 241,240 tokens/question** for the self-model.
The repository explicitly says these cannot support a cost ratio because forwarded-call
records do not prove both systems counted the same events; both mark cost comparability
false. The benchmark separates quality from cost and refuses to invent a missing model
price.

### Authors' claim

Structured memory plus separate evidence, judgment, corrections,
and governance improves enterprise-agent task performance and user control.

### Reported evidence

The public artifacts establish a deterministic 186-question
comparison on one synthetic corpus and one model, including per-question outputs and
two regressions. They establish measured outputs; they do not reveal enough of the
self-model implementation to reproduce or causally attribute the difference.

### Interpretation

This is the strongest practitioner memory-evaluation artifact in
the screened pool because its benchmark, comparator adapter, questions, answers,
verdicts, fingerprints, and caveats are inspectable. Evidence strength remains medium:
one unrepeated corpus/model comparison cannot establish robust generalization, the
largest category differences have n=5 or n=6, and the evaluated self-model itself is
not public. The aggregate gain should always be presented beside abstention and
single-hop regressions and the very large, noncomparable token counts.

### Strengths

- Fully synthetic public corpora avoid exposing private enterprise messages and permit
  question-level inspection.
- Deterministic grading avoids LLM-judge variability for the shipped questions.
- Chronological ingestion explicitly tests later facts superseding earlier ones.
- Same base model reduces one major comparator confound.
- Reports preserve fingerprints, answers, verdicts, evidence, and provenance notes.
- The authors prominently disclose missing implementation, transformed answers,
  single-corpus/model scope, and invalid cost comparison.
- Negative slices are published rather than hidden by the aggregate.

### Limitations and confounds

- Corpus A is synthetic and represents one software-platform domain; Corpus B was not
  used for the published comparison.
- One run per system, with no seed/repetition analysis or uncertainty intervals.
- The self-model adapter and memory do not ship, so the result cannot be reproduced as
  published or used to isolate which architecture feature caused the difference.
- The systems shift reasoning between ingest and answer time and appear to use radically
  different amounts of compute; quality comparison does not imply efficiency.
- Small slices make 40-point and 33.3-point differences unstable descriptions of a
  broader population.
- Publication-time substitutions mean the stored outputs were transformed before the
  headline table was computed.
- The article's offline walkthrough with invented entities and recorded turns is a demo,
  distinct from the benchmark comparison.
- A preference policy learned from repeated corrections is described functionally but
  not evaluated for false generalization, forgetting, or long-term stability.

## Discussion and follow-up

Use the evidence→knowledge→judgment→governed-action separation to explain memory state,
then make the audience audit the result table: overall gain, two regressions, tiny
temporal slices, missing self-model implementation, and incomparable cost. The decisive
follow-up is a fresh multi-seed run on both corpora, at least two models, with the full
self-model adapter/memory and matched accounting published.
