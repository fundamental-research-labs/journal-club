# Reef

[First-party announcement](https://huggingface.co/blog/quao627/your-inference-server-is-secretly-a-learner-reef), Ao Qu and collaborators, September 15, 2026; [repository snapshot](https://github.com/Human-Agent-Society/reef/tree/401db3670d34b1b5a77989234272e0bee4b90ce8), September 16. Accessed September 16; article and substantial README sections read. Web reader failed on the article; direct HTTP retrieval succeeded. Family: Reef.

**Question/design.** How does serving traffic become reusable learning evidence? Record inference receipts, attach delayed feedback, run learning recipes, evaluate candidates, and version accepted weight or harness changes.

**Observed artifact.** README maps serving, feedback matching, training, evaluation, and artifact delivery to modules; lists separate model and harness recipes and links recipe-level results. Code existence and documented interfaces were inspected; modules and results were not executed or comprehensively audited.

**Authors' claim.** Infrastructure can support continuous improvement of the whole agent.

**Interpretation/limits.** Useful implementation evidence about feedback attribution, versioning, and deployment. It does not supply a single controlled estimate of “Reef improvement,” and recipe results should not be pooled. The documentation's comparisons with other infrastructure are authors' characterizations, not independently verified exclusions.

**Inspect/discuss.** README architecture and recipe catalog. What prevents stale feedback from promoting a change to the wrong system version? Any demo remains separate from a longitudinal reliability test.
