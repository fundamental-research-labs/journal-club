# ScienceBuddy

## Source and access

**Source key:** `sciencebuddy`.

**Originals and source links:** [register](../sources.md#sciencebuddy); [canonical source](https://arxiv.org/abs/2609.17523v1). Retained unmodified: [2026-sciencebuddy-experiment-config-commit-454d11c.toml](../originals/2026-sciencebuddy/2026-sciencebuddy-experiment-config-commit-454d11c.toml); [2026-sciencebuddy-code-license-commit-454d11c.txt](../originals/2026-sciencebuddy/2026-sciencebuddy-code-license-commit-454d11c.txt); [2026-sciencebuddy-experiment-guide-commit-454d11c.md](../originals/2026-sciencebuddy/2026-sciencebuddy-experiment-guide-commit-454d11c.md); [2026-sciencebuddy-algorithm-guide-commit-454d11c.md](../originals/2026-sciencebuddy/2026-sciencebuddy-algorithm-guide-commit-454d11c.md). Repository-artifact license is recorded in the manifest; this does not license the paper or blog. [Manifest](../originals/manifest.json).

[Paper v1](https://arxiv.org/html/2609.17523v1); [code](https://github.com/Gen-Verse/ScienceBuddy/tree/454d11c6e0609de074f27391ef170ca748dfae37). Shuhan Xue et al.; September 15, 2026 preprint; PhAI release September 16. Accessed September 16; §§2, 4, 7.1–7.3 inspected. Family: ScienceBuddy (paper, preview, announcement, code).

**Acquisition:** paper [PDF](https://arxiv.org/pdf/2609.17523v1) is retention-restricted here: its arXiv perpetual non-exclusive license does not establish redistribution rights. Official arXiv HTML and the PhAI paper page were checked. The code's MIT license does permit retention of original guide/config files with its notice: [experiment guide](../originals/2026-sciencebuddy/2026-sciencebuddy-experiment-guide-commit-454d11c.md), [algorithm guide](../originals/2026-sciencebuddy/2026-sciencebuddy-algorithm-guide-commit-454d11c.md), [configuration](../originals/2026-sciencebuddy/2026-sciencebuddy-experiment-config-commit-454d11c.toml), [license](../originals/2026-sciencebuddy/2026-sciencebuddy-code-license-commit-454d11c.txt). Retrieved September 16; snapshot commit dated September 16 03:26 UTC. These are original files, a small partial repository capture; relative links may refer to unretained files. No code was executed.

## Question and methods

Alternate fixed-model harness refinement and fixed-harness GRPO. The auxiliary reflector stays fixed. Scientific inventory: 895 tasks across four families; standalone harness experiment has 288 adaptation conversations, not 288 independent evaluation tasks.

## Results and evidence

### Reported evidence

§4.2/Figure 8 reports three cycles, each ten harness steps plus twenty RL updates; single-attempt test accuracy 42.2→73.3. Standalone harness comparison: 31.1→51.1 validation accuracy. Fixed-harness model experiment: pass@4 48.3→67.8. Evaluation denominators, repeated-run uncertainty, and full resource accounting were not established from reviewed sections; 895 is not a verified denominator for each result.

### September 16 autonomous audit: released recipe versus reported experiment

The [experiment guide at commit 454d11c6e0609de074f27391ef170ca748dfae37](https://github.com/Gen-Verse/ScienceBuddy/blob/454d11c6e0609de074f27391ef170ca748dfae37/docs/experiments.md#data) gives a **715 Train / 90 Val / 90 Test** task-ID split: DbQA 411/50/50; GWAS 140/20/20; LitQA2 76/10/10; ProtocolQA 88/10/10. It explicitly discloses **20 related-material groups overlapping Train–Val and 18 overlapping Train–Test**. Thus distinct task IDs do not establish independence of underlying material. This is an acknowledged generalization limitation, not evidence that the code directly reads private test labels.

The maintained recipe uses **three harness stages with three steps each**, 16 interactions per step, three proposals from the same parent, full 90-task validation comparisons, then **30 RL updates per stage**. Evaluation is temperature zero, one attempt per task. It targets eight A100 GPUs, but that hardware requirement is not a measured total experiment cost. The guide itself distinguishes settings from measured performance. The paper describes ten harness steps and twenty RL updates per coupled cycle, and its standalone adaptation case uses 24×12 conversations. Therefore the current recipe's 90-test denominator **must not be assigned to Figures 8–10 without run provenance**. Actual repeated-run uncertainty and historical run costs remain unresolved.

The recipe evaluates the same Test assignment at stage boundaries. The documentation says this is excluded from optimization; repeated reporting nevertheless needs an audit of selection decisions before treating the final curve as a one-time sealed test. Paper §7.2 restricts its standalone edits to instructions and skills; the released general algorithm also supports Python-harness proposals. These are related implementations within one family, not interchangeable experiments. No released run ledger or raw result directory was found in the repository tree inspected at this commit. Task assets and weights are supplied separately.

## Appraisal and limitations

### Authors' claim

Coupled procedural and parameter learning supports continual scientific assistance.

### Interpretation and limitations

Fresh, relevant cross-surface demonstration. Simulated procedural feedback in the experiment differs from real researcher case studies. Stronger fixed helper models assist harness changes. Different splits/metrics prevent adding the gains. §4.2 heading says two cycles while text/figure say three: flag this editorial discrepancy. No proof that the improver itself strengthens.

## Discussion and follow-up

### Inspect/discuss

Figures 8–10 and Appendix 7.2 information boundaries.

### Revised priority

Retain as a frontier reserve and transparency case; do not rank its largest gain ahead of better-audited split/budget evidence solely because it is the newest paper.

[Prominent citations and their roles](../prominent-citations.md#sciencebuddy)
