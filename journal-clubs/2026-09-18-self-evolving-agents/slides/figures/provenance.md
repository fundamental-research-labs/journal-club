# Figure and data provenance

Current revision: September 16, 2026. Evidence slides use original source excerpts;
all four former HTML/SVG result bar charts have been removed. The original visual
encoding, type, colors, row order, baselines and uncertainty are preserved. Labels
and interpretation outside the white source image belong to this presentation.
Images are embedded in the HTML for offline use; PNG assets remain alongside it.

## Original excerpts

| Slide | Asset / creator | Exact source | Scope and reuse record |
| --- | --- | --- | --- |
| 4 | [WikiSkill Table 1](wikiskill-table-1.png), Liyan Tang et al. | [v1 PDF](https://arxiv.org/pdf/2608.27454v1#page=8), PDF p. 8, Table 1 | Headers and complete Qwen-3.5-4B / 9B blocks; later model blocks and caption omitted. Yellow highlights and bold are original. CC BY 4.0. |
| 5 | [SEAL Table 2](seal-table-2.png), Adam Zweiger et al. | [v2 PDF](https://arxiv.org/pdf/2506.10943v2#page=8), PDF p. 8, Table 2 | All methods and passage settings; caption omitted. CC BY 4.0. |
| 6 | [FinEvo Table 5](finevo-table-5.png), Bo Deng et al. | [v1 PDF](https://arxiv.org/pdf/2608.06144v1#page=6), PDF p. 6, Table 5 | All five conditions, compliance and cost columns; caption omitted. User explicitly requested original-source reuse for this local journal club. Source records arXiv non-exclusive distribution license; broader reuse permission is not established. Full PDF was used temporarily and is not added to the repository. |
| 7 | [Harness evaluation Table 1](harness-table-1.png), Yike Wang et al. | [v2 PDF](https://arxiv.org/pdf/2607.12227v2#page=6), PDF p. 6, Table 1 | Complete table including direct sampling and harness scaling; caption omitted. Printed averages unchanged. CC BY 4.0. |
| 10 | [Hyperagents Figure 4](hyperagents-figure-4.png), Jenny Zhang et al. | [v1 PDF](https://arxiv.org/pdf/2603.19461v1#page=13), PDF p. 13, Figure 4; §5.3 p. 12 | Both panels, legends, axes and error bars; caption omitted. Original test y-axis starts at 0.3; no rescaling. Run-bootstrap 95% uncertainty preserved. CC BY 4.0. |

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

- Slides 1–2: original conceptual learning-loop illustrations; no empirical data.
- Slides 3, 12, 13 and 16: original explanatory/proposed-evaluation tables. These
  are synthesis, not reproductions of a source's results figure.
- Slide 8: a **calculated summary**, not an original AgentStream table. The
  positive/negative/tie counts are reconstructed across Tables 11–13 and displayed
  with the reported means from [AgentStream v1](https://arxiv.org/html/2608.00155v1),
  Table 2. Keep this presentation-specific calculation as an editable table;
  [the audit](../../research/check-agentstream-aggregates.py) records its basis.
  The 45 cells share tasks; printed variability is not a confidence interval.
- Slide 9: cited numerical checkpoint summary from [R-Zero v4](https://arxiv.org/abs/2508.05004v4),
  Appendix D Table 6 (49.12 → 46.52), alongside a mechanism explanation. No result
  chart is reconstructed. The original unmodified PDF remains in research originals.
- Slide 10: Dream-RSI's 550 → 317 discovery-agent calls remains a cited text
  comparison from [v1 Figure 3](https://arxiv.org/html/2609.14858v1), distinct from
  the displayed Hyperagents plot and its experiment. No visual is reconstructed.

The original cover motif encodes no measured values. Reference JPEGs at the
repository root are not embedded. No synthetic empirical values are introduced.
