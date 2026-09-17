# MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

## Source and access

Key: `2026-memskill`. Haozhen Zhang et al. [Primary v2](https://arxiv.org/html/2602.02474v2); [register](../sources.md#2026-memskill). First submitted February 2, 2026; v2 May 24. Preprint. Read September 16: primary §§3–5, Tables 1–3, transfer experiments and Appendix F; coordinator reopened method/related-work HTML. [Retained CC BY 4.0 original](../originals/2026-memskill/2026-memskill-paper-v2.pdf). [Screening audit](../workers/thesis-additions-screening.md).

## Question and methods

Can an agent learn how to write memories as well as what to remember? A PPO-trained controller selects operations from a shared skill bank; a fixed LLM executor applies them to trace-specific memories. A fixed designer periodically revises skills from hard cases. Initial operations are Insert, Update, Delete and Skip (§3). Conversational QA and ALFWorld provide distinct settings. Clearly identified transfer tests reuse LLaMA-learned skills with Qwen and LoCoMo-trained skills on LongMemEval and HotpotQA; they do not establish transfer from conversation to embodied tasks.

## Results and evidence

Table 2's LoCoMo LLaMA judge score is 53.82, falling to 48.43 without the learned controller and 46.50 without the designer. Table 3 reports runtime use of 249K input tokens, 18K output tokens and 215 calls at span size 512; preparation for learning/evolving skills is excluded. Main tables do not report independent-run intervals.

## Appraisal and limitations

The authors argue that evolving reusable memory operations improves memory construction. The ablations and bounded transfers support that mechanism. Fixed executor/designer/judges, omitted preparation cost and absent repeated lifetime curves prevent interpreting the result as general accelerating improvement. The earlier worker phrase “transfer across conversational and embodied settings” was too broad and is superseded by this note. No experiment reproduced.

## Discussion and follow-up

How much does evolving the operation bank add beyond a well-designed static bank under matched preparation and deployment cost? Would the selector preserve older skills when task similarity decreases?
