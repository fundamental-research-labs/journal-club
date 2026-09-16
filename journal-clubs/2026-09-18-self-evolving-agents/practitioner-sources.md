# Practitioner resources and original artifacts

**Updated September 16, 2026.** These resources are part of the topic, alongside papers. The useful distinction is what can be inspected: a measured comparison, a working implementation, a demo, a design proposal, or an opinion. A publication format alone does not determine evidence quality. All reported measurements below remain the source authors' results; none were independently reproduced.

## Priority resources

| Resource / date | What it contributes | Evidence and limits |
| --- | --- | --- |
| **Shopify, [Sidekick's continual learning loop](https://shopify.engineering/sidekicks-continual-learning-loop)** — Aug 5, 2026 | Production account spanning harness search, trajectory repair, SFT, GRPO, daily weight updates, and prompt compression. Selected among the ten because it connects the research mechanisms to deployment. | Original article read. Public quality ablations, denominators, split manifests, and raw training traces are absent. Serving economics are not causal estimates of the learning loop's benefit. [Detailed note](research/notes/2026-shopify-sidekick.md). |
| **NVIDIA, [Building a Memory-Driven Agent with NVIDIA NemoClaw](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/)** — Sep 4, 2026; repository pinned Sep 16 | Readable Markdown knowledge, a judgment ledger, and updates from user corrections; public evaluation artifacts expose category-level gains and regressions. | Same Nemotron 3 Ultra backbone, **186 synthetic questions**, reported **90.9% vs 82.8%**. Faithfulness **100→92.3% on 13 questions**; single-hop **86.7→83.3% on 30**. One run/corpus, missing evaluated self-model adapter/memory, and incomparable ingestion accounting. Original/published transformed-answer results differ; both are preserved in [note and artifacts](research/notes/2026-nemoclaw-memory.md). |
| **Human-Agent Society, [Reef](https://github.com/Human-Agent-Society/reef)** — September 2026 release; pinned `401db36` | Delayed-feedback attribution, actor lineage, versioned candidates, inference receipts, and recipes for improving harnesses. | Code and original result records read; not executed. Meta-harness uses 30 tasks × two repeats, four outer iterations. Fresh selected-candidate comparison **22/60 vs 21/60 on the same tasks**; no held-out transfer and no statistical separation established. Small Apache-2.0 originals retained. [Detailed note](research/notes/2026-reef.md). |
| **Andrej Karpathy, [autoresearch](https://github.com/karpathy/autoresearch)** — repository inspected Sep 16 | A compact loop: modify training code, run a fixed experiment, measure, keep/revert, repeat. Useful for explaining the machinery required before calling a loop self-improvement. | Primary code/instructions inspected. Model experiments run under a fixed evaluation recipe; the repository is not evidence of autonomous general-purpose recursive improvement. [Detailed note](research/notes/2026-autoresearch.md). |
| **NVIDIA, [SoL-Pi](https://github.com/NVIDIA/SoL-Pi)** — September 2026 release; pinned Sep 15 commit | Concrete reusable harness-efficiency mechanisms and engineering choices. | README/code documentation inspected; a full empirical recipe was not independently audited and a paper was forthcoming in the inspected release. [Detailed note](research/notes/2026-sol-pi.md). |

## Useful engineering explanations and proposals

**Nous Research: [Hermes Agent skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).** Live documentation inspected September 16; publication date not established. Documents skill creation, update, and deletion with procedural reuse. It establishes functionality, not an effect size or long-term reliability. Pair it with WikiSkill and Library Drift: storage helps only if the procedure remains correct, applicable, and available at use time.

**Jake Broekhuizen / LangChain: [How To Give Your Agent Memory](https://www.langchain.com/blog/how-to-give-your-agent-memory), June 24, 2026.** Original article read. Trace capture, background analysis, and versioned context make the learning loop concrete. The inspected account provides engineering guidance rather than a controlled benchmark estimate. Its runtime-context issue matters: writing an improved memory is insufficient if later executions keep using stale context.

**Kirill Krainov: [Karpathy's Autoresearch: Improving Agentic Coding Skills](https://zerocopy.blog/2026/03/25/karpathys-autoresearch-improving-agentic-coding-skills/), March 25, 2026.** Original proposal read. Edits a skill, repeats test cases, scores correctness/time/cost, and retains or reverts changes. The article defers a working implementation and results; classify it as a proposal. Its additive scoring scheme prompts a useful discussion about whether efficiency should ever compensate for correctness failures.

Additional practitioner candidates and exclusions remain in the [source register](research/sources.md). Broadly promotional material and uninspectable claimed successes were not promoted merely because they describe “self-improving agents.”

## Paper-linked implementations are companions, not replications

- [Hyperagents code](https://github.com/facebookresearch/Hyperagents) was pinned and its statistical routine inspected. Equal-length run arrays use one-sided paired Wilcoxon tests; bootstrap intervals use run-level resampling. This resolves interpretation of the paper, without reproducing its experiments. [Audit](research/notes/2026-hyperagents.md).
- [ScienceBuddy code](https://github.com/Gen-Verse/ScienceBuddy) was pinned to `454d11c`; small MIT-licensed experiment/algorithm guides and configuration retained. The released split includes source-material overlap, and its schedule differs from the paper; its 90-task test count must not be assigned retrospectively to historical paper curves. [Audit](research/notes/2026-sciencebuddy.md).
- [MetaRSI's RSI-Harness](https://github.com/CosmosMind-AI/RSI-Harness) was inspected for experimental ledgers. A runnable-looking harness and accounting conventions do not replace actual per-variant split/cost records. [Audit](research/notes/2026-metarsi.md).
- [Dream-RSI](https://github.com/zhengkid/Dream-RSI) had a paper, images, and README in the inspected September 16 snapshot, with implementation forthcoming. Its animated demo labels its numbers illustrative. [Audit](research/notes/2026-dream-rsi.md).

## Talks, project pages, and X/Twitter

The [dated talks/social audit](research/workers/talks-social-audit.md) records original institutional/project pages for SEAL, Absolute Zero, and Hyperagents, along with an unverified video lead. SEAL's [MIT CSAIL article](https://www.csail.mit.edu/news/teaching-large-language-models-how-absorb-new-knowledge) is useful institutional context; it is not an independent evaluation.

No video was watched and no transcript was available in this pass. A YouTube description naming the SEAL authors did **not** establish the speaker or channel's provenance; that video is excluded from the evidence set. Original X/Twitter retrieval was unsuccessful for the selected research families. [The previously discovered Karpathy post](https://x.com/karpathy/status/2039805659525644595) remains an inaccessible lead, not verified content or a quotation. Project demonstrations and search snippets do not substitute for paper methods or original run artifacts.

## Reuse and access

Small unmodified Reef, NemoClaw, and ScienceBuddy artifacts are retained under their repository licenses. The [originals manifest](research/originals/manifest.json) records exact URLs, pins, dates, licenses, and hashes. Captures are deliberately partial; relative upstream links inside an original README may refer to files not copied here. Copyrighted blog pages and inaccessible posts are linked rather than archived without permission.
