# MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory

## Source and access

**Source key:** `2026-memrl`.

**Originals and source links:** [register](../sources.md#2026-memrl); [canonical source](https://arxiv.org/abs/2601.03192). retention-restricted. [Manifest](../originals/manifest.json).

. [arXiv v2](https://arxiv.org/abs/2601.03192v2); [PDF](https://arxiv.org/pdf/2601.03192v2). Shengtao Zhang et al. First posted January 6, 2026; v2 February 12, 2026. Read September 16, 2026: full paper, §§4–6, Tables 1–3, and relevant appendices inspected. No local copy retained: download succeeded, paper redistribution license unverified. Code/license status was not established.

## Question and methods

### Question and method

Can a frozen LLM learn at runtime by attaching learned utility values to episodic memories? MemRL first retrieves by semantic similarity, then ranks by a mixture of similarity and learned Q-value. Environmental scalar reward updates injected memories with a Monte Carlo-style rule; an LLM summarizes each trajectory into a new intent–experience–utility record (§§4.1–4.3).

### Evaluation and resources

Runtime learning repeats tasks for ten epochs on BigCodeBench, Lifelong Agent Bench OS/DB, ALFWorld, and HLE; the backbone varies by benchmark (GPT-4o, GPT-4o-mini, GPT-5-mini, Gemini-3-pro) to avoid floor/ceiling effects (§5.1, Table 1). Transfer freezes the selected memory bank and evaluates held-out sets (Table 2). Table 1 reports last-epoch success and cumulative success, while Pass@10 consumes multiple attempts and is not directly comparable to single-run last-epoch success. The paper provides no repeated-run standard deviations or confidence intervals in the main tables; full end-to-end token/dollar parity is not established.

## Results and evidence

Table 1 reports average last/CSR of .772/.798 for MemRL versus .736/.760 for MemP. CSR gains over MemP are +.025 BigCodeBench, +.062 OS, +.006 DB, +.062 ALFWorld, and +.036 HLE. Table 2 held-out transfer averages .794 versus .766 MemP, with the largest listed gap on ALFWorld (.979 versus .921). Table 3 shows cross-task retrieval .798 average versus .761 single-task reflection, but on HLE it is slightly worse (.606 versus .610), consistent with the paper's low-similarity explanation. Figure 6 shows an inverted-U sensitivity to retrieval width. The reported mean forgetting rate is .041 versus .051 for MemP (§5.4.2), without an uncertainty interval.

## Appraisal and limitations

### Authors' claim

Utility-weighted episodic retrieval resolves noise in semantic retrieval while retaining a stable frozen reasoner.

### Interpretation and limitations

The separation of frozen weights and plastic memory makes the mechanism easy to teach, and the held-out transfer table is more relevant than cumulative success on repeated tasks. Yet backbone selection differs across domains, repeated exposure inflates CSR by construction, and trajectory summaries still depend on an LLM. Q updates face ambiguous credit assignment when several memories are injected; the authors acknowledge this and drift under low task similarity (§6). Theoretical monotonicity relies on assumptions that do not guarantee monotonic empirical agent performance. No independent replication or matched-cost comparison is available.

## Discussion and follow-up

### Useful discussion/figure

Tables 1–3 support a stability/plasticity discussion: should memory retain a successful but semantically distant failure lesson, and how would one assign its credit?

[Prominent citations and their roles](../prominent-citations.md#2026-memrl)
