---
marp: true
theme: default
paginate: true
style: |
  section { font-size: 24px; }
  h1 { font-size: 36px; color: #2d3436; }
  h2 { font-size: 28px; color: #636e72; }
---

# DELEGATE-52: LLMs Corrupt Your Documents When You Delegate
## Philippe Laban, Tobias Schnabel, Jennifer Neville -- Microsoft Research -- April 2026

- **Problem**: As "vibe coding" and delegated work expand, can LLMs faithfully edit documents without silently introducing errors? This paper says: no.
- **Benchmark**: 310 work environments across **52 professional domains** (crystallography, music notation, accounting ledgers, 3D objects, weaving patterns, etc.). Each environment has real documents (~3-5k tokens) + 5-10 complex, reversible editing tasks + distractor context (8-12k tokens).
- **Evaluation method -- Round-trip relay**: Apply a forward edit then its inverse; a perfect model recovers the original exactly. Chain 10 round-trips (20 interactions) to simulate long delegation. Measure reconstruction score (RS@k) via domain-specific parsers -- no reference annotations needed.
- **Key insight**: Backtranslation-as-evaluation lets you scale to 52 diverse domains without expert annotation, and errors compound over sequential interactions.

---

# Key Results

- **19 LLMs tested**: Even frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4) corrupt **25% of document content** by interaction 20. Average degradation across all models: **50%**.
- **Best model**: Gemini 3.1 Pro retains 80.9% at RS@20. Claude 4.6 Opus: 73.1%. GPT 5.4: 71.5%.
- **"Ready" threshold (RS@20 >= 98%)**: Python is the **only domain** where most models pass. Gemini 3.1 Pro is ready in only **11 of 52 domains**. Catastrophic corruption (>20% loss) in **80%** of model-domain combinations.
- **Agentic tool use makes it worse**: Models with a basic ReAct harness (file read/write/code execution) degrade documents **6% more** than without tools. Overhead of 8-12 tool calls per task, 2-5x more input tokens.
- **Document size compounds with interaction length**: GPT 5.4 goes from 91.4% (1k tokens, RS@20) to 59.9% (10k tokens, RS@20). Each extra 1k tokens costs ~0.7% after 2 interactions but ~3.6% after 20 -- a 5x compounding effect.
- **100-interaction extended relays**: Degradation never plateaus. GPT 5.4 drops to 58.7% at 100 interactions.
- **Error pattern is sparse but severe**: ~80% of total degradation comes from critical failures (>=10pt drop in a single round-trip), not gradual "death by a thousand cuts". Stronger models delay critical failures rather than avoiding small errors.
- **Deletion vs. corruption**: Weaker models primarily *delete* content; frontier models primarily *corrupt* content (elements present but incorrect).

---

# Open Questions & Discussion

- **Is backtranslation a fair proxy?** Round-trip evaluation assumes every task is reversible and that reconstruction quality maps to delegation quality. Real work involves non-reversible edits, partial modifications, and creative tasks where "original recovery" is not the goal.
- **Basic agentic harness is a weak baseline**: The paper's tool-use experiment uses a minimal ReAct loop. More sophisticated agent architectures (diff-based editing, structured output, verification loops) might dramatically reduce corruption -- the paper acknowledges this but does not test it.
- **Short-term metrics don't predict long-term behavior**: GPT 5 and Kimi K2.5 start nearly identical at 2 interactions (91.5 vs. 91.1) but diverge to 48.3 vs. 64.1 by interaction 20. Standard single-turn benchmarks would miss this entirely.
- **For multi-agent system builders**: This is a strong argument for treating document state as immutable + applying diffs rather than asking LLMs to regenerate entire documents. The compounding error pattern means even small per-step corruption rates become catastrophic over multi-step workflows. Verification gates (like Refute-or-Promote's empirical validation) become essential.
- **Encouraging trajectory**: GPT 4o -> GPT 5.4 (16 months apart) improved RS@20 from 14.7% to 71.5%. If this pace continues, delegation-ready models across most domains may arrive within 1-2 years.
