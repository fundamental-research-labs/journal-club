# SelfMem: Self-Optimizing Memory for AI Agents

## Source and access

**Source key:** `2026-selfmem`.

**Originals and source links:** [register](../sources.md#2026-selfmem); [canonical source](https://arxiv.org/abs/2607.03726). Retained unmodified: [2026-selfmem-paper-v1.pdf](../originals/2026-selfmem/2026-selfmem-paper-v1.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

. [arXiv v1](https://arxiv.org/abs/2607.03726v1); [PDF](https://arxiv.org/pdf/2607.03726v1). Shu Yang et al.; July 4, 2026 preprint. Read September 16, 2026: full paper, main experiment, refinement analysis, and appendices inspected.

## Question and methods

### Question and method

Rather than impose fixed add/update/delete rules, SelfMem gives an LLM transcript access plus read/review/write tools and lets it construct and revise a workspace. A later study iteratively refines natural-language memory-strategy notes using aggregate training feedback (§§3, 5).

### Evaluation

The original BEAM benchmark supplies 100 conversations and 2,000 probing questions at 100K, 500K, and 1M tokens (§4.1). Questions are sequential and prior model answers enter later prompts. All memory construction and answering uses GPT-5.4-nano; GPT-5.4-mini is the official judge; temperature is 0. The main comparison shares conversations, questions, answerer, and judge across methods. Cost is token-derived API cost and includes answer/judge calls, excluding token-count requests (Table 1). The strategy-refinement study uses conversations 0–8 for feedback and 9–19 as held-out tests, only at 100K (§5).

## Results and evidence

Table 1 reports SelfMem Score/Pass0.5 of .504/59.0 at 100K, .487/57.0 at 500K, and .454/52.57 at 1M. RAG, the strongest score baseline, obtains .339/.346/.320, giving absolute score gains .165/.141/.134. At 1M, SelfMem costs $2.004 with 4,040 LLM requests and no embedding requests; RAG costs $1.843 with 74,153 embedding requests, while Mem0 costs $18.830 and scores .292. No confidence intervals or independent repetitions are reported. Figure 4's 100K refinement starts at held-out .472, ends at .497, and peaks at .510 at an intermediate iteration; average progress is non-monotonic.

## Appraisal and limitations

### Authors' claim

Agent-controlled memory construction outperforms fixed pipelines at long context lengths and exposes a useful space for strategy optimization.

### Interpretation and limitations

The shared harness and explicit cost columns make this a strong BEAM comparison. It remains memory QA, not evidence that a task-performing agent improves. One answerer/judge family, sequentially conditioned probing, and absent uncertainty limit the strength of small differences. The refinement test uses only 11 held-out conversations and one context scale; selecting the best observed strategy would itself require a validation protocol. The paper acknowledges the single benchmark/model family and shared-harness implementation limits. Ground Truth First is a credible challenge because it tests validity intervals, eviction, provenance, and judge robustness rather than only long-context recall.

## Discussion and follow-up

### Useful discussion/figure

Pair Table 1 with Figure 4: a flexible memory environment improves the benchmark, yet more optimization iterations do not monotonically improve the held-out score.
