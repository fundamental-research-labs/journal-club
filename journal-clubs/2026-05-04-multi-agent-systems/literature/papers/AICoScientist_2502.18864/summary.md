# Towards an AI co-scientist

**Authors:** Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, Khaled Saab, Dan Popovici, Jacob Blum, Fan Zhang, Katherine Chou, Avinatan Hassidim, Burak Gokturk, Amin Vahdat, Pushmeet Kohli, Yossi Matias, Andrew Carroll, Kavita Kulkarni, Nenad Tomasev, Yuan Guan, Vikram Dhillon, Eeshit Dhaval Vaishnav, Byron Lee, Tiago R D Costa, Jose R Penades, Gary Peltz, Yunhan Xu, Annalisa Pawlosky, Alan Karthikesalingam, Vivek Natarajan
**arXiv:** 2502.18864
**Venue:** Preprint
**Date:** February 2025

## Problem
Scientific discovery depends on forming novel, testable hypotheses from large, fragmented bodies of literature and domain expertise. The paper asks whether a frontier LLM-based, scientist-in-the-loop multi-agent system can help generate, critique, rank, and refine research hypotheses that are grounded enough to support downstream experimental validation.

## Method
The AI co-scientist is a Gemini 2.0-based multi-agent system organized around a natural language research goal, an asynchronous task framework, persistent context memory, tool use, and specialized agents. Generation agents explore literature, run simulated debates, and propose hypotheses; Reflection agents review novelty, correctness, safety, assumptions, and simulations; a Ranking agent runs Elo-style tournaments; Evolution, Proximity, and Meta-review agents refine ideas, organize related hypotheses, and propagate critique back into later iterations. Scientists can add constraints, feedback, reviews, and their own hypotheses, which are incorporated into the same tournament and refinement loop.

## Key Findings
- Elo-style auto-evaluation is used internally for ranking and correlates with GPQA Diamond answer quality in the paper's check; selecting top-rated results gives a reported 78.4% top-1 GPQA accuracy.
- Across 203 research goals and a 15-goal expert-curated subset, later tournament outputs have higher Elo ratings, suggesting benefit from scaled test-time compute; the paper cautions that Elo is an auto-evaluation metric, not independent ground truth.
- In a small expert study over 11 research goals, co-scientist outputs were preferred and rated higher for novelty and impact than several single-model baselines, but the authors frame this as subjective and preliminary.
- The biomedical validations cover three settings: AML drug repurposing, epigenetic targets for liver fibrosis, and cf-PICI mechanisms in antimicrobial resistance.
- In AML cell-line experiments, several co-scientist-suggested drugs inhibited cell viability, including KIRA6 across KG-1, MOLM-13, and HL-60 cells.
- In liver fibrosis, drugs targeting two of three co-scientist-suggested epigenetic modifiers showed anti-fibrotic activity in human hepatic organoids without observed cellular toxicity in the reported assay.
- For cf-PICIs, the system recapitulated an unpublished mechanism involving interactions with diverse phage tails after being given background material and relevant papers.
- The limitations are substantial: literature access is incomplete, negative results are underrepresented, multimodal/database/tool integration is limited, LLM hallucinations can propagate, metrics are preliminary, and wet-lab results are not clinical proof.

## Tags
`AI-scientist`, `multi-agent`, `scientific-discovery`, `hypothesis-generation`, `test-time-compute`, `biomedical-AI`, `drug-repurposing`, `Gemini-2.0`, `Elo-ranking`, `scientist-in-the-loop`

## Connections
- Related to **AIScientist** and **AgentLaboratory** as an agentic research-assistant system, but it emphasizes human oversight, hypothesis generation, and biomedical validation rather than fully automated paper production.
- Relevant to **MultiagentDebate** because simulated debate and pairwise tournament comparisons are core mechanisms for ranking and improving hypotheses.
- Connects to **CAID** and other asynchronous multi-agent systems through its supervisor/worker task framework and explicit scaling of test-time compute.
- Provides a biomedical counterpoint to general agent benchmarks: evaluation includes expert review and wet-lab follow-up, while still relying heavily on auto-evaluation and selected validation cases.
