# autoresearch

[Repository snapshot](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117), Andrej Karpathy; March 2026 project, inspected commit March 26. Accessed September 16; README re-read. Family: autoresearch, including linked social announcements.

**Question/design.** What is the smallest inspectable autonomous experiment loop? Modify training code, run a fixed-duration experiment, score validation bits per byte, retain or reject changes.

**Observed artifact.** README separates editable training code from preparation/evaluation utilities and human-directed program instructions. The fixed training interval is five minutes; it is not the entire wall-clock cost of proposal, evaluation setup, and research.

**Authors' framing.** Automated experimentation can search for improved training configurations.

**Interpretation/limits.** Excellent example of specifying the editable artifact and fixed evaluator. Better training code or a trained model is not automatically evidence that the experiment-generating agent improves. No controlled general-effect estimate or reproduction here.

**Social access.** [Announcement](https://x.com/karpathy/status/2030371219518931079) failed direct web retrieval again; [follow-up](https://x.com/karpathy/status/2031135152349524125) retains the earlier access limitation. Exact post dates unverified; no quotations or numerical claims imported.

**Inspect/discuss.** README experiment contract. Is the output an improved artifact, an improved agent, or an improved learning process?
