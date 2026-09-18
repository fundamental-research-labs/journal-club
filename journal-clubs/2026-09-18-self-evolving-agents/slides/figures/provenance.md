# Figure and data provenance

Current revision: September 18, 2026. Evidence slides use original source excerpts;
all four former HTML/SVG result bar charts have been removed. The original visual
encoding, type, colors, row order, baselines and uncertainty are preserved. Labels
and interpretation outside the white source image belong to this presentation.
Images are embedded in the HTML for offline use; PNG assets remain alongside it.

## Original excerpts

| Slide | Asset / creator | Exact source | Scope and reuse record |
| --- | --- | --- | --- |
| 7 | [WikiSkill Table 1](wikiskill-table-1.png), Liyan Tang et al. | [v1 PDF](https://arxiv.org/pdf/2608.27454v1#page=8), PDF p. 8, Table 1 | Headers and complete Qwen-3.5-4B / 9B blocks; later model blocks and caption omitted. Yellow highlights and bold are original. CC BY 4.0. |
| 29 | [SEAL Table 2](seal-table-2.png), Adam Zweiger et al. | [v2 PDF](https://arxiv.org/pdf/2506.10943v2#page=8), PDF p. 8, Table 2 | All methods and passage settings; caption omitted. CC BY 4.0. |
| 9 | [FinEvo Table 5](finevo-table-5.png), Bo Deng et al. | [v1 PDF](https://arxiv.org/pdf/2608.06144v1#page=6), PDF p. 6, Table 5 | All five conditions, compliance and cost columns; caption omitted. User explicitly requested original-source reuse for this local journal club. Source records arXiv non-exclusive distribution license; broader reuse permission is not established. Full PDF was used temporarily and is not added to the repository. |
| 11 | [Harness evaluation Table 1](harness-table-1.png), Yike Wang et al. | [v2 PDF](https://arxiv.org/pdf/2607.12227v2#page=6), PDF p. 6, Table 1 | Complete table including direct sampling and harness scaling; caption omitted. Printed averages unchanged. CC BY 4.0. |
| 20 | [Hyperagents Figure 4](hyperagents-figure-4.png), Jenny Zhang et al. | [v1 PDF](https://arxiv.org/pdf/2603.19461v1#page=13), PDF p. 13, Figure 4; §5.3 p. 12 | Both panels, legends, axes and error bars; caption omitted. Original test y-axis starts at 0.3; no rescaling. Run-bootstrap 95% uncertainty preserved. CC BY 4.0. |
| 19 | [Hyperagents Figure 3](hyperagents-figure-3.png), Jenny Zhang et al. | [v1 PDF](https://arxiv.org/pdf/2603.19461v1#page=10), PDF p. 10, Figure 3; §5.2 pp. 9–11 | Middle and right held-out panels, with all their comparators, axes, labels and uncertainty. Left training panel and caption omitted, explicitly labeled on-slide. CC BY 4.0. Whole-implementation transfer and formatting-failure qualifications remain visible. |

[CC BY 4.0 terms](https://creativecommons.org/licenses/by/4.0/).
Source versions and licenses follow the retained-original manifest and reading
notes. Reproduction changes are cropping, rasterization at 3 pixels per PDF point,
and proportional display scaling only. No annotations are painted onto the images.
Captions' relevant qualifications and source-vs-presenter interpretations are in
speaker notes. FinEvo's exact PDF locator corrects the prior notes' page-7 locator.

[extraction.json](extraction.json) records source PDF hashes, crop rectangles,
versions and page numbers. [extract.py](extract.py) regenerates the PNGs from the
retained PDFs, fetching FinEvo and the AgentStream artwork into a temporary directory. Run from the repo:

```sh
uv run --with pymupdf python journal-clubs/2026-09-18-self-evolving-agents/slides/figures/extract.py
python3 journal-clubs/2026-09-18-self-evolving-agents/slides/build.py
```

The normal HTML build needs only Python's standard library and the included PNGs.

## Intentional synthesis and numerical summaries

- Slides 1–5, 12, 17, and 22: original conceptual framing and cross-paper synthesis, not representations of a single paper’s figure. Slide 6 now uses the original WikiSkill Figure 2; the previous homemade version is removed.
- Slides 3, 32, 23, 26–27 and 30: mechanism synthesis, proposed controls, and a methods/uncertainty summary. They do not reproduce an individual empirical table.
- Slide 14: calculated AgentStream summary from v1 Tables 2 and 11–13. The [existing reconstruction](../../research/check-agentstream-aggregates.py) documents positive/negative/tie counts; 45 cells share 300 tasks. A presentation-specific aggregation is the reason for the editable table. No pooled causal estimate or CI is claimed.
- Slide 15: cited text summaries, not reconstructed charts, of R-Zero v4 Appendix D/Table 6 and Continual Internalization v1 §§3–5/Table 4. The purpose is cross-study synthesis of a failure and a bounded positive counterexample; the numbers are not compared on a common scale.
- Slide 16: first-party Shopify architecture plus an explicitly normative evaluator recommendation. No efficacy curve is invented.
- Slide 21: conceptual explanation of Dream-RSI replay, with its three mixed mathematics outcomes described in words from v1 Table 1. No empirical chart is redrawn. Replay-history selection and future online performance remain separate.
- Slide 27: conceptual comparison of curated skills and one-shot authoring from SkillsBench v4 Tables 2/6/Appendix D.6. Numerical details are in notes; no authoring-vs-evolution effect size is invented.

The previous Dream-RSI call-count sidebar was removed from the Hyperagents page so that each experiment has its own interpretation. Its qualified result remains in Dream-RSI speaker notes. All six empirical image assets preserve original artwork. Existing excerpts were reused unchanged; the new Figure 3 crop was compared with its original page at presentation size. No synthetic empirical values or new full-paper copies were added.

## Conceptual figures added September 18

| Slide | Asset / creator | Source and transformation | Reuse record |
| --- | --- | --- | --- |
| 13 | [AgentStream Figure 1(b)](agentstream-figure-1b.png), Dong Yan et al. | [v1 HTML Figure 1](https://arxiv.org/html/2608.00155v1#S1.F1); [original PNG](https://arxiv.org/html/2608.00155v1/evaluation_compare.png), 1600×900. Crop pixels [0,290,1600,900] retains complete panel (b); panel (a) and HTML caption omitted. No recoloring or annotations. | Source accessed September 18; arXiv perpetual non-exclusive license, no broader reuse license established. Attributed excerpt for this requested local presentation; no full paper retained. |
| 18 | [Hyperagents Figure 1](hyperagents-figure-1.png), Jenny Zhang et al. | [v1 PDF p. 4](https://arxiv.org/pdf/2603.19461v1#page=4), Figure 1, both panels; crop points [70,175,542,387], 3× rasterization; caption omitted. | CC BY 4.0; existing source manifest. |
| 28 | [SEAL Figure 1](seal-figure-1.png), Adam Zweiger et al. | [v2 PDF p. 2](https://arxiv.org/pdf/2506.10943v2#page=2), Figure 1, complete diagram; crop points [106,70,505,174], 3× rasterization; caption omitted. | CC BY 4.0; existing source manifest. |

Figures were inspected with their captions and method text. AgentStream's caption contrasts independent evaluation with a stateful stream and names the three modular dimensions. Hyperagents' caption distinguishes fixed DGM instruction generation from editable meta code; its broad potential claims are not presented as demonstrated acceleration. SEAL's caption explains candidate self-edits, inner weight updates, downstream testing, and outer policy learning. These distinctions are preserved in visible explanations and notes.

Slides 6, 8 and 10 now use original source conceptual figures. The homemade boxes/arrows have been removed, as have slide 14's invented ordering strings. Slide 15 remains a text-based cross-study comparison; it does not redraw either paper's figure.

## Source-artwork correction — September 18, 2026

| Slide | Asset / creator | Exact source and extraction | Reuse record |
| --- | --- | --- | --- |
| 6 | [WikiSkill Figure 2](wikiskill-figure-2.png), Liyan Tang et al. | [v1 PDF p. 4](https://arxiv.org/pdf/2608.27454v1#page=4), complete framework; crop points [61,82,535,306], 3× rasterization; caption omitted | CC BY 4.0; existing original manifest |
| 8 | [FinEvo Figure 1](finevo-figure-1.png), Bo Deng et al. | [v1 PDF p. 3](https://arxiv.org/pdf/2608.06144v1#page=3), both landscape/task-workspace panels; crop points [54,53,558,227], 3×; caption omitted | Attributed excerpt for the requested local presentation. ArXiv non-exclusive license; broader reuse permission not established. Full PDF remains temporary. |
| 10 | [Harness Figure 2](harness-figure-2.png), Yike Wang et al. | [v2 PDF p. 3](https://arxiv.org/pdf/2607.12227v2#page=3), all four method panels and legend; crop points [108,70,504,229], 3×; caption omitted | CC BY 4.0; existing original manifest |

Compared each extraction with its original page and caption. No recoloring, redraws, or overlays. Plain-language explanations sit outside the artwork. The numeric results and all prior empirical table/figure assets remain unchanged. `extract.py` now regenerates twelve source excerpts.
