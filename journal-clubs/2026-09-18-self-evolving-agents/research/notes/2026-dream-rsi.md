# Dream-RSI: Recursive Self-Improvement through Evolving Worlds

## Source and access

**Source key:** `2026-dream-rsi`.

**Originals and source links:** [register](../sources.md#2026-dream-rsi); [canonical source](https://arxiv.org/abs/2609.14858v1). retention-restricted. [Manifest](../originals/manifest.json).

**Key:** `2026-dream-rsi`. Tong Zheng, Xidong Wu, Zheng Zhang et al. [arXiv v1](https://arxiv.org/abs/2609.14858v1), first submitted September 14, 2026; preprint. [Full text](https://arxiv.org/html/2609.14858v1), [PDF](https://arxiv.org/pdf/2609.14858v1), [official project](https://www.dream-rsi.com/). Coordinator read §§2–5 and inspected Appendix B’s policy interface on September 16. Paper/code/project/demo belong to one evidence family.

**Acquisition/access:** original arXiv PDF downloaded and opened temporarily. ArXiv labels it perpetual non-exclusive, so no repository copy retained. The [official repository snapshot](https://github.com/zhengkid/Dream-RSI/tree/4149ea9181ab1db80f85717ffda2c9f0f130e85b) (September 16 10:32 UTC) contains a paper, images, and README, but no implementation; README says code is being prepared. Its alternative [author-hosted original PDF](https://github.com/zhengkid/Dream-RSI/blob/4149ea9181ab1db80f85717ffda2c9f0f130e85b/papers/Dream-RSI.pdf) has no separately established redistribution license. The project’s animated live demo explicitly uses illustrative numbers; it is not run evidence. No implementation or experiment reproduced.

## Question and methods

Can an exploration controller improve using historical discovery traces without paying for every new candidate policy to run online? A frozen coding agent executes proposals under a controller that selects branches, concurrency, and stopping. Each completed discovery tree becomes an exact replay of its **recorded outcomes**. A fixed policy-development LLM edits the controller; candidate controllers are scored by traversing recorded trees; the selected controller then runs online and adds a new tree. No new outcomes are generated during replay (§3). The changing state is exploration-policy code and the history pool, not base-model weights or the evaluator.

The objective combines best recorded task quality, a penalty for represented generation/evaluation requests, and a parallelism bonus (Equation 1). Including the incumbent policy guarantees no worse score **on the fixed replay history**, not monotonic improvement on future online samples. An observed branch’s deterministic replay is not an unbiased simulator of every unobserved alternative; that distinction is central to the discussion.

## Results and evidence

### Setup and measured results

Eight tasks span one algorithm-engineering problem, three mathematical objectives, and four GPU kernels. The principal controlled baseline uses the same discovery agent, initialization, first-round policy, and per-round ceilings, but keeps exploration fixed thereafter (§4).

**Lasso, Figure 3 / §4.1:** discovery uses 17 synthetic instances and evaluates discovered solvers on six held-out real datasets. Five outer rounds. Gemini-3.1-Pro fixed exploration uses 550 discovery-agent calls and achieves 3,587.1 ms average downstream runtime; Dream-RSI uses 317 calls and achieves 2,931.0 ms. Gemini-3.7-Flash uses 3,200→1,879 calls and 2,516.7→2,350.6 ms. The Pro result corresponds to 1.735× fewer calls and an 18.3% lower mean runtime, calculated from printed values. It regresses on some individual datasets: e.g. Gisette 1,861.8→2,841.0 ms, despite the aggregate improvement. The six datasets are downstream test instances, not six independent policy-training runs.

**Mathematics, Table 1 / §4.2:** ten rounds with Gemini-3.1-Pro. Dream-RSI versus fixed exploration: Sum–Difference 1.145427 vs 1.144047 (higher better); autocorrelation 1.456375 vs 1.456001 (lower better, therefore a regression); circle packing ties at 2.635983. Cross-system baselines use different models and budgets.

**Kernels, Figure 4 / §4.3:** VGG16/LayerNorm reach comparable performance with 2.43×/1.79× fewer generations; ConvDiv/ConvMax report 2.09×/1.44× higher inverse-runtime performance at comparable budgets. These are different endpoints—generation savings and solution speedup—not interchangeable percentages.

**History ablation, Figure 5 / §5.1:** on ConvDiv, converting history into semantic guidance underperforms the corresponding unguided system. This is a narrow counterexample to assuming that more textual lessons always help.

## Appraisal and limitations

### Authors' claim

Replay makes recursive exploration-policy refinement cheaper and improves discovery quality/cost tradeoffs. **Evidence:** controlled fixed-policy comparisons, downstream Lasso transfer, explicit interface/objective, and both positive and negative individual outcomes. **Interpretation:** a strong new mechanism to pair with Hyperagents; still emerging evidence, not a demonstrated indefinitely accelerating agent.

Reported discovery cost counts **discovery-agent calls**. It does not supply a complete equal-dollar, token, GPU-hour, policy-development, or replay-compute ledger. The frequently advertised 162× comparison uses SimpleTES with a different underlying model; prefer the within-model 550/317 comparison. Independent repeated-run counts, intervals, and seed schedules were not found in the reviewed methods/results or text search. Five/ten recursive rounds are not independent repetitions. Historical selection can overfit the finite replay pool, and successful transfer to unseen tasks is tested more clearly for the Lasso artifact than for the exploration controller across entirely new domains.

## Discussion and follow-up

Which parts of history are sufficient for valid off-policy evaluation? What held-out history or online trials would distinguish a better controller from a controller specialized to its replay trees?
