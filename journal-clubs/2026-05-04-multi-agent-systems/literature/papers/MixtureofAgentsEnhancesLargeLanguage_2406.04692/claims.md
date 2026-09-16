# Claims

## Claim 1: Layered proposer/aggregator composition can improve LLM outputs without fine-tuning.

**Evidence:** MoA uses multiple LLMs per layer, passes earlier outputs as auxiliary context, and applies an aggregate-and-synthesize prompt to generate refined responses. The method operates through prompting and generation interfaces rather than modifying weights.

**Caveats/Scope:** The paper evaluates response-generation benchmarks, not all downstream LLM uses. The approach increases inference work and requires full prior responses before later aggregation.

**Source pointers:** `paper.pdf`, Sections 2.2-2.3; Table 1; Figure 2; Limitations paragraph.

## Claim 2: The open-source MoA configuration beats GPT-4 Omni on AlpacaEval 2.0 in the paper's comparison.

**Evidence:** Table 2 reports 65.1 +/- 0.6% LC win rate for MoA and 57.5% for GPT-4 Omni; Section 3.2 describes this as a 7.6 percentage point absolute improvement using only open-source models.

**Caveats/Scope:** AlpacaEval 2.0 uses model-based preference judging and length control. The comparison reflects models and APIs available around June 2024, not a current leaderboard claim.

**Source pointers:** `paper.pdf`, Abstract; Section 3.2; Table 2(a).

## Claim 3: MoA improvements extend beyond AlpacaEval, but gains vary by benchmark and metric.

**Evidence:** Table 2(b) reports MT-Bench scores of 9.25 for MoA and 9.40 for MoA w/ GPT-4o, above the listed GPT-4 Omni score of 9.19. Figure 3 reports FLASK gains over the Qwen1.5-110B-Chat aggregator and some GPT-4 Omni dimensions.

**Caveats/Scope:** MT-Bench is near saturation for strong models, and FLASK results are presented as a radar plot rather than a full numeric table in the main paper. MoA is reported as weaker on conciseness.

**Source pointers:** `paper.pdf`, Section 3.2; Table 2(b); Figure 3.

## Claim 4: Diverse proposer models are more useful than repeated samples from one proposer in the tested setup.

**Evidence:** Table 3 compares multiple-proposer and single-proposer settings with the same number of proposed outputs. With six proposals, using six different models scores 61.3% on AlpacaEval 2.0, while six samples from one model score 56.7%.

**Caveats/Scope:** The table uses two MoA layers and Qwen1.5-110B-Chat as aggregator; it does not prove that every additional model or every heterogeneous set will help.

**Source pointers:** `paper.pdf`, Section 3.3; Table 3.

## Claim 5: Aggregation does more than rerank candidate answers.

**Evidence:** Figure 4 shows MoA outperforming an LLM-ranker baseline that selects a proposer response. The appendix case studies show aggregated answers borrowing useful content from multiple proposer responses, including cases where no individual proposer is highly preferred.

**Caveats/Scope:** The evidence is based on automatic evaluation, similarity analysis, and qualitative cases; it does not fully explain the internal aggregation mechanism.

**Source pointers:** `paper.pdf`, Section 3.3; Figure 4; Appendix C; Tables 6-7.

## Claim 6: MoA exposes a quality-cost-latency tradeoff.

**Evidence:** The budget analysis places MoA and MoA-Lite on a cost/performance Pareto frontier in Figure 5, and the paper states MoA-Lite can match GPT-4o's cost while achieving higher AlpacaEval quality. The limitations section notes delayed time to first token because later layers cannot start until earlier responses are complete.

**Caveats/Scope:** Cost estimates use provider pricing retrieved on May 22, 2024, and TFLOPs are only a latency proxy. Current prices, batching, and serving systems could change the tradeoff.

**Source pointers:** `paper.pdf`, Section 3.4; Figure 5; Limitations paragraph.
