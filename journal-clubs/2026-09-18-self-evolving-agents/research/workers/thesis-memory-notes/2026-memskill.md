# MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

**Provisional worker record, superseded for thesis use by the shared notes/register and [Tier 2 corrections](../thesis-additions-screening.md).**


Source: Haozhen Zhang et al., arXiv:2602.02474v2 (first 2026-02-02; v2 2026-05-24), https://arxiv.org/abs/2602.02474. Read 2026-09-16 via full arXiv HTML: §§1–4, Appendix B.2/B.3, and relevant tables. CC BY 4.0 is shown on the arXiv page; no local copy retained.

MemSkill separates a trace-specific memory bank from a shared skill bank (§3.1, lines 123–125). A controller selects top-K memory skills from span context and retrieved memories; a fixed LLM executor emits structured updates; a fixed LLM designer mines a bounded hard-case buffer, proposes edits/new skills, and can roll back regressions (§§3.3–3.5, lines 134–166). This is a direct mechanism for evolving the procedure that converts experience into memory.

Table 1 reports, for LLaMA3.3-70B, MemSkill LoCoMo F1/L-J 44.21/53.82 and LongMemEval 31.12/60.89, versus no-memory unavailable and static baselines; ALFWorld seen/unseen success rates are 77.14%/83.58%. Qwen3-Next transfer reports 42.08/54.14 and 25.29/60.40, with ALFWorld seen/unseen 85.71%/76.87% (§4, Table 1, lines 168–191). The paper uses LoCoMo, LongMemEval, HotpotQA shift, and ALFWorld; Qwen transfer applies skills learned on LoCoMo without further training (§4.1, lines 193–200).

Interpretation: positive evidence that learned memory-operation skills can transfer across conversational and embodied settings. Limits for the thesis are substantial: the executor/designer are fixed LLM/API components; no end-to-end cost parity against stronger static skills or extra attempts; no multi-cycle lifetime curve showing accelerating returns; and transfer is limited to the reported datasets/models. Rollback protects training reward but does not prove no forgetting on earlier task families.
