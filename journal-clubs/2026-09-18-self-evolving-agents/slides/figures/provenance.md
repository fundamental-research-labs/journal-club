# Figure and data provenance

Prepared September 16, 2026. Figures are editable HTML/SVG built from the existing claim ledger and source notes. No paper screenshots or third-party artwork are embedded. Charts reproduce reported values rather than reproducing the experiments. They use a zero baseline and full 0–100 scale. Missing confidence intervals are stated rather than invented.

| Slide | Figure | Source and locator | Adaptation / permission |
| --- | --- | --- | --- |
| 2 | Experience → proposal → selection → retained state | C001; Reflexion Algorithm 1, Voyager §2, SEAL §3 | Original illustrative explanation; not an empirical model diagram |
| 4 | Qwen-3.5-9B accuracy: 29.9, 47.4 | [WikiSkill v1](https://arxiv.org/abs/2608.27454v1), Table 1; Appendix B Table 6 | Redrawn reported data; equal-weight five-benchmark mean; three runs. Original paper CC BY 4.0 |
| 5 | Single-passage accuracy: 39.7, 46.3, 47.0 | [SEAL v2](https://arxiv.org/abs/2506.10943v2), Table 2; Appendix B | Redrawn reported data; 974 questions in 200 held-out passages. Original paper CC BY 4.0 |
| 6 | Reset / fixed expert / full evolution: 71.58, 86.67, 89.47 | [FinEvo v1](https://arxiv.org/html/2608.06144v1), Table 5 | Original chart of factual values; no original artwork copied. Redistribution license for the paper not established; paper not retained |
| 7 | Evolution / parallel sampling: 67.4, 72.3 | [Harness-evaluation critique v2](https://arxiv.org/abs/2607.12227v2), Table 1 | Redrawn printed averages; no silent correction of rounded-cell arithmetic. Original paper CC BY 4.0 |
| 7 | Separate holdout annotation: 68.3, 67.7 | Same source, Table 3 | Separate experiment explicitly labeled; not merged into chart data |
| 8 | Stream table and count reconstruction | [AgentStream v1](https://arxiv.org/html/2608.00155v1), Tables 2, 11–13; [local audit](../../research/check-agentstream-aggregates.py) | Original table of reported/reconstructed facts; no source artwork copied. 45 cells share tasks; printed ± is not a CI |
| 9–10 | Checkpoint and meta-improvement values | [R-Zero v4](https://arxiv.org/abs/2508.05004v4), Appendix D Table 6; [Hyperagents v1](https://arxiv.org/abs/2603.19461v1), Figure 4; [Dream-RSI v1](https://arxiv.org/html/2609.14858v1), Figure 3 | Typeset facts, not copied figures. R-Zero original CC BY-NC-ND 4.0 remains unmodified; Hyperagents CC BY 4.0; Dream-RSI redistribution rights not established |

Tables on slides 3, 12, 13, and 16 are original explanatory or proposed-evaluation tables, with supporting sources linked on the slides and in notes. Slides 12–13 are proposals, not results. No synthetic empirical values or decorative data were introduced.


## Cover learning-loop motif (styling revision)

Original HTML/CSS illustration made for this presentation. Concentric circles and
three labels suggest experience, revision, and reuse; they encode no measured
values or observed trajectory. Marked “Conceptual learning loop” on the slide.
The two root-level reference JPEGs were inspected but are not embedded or used as
empirical evidence. No third-party graphic was copied.
