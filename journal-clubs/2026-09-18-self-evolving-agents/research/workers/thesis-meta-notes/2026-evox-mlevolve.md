# EvoX and MLEvolve: meta-search omissions

**Provisional worker record, superseded for thesis use by the shared notes/register and [Tier 2 corrections](../thesis-additions-screening.md).**


EvoX (Liu et al., arXiv:2602.23413, first posted 2026-02-27, https://arxiv.org/abs/2602.23413) is cited by Dream-RSI v1 §6 as a direct comparator. Its abstract frames fixed search knobs as unable to adapt and reports joint evolution of candidate solutions and search strategies across nearly 200 optimization tasks, with comparisons to AlphaEvolve, OpenEvolve, GEPA, and ShinkaEvolve. The editable state is the search strategy/optimizer and candidate archive; this is harness/meta evolution, not demonstrated foundation-weight updating. Existing note `notes/2026-evox.md` flags that iteration parity is not total-compute parity and that dispersion is absent in a key figure. It is useful positive evidence for future-task value inside a broad optimization family, but not for acceleration or domain-general transfer.

MLEvolve (Du et al., arXiv:2606.06473, first posted 2026-06-08, https://arxiv.org/abs/2606.06473) is cited by Dream-RSI's memory/history discussion. The primary abstract describes progressive MCGS graph reference edges, retrospective memory, adaptive coding modes, and MLE-Bench evaluation under a 12-hour budget. Its contribution is hierarchical reuse of prior search experience across branches, making it a consequential comparator for persistent meta-state. The evidence is still one benchmark family and a fixed wall-clock budget; no independent replication or general acceleration result was verified.

Interpretation: both sources move the thesis toward “persistent search state can buy transfer” while leaving the central claim conditional on held-out task families, compute-matched controls, and retention over repeated updates.
