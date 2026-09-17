# Rethinking Continual Experience Internalization for Self-Evolving LLM Agents

## Source and access

Key: `2026-rethink-continual-internalization`. Jingwen Chen, Wenkai Yang, Shengda Fan, Wenbo Nie, Chenxing Sun, Shaodong Zheng, Yangen Hu, Lu Pan, Ke Zeng and Yankai Lin. [Primary v1](https://arxiv.org/html/2606.04703v1); [register](../sources.md#2026-rethink-continual-internalization). Submitted June 3, 2026; preprint. Read September 16: methods/results, Figures 1–6, Tables 1–4 and relevant appendices; coordinator reopened §§2–5. [Tier 2 audit](../workers/thesis-additions-screening.md). No original retained: primary HTML displays the arXiv non-exclusive distribution license, which does not authorize redistribution. [PDF link](https://arxiv.org/pdf/2606.04703v1).

## Question and methods

Can experience be repeatedly distilled into model weights without degrading later updates? Two Qwen models (4B and 8B) use a 15K corpus from five web-reasoning datasets. WebWalkerQA is in-domain; GAIA-Text103 and BrowseComp-ZH are treated as out-of-domain. Experiments compare instance/principle experience, global/step-wise injection, and student-trajectory on-policy versus teacher-trajectory off-policy distillation. Training uses five epochs, batch 128, learning rate 1e-5 and eight A800 GPUs (§4). The final recipe selects successful teacher trajectories; the teacher can be the student model conditioned on experience, with stronger-model experience generation in some settings.

## Results and evidence

Figure 1 shows deterioration under iterative on-policy internalization. Table 1: step-wise versus global injection yields 31.2/23.2, 22.7/16.8 and 5.2/4.5 on the three benchmarks in the Qwen-generated single-iteration setting. Table 4's final Qwen3-4B/DeepSeek-experience recipe gives WebWalkerQA 30.6→30.7→33.1 and GAIA 29.8→30.1→33.3 over three updates; BrowseComp-ZH is uneven at 5.2→4.4→5.9. In-context responsiveness is tabulated after iterations 1–2, not 3. Table 3's 21.9 versus base 2.5/teacher 4.5 assistant turns is after one on-policy update, not the final recipe's lifetime cost. No independent training-seed intervals are reported.

## Appraisal and limitations

This supplies both a failure and a positive counterexample: a researcher-designed recipe can sustain bounded gains across several weight updates. The result is not uniformly monotone, and neither the improver nor evaluation suite is independently evolving. Repeated benchmark use, in-domain training overlap, possible stronger-model assistance, missing total cost parity and absent training repeats limit causal and cross-domain claims. Earlier worker claims of measured in-context preservation through all three iterations and no tabulated final percentages are superseded by Table 4. No experiment reproduced.

## Discussion and follow-up

Would the final recipe preserve earlier tasks, work beyond web reasoning, and beat a fixed recipe or additional inference under equal total cost? Separate improvements in executing a task from improvements in producing the next training signal.

[Prominent citations and their roles](../prominent-citations.md#2026-rethink-continual-internalization)
