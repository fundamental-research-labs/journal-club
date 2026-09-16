# Presentation handoff: from experience to durable improvement

September 16, 2026. Audience: familiar with LLM basics. Duration: 45 minutes, including 10 minutes of discussion. Topic-wide argument; papers provide evidence for questions. [Thesis](thesis.md) · [Claim ledger](claims.md). No deck requested or created.

**Opening question:** If an agent improves its score after changing itself, what would convince you it learned something useful for tomorrow?

**Takeaway:** Useful self-evolution exists in bounded settings. Its value rests on changes that remain helpful on later work after costs and regressions are counted; general recursive acceleration requires stronger evidence.

| Beat / time | Argument and evidence | Suggested visual / claim trace |
| --- | --- | --- |
| B1 · 0–3 min | Pose the opening question. Distinguish solving a task from retaining a useful change. | Two runs: identical fresh agent versus agent carrying an update. C001, C011. |
| B2 · 3–8 min | Define memory/skills, harness (prompts, tools, orchestration), weights, curriculum, and improver. Show what is editable and what supplies feedback. Establish the dated trend without implying a linear march. | One loop diagram with selectable update locations; annotated 2023/2025/2026 timeline. STOP prevents calling meta-improvement entirely new. C001–C002. |
| B3 · 8–15 min | Show that useful learning is possible. WikiSkill illustrates persistent knowledge; SEAL contrasts weights. FinEvo's retained/reset pair supplies the main control. | Mechanism sketches, then a FinEvo paired-stream diagram. Keep WikiSkill accuracy and FinEvo rubric scores in separate panels. C003–C005. |
| B4 · 15–20 min | Ask what else the same resources could buy. Introduce the harness sampling result, then FinEvo's strong static skill. | Two separate comparisons: evolution versus sampling; static expertise versus continued updates. Preserve distinct protocols and units. C005–C006. |
| B5 · 20–26 min | Test whether gains last. Mixed streams can regress; more curriculum updates can pass the best checkpoint. | AgentStream scenario means with explicit shared-task/SD caveat; R-Zero Table 6 trajectory at steps 15/30/45/60. Label causal explanations as hypotheses. C004, C007–C008. |
| B6 · 26–31 min | Give the strongest recursive interpretation a fair test. Explain task agent versus improver; compare Hyperagents with Dream-RSI's history replay. | Nested loops, keeping evaluator and budget outside editable code. Separate controller transfer from transfer of a discovered solver. Show nonsignificant endpoint qualification. C009. |
| B7 · 31–35 min | Connect to practice through Shopify's reported pipeline. Define useful benefit after adaptation and serving costs. | Production loop with shared judge highlighted; “company-reported architecture, causal efficacy unresolved.” No cost-savings headline. C010, C012. |
| B8 · 35–45 min | State the preferred thesis, present the specialization/compute objection, then let the group design a decisive test. | Four experimental arms from thesis.md; choose one held-out unit, one regression threshold, and one budget. C005–C006, C011–C012. |

Minimum background: retained state versus frozen state; development/validation/test separation; why more attempts and more learning differ; meaning of a paired reset control. Introduce these at the moment each comparison needs them.

The decisive results are the positive FinEvo persistence comparison, the negative harness budget comparison, and the R-Zero peak-to-terminal decline. They answer different questions and must never be combined into an overall leaderboard. WikiSkill and SEAL establish mechanism breadth; Hyperagents/Dream-RSI address the stronger counterargument.

Discussion should invite a decision: Would we deploy the updating agent over a static skill? What new task distribution must it survive? What would distinguish a better improver from additional search? Use the five evidence-linked questions in thesis.md as prompts; leave time for disagreement.

Presentation constraints: cite source version and table/section near each result; retain sample sizes and uncertainty qualifications in notes. Do not label AgentStream SDs as CIs, FinEvo rubric gains as percentage accuracy, or Hyperagents' nonsignificant endpoint as confirmed compounding. Keep GEPA arithmetic, R-Zero disputed aggregates, and provisional MetaRSI/ScienceBuddy headline results out of decisive charts. Independent replication and complete cost accounting remain missing. Refresh only for a changed cutoff or a specific unresolved claim.

Ready for presentation development within these bounds. Next stage should build editable slides, preserve the claim mapping, and visually verify the deliverable if requested.
