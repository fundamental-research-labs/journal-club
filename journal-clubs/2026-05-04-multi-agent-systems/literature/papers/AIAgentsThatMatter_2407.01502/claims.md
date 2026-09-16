# Claims

## Claim 1: Agent evaluations must be cost-controlled.
**Claim:** Accuracy-only agent leaderboards can reward expensive inference strategies rather than better agent designs.

**Evidence:** The paper re-evaluates LDB, LATS, and Reflexion-style HumanEval agents alongside zero-shot, retry, warming, and escalation baselines, reporting both accuracy and total API cost. Figure 1 and Table A1 show that simple baselines can match or Pareto-improve over complex agents while costing much less in some comparisons.

**Caveats/Scope:** The empirical result is from HumanEval and the reproduced agents/versions tested by the authors. Dollar costs depend on model prices at the time of evaluation, and harder coding tasks may change the value of more complex control flow.

**Source pointers:** `paper.pdf`, Sections 2.1-2.3; Figure 1; Appendix A; Table A1.

## Claim 2: Jointly optimizing cost and accuracy can improve agent design.
**Claim:** Treating cost and accuracy as a joint optimization problem can reduce variable inference cost while preserving measured performance.

**Evidence:** In the HotPotQA/DSPy case study, the authors use Optuna to search over temperatures, few-shot examples, example counts, and formatting instructions. They report that joint optimization lowers variable cost by 53% for GPT-3.5 and 41% for Llama-3-70B compared with default DSPy implementations while maintaining similar accuracy.

**Caveats/Scope:** This is an illustrative optimizer on a multi-hop retrieval setup, not a general proof that all agent tasks admit the same savings. The fixed optimization cost must be amortized over enough uses, and price changes affect dollar-denominated conclusions.

**Source pointers:** `paper.pdf`, Sections 3.1-3.2; Figure 2; Appendix B; Table A3; Figure A6.

## Claim 3: Downstream agent evaluation should use actual usage costs.
**Claim:** Benchmarks for downstream selection should report dollar costs and token counts rather than relying on model-evaluation proxies such as parameter count or training compute.

**Evidence:** Section 4 distinguishes model evaluation, where timeless scientific comparison may avoid dollar prices, from downstream evaluation, where procurement decisions depend on current API costs. The NovelQA case study shows that the benchmark's batch-style long-context setup makes retrieval-augmented generation look less cost-effective than it would be for sequential user questions.

**Caveats/Scope:** NovelQA is used as a case study, and the authors ran the expensive NovelQA comparison once. The point is about benchmark construct validity for downstream use, not a claim that NovelQA's original model-evaluation goal is invalid.

**Source pointers:** `paper.pdf`, Section 4; Section 4.1; Appendix D; Table A5.

## Claim 4: Holdouts must match the intended generality of an agent benchmark.
**Claim:** Agent benchmarks need held-out samples, tasks, or domains at the appropriate level of generality to prevent agents from exploiting shortcuts.

**Evidence:** The paper proposes four levels of benchmark generality and maps each to an appropriate kind of holdout. Its survey of 17 agent benchmarks reports that 7 lack holdouts and do not indicate plans to add them, and that only 5 of 10 existing holdout sets are at the appropriate generality level.

**Caveats/Scope:** The benchmark survey involves judgment calls about each benchmark's intended level of generality, and some benchmark developers may have narrower goals than their leaderboards suggest.

**Source pointers:** `paper.pdf`, Section 5; Table 1; Appendix C; Table A4.

## Claim 5: WebArena-style leaderboards can overstate real-world web-agent capability.
**Claim:** A high WebArena score can reflect brittle task-specific policies rather than robust web automation.

**Evidence:** The WebArena/STeP case study notes that STeP was the top WebArena agent at 35.8% accuracy and used hardcoded policies for specific benchmark tasks, such as constructing Reddit profile URLs from known task structure. The paper argues that such policies would be vulnerable to website drift and unseen tasks, while WebArena lacks a held-out set for those shifts.

**Caveats/Scope:** The authors explicitly note that STeP's design can make sense for fixed tasks known in advance; the critique is about interpreting leaderboard accuracy as evidence of broad downstream capability.

**Source pointers:** `paper.pdf`, Section 5.1; Appendix C; Table A4.

## Claim 6: Agent evaluation standardization is currently inadequate.
**Claim:** Inconsistent benchmark versions, environment effects, and evaluation bugs make agent leaderboard results hard to reproduce or compare.

**Evidence:** Section 6 identifies five root causes, including evaluation scripts that assume particular agent designs, repurposed LLM benchmarks, expensive runs that limit confidence intervals, external environment effects, and bugs. Table A6 documents concrete HumanEval and WebArena issues, and Table A7 compares reported and reproduced HumanEval accuracies.

**Caveats/Scope:** The documented issues come from the authors' selected reproduction attempts and are often attributed to insufficient benchmark standardization rather than bad-faith agent developers.

**Source pointers:** `paper.pdf`, Section 6; Appendix E; Table A6; Table A7.
