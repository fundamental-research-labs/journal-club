# Claims

## Claim 1: WorkArena fills an enterprise-software gap in web-agent evaluation.
**Claim:** Existing web-agent benchmarks underrepresent routine enterprise knowledge-work tasks, and WorkArena provides a realistic ServiceNow-based benchmark for that setting.

**Evidence:** The benchmark covers 33 task types and 19,912 instances over ServiceNow interactions including lists, forms, knowledge bases, service catalogs, dashboards, and menus. The paper motivates ServiceNow as a widely used enterprise platform and implements tasks on real cloud-based Personal Developer Instances.

**Caveats/Scope:** WorkArena is broad within ServiceNow-style business workflows but is still one platform, not a complete sample of all enterprise software. Some task content, especially knowledge-base articles/questions, is generated.

**Source pointers:** PDF abstract; Section 1; Section 3; Section 3.3; Appendix A.1 Table 6

## Claim 2: Real enterprise UIs make superficially simple tasks difficult for browser agents.
**Claim:** WorkArena tasks are high-level routine actions, but their underlying interfaces expose hard web-agent problems: dynamic widgets, non-standard HTML, large DOM/AXTree observations, and complex interactions.

**Evidence:** Section 3.2 lists non-standard dynamic UIs, exotic HTML with nested iFrames/shadow DOMs, and page observations reaching tens or hundreds of thousands of tokens. In the results, all evaluated models score 0% on list-filter tasks despite those being conceptually simple for humans.

**Caveats/Scope:** The 0% list-filter result reflects the tested agent designs, model versions, and 15-step episode cap; stronger agents or ServiceNow-specific tools could change the outcome.

**Source pointers:** PDF Section 3.2; Section 5.3; Table 2; Appendix A.2 Figure 5

## Claim 3: Closed-source frontier models substantially outperform the tested open and older closed models on WorkArena.
**Claim:** GPT-4o is much more capable than GPT-3.5 and Llama3-70B in the WorkArena browser-control setting.

**Evidence:** Table 2 reports WorkArena success rates of 42.7% for GPT-4o, 6.1% for GPT-3.5, and 17.9% for Llama3-70B; the paper highlights that the gap is larger on WorkArena and WebArena than on MiniWoB.

**Caveats/Scope:** This is a 2024 model comparison with a single agent architecture and tuned configurations. It does not establish a permanent closed-source advantage.

**Source pointers:** PDF Section 5.1; Section 5.2; Section 5.3; Table 2

## Claim 4: BrowserGym provides a reusable harness for web-agent benchmarks and agent design studies.
**Claim:** BrowserGym is intended as a unified environment for building and evaluating browser agents across multiple benchmarks.

**Evidence:** BrowserGym exposes chat messages, URLs, action errors, HTML, accessibility trees, screenshots, augmented element identifiers/coordinates, tab support, and customizable action spaces. The experiments use it for WorkArena, MiniWoB, and WebArena.

**Caveats/Scope:** BrowserGym is an environment, not a complete solution to agent memory or reasoning; the paper explicitly notes that agents still need their own memory mechanisms.

**Source pointers:** PDF Section 4; Section 4.1; Section 4.2; Appendix B.1 Table 10

## Claim 5: More agent-interface features do not automatically improve performance.
**Claim:** Browser-agent performance depends on matching features to the task and model; adding screenshots, coordinate actions, longer action descriptions, or thought history can be neutral or harmful.

**Evidence:** The ablation tables show chain-of-thought helps across models, but GPT-4o's WorkArena score drops in tested variants with multi-actions, coordinate actions, or thought history. The paper also reports that the GPT-4o vision variant provides only minor changes and slightly underperforms text-only GPT-4o on WorkArena overall.

**Caveats/Scope:** These ablations are tied to the paper's prompting and action-space design, and the authors note that some features help on other benchmarks or tasks requiring 2D interaction.

**Source pointers:** PDF Section 5.4; Tables 3-5; Table 2
