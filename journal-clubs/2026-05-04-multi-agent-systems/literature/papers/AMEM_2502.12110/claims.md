# Claims

## Claim 1
**Claim:** A-Mem treats agent memory as a dynamically organized note network rather than a static store-and-retrieve database.

**Evidence:** The method constructs each interaction as a note with content, timestamp, generated keywords, generated tags, contextual description, embedding, and links; new notes trigger link generation and possible evolution of prior notes.

**Caveats/Scope:** The organization quality depends on the underlying LLM and text encoder, and the paper focuses on text-based interactions.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Figure 2; Sections 3.1-3.3

## Claim 2
**Claim:** Link generation and memory evolution both contribute to A-Mem's LoCoMo performance.

**Evidence:** In the GPT-4o-mini ablation, the system without both link generation and memory evolution performs worst, the version with link generation but without memory evolution is intermediate, and the full A-Mem model is best across all reported categories.

**Caveats/Scope:** The ablation is reported for GPT-4o-mini on the LoCoMo task categories, so it should not be assumed to generalize unchanged to every model or domain.

**Source pointers:** `paper.pdf`, Section 4.4; Table 3

## Claim 3
**Claim:** A-Mem improves long-term conversational QA performance across the tested LoCoMo model settings, especially where multi-hop or temporal memory is needed.

**Evidence:** Table 1 reports A-Mem with the strongest average F1/BLEU-1 ranking across six foundation-model settings, while Section 4.3 highlights gains for non-GPT models and strong multi-hop performance for GPT-based models.

**Caveats/Scope:** A-Mem does not win every individual category; full-history baselines remain strong in some open-domain or adversarial settings.

**Source pointers:** `paper.pdf`, Section 4.1; Section 4.3; Table 1

## Claim 4
**Claim:** Selective top-k memory retrieval can reduce prompt length compared with full-history baselines.

**Evidence:** Table 1 reports A-Mem using much shorter token lengths than LoCoMo and MemGPT, and Section 4.3 attributes this to selective top-k retrieval.

**Caveats/Scope:** Shorter prompt length is not the same as total system cost, because A-Mem also uses LLM calls during note construction, link generation, and memory evolution.

**Source pointers:** `paper.pdf`, Section 4.2; Section 4.3; Table 1

## Claim 5
**Claim:** A-Mem's retrieval layer scales similarly to vector-memory baselines in storage while keeping retrieval latency low in the paper's scaling experiment.

**Evidence:** Table 4 reports linear memory usage for A-Mem, MemoryBank, and ReadAgent across 1,000 to 1,000,000 memories, with A-Mem retrieval time remaining low as memory size grows.

**Caveats/Scope:** The scaling test concerns retrieval over stored memories and does not include the LLM cost of creating or evolving memories; the exact latency values are implementation- and hardware-dependent.

**Source pointers:** `paper.pdf`, Section 4.6; Table 4

## Claim 6
**Claim:** Increasing the number of retrieved memories helps only up to a point.

**Evidence:** The hyperparameter analysis varies k from 10 to 50 and reports that gains generally plateau or slightly decline at higher values, suggesting a tradeoff between richer context and extra noise or processing burden.

**Caveats/Scope:** This analysis uses GPT-4o-mini and the paper's LoCoMo category setup.

**Source pointers:** `paper.pdf`, Section 4.5; Figure 3
