---
marp: true
theme: default
paginate: true
style: |
  section { font-size: 24px; }
  h1 { font-size: 36px; color: #2d3436; }
  h2 { font-size: 28px; color: #636e72; }
---

# MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution
**Lin, Zhang, Lu, Liu, Tang, He, Zhang, Wang** -- Penn State / Amazon / Microsoft (Mar 2026)

- **Problem:** Memory-augmented LLM agents treat construction, retrieval, and utilization as isolated subroutines. This causes *strategic blindness* (myopic construction + aimless retrieval on the forward path) and *sparse delayed feedback* (downstream failures never repair the memory bank on the backward path)
- **Forward path -- planner-worker architecture:**
  - **Meta-Thinker** produces strategic guidance for what to store/consolidate/resolve
  - **Memory Manager** executes atomic edits (ADD/UPDATE/DELETE) steered by Meta-Thinker
  - **Query Reasoner** performs iterative retrieval guided by Meta-Thinker's gap diagnosis (not just semantic similarity rewrites)
- **Backward path -- in-situ self-evolution:**
  - After each session, synthesize probe QA pairs, verify memory against them, and convert failures into repair actions (SKIP/MERGE/INSERT) *before* committing memory
- **Plug-and-play:** Works on top of any storage backend (Single-Agent, A-Mem, LightMem)

---

# Key Results

Evaluated on LoCoMo benchmark (long-horizon conversational memory), GPT-4o-mini backbone:

| Method | F1 | BLEU-1 | ACC (LLM Judge) |
|---|---|---|---|
| Full Text | 34.13 | 24.63 | 61.18% |
| Naive RAG | 27.14 | 20.41 | 46.05% |
| A-Mem | 37.90 | 28.85 | 52.63% |
| LightMem (best baseline) | 44.58 | 36.66 | 75.66% |
| **MemMA + LightMem** | **49.40** | **38.28** | **81.58%** |

- **+5.92 ACC over already-strong LightMem baseline** (75.66 -> 81.58)
- **Plug-and-play gains across all backends:** Single-Agent 52.60 -> 84.87 ACC (+32.27!), A-Mem 52.63 -> 78.29 (+25.66)
- **Ablations reveal iterative retrieval is most critical:** Removing it drops ACC from 84.87 -> 70.39 (-14.48). Self-evolution removal: 84.87 -> 73.68 (-11.19)
- **Retrieval refinement converges fast:** 1-2 rounds optimal (ACC peaks at H=2: 85.53), further iterations cause drift
- **Multi-hop QA sees largest gains:** ACC jumps from 65.62 to 78.12 (+12.5), consistent with diagnosis-guided retrieval recovering distributed evidence

---

# Open Questions & Discussion

- **Evaluation is narrow:** All results on a single conversation (conv-26) from LoCoMo with 152 QA pairs after excluding adversarial samples. Hard to know if gains generalize
- **Cost analysis is missing:** MemMA adds a Meta-Thinker call for every construction step and every retrieval iteration, plus probe generation + verification after each session. How many extra LLM calls does this add? What is the latency/cost overhead?
- **The "memory cycle" framing is useful beyond this paper:** The forward-path (construction constrains retrieval constrains utilization) and backward-path (utilization failures should repair construction) decomposition applies to any system with persistent state
- **Self-evolution is essentially test-driven memory:** Generate tests (probe QA), run them against memory, fix failures. This is an elegant pattern -- but relies on the quality of synthetic probes
- **Relevance for multi-agent systems:** The Meta-Thinker/Manager/Reasoner split is a clean separation of strategic planning from execution. The key lesson: agents that "do things" to memory need a separate agent that "thinks about what to do" -- local heuristics produce myopic behavior
