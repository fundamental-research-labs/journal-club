# ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory

## Source and access

Siru Ouyang et al., *ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory*, arXiv:2509.25140v2 (first 2025-09-29; v2 2026-03-16), https://arxiv.org/abs/2509.25140; ICLR 2026. Full arXiv HTML read 2026-09-16, including §§3–4 and Appendix E. The arXiv version is under a non-exclusive distribution license; no copy retained. Official code: https://github.com/google-research/reasoning-bank.

[Register](../sources.md#2025-reasoningbank); [version read](https://arxiv.org/abs/2509.25140v2).

## Question and methods

ReasoningBank distills strategy-level items from self-judged successful and failed trajectories, retrieves relevant items for new tasks, and integrates new lessons. MaTTS adds parallel k=5 trajectories or sequential refinement, using extra test-time compute to generate contrastive evidence and improve memory (§§3–4). Experiments cover WebArena (684 tasks after excluding Map), Mind2Web, and SWE-Bench-Verified across Gemini-2.5 and Claude-3.7 backbones; success rate and interaction steps are reported (lines 129–132).

## Results and evidence

WebArena Table 1 reports ReasoningBank overall success of 48.8%/53.9%/46.3% for Gemini-2.5-flash/pro/Claude-3.7, versus no-memory 40.5%/46.7%/41.7%; mean steps also fall (8.3/7.4/7.3 versus 9.7/8.8/8.0) (lines 133–153). The paper reports consistent gains across datasets and states that MaTTS further amplifies them (§4.2, lines 154–157). These are primary reported benchmark results, not evidence of indefinite improvement: k=5 scaling allocates additional inference attempts.

## Appraisal and limitations

ReasoningBank is distinct from ACE: it distills positive and negative reasoning strategies and explicitly couples memory with test-time scaling. It is also distinct from MemRL: retrieval is embedding-based and memory content is self-judged, without learned Q utilities. The authors explicitly limit scope to memory content, use simple retrieval/consolidation, and depend on an LLM judge for success/failure labels; they did not extensively compare episodic or hierarchical architectures (Appendix E, lines 440–446). Main tables lack repeated-run uncertainty in the inspected HTML, and extra MaTTS compute complicates attribution of gains to memory.

## Discussion and follow-up

Use this as a consequential foundation for the thesis's “memory versus extra compute” question. It supports the claim that structured failure memory can improve future tasks, but MaTTS makes the required counterfactual explicit: compare memory at fixed attempt/token budgets against a no-memory multi-attempt baseline, then test novel domains, old-task retention, and many update cycles. No independent reproduction was performed.
