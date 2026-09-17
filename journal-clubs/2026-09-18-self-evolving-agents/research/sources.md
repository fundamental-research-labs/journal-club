# Source register

**Research cutoff and access date: September 16, 2026.** The [ranked ten](shortlist.md) are the reading priorities; the [landscape](landscape.md) organizes the topic. This register preserves 154 candidate/resource records, including companions, excluded leads, and metadata-only watchlist items. It is not a claim that all records were fully read. There are 59 substantive note files, with exact reading depth recorded individually.

The structured [sources.json](sources.json) contains the same records with complete author lists, metadata histories where checked, screening provenance, rubric reasons, and acquisition records. Primary metadata was checked against current arXiv records for 85 modern-ID sources, plus STOP separately; one requested arXiv metadata response failed. Version **read** and latest **available** metadata are separate: a newly observed version is not silently treated as read.

The [thesis-driven coverage audit](thesis-coverage.md) maps the 60 reviewed evidence families and distinguishes the 36 directly cited in the essay. The ten reading priorities do not cap the evidence base. The [prominent-citation map](prominent-citations.md) exposes per-paper predecessors and baselines; unreviewed cited leads remain distinct from this evidence base.

## Status and scope

- **Shortlist (10):** selected for the topic-wide reading set, with primary substantive notes.
- **Reviewed reserve (50):** substantive reading, useful alternatives or challenge companions.
- **Screened reserve (20):** screened sufficiently to retain as a lead; depth varies and a standalone note may be absent.
- **Watchlist (61):** incomplete/abstract/metadata-level support; not evidence for an empirical claim.
- **Companion (3):** related project or institutional communication; not independent replication.
- **Excluded (10):** retained for traceability, including unverified or redundant leads.

Rubric order is relevance / evidence / novelty / teaching / coverage, with H/M/L/U as defined in the [shortlist](shortlist.md#selection-rubric). A venue, brand, recent date, or functioning demo does not by itself establish evidence strength. The rationale and narrow claim matter more than a letter.

## Acquisition

The [originals manifest](originals/manifest.json) records immutable source URLs, versions, licenses, dates, byte counts, and SHA-256 hashes. [Originals guide](originals/README.md) explains partial captures and restrictions. Saved files are unmodified downloads; derived extraction/rendering files remain outside the repository. A paper's license does not apply automatically to its code, and a repository's license does not license the corresponding paper.


## Selected ten

<a id="wikiskill"></a>

### 1. [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://arxiv.org/abs/2608.27454v1)

- **Key / type / family:** `wikiskill`; preprint; `wikiskill`. **Authors:** Tang, Liyan, Rashtchian, Cyrus, Ferng, Chun-Sung et al..
- **Dates / version:** first 2026-08-27; latest metadata 2026-08-27; read/inspected v1. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** shortlist; rubric H / M / H / H / H. Controlled persistent-knowledge positive result; regressions, retrieval bypass, and small validation sets qualify it. **Notes:** [reading record](notes/2026-wikiskill.md).
- **Originals:** [2026-wikiskill-paper-v1.pdf](originals/2026-wikiskill/2026-wikiskill-paper-v1.pdf). License/permission: CC BY 4.0. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="harness-evolution-evaluation"></a>

### 2. [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v2)

- **Key / type / family:** `harness-evolution-evaluation`; preprint; `harness-evolution-evaluation`. **Authors:** Wang, Yike, Zhu, Huaisheng, Hu, Zhengyu et al..
- **Dates / version:** first 2026-07-14; latest metadata 2026-08-27; read/inspected v2. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** shortlist; rubric H / M / H / H / H. Direct alternative-budget and held-out controls; narrow implementation and rollout-only budget matching. **Notes:** [reading record](notes/2026-harness-evolution-evaluation.md).
- **Originals:** [2026-harness-evolution-evaluation-paper-v2.pdf](originals/2026-harness-evolution-evaluation/2026-harness-evolution-evaluation-paper-v2.pdf). License/permission: CC BY 4.0. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2025-gepa"></a>

### 3. [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457)

- **Key / type / family:** `2025-gepa`; peer-reviewed conference paper; `2025-gepa`. **Authors:** Agrawal, Lakshya A, Tan, Shangyin, Soylu, Dilara et al..
- **Dates / version:** first 2025-07-25; latest metadata 2026-02-14; read/inspected v2. **Access:** 2026-09-16; full text.
- **Selection:** shortlist; rubric H / M / H / H / H. Strong split/budget evidence with a task regression; total compute and repeated-run uncertainty unresolved. **Notes:** [reading record](notes/2025-gepa.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2507.19457v2).

<a id="2025-self-adapting-language-models"></a>

### 4. [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943)

- **Key / type / family:** `2025-self-adapting-language-models`; peer-reviewed conference paper; `2025-self-adapting-language-models`. **Authors:** Zweiger, Adam, Pari, Jyothish, Guo, Han et al..
- **Dates / version:** first 2025-06-12; latest metadata 2025-09-18; read/inspected arXiv v2; NeurIPS 2025. **Access:** 2026-09-16; full paper and appendices.
- **Selection:** shortlist; rubric H / M / H / H / H. Direct learned self-edit policy with held-out tasks, strong mechanism detail, compute accounting, and an explicit forgetting probe; narrow curated tasks and limited final-score uncertainty bound the claim. **Notes:** [reading record](notes/2025-self-adapting-language-models.md).
- **Originals:** [2025-self-adapting-language-models-paper-v2.pdf](originals/2025-self-adapting-language-models/2025-self-adapting-language-models-paper-v2.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="hyperagents"></a>

### 5. [Hyperagents](https://arxiv.org/abs/2603.19461v1)

- **Key / type / family:** `hyperagents`; preprint; `hyperagents`. **Authors:** Zhang, Jenny, Zhao, Bingchen, Yang, Wannan et al..
- **Dates / version:** first 2026-03-19; latest metadata 2026-03-19; read/inspected v1. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** shortlist; rubric H / M / H / H / H. Improves task and meta agents; five-run bootstrap and one-sided tests audited; compounding endpoint nonsignificant. **Notes:** [reading record](notes/2026-hyperagents.md).
- **Originals:** [2026-hyperagents-paper-v1.pdf](originals/2026-hyperagents/2026-hyperagents-paper-v1.pdf). License/permission: CC BY 4.0. Retrieved September 16; exact artifact versions and hashes in manifest.
- **Relationship:** DGM/SICA/HGM/Hyperagents: related methods; distinct experiments, not independent replications.

<a id="agentstream"></a>

### 6. [AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?](https://arxiv.org/abs/2608.00155v1)

- **Key / type / family:** `agentstream`; preprint; `agentstream`. **Authors:** Yan, Dong, Liang, Jian, Hu, Dapeng et al..
- **Dates / version:** first 2026-07-31; latest metadata 2026-07-31; read/inspected v1. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** shortlist; rubric H / M / H / H / H. Cross-method stream evaluation; Table 2 reconstructed from per-seed tables; 45 cells are not independent datasets. **Notes:** [reading record](notes/2026-agentstream.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2608.00155v1).

<a id="2025-r-zero"></a>

### 7. [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004)

- **Key / type / family:** `2025-r-zero`; peer-reviewed conference paper; `2025-r-zero`. **Authors:** Huang, Chengsong, Yu, Wenhao, Wang, Xiaoyang et al..
- **Dates / version:** first 2025-08-07; latest metadata 2026-02-13; read/inspected arXiv v4; ICLR 2026. **Access:** 2026-09-16; full paper and appendices.
- **Selection:** shortlist; rubric H / M / H / H / H. Role-separated co-evolution, matched ablations, pseudo-label audits, and eventual collapse are highly informative; metric inconsistencies and missing compute/repeats lower evidence confidence. **Notes:** [reading record](notes/2025-r-zero.md).
- **Originals:** [2025-r-zero-paper-v4.pdf](originals/2025-r-zero/2025-r-zero-paper-v4.pdf). License/permission: http://creativecommons.org/licenses/by-nc-nd/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.
- **Relationship:** Self-generated curricula: distinct studies; R-Zero core with Absolute Zero companion, not duplicate evidence.

<a id="harnessdev"></a>

### 8. [HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?](https://arxiv.org/abs/2609.01437v1)

- **Key / type / family:** `harnessdev`; preprint; `harnessdev`. **Authors:** Wu, Yuhao, Zhang, Jingyuan, Shi, Jiajun et al..
- **Dates / version:** first 2026-09-01; latest metadata 2026-09-01; read/inspected v1. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** shortlist; rubric H / M / H / H / H. Distinguishes visible feedback, declared versions, and held-out tests; one trajectory per lineage. **Notes:** [reading record](notes/2026-harnessdev.md).
- **Originals:** [2026-harnessdev-paper-v1.pdf](originals/2026-harnessdev/2026-harnessdev-paper-v1.pdf). License/permission: https://creativecommons.org/licenses/by-nc-nd/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-finevo-bench"></a>

### 9. [FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows](https://arxiv.org/abs/2608.06144v1)

- **Key / type / family:** `2026-finevo-bench`; arXiv preprint; `2026-finevo-bench`. **Authors:** Deng, Bo, Zhou, Kang, Guo, Lifan et al..
- **Dates / version:** first 2026-08-06; latest metadata 2026-08-06; read/inspected v1. **Access:** 2026-09-16; full primary methods/results and task/rubric appendices read.
- **Selection:** shortlist; rubric H / M / H / H / H. Best paired persistent-state versus reset design in the lane, with professional-process and compliance outcomes; main-run uncertainty is not reported. **Notes:** [reading record](notes/2026-finevo-bench.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2608.06144v1).

<a id="2026-shopify-sidekick"></a>

### 10. [Sidekick's continual learning loop](https://shopify.engineering/sidekicks-continual-learning-loop)

- **Key / type / family:** `2026-shopify-sidekick`; first-party engineering article; `2026-shopify-sidekick`. **Authors:** Cody Mazza-Anthony; Andrew McNamara; Shopify Engineering.
- **Dates / version:** first 2026-08-05; latest metadata 2026-08-05; read/inspected published HTML. **Access:** 2026-09-16; full article read.
- **Selection:** shortlist; rubric H / L / H / H / H. Most complete production account of harness, data, weight, and serving updates, but no public evaluation artifacts or ablations. **Notes:** [reading record](notes/2026-shopify-sidekick.md).
- **Original:** not retained: public original inspected; no redistribution license verified for page, or only metadata/theoretical background reviewed. License/permission: No reuse license found; canonical link only. Canonical page above is the inspected location.

## Reviewed alternatives and challenges

<a id="2025-absolute-zero"></a>

### [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)

- **Key / type / family:** `2025-absolute-zero`; preprint; `2025-absolute-zero`. **Authors:** Zhao, Andrew, Wu, Yiran, Yue, Yang et al..
- **Dates / version:** first 2025-05-06; latest metadata 2025-10-16; read/inspected arXiv v3. **Access:** 2026-09-16; full paper and appendices.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Consequential autonomous curriculum demonstration; no run uncertainty, incomplete GPU-hours, unmatched baselines, and nonzero pretrained/seeding/verifier inputs qualify the zero-data framing. **Notes:** [reading record](notes/2025-absolute-zero.md).
- **Originals:** [2025-absolute-zero-paper-v3.pdf](originals/2025-absolute-zero/2025-absolute-zero-paper-v3.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.
- **Relationship:** Self-generated curricula: distinct studies; R-Zero core with Absolute Zero companion, not duplicate evidence.

<a id="2026-agent-world"></a>

### [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292)

- **Key / type / family:** `2026-agent-world`; preprint; work in progress; empirical training arena; `2026-agent-world`. **Authors:** Dong, Guanting, Lu, Junting, Huang, Junjie et al..
- **Dates / version:** first 2026-04-20; latest metadata 2026-04-20; read/inspected v1. **Access:** 2026-09-16; Full primary PDF methods, experiments, tables, and appendices; no experiment reproduction or identified code/data release..
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Do not displace a stronger top-ten evidence family. Use as first reserve for the missing autonomous environment/curriculum mechanism; include only if replacing the weakest redundant framing source for coverage balance. **Notes:** [reading record](notes/2026-agent-world.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2604.18292v1).

<a id="2025-agentic-context-engineering"></a>

### [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618)

- **Key / type / family:** `2025-agentic-context-engineering`; peer-reviewed conference paper; `2025-agentic-context-engineering`. **Authors:** Zhang, Qizheng, Hu, Changran, Upasani, Shubhangi et al..
- **Dates / version:** first 2025-10-06; latest metadata 2026-03-29; read/inspected v3. **Access:** 2026-09-16; full text.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Central context mechanism with cost detail; qualify using AgentStream and VISTA. **Notes:** [reading record](notes/2025-agentic-context-engineering.md).
- **Originals:** [2025-agentic-context-engineering-paper-v3.pdf](originals/2025-agentic-context-engineering/2025-agentic-context-engineering-paper-v3.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-agentic-harness-engineering"></a>

### [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850)

- **Key / type / family:** `2026-agentic-harness-engineering`; preprint; `2026-agentic-harness-engineering`. **Authors:** Lin, Jiahang, Liu, Shichun, Pan, Chengjun et al..
- **Dates / version:** first 2026-04-28; latest metadata 2026-05-18; read/inspected v4 (read and latest). **Access:** 2026-09-16; primary full text: methods, Tables 1-3, Figures 3-4, limitations.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Closest direct HarnessDev competitor with full-component edits, held-out benchmark, five-model transfer, and token accounting. **Notes:** [reading record](notes/2026-agentic-harness-engineering.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2604.25850).

<a id="2025-alphaevolve"></a>

### [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)

- **Key / type / family:** `2025-alphaevolve`; DeepMind white paper/preprint; `2025-alphaevolve`. **Authors:** Novikov, Alexander, Vũ, Ngân, Eisenberger, Marvin et al..
- **Dates / version:** first 2025-06-16; latest metadata 2025-06-16; read/inspected v1 (read and latest). **Access:** 2026-09-16; primary full text: architecture, results, ablations, limitations.
- **Selection:** reviewed-reserve; rubric M / M / H / H / H. Strong adjacent evidence for evaluator-driven code evolution; not self-modification of an agent harness and budgets are opaque. **Notes:** [reading record](notes/2025-alphaevolve.md).
- **Originals:** [2025-alphaevolve-paper-v1.pdf](originals/2025-alphaevolve/2025-alphaevolve-paper-v1.pdf). License/permission: http://creativecommons.org/licenses/by-nc-nd/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-nemoclaw-memory"></a>

### [Building a Memory-Driven Agent with NVIDIA NemoClaw](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/)

- **Key / type / family:** `2026-nemoclaw-memory`; first-party technical article, recipe, benchmark, and result artifacts; `2026-nemoclaw-memory`. **Authors:** Xuan Wu; Alexia Huang; Yijie Lai; Joe Liu; Xiaowei Li; NVIDIA.
- **Dates / version:** first 2026-09-04; latest metadata 2026-09-16; read/inspected repository commit 718eb6d8e49bad20a27f36065a205a204e699589. **Access:** 2026-09-16; full article and relevant pinned repository READMEs/results inspected; not executed.
- **Selection:** reviewed-reserve; rubric H / M / M / H / H. Best inspectable practitioner memory evaluation in pool, though evaluated self-model implementation is missing and results are one corpus/model/run. **Notes:** [reading record](notes/2026-nemoclaw-memory.md).
- **Originals:** [2026-nemoclaw-memory-code-license-commit-718eb6d.txt](originals/2026-nemoclaw-memory/2026-nemoclaw-memory-code-license-commit-718eb6d.txt); [2026-nemoclaw-memory-eval-readme-commit-718eb6d.md](originals/2026-nemoclaw-memory/2026-nemoclaw-memory-eval-readme-commit-718eb6d.md); [2026-nemoclaw-memory-results-readme-commit-718eb6d.md](originals/2026-nemoclaw-memory/2026-nemoclaw-memory-results-readme-commit-718eb6d.md); [2026-nemoclaw-memory-agentic-rag-report-commit-718eb6d.json](originals/2026-nemoclaw-memory/2026-nemoclaw-memory-agentic-rag-report-commit-718eb6d.json); [2026-nemoclaw-memory-self-model-report-commit-718eb6d.json](originals/2026-nemoclaw-memory/2026-nemoclaw-memory-self-model-report-commit-718eb6d.json). License/permission: Apache-2.0; Apache-2.0 (repository LICENSE and file SPDX header); Apache-2.0 (repository LICENSE). Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2025-darwin-godel-machine"></a>

### [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954)

- **Key / type / family:** `2025-darwin-godel-machine`; ICLR 2026 conference paper and code; `2025-darwin-godel-machine`. **Authors:** Zhang, Jenny, Hu, Shengran, Lu, Cong et al..
- **Dates / version:** first 2025-05-29; latest metadata 2026-03-12; read/inspected v3 (read and latest). **Access:** 2026-09-16; primary full text: methods, results, transfer, cost appendix.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Foundational open-ended self-editing system with cross-benchmark transfer and explicit $22k run cost; one adaptive search run limits strength. **Notes:** [reading record](notes/2025-darwin-godel-machine.md).
- **Originals:** [2025-darwin-godel-machine-paper-v3.pdf](originals/2025-darwin-godel-machine/2025-darwin-godel-machine-paper-v3.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.
- **Relationship:** DGM/SICA/HGM/Hyperagents: related methods; distinct experiments, not independent replications.

<a id="2026-dream-rsi"></a>

### [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858v1)

- **Key / type / family:** `2026-dream-rsi`; preprint; `2026-dream-rsi`. **Authors:** Zheng, Tong, Wu, Xidong, Zhang, Zheng et al..
- **Dates / version:** first 2026-09-14; latest metadata 2026-09-14; read/inspected v1; repository4149ea9. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Replay-based exploration-policy improvement with fixed-policy comparisons; call counts omit total costs, no repeated-run uncertainty. **Notes:** [reading record](notes/2026-dream-rsi.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2609.14858v1).

<a id="2026-escher-loop"></a>

### [Escher-Loop: Mutual Evolution by Closed-Loop Self-Referential Optimization](https://arxiv.org/abs/2604.23472)

- **Key / type / family:** `2026-escher-loop`; preprint; empirical program/meta-optimizer evolution; `2026-escher-loop`. **Authors:** Liu, Ziyang, Guo, Xinyan, Wei, Xuchen et al..
- **Dates / version:** first 2026-04-25; latest metadata 2026-05-27; read/inspected v2. **Access:** 2026-09-16; Primary PDF: full methods/results, mechanism ablations, and Appendix A read; linked code not audited; experiments not reproduced..
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Strongest new empirical meta-improvement candidate: matched token budgets and three-run ablations, but only three fixed task instances and no held-out cross-domain optimizer transfer. **Notes:** [reading record](notes/2026-escher-loop.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2604.23472v2).

<a id="2026-evo-harness"></a>

### [Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents](https://arxiv.org/abs/2608.15071)

- **Key / type / family:** `2026-evo-harness`; EMNLP 2026 Main paper and code; `2026-evo-harness`. **Authors:** Wei, Tianxin, Shi, Zhan, Lin, Minhua et al..
- **Dates / version:** first 2026-08-15; latest metadata 2026-08-30; read/inspected v2 (read and latest). **Access:** 2026-09-16; primary full text: algorithm, Tables 1-5, transfer and feedback ablations.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Broad five-benchmark evidence, held-out transfer, and valuable negative feedback result; no repeat intervals or full cost ledger. **Notes:** [reading record](notes/2026-evo-harness.md).
- **Originals:** [2026-evo-harness-paper-v2.pdf](originals/2026-evo-harness/2026-evo-harness-paper-v2.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="evoharnessbench"></a>

### [EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness?](https://arxiv.org/abs/2609.04280v2)

- **Key / type / family:** `evoharnessbench`; preprint; `evoharnessbench`. **Authors:** Ke, Zixuan, Patil, Vaidehi, Shi, Haizhou et al..
- **Dates / version:** first 2026-09-03; latest metadata 2026-09-10; read/inspected v2. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. External catalog growth complements task-stream changes; three-run population SD verified. **Notes:** [reading record](notes/2026-evoharnessbench.md).
- **Originals:** [2026-evoharnessbench-paper-v2.pdf](originals/2026-evoharnessbench/2026-evoharnessbench-paper-v2.pdf). License/permission: CC BY-SA 4.0. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-ground-truth-first"></a>

### [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](https://arxiv.org/abs/2607.21962)

- **Key / type / family:** `2026-ground-truth-first`; preprint; `2026-ground-truth-first`. **Authors:** Spencer, Quentin.
- **Dates / version:** first 2026-07-24; latest metadata 2026-07-24; read/inspected v1. **Access:** 2026-09-16; full text.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Strongest evaluation challenge; synthetic single-author preprint with artifact package still pending and no independent replication. **Notes:** [reading record](notes/2026-ground-truth-first.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2607.21962v1).

<a id="2025-huxley-godel-machine"></a>

### [Huxley-G\"odel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](https://arxiv.org/abs/2510.21614)

- **Key / type / family:** `2025-huxley-godel-machine`; ICLR 2026 conference paper and code; `2025-huxley-godel-machine`. **Authors:** Wang, Wenyi, Piękos, Piotr, Nanbo, Li et al..
- **Dates / version:** first 2025-10-24; latest metadata 2025-10-29; read/inspected v3 (read and latest). **Access:** 2026-09-16; primary full text: methods, Tables 1-4, setup appendices.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Directly addresses fitness-proxy mismatch with task, evaluation, CPU-hour, and unseen-task accounting. **Notes:** [reading record](notes/2025-huxley-godel-machine.md).
- **Originals:** [2025-huxley-godel-machine-paper-v3.pdf](originals/2025-huxley-godel-machine/2025-huxley-godel-machine-paper-v3.pdf). License/permission: http://creativecommons.org/licenses/by-nc-sa/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.
- **Relationship:** DGM/SICA/HGM/Hyperagents: related methods; distinct experiments, not independent replications.

<a id="library-drift"></a>

### [Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries](https://arxiv.org/abs/2605.19576v3)

- **Key / type / family:** `library-drift`; preprint; `library-drift`. **Authors:** Zhang, Xing, Cui, Yanwei, Wang, Guanghui et al..
- **Dates / version:** first 2026-05-19; latest metadata 2026-07-29; read/inspected v3. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Narrow three-seed lifecycle ablations expose harmful retirement; unmatched costs and selected tasks. **Notes:** [reading record](notes/2026-library-drift.md).
- **Originals:** [2026-library-drift-paper-v3.pdf](originals/2026-library-drift/2026-library-drift-paper-v3.pdf). License/permission: https://creativecommons.org/licenses/by-nc-sa/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-memrl"></a>

### [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192)

- **Key / type / family:** `2026-memrl`; preprint; `2026-memrl`. **Authors:** Zhang, Shengtao, Wang, Jiaqian, Zhou, Ruiwen et al..
- **Dates / version:** first 2026-01-06; latest metadata 2026-02-12; read/inspected v2. **Access:** 2026-09-16; full text.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Clean stability/plasticity mechanism with held-out transfer; no uncertainty and mixed backbones. **Notes:** [reading record](notes/2026-memrl.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2601.03192v2).

<a id="metarsi"></a>

### [MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves](https://arxiv.org/abs/2609.06396v2)

- **Key / type / family:** `metarsi`; preprint; `metarsi`. **Authors:** Tan, Zihan, Sun, Leixin, Shi, Zitong et al..
- **Dates / version:** first 2026-09-06; latest metadata 2026-09-09; read/inspected v2. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** reviewed-reserve; rubric H / L / H / H / H. Provisional composition results; accounting conventions found but empirical split/budget ledgers not verified. **Notes:** [reading record](notes/2026-metarsi.md).
- **Originals:** [2026-metarsi-paper-v2.pdf](originals/2026-metarsi/2026-metarsi-paper-v2.pdf). License/permission: CC BY 4.0. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="reef"></a>

### [Reef: inference-time learning infrastructure](https://github.com/Human-Agent-Society/reef/tree/401db3670d34b1b5a77989234272e0bee4b90ce8)

- **Key / type / family:** `reef`; first-party technical article and open-source code; `reef`. **Authors:** Ao Qu and collaborators; Human-Agent-Society.
- **Dates / version:** first 2026-09-15; latest metadata 2026-09-16; read/inspected commit 401db3670d34b1b5a77989234272e0bee4b90ce8. **Access:** 2026-09-16; article, README, repository tree, and meta-harness results inspected; not executed.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Strong infrastructure and audit artifact for feedback attribution and versioned learning, with bounded same-task meta-harness evidence. **Notes:** [reading record](notes/2026-reef.md).
- **Originals:** [2026-reef-code-license-commit-401db36.txt](originals/2026-reef/2026-reef-code-license-commit-401db36.txt); [2026-reef-meta-harness-results-commit-401db36.md](originals/2026-reef/2026-reef-meta-harness-results-commit-401db36.md); [2026-reef-meta-harness-eval-readme-commit-401db36.md](originals/2026-reef/2026-reef-meta-harness-eval-readme-commit-401db36.md). License/permission: Apache-2.0; Apache-2.0 (repository LICENSE). Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-reflection-in-the-dark"></a>

### [Reflection in the Dark: Exposing and Escaping the Black Box in Reflective Prompt Optimization](https://arxiv.org/abs/2603.18388)

- **Key / type / family:** `2026-reflection-in-the-dark`; preprint; `2026-reflection-in-the-dark`. **Authors:** Liu, Shiyan, Xia, Qifeng, Xia, Qiyun et al..
- **Dates / version:** first 2026-03-19; latest metadata 2026-06-08; read/inspected v2. **Access:** 2026-09-16; full text; methods, main tables, appendices B-C, and traces inspected.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Credible matched-budget GEPA counterexample under the official defective seed, but one random seed, two math benchmarks, no repeated optimization runs, and a hand-curated heuristic set limit breadth. **Notes:** [reading record](notes/2026-reflection-in-the-dark.md).
- **Originals:** [2026-reflection-in-the-dark-paper-v2.pdf](originals/2026-reflection-in-the-dark/2026-reflection-in-the-dark-paper-v2.pdf). License/permission: http://creativecommons.org/licenses/by-nc-nd/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2023-reflexion"></a>

### [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366v4)

- **Key / type / family:** `2023-reflexion`; peer-reviewed paper; `2023-reflexion`. **Authors:** Shinn, Noah, Cassano, Federico, Berman, Edward et al..
- **Dates / version:** first 2023-03-20; latest metadata 2023-10-10; read/inspected v4; NeurIPS2023. **Access:** 2026-09-16; primary methods/results read.
- **Selection:** reviewed-reserve; rubric H / M / M / H / H. Historical verbal-feedback mechanism; repeated attempts differ from new-task transfer. **Notes:** [reading record](notes/2023-reflexion.md).
- **Originals:** [2023-reflexion-paper-v4.pdf](originals/2023-reflexion/2023-reflexion-paper-v4.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-reward-hacking-benchmark"></a>

### [Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964v1)

- **Key / type / family:** `2026-reward-hacking-benchmark`; arXiv preprint; `2026-reward-hacking-benchmark`. **Authors:** Thaman, Kunvar.
- **Dates / version:** first 2026-05-03; latest metadata 2026-05-03; read/inspected v1. **Access:** 2026-09-16; full primary methods/results and limitations read.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Broad integrity counterevidence with hardening and difficulty comparisons; RL post-training comparison is observational and exploit classification has limited audit coverage. **Notes:** [reading record](notes/2026-reward-hacking-agents.md).
- **Originals:** [2026-reward-hacking-benchmark-paper-v1.pdf](originals/2026-reward-hacking-benchmark/2026-reward-hacking-benchmark-paper-v1.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-reward-hacking-agents"></a>

### [RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents](https://arxiv.org/abs/2603.11337v1)

- **Key / type / family:** `2026-reward-hacking-agents`; arXiv preprint and code; `2026-reward-hacking-agents`. **Authors:** Atinafu, Yonas, Cohen, Robin.
- **Dates / version:** first 2026-03-11; latest metadata 2026-03-11; read/inspected v1; repository HEAD 9ea7cdc8dde6c89b1ea75e2ba86a61ffff72eb34 inspected 2026-09-16. **Access:** 2026-09-16; full primary methods/results plus repository README/license read.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Cleanly isolates two editable-workspace compromise channels; natural-policy prevalence does not generalize beyond three tasks and two small models. **Notes:** [reading record](notes/2026-reward-hacking-agents.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2603.11337v1).

<a id="2026-sea-eval"></a>

### [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988v3)

- **Key / type / family:** `2026-sea-eval`; arXiv preprint; `2026-sea-eval`. **Authors:** Jiang, Sihang, Ma, Lipeng, Hong, Zhonghua et al..
- **Dates / version:** first 2026-04-10; latest metadata 2026-05-24; read/inspected v3. **Access:** 2026-09-16; full primary methods/results and selected appendix read.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Directly contrasts episodic success with cost and transfer trajectories; quantitative scope and cross-system comparability require qualification. **Notes:** [reading record](notes/2026-sea-eval.md).
- **Originals:** [2026-sea-eval-paper-v3.pdf](originals/2026-sea-eval/2026-sea-eval-paper-v3.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-sia"></a>

### [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276)

- **Key / type / family:** `2026-sia`; preprint; empirical agent system; `2026-sia`. **Authors:** Hebbar, Prannay, Manawat, Yogendra, Verboomen, Samuel et al..
- **Dates / version:** first 2026-05-26; latest metadata 2026-05-28; read/inspected v2. **Access:** 2026-09-16; Primary PDF: methods, all results, discussion, and limitations read; project/code not audited; experiments not reproduced..
- **Selection:** reviewed-reserve; rubric H / L / H / H / H. Clearest direct weight+harness mechanism, but reported endpoints reuse the optimization evaluator; LawBench's nominal test split is used during iterative updates, and no repeated-run uncertainty or fresh post-selection test is reported. **Notes:** [reading record](notes/2026-sia.md).
- **Originals:** [2026-sia-paper-v2.pdf](originals/2026-sia/2026-sia-paper-v2.pdf). License/permission: http://creativecommons.org/licenses/by-sa/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="sciencebuddy"></a>

### [ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents](https://arxiv.org/abs/2609.17523v1)

- **Key / type / family:** `sciencebuddy`; preprint; `sciencebuddy`. **Authors:** Xue, Shuhan, Zhong, Jianyuan, Nan, Ziyuan et al..
- **Dates / version:** first 2026-09-15; latest metadata 2026-09-15; read/inspected v1; code454d11c. **Access:** 2026-09-16; primary methods/results inspected.
- **Selection:** reviewed-reserve; rubric H / L / H / H / H. Recipe discloses material overlap and differs from paper schedule; historical evaluation denominators unresolved. **Notes:** [reading record](notes/2026-sciencebuddy.md).
- **Originals:** [2026-sciencebuddy-experiment-config-commit-454d11c.toml](originals/2026-sciencebuddy/2026-sciencebuddy-experiment-config-commit-454d11c.toml); [2026-sciencebuddy-code-license-commit-454d11c.txt](originals/2026-sciencebuddy/2026-sciencebuddy-code-license-commit-454d11c.txt); [2026-sciencebuddy-experiment-guide-commit-454d11c.md](originals/2026-sciencebuddy/2026-sciencebuddy-experiment-guide-commit-454d11c.md); [2026-sciencebuddy-algorithm-guide-commit-454d11c.md](originals/2026-sciencebuddy/2026-sciencebuddy-algorithm-guide-commit-454d11c.md). License/permission: MIT (repository artifacts only). Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-shaper"></a>

### [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350v2)

- **Key / type / family:** `2026-shaper`; arXiv preprint; `2026-shaper`. **Authors:** Wang, Peidong, Ma, Zhiming, Chang, Ying et al..
- **Dates / version:** first 2026-08-11; latest metadata 2026-09-10; read/inspected v2. **Access:** 2026-09-16; full primary methods/results and optimization-cost appendix read.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Adds held-out embodied transfer across two action interfaces with frozen weights; one optimization/evaluation run and no intervals. **Notes:** [reading record](notes/2026-shaper.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2608.11350v2).

<a id="2023-stop"></a>

### [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304v3)

- **Key / type / family:** `2023-stop`; peer-reviewed conference paper and preprint; `2023-stop`. **Authors:** Eric Zelikman, Eliana Lorch, Lester Mackey et al..
- **Dates / version:** first 2023-10-03; latest metadata 2024-08-16; read/inspected v3; COLM2024. **Access:** 2026-09-16; full PDF methods, experiments, safety, and limitations.
- **Selection:** reviewed-reserve; rubric H / M / M / H / M. Foundational code-level RSI with held-out same-task and small cross-task tests plus explicit sandbox/reward-hacking audit; not full model RSI. **Notes:** [reading record](notes/2023-stop.md).
- **Original:** retention-restricted. License/permission: arXiv non-exclusive; OpenReview alternate inaccessible. [Download/source location](https://arxiv.org/pdf/2310.02304v3).

<a id="2026-selfmem"></a>

### [SelfMem: Self-Optimizing Memory for AI Agents](https://arxiv.org/abs/2607.03726)

- **Key / type / family:** `2026-selfmem`; preprint; `2026-selfmem`. **Authors:** Yang, Shu, Wu, Junchao, Wong, Derek F. et al..
- **Dates / version:** first 2026-07-04; latest metadata 2026-07-04; read/inspected v1. **Access:** 2026-09-16; full text.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Strong shared-harness and cost evidence; one benchmark/model family and no uncertainty. **Notes:** [reading record](notes/2026-selfmem.md).
- **Originals:** [2026-selfmem-paper-v1.pdf](originals/2026-selfmem/2026-selfmem-paper-v1.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="sol-pi"></a>

### [SoL-Pi](https://github.com/NVIDIA/SoL-Pi)

- **Key / type / family:** `sol-pi`; code release; `sol-pi`. **Authors:** NVIDIA.
- **Dates / version:** first unknown; inspected September2026 release; latest metadata 2026-09-15 (inspected commit); read/inspected repository snapshot in note. **Access:** 2026-09-16; README inspected.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Implementation of reusable efficiency mechanisms; paper forthcoming and empirical recipe not independently audited. **Notes:** [reading record](notes/2026-sol-pi.md).
- **Original:** not retained: public original inspected; no redistribution license verified for page, or only metadata/theoretical background reviewed. License/permission: unknown. Canonical page above is the inspected location.

<a id="2025-test-time-reinforcement-learning"></a>

### [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084)

- **Key / type / family:** `2025-test-time-reinforcement-learning`; preprint; `2025-test-time-reinforcement-learning`. **Authors:** Zuo, Yuxin, Zhang, Kaiyan, Sheng, Li et al..
- **Dates / version:** first 2025-04-22; latest metadata 2025-06-30; read/inspected arXiv v3. **Access:** 2026-09-16; full paper and appendices.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Strong bridge between test-time inference and parameter learning, but adaptation and scoring use the same finite prompt sets and no independent repeats are reported. **Notes:** [reading record](notes/2025-test-time-reinforcement-learning.md).
- **Originals:** [2025-test-time-reinforcement-learning-paper-v3.pdf](originals/2025-test-time-reinforcement-learning/2025-test-time-reinforcement-learning-paper-v3.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-economics-rsi"></a>

### [The Economics of Recursive Self-Improvement](https://arxiv.org/abs/2609.15802)

- **Key / type / family:** `2026-economics-rsi`; economics theory and calibration preprint; `2026-economics-rsi`. **Authors:** Cunningham, Tom, Althoff, Lukas, Halperin, Basil et al..
- **Dates / version:** first 2026-09-14; latest metadata 2026-09-14; read/inspected v1. **Access:** 2026-09-16; Primary PDF: full models, data discussion, and calibration read; underlying datasets/cited estimates not reanalyzed..
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Best theoretical interpretation of when local self-improvement could become self-sustaining; its roughly 0.15 threshold is an assumption-sensitive scenario calculation, not empirical agent evidence. **Notes:** [reading record](notes/2026-economics-rsi.md).
- **Originals:** [2026-economics-rsi-paper-v1.pdf](originals/2026-economics-rsi/2026-economics-rsi-paper-v1.pdf). License/permission: http://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2026-spontaneous-world-knowledge"></a>

### [Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration](https://arxiv.org/abs/2604.18131)

- **Key / type / family:** `2026-spontaneous-world-knowledge`; preprint; trained inference-time adaptation; `2026-spontaneous-world-knowledge`. **Authors:** Zhang, Qifan, Ma, Dongyang, Fang, Tianqing et al..
- **Dates / version:** first 2026-04-20; latest metadata 2026-04-20; read/inspected v1. **Access:** 2026-09-16; Full primary PDF methods, experiments, tables, prompts, and input-processing appendix; no experiment reproduction or identified code/data release..
- **Selection:** reviewed-reserve; rubric M / M / M / H / M. Do not replace a current top-ten family. Retain below Agent-World as an adjacent proactive-context example; persistent memory/task-stream sources provide stronger coverage of lasting improvement. **Notes:** [reading record](notes/2026-spontaneous-world-knowledge.md).
- **Originals:** [2026-spontaneous-world-knowledge-paper-v1.pdf](originals/2026-spontaneous-world-knowledge/2026-spontaneous-world-knowledge-paper-v1.pdf). License/permission: https://creativecommons.org/licenses/by/4.0/. Retrieved September 16; exact artifact versions and hashes in manifest.

<a id="2023-voyager"></a>

### [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)

- **Key / type / family:** `2023-voyager`; preprint / project paper; `2023-voyager`. **Authors:** Wang, Guanzhi, Xie, Yuqi, Jiang, Yunfan et al..
- **Dates / version:** first 2023-05-25; latest metadata 2023-10-19; read/inspected arXiv v2. **Access:** 2026-09-16; primary methods/results reviewed in notes/2023-voyager.md.
- **Selection:** reviewed-reserve; rubric M / M / M / H / M. Canonical frozen-weight skill/curriculum comparator, but older, embodied-specific, and covered by the memory/skills lane. **Notes:** [reading record](notes/2023-voyager.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2305.16291v2).

<a id="2026-self-evolution-backfires"></a>

### [When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents](https://arxiv.org/abs/2608.05810)

- **Key / type / family:** `2026-self-evolution-backfires`; preprint; `2026-self-evolution-backfires`. **Authors:** Shang, Linfang, Xu, Ming, Sun, Yiding et al..
- **Dates / version:** first 2026-08-06; latest metadata 2026-08-06; read/inspected v1. **Access:** 2026-09-16; full text; methods, Tables 1-4, transfer, rollback, and uncertainty discussion inspected.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Useful admission/descendant-contamination mechanism, but the headline phase transition is on the 50-task evolution split with one correlated trajectory; Test-25 verifies final-pool transfer rather than the trajectory. **Notes:** [reading record](notes/2026-self-evolution-backfires.md).
- **Original:** retention-restricted. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2608.05810v1).

<a id="autoresearch"></a>

### [autoresearch](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117)

- **Key / type / family:** `autoresearch`; open-source code; `autoresearch`. **Authors:** Andrej Karpathy.
- **Dates / version:** first 2026-03-06; latest metadata 2026-03-26; read/inspected commit 228791fb499afffb54b46200aca536f79142f117. **Access:** 2026-09-16; README and tree inspected; not executed.
- **Selection:** reviewed-reserve; rubric H / L / M / H / H. Essential minimal comparator and teaching artifact, but not itself controlled evidence of general self-improvement. **Notes:** [reading record](notes/2026-autoresearch.md).
- **Original:** not retained: public original inspected; no redistribution license verified for page, or only metadata/theoretical background reviewed. License/permission: README declares MIT; no standalone LICENSE present at pin. Canonical page above is the inspected location.

## Screened reserves

<a id="2025-self-improving-coding-agent"></a>

### [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228v2)

- **Key / type / family:** `2025-self-improving-coding-agent`; preprint/workshop paper and code; `2025-self-improving-coding-agent`. **Authors:** Robeyns, Maxime, Szummer, Martin, Aitchison, Laurence.
- **Dates / version:** first 2025-04-21; revision 2025-05-16; read v2. **Access:** 2026-09-16; primary §3/Algorithm 1 and §§5.1–6 mechanism/limitations read; selected citation contexts checked.
- **Selection:** reviewed-reserve. Direct DGM comparator: best-agent archive expansion versus broader stepping-stone search. **Notes:** [reading record](notes/2025-self-improving-coding-agent.md).
- **Originals:** saved. License/permission: CC BY 4.0. [Original PDF](originals/2025-self-improving-coding-agent/2025-self-improving-coding-agent-paper-v2.pdf).

<a id="2024-aflow"></a>

### [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762v4)

- **Key / type / family:** `2024-aflow`; ICLR 2025 paper; arXiv v4 read; `2024-aflow`. **Authors:** Zhang, Jiayi, Xiang, Jinyu, Yu, Zhaoyang et al..
- **Dates / version:** first 2024-10-14; latest metadata 2025-04-15; read v4. **Access:** 2026-09-16; primary methods/results read; coordinator metadata and methods checked.
- **Selection:** reviewed-reserve; rubric H / M / M / H / H. Thesis foundation: workflow optimization yields reusable fixed artifacts and makes execution/search cost distinction explicit. **Notes:** [reading record](notes/2024-aflow.md).
- **Originals:** Official versioned HTML read; arXiv non-exclusive distribution license does not establish redistribution permission. License/permission: arXiv non-exclusive distribution license. Metadata and preparation costs remain source-specific.

<a id="2024-curse-of-recursion-model-collapse"></a>

### [AI models collapse when trained on recursively generated data](https://doi.org/10.1038/s41586-024-07566-y)

- **Key / type / family:** `2024-curse-of-recursion-model-collapse`; peer-reviewed journal paper; `2024-curse-of-recursion-model-collapse`. **Authors:** Ilia Shumailov et al..
- **Dates / version:** first 2024; latest metadata 2024; read/inspected Nature 631. **Access:** 2026-09-16; full paper.
- **Selection:** screened-reserve; rubric H / H / H / H / H. Strong failure-mode evidence for recursive replacement, with theory and OPT-125M experiments; does not test retaining real data or verification-heavy agent curricula. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: retention/redistribution basis not established. [Download/source location](https://www.nature.com/articles/s41586-024-07566-y.pdf).

<a id="2024-automated-design-agentic-systems"></a>

### [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435v2)

- **Key / type / family:** `2024-automated-design-agentic-systems`; ICLR 2025 paper; arXiv v2 read; `2024-automated-design-agentic-systems`. **Authors:** Hu, Shengran, Lu, Cong, Clune, Jeff.
- **Dates / version:** first 2024-08-15; latest metadata 2025-03-02; read v2. **Access:** 2026-09-16; primary methods/results read; coordinator metadata and methods checked.
- **Selection:** reviewed-reserve; rubric H / M / M / H / H. Thesis foundation: code-defined design search with fixed meta-agent is a predecessor to recursive improver editing. **Notes:** [reading record](notes/2024-automated-design-agentic-systems.md).
- **Originals:** [2024-automated-design-agentic-systems-paper-v2.pdf](originals/2024-automated-design-agentic-systems/2024-automated-design-agentic-systems-paper-v2.pdf) License/permission: CC BY 4.0. Metadata and preparation costs remain source-specific.

<a id="2026-nist-evaluation-cheating-background"></a>

### [Background: AI Models Can Cheat on Evaluations](https://www.nist.gov/caisi/cheating-ai-agent-evaluations/1-background-ai-models-can-cheat-evaluations)

- **Key / type / family:** `2026-nist-evaluation-cheating-background`; government background explainer; `2026-nist-evaluation-cheating-background`. **Authors:** NIST CAISI.
- **Dates / version:** first unknown; latest metadata unknown; read/inspected web page accessed via discovery on 2026-09-16. **Access:** 2026-09-16; first-party background lead.
- **Selection:** screened-reserve; rubric M / L / L / H / M. Authoritative teaching background but not primary empirical evidence and not specific to weight adaptation. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: U.S. government page; exact reuse terms not checked. Canonical page above is the inspected location.

<a id="2026-evo-bench"></a>

### [Evo-Bench: Can Language Models Improve Agent Harness?](https://arxiv.org/abs/2608.09096v2)

- **Key / type / family:** `2026-evo-bench`; arXiv preprint; `2026-evo-bench`. **Authors:** Huang, Lisheng, Yang, Chen, Zhou, Hao et al..
- **Dates / version:** first 2026-08-10; latest metadata 2026-08-11; read/inspected v2. **Access:** 2026-09-16; full primary benchmark construction, methods, results, and selected appendix read.
- **Selection:** screened-reserve; rubric H / M / H / H / H. Broad harness-evolution test with held-out suites and fixed budgets; all main experiments are single runs and selection favors harness-sensitive tasks. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2608.09096v2).

<a id="undated-hermes-skills"></a>

### [Hermes Agent Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)

- **Key / type / family:** `undated-hermes-skills`; documentation; `undated-hermes-skills`. **Authors:** Nous Research.
- **Dates / version:** first unknown; latest metadata unknown; read/inspected live docs September16. **Access:** 2026-09-16; relevant sections read.
- **Selection:** screened-reserve; rubric H / L / M / H / M. Documented creation/update/deletion functions; no controlled generalization result. **Notes:** [reading record](../practitioner-sources.md).
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2026-langchain-memory"></a>

### [How To Give Your Agent Memory](https://www.langchain.com/blog/how-to-give-your-agent-memory)

- **Key / type / family:** `2026-langchain-memory`; technical blog; `2026-langchain-memory`. **Authors:** Jake Broekhuizen / LangChain.
- **Dates / version:** first 2026-06-24; latest metadata 2026-06-24; read/inspected published HTML. **Access:** 2026-09-16; article read.
- **Selection:** screened-reserve; rubric H / L / M / H / M. Trace capture, analysis, and versioned context engineering; no controlled result. **Notes:** [reading record](../practitioner-sources.md).
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2026-rememberloop-continuously-improving-agents"></a>

### [How to build continuously improving agents](https://blog.rememberloop.com/p/how-to-build-continuously-improving)

- **Key / type / family:** `2026-rememberloop-continuously-improving-agents`; firsthand practitioner essay; `2026-rememberloop-continuously-improving-agents`. **Authors:** Sriram Natarajan.
- **Dates / version:** first 2026-06-15; latest metadata 2026-06-15; read/inspected published HTML. **Access:** 2026-09-16; full essay read.
- **Selection:** screened-reserve; rubric M / L / M / H / M. Memorable firsthand degradation incidents and monitoring design, but anecdotal with no logs or controlled outcome. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: No reuse license found; canonical link only. Canonical page above is the inspected location.

<a id="2024-model-collapse-accumulation"></a>

### [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](https://arxiv.org/abs/2404.01413)

- **Key / type / family:** `2024-model-collapse-accumulation`; conference paper / preprint; `2024-model-collapse-accumulation`. **Authors:** Gerstgrasser, Matthias, Schaeffer, Rylan, Dey, Apratim et al..
- **Dates / version:** first 2024-04-01; latest metadata 2024-04-29; read/inspected arXiv v2. **Access:** 2026-09-16; full paper and appendices.
- **Selection:** screened-reserve; rubric H / H / H / H / H. Shows replacement degrades while real-plus-synthetic accumulation stays bounded across three generative model classes; growing data/compute and small models limit transfer to agents. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2404.01413v2).

<a id="2026-krainov-skill-optimization"></a>

### [Karpathy’s Autoresearch: Improving Agentic Coding Skills](https://zerocopy.blog/2026/03/25/karpathys-autoresearch-improving-agentic-coding-skills/)

- **Key / type / family:** `2026-krainov-skill-optimization`; practitioner proposal; `2026-krainov-skill-optimization`. **Authors:** Kirill Krainov.
- **Dates / version:** first 2026-03-25; latest metadata 2026-03-25; read/inspected published HTML. **Access:** 2026-09-16; article read.
- **Selection:** screened-reserve; rubric H / L / M / H / M. Experiment-based skill optimization proposal; article defers working implementation/results. **Notes:** [reading record](../practitioner-sources.md).
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2026-living-harness"></a>

### [Living-Harness Is an Interactive-Agent Evolver](https://arxiv.org/abs/2607.26598)

- **Key / type / family:** `2026-living-harness`; preprint; `2026-living-harness`. **Authors:** Du, Yuetian, Wang, Yucheng, Xu, He et al..
- **Dates / version:** first 2026-07-29; latest metadata 2026-08-11; read/inspected v2. **Access:** 2026-09-16; primary full text: main tables, cycles, ablations, transfer, appendix protocol.
- **Selection:** screened-reserve; rubric H / M / H / H / H. Distinct interactive-domain evidence with frozen cross-model reuse; denominators and variance are unclear. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2607.26598).

<a id="2025-longmemeval"></a>

### [LongMemEval](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)

- **Key / type / family:** `2025-longmemeval`; peer-reviewed conference paper; `2025-longmemeval`. **Authors:** Di Wu et al..
- **Dates / version:** first unknown (ICLR 2025 proceedings version); latest metadata unknown (ICLR 2025 proceedings version); read/inspected conference version. **Access:** 2026-09-16; metadata plus prior-session context.
- **Selection:** screened-reserve; rubric M / H / M / H / H. Older benchmark foundation; short/medium horizons and LLM judging limit lifelong claims. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: Unknown/unverified for retention. [Download/source location](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf).

<a id="2026-memskill"></a>

### [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474)

- **Key / type / family:** `2026-memskill`; preprint; `2026-memskill`. **Authors:** Zhang, Haozhen, Long, Quanyu, Bao, Jianzhu et al..
- **Dates / version:** first 2026-02-02; latest metadata 2026-05-24; read v2. **Access:** 2026-09-16; primary methods/results and relevant appendices read; tier2/coordinator verified 2026-09-16.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Thesis coverage: evolving memory-operation bank separates learning what to retain from learning how to retain it. **Notes:** [reading record](notes/2026-memskill.md).
- **Originals:** [2026-memskill-paper-v2.pdf](originals/2026-memskill/2026-memskill-paper-v2.pdf) License/permission: http://creativecommons.org/licenses/by/4.0/. Metadata and preparation costs remain source-specific.

<a id="2024-rate-model-collapse-recursive-training"></a>

### [Rate of Model Collapse in Recursive Training](https://arxiv.org/abs/2412.17646)

- **Key / type / family:** `2024-rate-model-collapse-recursive-training`; preprint; `2024-rate-model-collapse-recursive-training`. **Authors:** Suresh, Ananda Theertha, Thangaraj, Andrew, Khandavally, Aditya Nanda Kishore.
- **Dates / version:** first 2024-12-23; latest metadata 2024-12-23; read/inspected arXiv v1. **Access:** 2026-09-16; full paper.
- **Selection:** screened-reserve; rubric M / M / M / M / M. Useful idealized rate analysis, but Bernoulli/Poisson/Gaussian recursions are indirect evidence for LLM agents. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2412.17646v1).

<a id="2025-reasoningbank"></a>

### [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140v2)

- **Key / type / family:** `2025-reasoningbank`; ICLR 2026 paper; arXiv v2 read; `2025-reasoningbank`. **Authors:** Ouyang, Siru, Yan, Jun, Hsu, I-Hung et al..
- **Dates / version:** first 2025-09-29; latest metadata 2026-03-16; read v2. **Access:** 2026-09-16; primary methods/results read; coordinator metadata and methods checked.
- **Selection:** reviewed-reserve; rubric H / M / M / H / H. Thesis foundation: memory and extra inference jointly generate learning signal; controls must separate their costs. **Notes:** [reading record](notes/2025-reasoningbank.md).
- **Originals:** Official versioned HTML read; arXiv non-exclusive distribution license does not establish redistribution permission. License/permission: arXiv non-exclusive distribution license. Metadata and preparation costs remain source-specific.

<a id="2025-self-evolving-curriculum"></a>

### [Self-Evolving Curriculum for LLM Reasoning](https://arxiv.org/abs/2505.14970)

- **Key / type / family:** `2025-self-evolving-curriculum`; preprint; `2025-self-evolving-curriculum`. **Authors:** Chen, Xiaoyin, Lu, Jiarui, Kim, Minsu et al..
- **Dates / version:** first 2025-05-20; latest metadata 2025-10-30; read/inspected arXiv v4. **Access:** 2026-09-16; full PDF spot inspection; results not fully audited.
- **Selection:** screened-reserve; rubric M / M / M / M / M. Controlled learned curriculum baseline, though it selects fixed task categories rather than generating open-ended experience. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2505.14970v4).

<a id="2026-betterforall-self-improving-agents"></a>

### [Self-Improving Agents -- A Progression](https://github.com/BetterForAll/self-improving-agents/tree/5f7823732d87c515ed7842d06bc3c2613ed0445b)

- **Key / type / family:** `2026-betterforall-self-improving-agents`; open-source code and experiment logs; `2026-betterforall-self-improving-agents`. **Authors:** BetterForAll.
- **Dates / version:** first 2026-04-04; latest metadata 2026-04-09; read/inspected commit 5f7823732d87c515ed7842d06bc3c2613ed0445b. **Access:** 2026-09-16; README and repository tree/results inspected; not executed.
- **Selection:** screened-reserve; rubric H / L / M / H / M. Inspectable teaching artifact with logs and evolving tests, but independent results were not audited or reproduced. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: MIT. Canonical page above is the inspected location.

<a id="2026-skillhone"></a>

### [SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History](https://arxiv.org/abs/2606.08671)

- **Key / type / family:** `2026-skillhone`; preprint and code; `2026-skillhone`. **Authors:** Li, Zhiwei, Hu, Yong.
- **Dates / version:** first 2026-06-07; latest metadata 2026-07-06; read/inspected v2. **Access:** 2026-09-16; primary full text: setup, Tables 1-3, transfer, limitations.
- **Selection:** screened-reserve; rubric H / M / H / H / H. Disjoint practice/final sets and strong ablations support persistent optimization history; missing final denominators, variance, and cost. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2606.08671).

<a id="2026-skillos"></a>

### [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614)

- **Key / type / family:** `2026-skillos`; preprint; `2026-skillos`. **Authors:** Ouyang, Siru, Yan, Jun, Chen, Yanfei et al..
- **Dates / version:** first 2026-05-07; latest metadata 2026-05-07; read/inspected v1. **Access:** 2026-09-16; full text.
- **Selection:** screened-reserve; rubric H / M / H / H / H. Three-run cross-executor evidence and grouping ablation; related-group construction and LLM judge constrain interpretation. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2605.06614v1).

<a id="2024-anthropic-reward-tampering"></a>

### [Sycophancy to Subterfuge: Investigating Reward-Tampering in Language Models](https://www.anthropic.com/research/reward-tampering)

- **Key / type / family:** `2024-anthropic-reward-tampering`; first-party research paper and article; `2024-anthropic-reward-tampering`. **Authors:** Anthropic.
- **Dates / version:** first 2024; latest metadata 2024; read/inspected exact paper version provisional. **Access:** 2026-09-16; first-party article lead; no fresh full audit.
- **Selection:** screened-reserve; rubric M / M / M / H / M. Motivates sealed evaluators and demonstrates specification gaming, but is not direct evidence about the screened self-play systems. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2026-postsyntax-agent-improvement-loop"></a>

### [The Agent Improvement Loop: Turning Production Failures into Regression Tests](https://postsyntax.substack.com/p/the-agent-improvement-loop-turning)

- **Key / type / family:** `2026-postsyntax-agent-improvement-loop`; practitioner essay; `2026-postsyntax-agent-improvement-loop`. **Authors:** Rafay A..
- **Dates / version:** first 2026-07-01; latest metadata 2026-07-01; read/inspected published HTML. **Access:** 2026-09-16; full essay read.
- **Selection:** screened-reserve; rubric M / L / L / H / M. Concrete operational loop and useful counterweight, but no measured deployment study or artifact. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: No reuse license found; canonical link only. Canonical page above is the inspected location.

<a id="2026-arcfusion-self-improving-parser"></a>

### [The Agent That Learns: How We Built a Self-Improving AI Loop That Went from 86% to 99.8% Accuracy](https://www.arcfusion.ai/blog/the-agent-that-learns)

- **Key / type / family:** `2026-arcfusion-self-improving-parser`; first-party engineering case study; `2026-arcfusion-self-improving-parser`. **Authors:** Napat Dollapavijit; ArcFusion.
- **Dates / version:** first 2026-04-30; latest metadata 2026-04-30; read/inspected published HTML. **Access:** 2026-09-16; full article read.
- **Selection:** screened-reserve; rubric H / M / M / H / M. Candid repeated-run prompt case study with metric failures and costs, but no formal holdout, public data, or code. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: All rights reserved. Canonical page above is the inspected location.

<a id="2025-understanding-self-play-llm-reasoning"></a>

### [Towards Understanding Self-play for LLM Reasoning](https://arxiv.org/abs/2510.27072)

- **Key / type / family:** `2025-understanding-self-play-llm-reasoning`; workshop paper; `2025-understanding-self-play-llm-reasoning`. **Authors:** Chae, Justin Yang, Alam, Md Tanvirul, Rastogi, Nidhi.
- **Dates / version:** first 2025-10-31; latest metadata 2025-10-31; read/inspected arXiv v1; NeurIPS 2025 Math-AI workshop. **Access:** 2026-09-16; full paper.
- **Selection:** screened-reserve; rubric H / M / H / H / H. Direct AZR analysis finds distributional sharpening, entropy collapse, bounded large-k support, and unsuccessful reward shaping; scope is one framework and two sizes. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by-sa/4.0/. [Download/source location](https://arxiv.org/pdf/2510.27072v1).

<a id="2026-prolific-autoresearch-human-loop"></a>

### [When does autoresearch need a human?](https://huggingface.co/blog/ProlificAI/autoresearch-hitl-experiment)

- **Key / type / family:** `2026-prolific-autoresearch-human-loop`; first-party practitioner experiment and researcher post; `2026-prolific-autoresearch-human-loop`. **Authors:** Nora Petrova; Viviana Márquez; Prolific.
- **Dates / version:** first 2026-05-21; latest metadata 2026-05-21; read/inspected published article. **Access:** 2026-09-16; full article read; linked report/dataset identified.
- **Selection:** screened-reserve; rubric H / M / H / H / H. Rare evidence-bearing practitioner counterexample with participant evaluation, uncertainty, and downloadable annotations; limited to one run/task/model. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: Article reuse and annotation-dataset license not verified. Canonical page above is the inspected location.

## Watchlist: further reading needed

<a id="2025-survey-self-evolving-agents"></a>

### [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046)

- **Key / type / family:** `2025-survey-self-evolving-agents`; TMLR survey; `2025-survey-self-evolving-agents`. **Authors:** Gao, Huan-ang, Geng, Jiayi, Hua, Wenyue et al..
- **Dates / version:** first 2025-07-28; latest metadata 2026-01-16; read/inspected v4. **Access:** 2026-09-16; Primary arXiv metadata and abstract only in the audit; cited primary studies not verified through this source..
- **Selection:** watchlist; rubric H / U / M / H / H. Strong taxonomy and benchmark-reset warning; a survey is navigation, not independent efficacy evidence. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2507.21046v4).

<a id="2025-a-mem"></a>

### [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110v11)

- **Key / type / family:** `2025-a-mem`; peer-reviewed conference paper; `2025-a-mem`. **Authors:** Xu, Wujiang, Liang, Zujie, Mei, Kai, Gao, Hang, Tan, Juntao, Zhang, Yongfeng.
- **Dates / version:** first 2025-02-17; revision 2025-10-08; read arXiv v11 read; NeurIPS 2025. **Access:** 2026-09-16; selected primary methods §§3.1–3.4, evaluation scope and §6 limitations read; citation contexts checked.
- **Selection:** reviewed-reserve. Linked-note memory explains retrieval-based alternative to ACE and an actual AgentStream comparator; no new numerical claim. **Notes:** [reading record](notes/2025-a-mem.md).
- **Originals:** retention-restricted; arXiv non-exclusive license; temporary v11 PDF inspected. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/.

<a id="2025-agent0"></a>

### [Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning](https://arxiv.org/abs/2511.16043)

- **Key / type / family:** `2025-agent0`; preprint and code; `2025-agent0`. **Authors:** Xia, Peng, Zeng, Kaide, Liu, Jiaqi et al..
- **Dates / version:** first 2025-11-20; latest metadata 2025-11-20; read/inspected v1 metadata checked; full version not read. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** watchlist; rubric M / U / H / M / M. Relevant competing mechanism, but better owned by weights/data lane than harness screening. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2511.16043).

<a id="2025-agentarch"></a>

### [AgentArch: A Comprehensive Benchmark to Evaluate Agent Architectures in Enterprise](https://arxiv.org/abs/2509.10769)

- **Key / type / family:** `2025-agentarch`; benchmark preprint; `2025-agentarch`. **Authors:** Bogavelli, Tara, Sharma, Roshnee, Subramani, Hari.
- **Dates / version:** first 2025-09-13; latest metadata 2026-01-06; read/inspected v2 metadata checked; full version not read. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** watchlist; rubric L / U / M / M / M. Useful fixed-architecture control and taxonomy, not self-evolution evidence. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by-nc-sa/4.0/. [Download/source location](https://arxiv.org/pdf/2509.10769).

<a id="2026-agentmemorybench"></a>

### [AgentMemoryBench](https://github.com/solomoon313/AgentMemoryBench)

- **Key / type / family:** `2026-agentmemorybench`; preprint/code artifact; `2026-agentmemorybench`. **Authors:** Solomoon et al..
- **Dates / version:** first unknown (2026 repository paper label); latest metadata None; read/inspected repository version unknown. **Access:** 2026-09-16; README/abstract only.
- **Selection:** watchlist; rubric H / U / H / M / M. Provisional; frozen partitions, paper version, and license require verification. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: Unknown/unverified for retention. Canonical page above is the inspected location.

<a id="2026-agentswift"></a>

### [AgentSwift](https://ojs.aaai.org/index.php/AAAI/article/view/40453)

- **Key / type / family:** `2026-agentswift`; AAAI 2026 paper; `2026-agentswift`. **Authors:** authors not verified in this pass.
- **Dates / version:** first 2026; latest metadata unknown; read/inspected unknown. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** watchlist; rubric M / U / M / L / L. Search-efficiency baseline; lower teaching and coverage value than HGM or FlashEvolve. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2025-automaas"></a>

### [AutoMaAS: Self-Evolving Multi-Agent Architecture Search for Large Language Models](https://arxiv.org/abs/2510.02669)

- **Key / type / family:** `2025-automaas`; preprint; `2025-automaas`. **Authors:** Ma, Bo, Li, Hang, Hu, ZeHua et al..
- **Dates / version:** first 2025-10-03; latest metadata 2025-10-03; read/inspected v1 metadata checked; full version not read. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** watchlist; rubric M / U / M / M / L. Potential architecture-search coverage but redundant and uninspected. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2510.02669).

<a id="2026-automated-design-embodied-agent-architectures"></a>

### [Automating the Design of Embodied Agent Architectures](https://arxiv.org/abs/2606.30111)

- **Key / type / family:** `2026-automated-design-embodied-agent-architectures`; preprint; `2026-automated-design-embodied-agent-architectures`. **Authors:** Zhou, Jian, Lin, Sihao, Li, Jin et al..
- **Dates / version:** first 2026-06-29; latest metadata 2026-07-03; read/inspected v2 metadata checked; full version not read. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** watchlist; rubric M / U / M / M / H. Fills an embodied-domain gap, but evidence was not inspected. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2606.30111).

<a id="2025-benchmark-self-evolving"></a>

### [Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation](https://aclanthology.org/2025.coling-main.223/)

- **Key / type / family:** `2025-benchmark-self-evolving`; COLING 2025 conference paper; `2025-benchmark-self-evolving`. **Authors:** Siyuan Wang; Zhuohan Long; Zhihao Fan; Xuanjing Huang; Zhongyu Wei.
- **Dates / version:** first 2025-01; latest metadata 2025-01; read/inspected published proceedings version. **Access:** 2026-09-16; official metadata and abstract only; provisional.
- **Selection:** watchlist; rubric M / U / M / M / M. Useful benchmark-side evolution contrast, but indirect to persistent agent improvement and not substantively read here. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: ACL Anthology open access; redistribution terms not checked. [Download/source location](https://aclanthology.org/2025.coling-main.223.pdf).

<a id="2025-cl-bench-arc"></a>

### [CL-Bench: Benchmark Framework for Evaluating LLM Agent Continual Learning in Stateful Environments](https://github.com/Arc-Computer/CL-Bench)

- **Key / type / family:** `2025-cl-bench-arc`; code repository; `2025-cl-bench-arc`. **Authors:** Arc Intelligence.
- **Dates / version:** first 2025; latest metadata 2025-11-14 repository update reported; read/inspected repository; commit not pinned. **Access:** 2026-09-16; repository README only; provisional.
- **Selection:** watchlist; rubric H / U / M / H / H. Production-like stateful CRM environment is relevant, but no paper-level protocol/results appraisal was available. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown for CL-Bench repository in this pass. Canonical page above is the inspected location.

<a id="2026-closedloop-ai-blog"></a>

### [ClosedLoop AI blog](https://closedloopai.co/blog/)

- **Key / type / family:** `2026-closedloop-ai-blog`; first-party blog index; `2026-closedloop-ai-blog`. **Authors:** ClosedLoop AI.
- **Dates / version:** first unknown; latest metadata None; read/inspected unknown. **Access:** 2026-09-16; index/marketing summaries only.
- **Selection:** watchlist; rubric M / U / U / L / L. Potentially relevant, but no substantive measured primary artifact was verified. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: Unknown. Canonical page above is the inspected location.

<a id="2025-collapse-or-thrive-synthetic-data"></a>

### [Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World](https://proceedings.mlr.press/v267/kazdan25a.html)

- **Key / type / family:** `2025-collapse-or-thrive-synthetic-data`; peer-reviewed conference paper; `2025-collapse-or-thrive-synthetic-data`. **Authors:** Emre Kazdan et al..
- **Dates / version:** first 2025; latest metadata 2025; read/inspected ICML 2025 / PMLR 267. **Access:** 2026-09-16; primary abstract and proceedings page.
- **Selection:** watchlist; rubric H / U / H / H / H. Three controlled workflow regimes may provide the cleanest teaching comparison, but full methods/results were not audited in this pass. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: PMLR proceedings; exact PDF license not recorded. [Download/source location](https://proceedings.mlr.press/v267/kazdan25a/kazdan25a.pdf).

<a id="2026-continual-learning-bench"></a>

### [Continual Learning Bench](https://snorkel.ai/blog/continual-learning-ai-agents-explained/)

- **Key / type / family:** `2026-continual-learning-bench`; first-party project article; `2026-continual-learning-bench`. **Authors:** Parth Asawa; Chris Glaze; Gabe Orlanski; Benji Xu; Ramya Ramakrishnan; Asim Biswal; collaborators at UC Berkeley SkyRL, Snorkel AI, and UW–Madison.
- **Dates / version:** first 2026-06-29; latest metadata 2026-06-29; read/inspected project article; benchmark 1.0 described. **Access:** 2026-09-16; first-party article read; benchmark artifacts/results not audited; provisional.
- **Selection:** watchlist; rubric H / U / M / H / H. Excellent stateful-versus-stateless gain control, but the article is not sufficient evidence for benchmark validity or performance claims. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2025-curll"></a>

### [CurLL: A Developmental Framework to Evaluate Continual Learning in Language Models](https://aclanthology.org/2025.babylm-main.20/)

- **Key / type / family:** `2025-curll`; workshop paper; `2025-curll`. **Authors:** Pavan Kalyan; Shubhra Mishra; Satya Lokam; Navin Goyal.
- **Dates / version:** first 2025-10-14; latest metadata 2025-10-14; read/inspected arXiv v1 / BabyLM 2025; relationship provisional. **Access:** 2026-09-16; abstract and ACL metadata.
- **Selection:** watchlist; rubric M / U / M / M / M. Potentially useful retention benchmark, but abstract-only and its 135M developmental setting is remote from deployed agents. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. [Download/source location](https://aclanthology.org/2025.babylm-main.20.pdf).

<a id="2026-darwinx"></a>

### [DarwinX: Evolving Agent Harnesses Through Natural Selection](https://arxiv.org/abs/2608.07545)

- **Key / type / family:** `2026-darwinx`; preprint and companion Beagle code; `2026-darwinx`. **Authors:** Zhang, Yifan, Dai, Yutong, Tan, Juntao et al..
- **Dates / version:** first 2026-07-31; latest metadata 2026-07-31; read/inspected v1 metadata checked; full version not read. **Access:** 2026-09-16; provisional primary abstract and first-party repository/project screen.
- **Selection:** watchlist; rubric H / U / H / H / H. Direct regression-aware harness evolution across four benchmarks; full text must be audited before numeric claims are used. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2608.07545).

<a id="2026-diving-reliable-self-evolving-agents"></a>

### [Diving into Reliable Self-Evolving Agents: A Survey](https://www.preprints.org/manuscript/202609.0913)

- **Key / type / family:** `2026-diving-reliable-self-evolving-agents`; preprint survey; `2026-diving-reliable-self-evolving-agents`. **Authors:** Kaiqi Wang; Wenjin Hou; Yuchen Yan; Hongrui Jia; Zhisheng Zhong; Botao Ren; Yifei Chen; Songyang Zhang; Yongliang Shen; Jun Xiao; Yi Yang; Yueting Zhuang; Hehe Fan.
- **Dates / version:** first 2026-09-11; latest metadata 2026-09-11; read/inspected v1 preprint. **Access:** 2026-09-16; project page and abstract only; provisional.
- **Selection:** watchlist; rubric M / U / M / H / M. Useful orientation and citation map, but not independent primary evidence for benchmark findings. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. [Download/source location](https://www.preprints.org/manuscript/202609.0913/download/final_file).

<a id="2026-escaping-model-collapse-verification"></a>

### [Escaping Model Collapse via Synthetic Data Verification](https://proceedings.iclr.cc/paper_files/paper/2026/hash/29806b2e4dcb35e42abed21d43e2b7d8-Abstract-Conference.html)

- **Key / type / family:** `2026-escaping-model-collapse-verification`; peer-reviewed conference paper; `2026-escaping-model-collapse-verification`. **Authors:** unknown.
- **Dates / version:** first 2026; latest metadata 2026; read/inspected ICLR 2026; exact version unknown. **Access:** 2026-09-16; conference abstract only.
- **Selection:** watchlist; rubric H / U / H / H / H. Highly relevant verification countermeasure, but evidence remains unknown without methods/results inspection. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2025-memoryagentbench"></a>

### [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257)

- **Key / type / family:** `2025-memoryagentbench`; peer-reviewed conference paper; `2025-memoryagentbench`. **Authors:** Hu, Yuanzhe, Wang, Yu, McAuley, Julian.
- **Dates / version:** first 2025-07-07; latest metadata 2026-06-28; read/inspected v4. **Access:** 2026-09-16; abstract/metadata only in this run.
- **Selection:** watchlist; rubric H / U / H / H / H. Important benchmark foundation; implementation of selective forgetting still needs inspection. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2507.05257v4).

<a id="2025-evaluating-the-evaluator"></a>

### [Evaluating the Evaluator: Measuring LLMs' Adherence to Task Evaluation Instructions](https://doi.org/10.1609/aaai.v39i18.34157)

- **Key / type / family:** `2025-evaluating-the-evaluator`; AAAI 2025 conference paper; `2025-evaluating-the-evaluator`. **Authors:** Bhuvanashree Murugadoss; Christian Poelitz; Ian Drosos; Vu Le; Nick McKenna; Carina Suzana Negreanu; Chris Parnin; Advait Sarkar.
- **Dates / version:** first 2025-04-11; latest metadata 2025-04-11; read/inspected AAAI proceedings version. **Access:** 2026-09-16; official metadata and abstract only; provisional.
- **Selection:** watchlist; rubric M / U / M / M / M. Relevant caution for optimization against rubric judges, but not a direct self-evolution experiment. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. [Download/source location](https://ojs.aaai.org/index.php/AAAI/article/download/34157/36312).

<a id="2026-evermemos"></a>

### [EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning](https://arxiv.org/abs/2601.02163)

- **Key / type / family:** `2026-evermemos`; preprint; `2026-evermemos`. **Authors:** Hu, Chuanrui, Gao, Xingze, Zhou, Zuyi et al..
- **Dates / version:** first 2026-01-05; latest metadata 2026-01-09; read/inspected v1. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric M / U / M / M / L. Provisional; needs component ablation and judge audit. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2601.02163v1).

<a id="2025-evoflow"></a>

### [EvoFlow: Evolving Diverse Agentic Workflows On The Fly](https://arxiv.org/abs/2502.07373)

- **Key / type / family:** `2025-evoflow`; preprint; `2025-evoflow`. **Authors:** Zhang, Guibin, Chen, Kaijie, Wan, Guancheng et al..
- **Dates / version:** first 2025-02-11; latest metadata 2025-02-11; read/inspected v1 metadata checked; full version not read. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** watchlist; rubric M / U / M / M / M. Promising diversity and cost comparator; effect claims require full-text audit. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2502.07373).

<a id="2022-fine-tuned-language-models-continual-learners"></a>

### [Fine-tuned Language Models are Continual Learners](https://arxiv.org/abs/2205.12393)

- **Key / type / family:** `2022-fine-tuned-language-models-continual-learners`; preprint; `2022-fine-tuned-language-models-continual-learners`. **Authors:** Scialom, Thomas, Chakrabarty, Tuhin, Muresan, Smaranda.
- **Dates / version:** first 2022-05-24; latest metadata 2022-10-29; read/inspected arXiv v4. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric M / U / M / H / M. Important counterweight to universal forgetting claims, but the reported sub-2% forgetting needs a full setting audit. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2205.12393v4).

<a id="2026-flashevolve"></a>

### [FlashEvolve: Accelerating Agent Self-Evolution with Asynchronous Stage Orchestration](https://arxiv.org/abs/2605.08520)

- **Key / type / family:** `2026-flashevolve`; preprint and code; `2026-flashevolve`. **Authors:** Hu, Zhengding, Lu, Mingge, Wang, Zhen et al..
- **Dates / version:** first 2026-05-08; latest metadata 2026-05-08; read/inspected v1 metadata checked; full version not read. **Access:** 2026-09-16; provisional primary abstract and project/repository screen.
- **Selection:** watchlist; rubric M / U / H / H / H. Fills wall-clock efficiency gap; 3.5x/4.9x throughput claims require full-text audit and do not establish better final artifacts alone. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2605.08520).

<a id="2026-generalized-agent-iteration"></a>

### [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406)

- **Key / type / family:** `2026-generalized-agent-iteration`; formal/conceptual preprint; `2026-generalized-agent-iteration`. **Authors:** Tang, Hongyao, Ma, Yi, Li, Pengyi et al..
- **Dates / version:** first 2026-09-11; latest metadata 2026-09-11; read/inspected v1. **Access:** 2026-09-16; Primary abstract and metadata only..
- **Selection:** watchlist; rubric H / U / M / H / H. High teaching value for classifying mechanisms, but it is not empirical evidence that iterative improvement works. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by-nc-nd/4.0/. [Download/source location](https://arxiv.org/pdf/2609.13406v1).

<a id="2003-goedel-machines"></a>

### [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](https://arxiv.org/abs/cs/0309048v5)

- **Key / type / family:** `2003-goedel-machines`; technical report and theoretical preprint; `2003-goedel-machines`. **Authors:** Jürgen Schmidhuber.
- **Dates / version:** first 2003-09-25; revision 2006-12-17; read v5. **Access:** 2026-09-16; primary §§2.2/3.2/4.1–4.4 proof criterion and qualifications read; selected citation contexts checked.
- **Selection:** reviewed-reserve. Formal proof-gated foundation clarifies which guarantee empirical DGM does not inherit. **Notes:** [reading record](notes/2003-goedel-machines.md).
- **Originals:** retention-restricted; temporary versioned PDF inspected. License/permission: arXiv assumed non-exclusive distribution license.

<a id="2026-hyperstruck-learning-failures"></a>

### [Hyperstruck experience and failure blog series](https://hyperstruck.com/blog/)

- **Key / type / family:** `2026-hyperstruck-learning-failures`; first-party engineering blog series; `2026-hyperstruck-learning-failures`. **Authors:** Hyperstruck.
- **Dates / version:** first 2026-05-15; latest metadata 2026-09-10; read/inspected blog index through cutoff. **Access:** 2026-09-16; index, dates, titles, and summaries inspected; individual claims not fully audited.
- **Selection:** watchlist; rubric H / U / M / M / H. High-value failure taxonomy, but evidence strength is unknown until individual posts and artifacts are inspected. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: All rights reserved. Canonical page above is the inspected location.

<a id="2026-in-place-ttt"></a>

### [In-Place Test-Time Training](https://arxiv.org/abs/2604.06169)

- **Key / type / family:** `2026-in-place-ttt`; peer-reviewed paper/preprint; arXiv reports ICLR 2026 Oral; `2026-in-place-ttt`. **Authors:** Feng, Guhao, Luo, Shengjie, Hua, Kai et al..
- **Dates / version:** first 2026-04-07; latest metadata 2026-04-07; read/inspected v1. **Access:** 2026-09-16; Primary abstract and metadata only..
- **Selection:** watchlist; rubric M / U / H / H / M. Genuine weight adaptation and useful boundary case, but not an autonomous agent or self-chosen improvement loop. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2604.06169v1).

<a id="2025-judgebench"></a>

### [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)

- **Key / type / family:** `2025-judgebench`; ICLR 2025 conference paper; `2025-judgebench`. **Authors:** Sijun Tan; Siyuan Zhuang; Kyle Montgomery; William Yuan Tang; Alejandro Cuadron; Chenguang Wang; Raluca Ada Popa; Ion Stoica.
- **Dates / version:** first 2024-10; latest metadata 2025 conference version; read/inspected ICLR 2025. **Access:** 2026-09-16; official primary abstract only; provisional.
- **Selection:** watchlist; rubric M / U / M / H / M. Strong general reason to calibrate judges independently; indirect to longitudinal self-evolution and not fully appraised here. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. [Download/source location](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf).

<a id="2025-justice-or-prejudice-calm"></a>

### [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/hash/fdca08d371e4b6c031397909e20043bd-Abstract-Conference.html)

- **Key / type / family:** `2025-justice-or-prejudice-calm`; ICLR 2025 conference paper; `2025-justice-or-prejudice-calm`. **Authors:** Jiayi Ye; Yanbo Wang; Yue Huang; Dongping Chen; Qihui Zhang; Nuno Moniz; Tian Gao; Werner Geyer; Chao Huang; Pin-Yu Chen; Nitesh V. Chawla; Xiangliang Zhang.
- **Dates / version:** first 2024-10-03; latest metadata 2025 conference version; read/inspected ICLR 2025. **Access:** 2026-09-16; official abstract only; provisional.
- **Selection:** watchlist; rubric M / U / M / H / M. Useful audit taxonomy for judges that feed adaptation, but no direct evidence that a screened self-evolution benchmark exhibits these biases. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. [Download/source location](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdca08d371e4b6c031397909e20043bd-Paper-Conference.pdf).

<a id="2025-lifelong-learning-large-language-models-survey"></a>

### [Lifelong Learning of Large Language Models: A Survey](https://doi.org/10.1145/3716629)

- **Key / type / family:** `2025-lifelong-learning-large-language-models-survey`; peer-reviewed survey; `2025-lifelong-learning-large-language-models-survey`. **Authors:** Wang et al..
- **Dates / version:** first 2025; latest metadata 2025; read/inspected ACM Computing Surveys publication. **Access:** 2026-09-16; metadata and abstract.
- **Selection:** watchlist; rubric M / U / L / M / M. Useful taxonomy but not primary empirical evidence and redundant with direct studies for claims. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2026-muse-autoskill"></a>

### [MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation](https://arxiv.org/abs/2605.27366)

- **Key / type / family:** `2026-muse-autoskill`; preprint; `2026-muse-autoskill`. **Authors:** Lin, Huawei, Li, Peng, Song, Jie et al..
- **Dates / version:** first 2026-05-26; latest metadata 2026-07-03; read/inspected v1. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric H / U / M / M / L. Provisional metadata-only; full text needed and overlaps selected skill systems. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2605.27366v1).

<a id="2025-mem-alpha"></a>

### [Mem-{\alpha}: Learning Memory Construction via Reinforcement Learning](https://arxiv.org/abs/2509.25911)

- **Key / type / family:** `2025-mem-alpha`; preprint; `2025-mem-alpha`. **Authors:** Wang, Yu, Takanobu, Ryuichi, Liang, Zhiqi et al..
- **Dates / version:** first 2025-09-30; latest metadata 2025-09-30; read/inspected v1. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric H / U / H / M / M. Provisional; train/evaluation overlap and 30K-to-400K extrapolation need audit. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2509.25911v1).

<a id="2026-mem2actbench"></a>

### [Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents](https://arxiv.org/abs/2601.19935)

- **Key / type / family:** `2026-mem2actbench`; preprint; `2026-mem2actbench`. **Authors:** Shen, Yiting, Li, Kun, Zhou, Wei et al..
- **Dates / version:** first 2026-01-13; latest metadata 2026-01-13; read/inspected v1. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric H / U / H / H / H. Provisional; synthetic reverse-generation and human/judge protocol need audit. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2601.19935v1).

<a id="2025-memory-r1"></a>

### [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)

- **Key / type / family:** `2025-memory-r1`; preprint; `2025-memory-r1`. **Authors:** Yan, Sikuan, Yang, Xiufeng, Huang, Zuchao et al..
- **Dates / version:** first 2025-08-27; latest metadata 2026-01-14; read/inspected v1. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric H / U / M / M / M. Provisional; small-data, reward, judge, and split claims require full audit. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2508.19828v1).

<a id="2025-multi-agent-architecture-search"></a>

### [Multi-agent Architecture Search via Agentic Supernet](https://arxiv.org/abs/2502.04180)

- **Key / type / family:** `2025-multi-agent-architecture-search`; preprint; `2025-multi-agent-architecture-search`. **Authors:** Zhang, Guibin, Niu, Luyang, Fang, Junfeng et al..
- **Dates / version:** first 2025-02-06; latest metadata 2025-06-09; read/inspected v2 metadata checked; full version not read. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** watchlist; rubric M / U / M / M / M. Dynamic resource allocation and transfer are useful comparators; full text not inspected. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2502.04180).

<a id="2026-agentic-rl-systems"></a>

### [Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents](https://arxiv.org/abs/2607.01120)

- **Key / type / family:** `2026-agentic-rl-systems`; position and systems architecture preprint; `2026-agentic-rl-systems`. **Authors:** Yan, Ran, Fu, Wei, Li, Jiale et al..
- **Dates / version:** first 2026-07-01; latest metadata 2026-07-02; read/inspected v2. **Access:** 2026-09-16; Primary abstract and metadata only..
- **Selection:** watchlist; rubric H / U / M / M / M. Useful production architecture; inspected material does not establish a comparative self-evolution effect. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2607.01120v2).

<a id="2026-pilot-in-the-loop"></a>

### [PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents](https://arxiv.org/abs/2608.26530)

- **Key / type / family:** `2026-pilot-in-the-loop`; preprint; `2026-pilot-in-the-loop`. **Authors:** Xiao, Yang, Sun, Yusong, Wu, Haoyi et al..
- **Dates / version:** first 2026-08-27; latest metadata 2026-08-27; read/inspected v1. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric H / U / H / H / M. Provisional; frozen splits and all-call supervisor overhead need audit. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2608.26530v1).

<a id="2025-paperbench"></a>

### [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848)

- **Key / type / family:** `2025-paperbench`; arXiv preprint and code benchmark; `2025-paperbench`. **Authors:** Starace, Giulio, Jaffe, Oliver, Sherburn, Dane et al..
- **Dates / version:** first 2025-04-02; latest metadata 2025-04-07; read/inspected v3 metadata checked; full version not read. **Access:** 2026-09-16; primary abstract and first-party repository page read; provisional for methods.
- **Selection:** watchlist; rubric M / U / M / H / M. Strong adjacent reality check for research-agent capability, but not an evaluation of retained cross-task evolution. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2504.01848).

<a id="2026-recuris"></a>

### [Recuris: Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses](https://github.com/Gen-Verse/Recuris)

- **Key / type / family:** `2026-recuris`; code/practitioner artifact; `2026-recuris`. **Authors:** Gen-Verse.
- **Dates / version:** first 2026-08 (day unverified); latest metadata None; read/inspected unknown. **Access:** 2026-09-16; README only.
- **Selection:** watchlist; rubric H / L / M / M / M. Provisional; paper metadata, protocol, version, and license unresolved. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: Unknown/unverified for retention. Canonical page above is the inspected location.

<a id="2024-recursive-introspection"></a>

### [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://arxiv.org/abs/2407.18219)

- **Key / type / family:** `2024-recursive-introspection`; peer-reviewed conference paper; `2024-recursive-introspection`. **Authors:** Qu, Yuxiao, Zhang, Tianjun, Garg, Naman et al..
- **Dates / version:** first 2024-07-25; latest metadata 2024-07-26; read/inspected arXiv v2; NeurIPS 2024. **Access:** 2026-09-16; methods and abstract inspected; results not freshly audited.
- **Selection:** watchlist; rubric M / U / M / H / M. Close weight-trained alternative for multi-turn error correction, but less directly about persistent autonomous update generation than SEAL. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://papers.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf).

<a id="2026-inverter-rsi"></a>

### [Recursive Self-Improvement LLM Agents for Inverter Dynamic Model Identification](https://arxiv.org/abs/2609.14260)

- **Key / type / family:** `2026-inverter-rsi`; position paper and empirical proof of concept; `2026-inverter-rsi`. **Authors:** Feng, Jie, Wang, Xiaoyang, Chen, Xin et al..
- **Dates / version:** first 2026-09-13; latest metadata 2026-09-13; read/inspected v1. **Access:** 2026-09-16; Primary abstract and metadata only..
- **Selection:** watchlist; rubric M / U / M / M / L. Distinct domain application but only one unaudited proof-of-concept result and limited contribution to the central evaluation argument. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by-nc-nd/4.0/. [Download/source location](https://arxiv.org/pdf/2609.14260v1).

<a id="2025-reinforcement-fine-tuning-forgetting"></a>

### [Reinforcement Fine-Tuning Naturally Mitigates Forgetting in Continual Post-Training](https://arxiv.org/abs/2507.05386)

- **Key / type / family:** `2025-reinforcement-fine-tuning-forgetting`; preprint; `2025-reinforcement-fine-tuning-forgetting`. **Authors:** Lai, Song, Zhao, Haohan, Feng, Rong et al..
- **Dates / version:** first 2025-07-07; latest metadata 2026-06-29; read/inspected arXiv v6. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric H / U / H / H / H. Directly addresses whether RL retains prior abilities better than SFT, but current v6 results were not fully inspected. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2507.05386v6).

<a id="2026-reward-hacking-ai-safety-gridworlds"></a>

### [Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds](https://arxiv.org/abs/2606.15385)

- **Key / type / family:** `2026-reward-hacking-ai-safety-gridworlds`; arXiv preprint and code; `2026-reward-hacking-ai-safety-gridworlds`. **Authors:** Çağatan, Ömer Veysel, Zhao, Xuandong.
- **Dates / version:** first 2026-06-13; latest metadata 2026-06-13; read/inspected v1 metadata checked; full version not read. **Access:** 2026-09-16; primary abstract and repository link only; provisional.
- **Selection:** watchlist; rubric H / U / H / H / M. Clean observed-versus-hidden reward mechanism, but methods, seeds, and mitigation experiments require full reading. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2606.15385).

<a id="2025-scale-continual-learning"></a>

### [SCALE: Upscaled Continual Learning of Large Language Models](https://arxiv.org/abs/2511.03270)

- **Key / type / family:** `2025-scale-continual-learning`; preprint; `2025-scale-continual-learning`. **Authors:** Lee, Jin-woo, Choi, Junhwa, Hwang, Bongkyu et al..
- **Dates / version:** first 2025-11-05; latest metadata 2025-12-11; read/inspected arXiv v2. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric M / U / M / M / M. Potential retention mechanism, but abstract-only and tested in a controlled biography setting. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2511.03270v2).

<a id="2026-seagym"></a>

### [SEAGym: An Evaluation Environment for Self-Evolving LLM Agents](https://openreview.net/forum?id=hLHB7NCuke)

- **Key / type / family:** `2026-seagym`; anonymous OpenReview submission; `2026-seagym`. **Authors:** anonymous ACL submission.
- **Dates / version:** first 2026; latest metadata unknown; read/inspected anonymous submission version. **Access:** 2026-09-16; primary abstract only; provisional.
- **Selection:** watchlist; rubric H / U / H / H / H. Direct train/validation/test/replay/cost design is promising, but anonymous status and unreviewed methods/results make it provisional. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. [Download/source location](https://openreview.net/pdf?id=hLHB7NCuke).

<a id="2026-self-evolving-coding-agents"></a>

### [Self-Evolving Coding Agents](https://arxiv.org/abs/2608.03392)

- **Key / type / family:** `2026-self-evolving-coding-agents`; survey preprint; `2026-self-evolving-coding-agents`. **Authors:** Zhou, Hao, Hu, Haichuan, Luo, Tianyu et al..
- **Dates / version:** first 2026-08-04; latest metadata 2026-08-29; read/inspected v3. **Access:** 2026-09-16; Primary arXiv metadata and abstract only in the audit; companion collection and cited studies not audited..
- **Selection:** watchlist; rubric H / U / H / H / H. Best coding-specific map and discovery index, but not independent empirical support. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2608.03392v3).

<a id="2025-self-evolving-llms-continual-instruction-tuning"></a>

### [Self-Evolving LLMs via Continual Instruction Tuning](https://arxiv.org/abs/2509.18133)

- **Key / type / family:** `2025-self-evolving-llms-continual-instruction-tuning`; preprint; `2025-self-evolving-llms-continual-instruction-tuning`. **Authors:** Kang, Jiazheng, Huang, Le, Hou, Cheng et al..
- **Dates / version:** first 2025-09-14; latest metadata 2025-10-15; read/inspected arXiv v4. **Access:** 2026-09-16; abstract only.
- **Selection:** watchlist; rubric M / U / M / M / M. Direct alternative for retention/generalization, but no primary results were audited. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2509.18133v4).

<a id="2023-self-refine"></a>

### [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)

- **Key / type / family:** `2023-self-refine`; peer-reviewed conference paper; `2023-self-refine`. **Authors:** Madaan, Aman, Tandon, Niket, Gupta, Prakhar et al..
- **Dates / version:** first 2023-03-30; latest metadata 2023-05-25; read/inspected arXiv v2; NeurIPS 2023. **Access:** 2026-09-16; abstract and prior paper excerpts.
- **Selection:** watchlist; rubric M / U / M / H / M. Clear frozen-weight comparator across tasks; detailed result audit is inherited rather than completed here. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2303.17651v2).

<a id="2025-self-training-multilingual-reasoning"></a>

### [Self-Training for Multilingual Reasoning](https://aclanthology.org/2025.naacl-long.577/)

- **Key / type / family:** `2025-self-training-multilingual-reasoning`; peer-reviewed conference paper; `2025-self-training-multilingual-reasoning`. **Authors:** unknown.
- **Dates / version:** first 2025; latest metadata 2025; read/inspected NAACL 2025. **Access:** 2026-09-16; ACL metadata only.
- **Selection:** watchlist; rubric M / U / M / M / M. Relevant pseudo-label dependence but task-specific and not audited beyond metadata. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. [Download/source location](https://aclanthology.org/2025.naacl-long.577.pdf).

<a id="2026-slopcodebench"></a>

### [SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks](https://arxiv.org/abs/2603.24755)

- **Key / type / family:** `2026-slopcodebench`; benchmark preprint; `2026-slopcodebench`. **Authors:** Orlanski, Gabriel, Roy, Devjeet, Yun, Alexander et al..
- **Dates / version:** first 2026-03-25; latest metadata 2026-05-07; read/inspected v2 metadata checked; full version not read. **Access:** 2026-09-16; provisional primary abstract screen; secondary quantitative claims rejected pending full text.
- **Selection:** watchlist; rubric M / U / H / H / H. High-value counterbenchmark with 20 problems/93 checkpoints; read before using degradation percentages. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2603.24755).

<a id="2026-last-ai-built-by-humans"></a>

### [The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement](https://arxiv.org/abs/2609.11873)

- **Key / type / family:** `2026-last-ai-built-by-humans`; roadmap/conceptual preprint; `2026-last-ai-built-by-humans`. **Authors:** Duan, Yi, Liu, Ying, Tang, Zirui et al..
- **Dates / version:** first 2026-09-10; latest metadata 2026-09-15; read/inspected v2. **Access:** 2026-09-16; Primary arXiv metadata and abstract only in the audit..
- **Selection:** watchlist; rubric H / U / M / H / M. Consequential September framing, but preliminary-evidence language is unsupported by an inspected reproducible experiment. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by-nc-nd/4.0/. [Download/source location](https://arxiv.org/pdf/2609.11873v2).

<a id="2024-tic-lm"></a>

### [TiC-LM: Web-Scale Time-Continual Pretraining](https://pr-mlr-shield-prod.apple.com/research/tic-lm-web-scale)

- **Key / type / family:** `2024-tic-lm`; workshop paper / first-party research page; `2024-tic-lm`. **Authors:** Apple Machine Learning Research; authors provisional.
- **Dates / version:** first 2024; latest metadata unknown; read/inspected unknown. **Access:** 2026-09-16; official abstract-level page.
- **Selection:** watchlist; rubric M / U / M / M / M. Adds realistic temporal pretraining and replay tradeoffs, but exact results and bibliographic metadata remain provisional. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2025-unbiased-evaluation-causal-perspective"></a>

### [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://proceedings.mlr.press/v267/chen25bi.html)

- **Key / type / family:** `2025-unbiased-evaluation-causal-perspective`; ICML 2025 conference paper; `2025-unbiased-evaluation-causal-perspective`. **Authors:** Meilin Chen; Jian Tian; Liang Ma; Di Xie; Weijie Chen; Jiang Zhu.
- **Dates / version:** first 2025-07-13; latest metadata 2025-07-13; read/inspected PMLR 267. **Access:** 2026-09-16; official metadata and abstract only; provisional.
- **Selection:** watchlist; rubric M / U / M / M / M. Potential formal vocabulary for evaluator bias, but indirect to self-evolving agents and not fully appraised. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: PMLR open access; specific license not checked. [Download/source location](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf).

## Related communication artifacts

<a id="2025-azr-author-project"></a>

### [Absolute Zero Reasoner (AZR)](https://tongagents.mybigai.ac.cn/en/index/azr/)

- **Key / type / family:** `2025-azr-author-project`; first-party project page; `2025-absolute-zero`. **Authors:** TongAgents / author project page.
- **Dates / version:** first 2025; latest metadata 2025; read/inspected live page inspected 2026-09-16. **Access:** 2026-09-16; page read; no video/transcript.
- **Selection:** companion; rubric M / U / L / M / L. Navigation/communication companion to the primary paper; not independent empirical evidence. **Notes:** [reading record](workers/talks-social-audit.md).
- **Original:** not retained: public original inspected; no redistribution license verified for page, or only metadata/theoretical background reviewed. License/permission: not verified. Canonical page above is the inspected location.

<a id="2026-hyperagents-official-project"></a>

### [HyperAgents project site](https://hyperagents.agency/)

- **Key / type / family:** `2026-hyperagents-official-project`; first-party project/demo site; `hyperagents`. **Authors:** HyperAgents / Meta research project.
- **Dates / version:** first 2026; latest metadata 2026; read/inspected live page inspected 2026-09-16. **Access:** 2026-09-16; page read; no video/transcript.
- **Selection:** companion; rubric M / U / L / M / L. Navigation/communication companion to the primary paper; not independent empirical evidence. **Notes:** [reading record](workers/talks-social-audit.md).
- **Original:** not retained: public original inspected; no redistribution license verified for page, or only metadata/theoretical background reviewed. License/permission: not verified. Canonical page above is the inspected location.

<a id="2025-seal-lab-news"></a>

### [Teaching large language models how to absorb new knowledge](https://www.csail.mit.edu/news/teaching-large-language-models-how-absorb-new-knowledge)

- **Key / type / family:** `2025-seal-lab-news`; official institutional news; `2025-self-adapting-language-models`. **Authors:** MIT CSAIL.
- **Dates / version:** first 2025; latest metadata 2025; read/inspected live page inspected 2026-09-16. **Access:** 2026-09-16; page read.
- **Selection:** companion; rubric M / U / L / M / L. Navigation/communication companion to the primary paper; not independent empirical evidence. **Notes:** [reading record](workers/talks-social-audit.md).
- **Original:** not retained: public original inspected; no redistribution license verified for page, or only metadata/theoretical background reviewed. License/permission: not verified. Canonical page above is the inspected location.

## Excluded or unverified leads

<a id="2024-autoflow"></a>

### [AutoFlow: Automated Workflow Generation for Large Language Model Agents](https://arxiv.org/abs/2407.12821)

- **Key / type / family:** `2024-autoflow`; preprint and code; `2024-autoflow`. **Authors:** Li, Zelong, Xu, Shuyuan, Mei, Kai et al..
- **Dates / version:** first 2024-07-01; latest metadata 2024-07-01; read/inspected v1 metadata checked; full version not read. **Access:** 2026-09-16; provisional metadata/abstract only.
- **Selection:** excluded; rubric M / U / M / M / L. Retain as predecessor; inspected AFlow supplies a stronger representative for the same coverage role. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. [Download/source location](https://arxiv.org/pdf/2407.12821).

<a id="2026-storage-to-experience-survey"></a>

### [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://github.com/FeishuLuo/Evolving-LLM-Agent-Memory-Survey)

- **Key / type / family:** `2026-storage-to-experience-survey`; survey/repository; `2026-storage-to-experience-survey`. **Authors:** Feishu Luo et al..
- **Dates / version:** first unknown (2026 survey/repository label); latest metadata None; read/inspected unknown. **Access:** 2026-09-16; README/index only.
- **Selection:** excluded; rubric M / L / M / M / M. Secondary discovery index, not primary evidence. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: Unknown/unverified for retention. Canonical page above is the inspected location.

<a id="2026-continual-deployed-rl"></a>

### [Position: Deployed Reinforcement Learning should be Continual](https://arxiv.org/abs/2606.04029)

- **Key / type / family:** `2026-continual-deployed-rl`; ICML 2026 position paper; `2026-continual-deployed-rl`. **Authors:** Behdin, Parnian, Roice, Kevin, Mesbahi, Golnaz.
- **Dates / version:** first 2026-06-01; latest metadata 2026-06-06; read/inspected v2. **Access:** 2026-09-16; Primary abstract and metadata only..
- **Selection:** excluded; rubric M / U / L / M / M. Helpful deployment motivation but redundant with stronger empirical drift/evaluation coverage and supplies no new effect estimate in inspected material. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: http://creativecommons.org/licenses/by/4.0/. [Download/source location](https://arxiv.org/pdf/2606.04029v2).

<a id="2025-seal-community-arc-claims"></a>

### SEAL ARC community and public performance claims (source location unverified)

- **Key / type / family:** `2025-seal-community-arc-claims`; secondary reports; `2025-seal-community-arc-claims`. **Authors:** unknown secondary sources.
- **Dates / version:** first 2025; latest metadata unknown; read/inspected unknown. **Access:** 2026-09-16; discovery mentions only.
- **Selection:** excluded; rubric L / L / L / L / L. Unverified secondary claims; duplicate SEAL family, not independent evidence. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: unknown. Canonical page above is the inspected location.

<a id="2025-seal-author-talk"></a>

### [Self-Adapting Language Models — unverified video lead](https://www.youtube.com/watch?v=XEb0iDkpy5M)

- **Key / type / family:** `2025-seal-author-talk`; YouTube video; `2025-self-adapting-language-models`. **Authors:** Statistical Machine Learning channel; description lists Adam Zweiger, Jyothish Pari, Han Guo, Ekin Akyürek, Yoon Kim, Pulkit Agrawal.
- **Dates / version:** first 2025-06-15; latest metadata 2025-06-15; read/inspected live page inspected 2026-09-16. **Access:** 2026-09-16; video unseen; description read.
- **Selection:** excluded; rubric M / U / L / M / L. Video unseen; channel/speaker authorship not established. Description naming paper authors is not proof this is an author talk. **Notes:** [reading record](workers/talks-social-audit.md).
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: not verified. Canonical page above is the inspected location.

<a id="2026-self-improving-agent-survey-resources"></a>

### [Self-Improvements in Modern Agentic Systems survey and Awesome list](https://github.com/selfimproving-agent/Awesome-Self-Improving-Agents/tree/99ce3979185536c1efb57b5c6935244b56f1dfec)

- **Key / type / family:** `2026-self-improving-agent-survey-resources`; secondary survey and curated list; `2026-self-improving-agent-survey-resources`. **Authors:** Survey authors and selfimproving-agent maintainers.
- **Dates / version:** first 2026-07-14; latest metadata 2026-09-11; read/inspected list commit 99ce3979185536c1efb57b5c6935244b56f1dfec. **Access:** 2026-09-16; repository README inspected; used for discovery only.
- **Selection:** excluded; rubric H / M / L / M / L. Useful discovery map but secondary, redundant with academic lanes, and not practitioner evidence for listed systems. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: MIT for repository; paper terms not checked. [Download/source location](https://arxiv.org/pdf/2607.13104).

<a id="2026-zeltrex-living-agent"></a>

### [The Living Agent: Production Evolutionary Self-Improvement in Autonomous AI Systems](https://zeltrex.com/papers/the-living-agent-2026.pdf)

- **Key / type / family:** `2026-zeltrex-living-agent`; first-party technical report; `2026-zeltrex-living-agent`. **Authors:** Vasyl Golubenko; TOV ZELTREX.
- **Dates / version:** first 2026-03; latest metadata 2026-03; read/inspected March 2026 PDF. **Access:** 2026-09-16; full-text relevant sections read.
- **Selection:** excluded; rubric H / L / H / M / M. Broadly relevant but self-scored, unauditable, and internally inconsistent on score totals and dimensions; several claimed components remain future or untrained. **Notes:** no standalone substantive note.
- **Original:** not acquired: screening/navigation lead; not needed for selected evidence. License/permission: No redistribution license verified. [Download/source location](https://zeltrex.com/papers/the-living-agent-2026.pdf).

## Citation-mining additions — September 16, 2026

These newly discovered older works supplement the existing ten. Five received substantive primary-source screening; the other records remain explicitly limited. [Pass summary](citation-mining.md).

<a id="2026-evox"></a>

### [EvoX: Meta-Evolution for Automated Discovery](https://arxiv.org/abs/2602.23413v2)

- **Key / family / type:** `2026-evox` / `2026-evox`; arXiv preprint record; venue not independently checked. **Authors:** Liu, Shu, Agarwal, Shubham, Maheswaran, Monishwaran et al.
- **Dates / access:** first 2026-02-26; latest 2026-03-16 (v2); accessed September 16. primary methods/results and relevant appendices inspected.
- **Decision:** reviewed-reserve; rubric H / M / H / H / M. Search-strategy evolution comparator to Dream-RSI; broad tasks, partial resource matching. [Discovery provenance](workers/citation-mining-meta.md). [Reading note](notes/2026-evox.md).
- **Original:** [saved v2](originals/2026-evox/2026-evox-paper-v2.pdf); [download](https://arxiv.org/pdf/2602.23413v2); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-mlevolve"></a>

### [MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473v1)

- **Key / family / type:** `2026-mlevolve` / `2026-mlevolve`; arXiv preprint record; venue not independently checked. **Authors:** Du, Shangheng, Yan, Xiangchao, Shi, Jinxin et al.
- **Dates / access:** first 2026-06-04; latest 2026-06-04 (v1); accessed September 16. primary methods/results and relevant appendices inspected.
- **Decision:** reviewed-reserve; rubric H / M / H / H / M. Cross-branch memory and adaptive ML engineering; heterogeneous baseline models/budgets. [Discovery provenance](workers/citation-mining-meta.md). [Reading note](notes/2026-mlevolve.md).
- **Original:** retention-restricted — Canonical arXiv license permits arXiv distribution, not general redistribution; no original retained.; [download](https://arxiv.org/pdf/2606.06473v1); [license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/).

<a id="2026-skillopt"></a>

### [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904v2)

- **Key / family / type:** `2026-skillopt` / `2026-skillopt`; arXiv preprint record; venue not independently checked. **Authors:** Yang, Yifan, Gong, Ziyang, Huang, Weiquan et al.
- **Dates / access:** first 2026-05-22; latest 2026-05-25 (v2); accessed September 16. primary methods/results and relevant appendices inspected.
- **Decision:** reviewed-reserve; rubric H / M / H / H / M. Direct WikiSkill baseline and SHAPER predecessor; bounded skill edits with selection gates. [Discovery provenance](workers/citation-mining-memory.md). [Reading note](notes/2026-skillopt.md).
- **Original:** retention-restricted — Canonical arXiv license permits arXiv distribution, not general redistribution; no original retained.; [download](https://arxiv.org/pdf/2605.23904v2); [license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/).

<a id="2026-evoskill"></a>

### [EvoSkill: Automated Skill Discovery for Multi-Agent Systems](https://arxiv.org/abs/2603.02766v1)

- **Key / family / type:** `2026-evoskill` / `2026-evoskill`; arXiv preprint record; venue not independently checked. **Authors:** Alzubi, Salaheddin, Provenzano, Noah, Bingham, Jaydon et al.
- **Dates / access:** first 2026-03-03; latest 2026-03-03 (v1); accessed September 16. primary methods/results and relevant appendices inspected.
- **Decision:** reviewed-reserve; rubric H / M / H / H / M. Direct WikiSkill baseline; single-run results and table/prose discrepancy. [Discovery provenance](workers/citation-mining-memory.md). [Reading note](notes/2026-evoskill.md).
- **Original:** [saved v1](originals/2026-evoskill/2026-evoskill-paper-v1.pdf); [download](https://arxiv.org/pdf/2603.02766v1); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-trace2skill"></a>

### [Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills](https://arxiv.org/abs/2603.25158v5)

- **Key / family / type:** `2026-trace2skill` / `2026-trace2skill`; arXiv preprint record; venue not independently checked. **Authors:** Ni, Jingwei, Liu, Yihao, Liu, Xinpeng et al.
- **Dates / access:** first 2026-03-26; latest 2026-06-04 (v5); accessed September 16. primary methods/results and relevant appendices inspected.
- **Decision:** reviewed-reserve; rubric H / M / H / H / M. Direct WikiSkill baseline; trajectory distillation and cross-model/task transfer. [Discovery provenance](workers/citation-mining-memory.md). [Reading note](notes/2026-trace2skill.md).
- **Original:** [saved v5](originals/2026-trace2skill/2026-trace2skill-paper-v5.pdf); [download](https://arxiv.org/pdf/2603.25158v5); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-embodiskill"></a>

### [EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents](https://arxiv.org/abs/2605.10332v2)

- **Key / family / type:** `2026-embodiskill` / `2026-embodiskill`; arXiv preprint record; venue not independently checked. **Authors:** Ju, Ruofei, Wang, Xinrui, Ding, Xin et al.
- **Dates / access:** first 2026-05-11; latest 2026-07-11 (v2); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. SHAPER skill-only comparator; primary abstract checked, efficacy not appraised. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** retention-restricted — Canonical arXiv license permits arXiv distribution, not general redistribution; no original retained.; [download](https://arxiv.org/pdf/2605.10332v2); [license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/).

<a id="2026-autoharness"></a>

### [AutoHarness: improving LLM agents by automatically synthesizing a code harness](https://arxiv.org/abs/2603.03329v1)

- **Key / family / type:** `2026-autoharness` / `2026-autoharness`; arXiv preprint record; venue not independently checked. **Authors:** Lou, Xinghua, Lázaro-Gredilla, Miguel, Dedieu, Antoine et al.
- **Dates / access:** first 2026-02-10; latest 2026-02-10 (v1); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. SHAPER harness-only comparator; primary abstract checked, efficacy not appraised. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2603.03329v1); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-agentspec"></a>

### [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](https://arxiv.org/abs/2606.14674v1)

- **Key / family / type:** `2026-agentspec` / `2026-agentspec`; arXiv preprint record; venue not independently checked. **Authors:** Chen, Jixuan, Shen, Jianzhi, Kang, Haoqiang et al.
- **Dates / access:** first 2026-06-12; latest 2026-06-12 (v1); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. Controlled embodied scaffold composition; primary abstract checked, efficacy not appraised. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2606.14674v1); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-natural-language-agent-harnesses"></a>

### [Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723v2)

- **Key / family / type:** `2026-natural-language-agent-harnesses` / `2026-natural-language-agent-harnesses`; arXiv preprint record; venue not independently checked. **Authors:** Pan, Linyue, Zou, Lexiao, Guo, Shuo et al.
- **Dates / access:** first 2026-03-26; latest 2026-05-18 (v2); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. Harness representation predecessor identified in HarnessDev introduction. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** retention-restricted — Canonical arXiv license permits arXiv distribution, not general redistribution; no original retained.; [download](https://arxiv.org/pdf/2603.25723v2); [license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/).

<a id="2026-aspire"></a>

### [ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272v1)

- **Key / family / type:** `2026-aspire` / `2026-aspire`; arXiv preprint record; venue not independently checked. **Authors:** Lu, Runyu, Wu, Yubo, Kou, Ethan et al.
- **Dates / access:** first 2026-06-30; latest 2026-06-30 (v1); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. SHAPER introduction cites robot skill discovery; robotics depth is secondary to current session. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2607.00272v1); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2024-swe-agent"></a>

### [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793v3)

- **Key / family / type:** `2024-swe-agent` / `2024-swe-agent`; arXiv preprint record; venue not independently checked. **Authors:** Yang, John, Jimenez, Carlos E., Wettig, Alexander et al.
- **Dates / access:** first 2024-05-06; latest 2024-11-11 (v3); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** excluded; rubric H / U / U / U / U. Foundational interface background; outside this update’s persistent self-evolution emphasis. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2405.15793v3); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2023-open-x-embodiment"></a>

### [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864v9)

- **Key / family / type:** `2023-open-x-embodiment` / `2023-open-x-embodiment`; arXiv preprint record; venue not independently checked. **Authors:** Embodiment Collaboration, O'Neill, Abby, Rehman, Abdul et al.
- **Dates / access:** first 2023-10-13; latest 2025-05-14 (v9); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** excluded; rubric H / U / U / U / U. Robot data/weight-adaptation background; not prioritized for this topic-wide session. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2310.08864v9); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2022-code-as-policies"></a>

### [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753v4)

- **Key / family / type:** `2022-code-as-policies` / `2022-code-as-policies`; arXiv preprint record; venue not independently checked. **Authors:** Liang, Jacky, Huang, Wenlong, Xia, Fei et al.
- **Dates / access:** first 2022-09-16; latest 2023-05-25 (v4); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** excluded; rubric H / U / U / U / U. Embodied code-policy foundation; relevant lineage, but not a central self-evolution test. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** retention-restricted — Canonical arXiv license permits arXiv distribution, not general redistribution; no original retained.; [download](https://arxiv.org/pdf/2209.07753v4); [license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/).

<a id="2023-memgpt"></a>

### [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560v2)

- **Key / family / type:** `2023-memgpt` / `2023-memgpt`; arXiv preprint record; venue not independently checked. **Authors:** Packer, Charles, Wooders, Sarah, Lin, Kevin et al.
- **Dates / access:** first 2023-10-12; latest 2024-02-12 (v2); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. Memory-management foundation cited by SelfMem; useful historical framing. [Discovery provenance](workers/citation-mining-memory.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2310.08560v2); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-seaevo"></a>

### [SeaEvo: Advancing Algorithm Discovery with Strategy Space Evolution](https://arxiv.org/abs/2604.24372v2)

- **Key / family / type:** `2026-seaevo` / `2026-seaevo`; arXiv preprint record; venue not independently checked. **Authors:** Luo, Sichun, Huang, Yi, Luo, Haochen et al.
- **Dates / access:** first 2026-04-27; latest 2026-05-08 (v2); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. Related-search discovery, not a verified backward citation; strategy-space evolution lead. [Discovery provenance](workers/citation-mining-meta.md).
- **Original:** retention-restricted — Canonical arXiv license permits arXiv distribution, not general redistribution; no original retained.; [download](https://arxiv.org/pdf/2604.24372v2); [license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/).

<a id="2026-skillsbench"></a>

### [SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks](https://arxiv.org/abs/2602.12670v4)

- **Key / type / family:** `2026-skillsbench`; arXiv preprint record; venue not independently checked; `2026-skillsbench`. **Authors:** Li, Xiangyi, Liu, Yimin, Chen, Wenbo et al..
- **Dates / version:** first 2026-02-13; latest metadata 2026-06-14; read v4. **Access:** 2026-09-16; primary methods/results and relevant appendices read; tier2/coordinator verified 2026-09-16.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Thesis coverage: paired curated/no-skill and self-authoring controls materially qualify the fixed-expertise comparison; v4 replaces obsolete snapshot. **Notes:** [reading record](notes/2026-skillsbench.md).
- **Originals:** [2026-skillsbench-paper-v4.pdf](originals/2026-skillsbench/2026-skillsbench-paper-v4.pdf) License/permission: http://creativecommons.org/licenses/by/4.0/. Metadata and preparation costs remain source-specific.

<a id="2026-meta-agent-challenge"></a>

### [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455v1)

- **Key / family / type:** `2026-meta-agent-challenge` / `2026-meta-agent-challenge`; arXiv preprint record; venue not independently checked. **Authors:** Lu, Xinyu, Wang, Tianshu, Wang, Pengbo et al.
- **Dates / access:** first 2026-06-03; latest 2026-06-03 (v1); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. HarnessDev §5 names it as closest Creation comparator; development benchmark priority. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** retention-restricted — Canonical arXiv license permits arXiv distribution, not general redistribution; no original retained.; [download](https://arxiv.org/pdf/2606.04455v1); [license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/).

<a id="2026-harnessopt-bench"></a>

### [HarnessOpt-Bench: Evaluating LLMs at Harness Optimization](https://arxiv.org/abs/2608.06301v1)

- **Key / family / type:** `2026-harnessopt-bench` / `2026-harnessopt-bench`; arXiv preprint record; venue not independently checked. **Authors:** Ursekar, Varun, Shanker, Apaar, Maurya, Yash et al.
- **Dates / access:** first 2026-08-06; latest 2026-08-06 (v1); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. HarnessDev §5 names closest concurrent Evolution benchmark; independent test partition lead. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2608.06301v1); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-self-harness"></a>

### [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498v3)

- **Key / family / type:** `2026-self-harness` / `2026-self-harness`; arXiv preprint record; venue not independently checked. **Authors:** Zhang, Hangfan, Zhang, Shao, Li, Kangcong et al.
- **Dates / access:** first 2026-06-08; latest 2026-08-20 (v3); accessed September 16. primary abstract and metadata only; seed citation context where applicable.
- **Decision:** watchlist; rubric H / U / U / U / U. HarnessDev §5 names model-specific edits and regression testing; methods unread. [Discovery provenance](workers/citation-mining-harness.md).
- **Original:** pending — Discovery-only source; original acquisition deferred until substantive reading.; [download](https://arxiv.org/pdf/2606.09498v3); [license](http://creativecommons.org/licenses/by/4.0/).

<a id="2026-rethink-continual-internalization"></a>

### [Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703v1)

- **Key / type / family:** `2026-rethink-continual-internalization`; arXiv preprint; `2026-rethink-continual-internalization`. **Authors:** Jingwen Chen, Wenkai Yang, Shengda Fan et al..
- **Dates / version:** first 2026-06-03; latest metadata 2026-06-03; read v1. **Access:** 2026-09-16; full primary methods/results and relevant appendices; tier2 verification; coordinator HTML §§2–5.
- **Selection:** reviewed-reserve; rubric H / M / H / H / H. Tests repeated weight updates with both on-policy deterioration and bounded gains for a fixed off-policy recipe. New thesis-relevant omission. **Notes:** [reading record](notes/2026-rethink-continual-internalization.md).
- **Originals:** Official HTML inspected; arXiv non-exclusive distribution license does not establish permission to retain redistributed paper. License/permission: http://arxiv.org/licenses/nonexclusive-distrib/1.0/. Metadata and preparation costs remain source-specific.


<a id="2023-expel"></a>

### [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144v3)

- **Key / type / family:** `2023-expel`; AAAI 2024 paper; arXiv v3 read; `2023-expel`. **Authors:** Andrew Zhao, Daniel Huang, Quentin Xu et al..
- **Dates / version:** first 2023-08-20; latest metadata 2024-12-20; read v3. **Access:** 2026-09-16; primary methods/results read; coordinator metadata and methods checked.
- **Selection:** reviewed-reserve; rubric H / M / M / H / H. Thesis foundation: cross-task insight and episodic retrieval predate newer memory systems. **Notes:** [reading record](notes/2023-expel.md).
- **Originals:** [2023-expel-paper-v3.pdf](originals/2023-expel/2023-expel-paper-v3.pdf) License/permission: CC BY 4.0. Metadata and preparation costs remain source-specific.

<a id="2025-dynamic-cheatsheet"></a>

### [Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952v1)

- **Key / type / family:** `2025-dynamic-cheatsheet`; arXiv preprint; `2025-dynamic-cheatsheet`. **Authors:** Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, James Zou.
- **Dates / version:** first 2025-04-10; revision 2025-04-10; read v1. **Access:** 2026-09-16; selected primary methods §§2.1–2.3, evaluation setup and §§4.5–5 limitations read; citation contexts checked.
- **Selection:** reviewed-reserve. ACE explicitly credits Dynamic Cheatsheet as architectural inspiration and tests it as an online baseline. **Notes:** [reading record](notes/2025-dynamic-cheatsheet.md).
- **Originals:** saved. License/permission: CC BY 4.0. [Original PDF](originals/2025-dynamic-cheatsheet/2025-dynamic-cheatsheet-paper-v1.pdf).
