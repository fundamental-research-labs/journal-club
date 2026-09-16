# Research source register

Updated and accessed **September 16, 2026** for the September 18 session. Names and descriptive filenames identify sources. This is a curated research update, not an exhaustive systematic review. “Sections read” means primary full-text methods/results were inspected to the depth recorded in the linked note; it does not mean every appendix or code artifact was audited. None of the experiments was reproduced.

## Sources examined in this update

Each name links to reading notes containing the primary URL, findings, result locators, limitations, and evidence family. A paper, its repository, project page, and announcement count as one family, not independent confirmation.

| Source / authors | First publication; latest verified version | Type | Review depth and role |
| --- | --- | --- | --- |
| [WikiSkill](notes/wikiskill.md), Liyan Tang et al. | Aug 27, 2026; v1 | Preprint | Methods, results, data splits, bootstrap procedure; positive skill-evolution evidence |
| [AgentStream](notes/agentstream.md), Dong Yan et al. | Jul 31, 2026; v1 | Preprint | Framework, setup, main results; streaming conditions and regressions |
| [Rethinking harness-evolution evaluation](notes/harness-evolution-evaluation.md), Yike Wang et al. | Jul 14; v2 Aug 27, 2026 | Preprint | Methods, Tables 1–3, discussion; budget baselines and held-out transfer |
| [Hyperagents](notes/hyperagents.md), Jenny Zhang et al. | Mar 19, 2026; v1 | Preprint | Selected methods/results; improving the modification process |
| [MetaRSI / RSI2](notes/metarsi.md), Zihan Tan et al. | Sep 6; v2 Sep 9, 2026 | Preprint | Methods, setup, Table 3; data/harness/model composition |
| [HarnessDev](notes/harnessdev.md), Yuhao Wu et al. | Sep 1, 2026; v1 | Preprint | Evolution setup/results and cost/reference caveats; selection and transfer |
| [EvoHarnessBench](notes/evoharnessbench.md), Zixuan Ke et al. | Sep 3; v2 Sep 10, 2026 | Preprint | Design and evolving-tools results; changing interfaces |
| [Library Drift](notes/library-drift.md), Xing Zhang et al. | May 19; v3 Jul 29, 2026 | Preprint; repository reports ICML 2026 failure-modes workshop acceptance | Protocol, ablations, cost; skill retirement and routing. Ratchet companion/code share this family |
| [ScienceBuddy](notes/sciencebuddy.md), Shuhan Xue et al. | Sep 15, 2026; v1; lab announcement Sep 16 | Preprint, product demonstration, code | Selected methods/results/appendices; coupled harness and model learning |
| [Reef](notes/reef.md), Ao Qu and collaborators / Human-Agent-Society | Announcement Sep 15; inspected commit Sep 16, 2026 | First-party technical article and code | Article and README; serving, feedback, versioning; recipe results not audited |
| [SoL-Pi](notes/sol-pi.md), NVIDIA | First release date unverified; inspected commit Sep 15, 2026 | Code release | README; reusable efficiency mechanisms. Paper listed as forthcoming |
| [autoresearch](notes/autoresearch.md), Andrej Karpathy | March 2026; inspected commit Mar 26 | Code and inaccessible linked social announcements | README; experiment boundaries. No social claims used |

Repository commit hashes and dates are in the notes. Academic version dates were checked against arXiv submission histories; revisions are not treated as newly introduced findings. Peer review is not assumed for unverified venues.

## Existing sources retained

The [original reading list](../reading-list.md) remains the index for foundational papers, surveys, and candidates outside the detailed update: Reflexion, Voyager, SICA, DGM, SEAL, GEPA, Huxley-Gödel Machine, SelfMem, SEA-Eval, FinEvo-Bench, and the broad/coding surveys. Their existing review statuses are preserved; inclusion here does not upgrade an abstract screen to full-text review. The September autonomy survey's arXiv history was rechecked: September 10 first submission, September 15 v2; detailed v2 claims remain unreviewed.

The [practitioner register](../practitioner-sources.md) preserves first-party Hermes documentation, LangChain's June memory article, NVIDIA's September memory evaluation, and Kirill Krainov's skill-optimization proposal, with authors, dates, access depths, and evidence categories. These remain useful examples, not independent replications of the academic systems.

## Additional discovery leads

| Lead | Verified access in this pass | Why retained / restriction |
| --- | --- | --- |
| [SHAPER: Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350), Peidong Wang et al., Aug 11, 2026 | Primary abstract screened | Embodied frozen-weight adaptation; no quantitative findings adopted |
| [MemRL](https://arxiv.org/abs/2601.03192), Jan 6, 2026 | Primary abstract screened | Runtime memory-value learning; complementary mechanism, results not audited |
| [SimSkill](https://arxiv.org/abs/2609.03753) | Secondary discovery only | Traffic-simulation skill accumulation; not reviewed support |
| [Sepo project writeup](https://www.szj.io/posts/sepo.html), May 21, 2026 | First-party search excerpt only | Repository-level retained team preferences; body/code not reviewed |
| [Researcher social announcement](https://x.com/karpathy/status/2030371219518931079) | Direct retrieval failed | No quotations, post-date claims, or performance numbers used |

There is no comprehensive X/Twitter or talk/video review. Search results and product demos alone do not establish empirical effectiveness.
