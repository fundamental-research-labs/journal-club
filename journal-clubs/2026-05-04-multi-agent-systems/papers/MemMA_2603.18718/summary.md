# MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution

**Authors:** Minhua Lin, Zhiwei Zhang, Hanqing Lu, Hui Liu, Xianfeng Tang, Qi He, Xiang Zhang, Suhang Wang
**arXiv:** 2603.18718
**Venue:** Preprint
**Date:** March 2025

## Problem
Memory-augmented LLM agents treat memory construction, retrieval, and utilization as isolated subroutines. This causes two problems: "strategic blindness" on the forward path (construction and retrieval driven by local heuristics rather than strategic reasoning) and sparse, delayed supervision on the backward path (downstream failures rarely translate into repairs of the memory bank itself).

## Method
MemMA is a plug-and-play multi-agent framework that coordinates the full memory cycle along forward and backward paths. On the forward path, it uses a planner-worker architecture with four roles: a Meta-Thinker (strategic planning), a Memory Manager (memory editing via ADD/UPDATE/DELETE/NONE), a Query Reasoner (iterative retrieval with diagnosis-guided refinement), and an Answer Agent. The Meta-Thinker produces structured guidance that steers both construction (what to retain, consolidate, or resolve) and retrieval (diagnosing information gaps and directing query refinement). On the backward path, MemMA introduces in-situ self-evolving memory construction: after each session, it generates synthetic probe QA pairs, tests the current memory against them, and converts failures into repair actions (via evidence-grounded critique and semantic consolidation) before the memory is committed. The framework is backend-agnostic and can wrap existing memory systems like LightMem, A-Mem, or simple single-agent pipelines.

## Key Findings
- With GPT-4o-mini on LoCoMo, MemMA (using LightMem backend) achieves 81.58% ACC, improving over LightMem alone by +5.92 ACC, +4.82 F1, +1.62 B1
- Largest gains on multi-hop questions: ACC 65.62 to 78.12 (+12.5 points)
- Consistently improves all three tested storage backends: Single-Agent 52.60 to 84.87 ACC (+32.27), A-Mem 52.63 to 78.29 ACC (+25.66), LightMem 75.66 to 81.58 ACC (+5.92)
- Ablations show iterative retrieval is the most critical component (removing it drops ACC from 84.87 to 70.39), followed by self-evolution (84.87 to 73.68), then construction guidance
- Diagnosis-guided retrieval converges quickly: 1-2 refinement rounds close most gaps; further iterations risk retrieval drift
- Preliminary study shows strategic guidance (59.2% ACC) substantially outperforms both static retrieval (52.6%) and unguided active retrieval (54.6%)

## Tags
`multi-agent-coordination`, `memory-augmented-agents`, `long-horizon-memory`, `retrieval-augmented-generation`, `self-evolution`, `planner-worker-architecture`, `memory-cycle`

## Connections
- **WhyMultiAgentFail**: MemMA's planner-worker architecture with specialized roles (Meta-Thinker, Memory Manager, Query Reasoner, Answer Agent) is a concrete instantiation of multi-agent coordination; the failure taxonomy from WhyMultiAgentFail (inter-agent misalignment, task verification) applies to understanding when MemMA's coordination breaks down
- **DELEGATE-52 / SlopCodeBench**: Both show that LLM quality degrades over extended interactions. MemMA's in-situ self-evolution (probe-and-repair loop) is a direct counter-strategy -- an architectural "immune system" that detects and repairs degradation before it propagates
- **SingleAgentOutperforms**: MemMA's multi-agent design raises the question of whether its gains come from coordination or simply more compute. The ablations suggest coordination structure genuinely matters (removing any component degrades performance), but the single-agent efficiency argument applies
- **MaAS**: Both papers explore multi-agent architectures for improving LLM task performance. MaAS selects topology per-query; MemMA uses a fixed but specialized topology focused on memory coordination
- **CAID**: Both use multi-agent coordination with role specialization. CAID focuses on software engineering with branch-and-merge; MemMA focuses on memory management with planner-worker separation
- **ScienceOfScaling / AgentScalingDiversity**: MemMA's iterative retrieval with bounded refinement budget relates to the diminishing returns of scaling -- 1-2 refinement rounds suffice, mirroring findings that coordination yields diminishing returns past a threshold
