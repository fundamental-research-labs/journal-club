# Figure and data provenance

Current revision: September 18, 2026. Evidence slides use original source excerpts;
all four former HTML/SVG result bar charts have been removed. The original visual
encoding, type, colors, row order, baselines and uncertainty are preserved. Labels
and interpretation outside the white source image belong to this presentation.
Images are embedded in the HTML for offline use; PNG assets remain alongside it.

## Original excerpts

| Slide | Asset / creator | Exact source | Scope and reuse record |
| --- | --- | --- | --- |
| 4 | [WikiSkill Table 1](wikiskill-table-1.png), Liyan Tang et al. | [v1 PDF](https://arxiv.org/pdf/2608.27454v1#page=8), PDF p. 8, Table 1 | Headers and complete Qwen-3.5-4B / 9B blocks; later model blocks and caption omitted. Yellow highlights and bold are original. CC BY 4.0. |
| 20 | [SEAL Table 2](seal-table-2.png), Adam Zweiger et al. | [v2 PDF](https://arxiv.org/pdf/2506.10943v2#page=8), PDF p. 8, Table 2 | All methods and passage settings; caption omitted. CC BY 4.0. |
| 6 | [FinEvo Table 5](finevo-table-5.png), Bo Deng et al. | [v1 PDF](https://arxiv.org/pdf/2608.06144v1#page=6), PDF p. 6, Table 5 | All five conditions, compliance and cost columns; caption omitted. User explicitly requested original-source reuse for this local journal club. Source records arXiv non-exclusive distribution license; broader reuse permission is not established. Full PDF was used temporarily and is not added to the repository. |
| 7 | [Harness evaluation Table 1](harness-table-1.png), Yike Wang et al. | [v2 PDF](https://arxiv.org/pdf/2607.12227v2#page=6), PDF p. 6, Table 1 | Complete table including direct sampling and harness scaling; caption omitted. Printed averages unchanged. CC BY 4.0. |
| 13 | [Hyperagents Figure 4](hyperagents-figure-4.png), Jenny Zhang et al. | [v1 PDF](https://arxiv.org/pdf/2603.19461v1#page=13), PDF p. 13, Figure 4; §5.3 p. 12 | Both panels, legends, axes and error bars; caption omitted. Original test y-axis starts at 0.3; no rescaling. Run-bootstrap 95% uncertainty preserved. CC BY 4.0. |

| 12 | [Hyperagents Figure 3](hyperagents-figure-3.png), Jenny Zhang et al. | [v1 PDF](https://arxiv.org/pdf/2603.19461v1#page=10), PDF p. 10, Figure 3; §5.2 pp. 9–11 | Middle and right held-out panels, with all their comparators, axes, labels and uncertainty. Left training panel and caption omitted, explicitly labeled on-slide. CC BY 4.0. Whole-implementation transfer and formatting-failure qualifications remain visible. |

[CC BY 4.0 terms](https://creativecommons.org/licenses/by/4.0/).
Source versions and licenses follow the retained-original manifest and reading
notes. Reproduction changes are cropping, rasterization at 3 pixels per PDF point,
and proportional display scaling only. No annotations are painted onto the images.
Captions' relevant qualifications and source-vs-presenter interpretations are in
speaker notes. FinEvo's exact PDF locator corrects the prior notes' page-7 locator.

[extraction.json](extraction.json) records source PDF hashes, crop rectangles,
versions and page numbers. [extract.py](extract.py) regenerates the PNGs from the
retained PDFs, fetching FinEvo only into a temporary directory. Run from the repo:

```sh
uv run --with pymupdf python journal-clubs/2026-09-18-self-evolving-agents/slides/figures/extract.py
python3 journal-clubs/2026-09-18-self-evolving-agents/slides/build.py
```

The normal HTML build needs only Python's standard library and the included PNGs.

## Intentional synthesis and numerical summaries

- Slides 1–3: original conceptual illustrations, not empirical data. Slide 2 compares three evidentiary ambitions without implying measured progress. Slide 3 adapts WikiSkill v1 §3/Figure 2 to explain the distinct fates of knowledge and a rejected skill; its causal-scrutiny takeaway is presenter interpretation. This explanatory simplification is not a redrawn result figure. SkillOpt’s prior rejected-edit feedback is acknowledged in notes.
- Slides 5, 11, 15–17 and 21: mechanism synthesis, proposed controls, and a methods/uncertainty summary. They do not reproduce an individual empirical table.
- Slide 8: calculated AgentStream summary from v1 Tables 2 and 11–13. The [existing reconstruction](../../research/check-agentstream-aggregates.py) documents positive/negative/tie counts; 45 cells share 300 tasks. A presentation-specific aggregation is the reason for the editable table. No pooled causal estimate or CI is claimed.
- Slide 9: cited text summaries, not reconstructed charts, of R-Zero v4 Appendix D/Table 6 and Continual Internalization v1 §§3–5/Table 4. The purpose is cross-study synthesis of a failure and a bounded positive counterexample; the numbers are not compared on a common scale.
- Slide 10: first-party Shopify architecture plus an explicitly normative evaluator recommendation. No efficacy curve is invented.
- Slide 14: conceptual explanation of Dream-RSI replay, with its three mixed mathematics outcomes described in words from v1 Table 1. No empirical chart is redrawn. Replay-history selection and future online performance remain separate.
- Slide 22: conceptual comparison of curated skills and one-shot authoring from SkillsBench v4 Tables 2/6/Appendix D.6. Numerical details are in notes; no authoring-vs-evolution effect size is invented.

The previous Dream-RSI call-count sidebar was removed from the Hyperagents page so that each experiment has its own interpretation. Its qualified result remains in Dream-RSI speaker notes. All six empirical image assets preserve original artwork. Existing excerpts were reused unchanged; the new Figure 3 crop was compared with its original page at presentation size. No synthetic empirical values or new full-paper copies were added.
