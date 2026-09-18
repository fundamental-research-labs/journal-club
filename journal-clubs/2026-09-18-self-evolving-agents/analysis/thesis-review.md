# Thesis review — September 18, 2026

## Reader follow-up — concrete science writing, September 18, 2026

The first conclusion rewrite still required the reader to supply examples for abstractions such as “recurring needs,” “selective updating,” and “acquired expertise.” The current ending instead follows a documented mistake in a financial report through judge feedback and saved instructions, then asks what would establish that the instruction helped on the next report. It explains gross margin in place and keeps the distinction between an observed edit and an unmeasured later benefit. The proposed update schedule has moved out of the essay's conclusion; it remains a qualified hypothesis in C012. The preceding sections and their numerical comparisons are unchanged in this follow-up. Primary verification: FinEvo v1 Appendix C, Tables 25–27/Figure 10. No invented scene, reported single-edit efficacy, or stylistic imitation.

## Resolution — conclusion and practical-value revision, September 18, 2026

The three substantive findings below are addressed in the current thesis and C005/C007/C011/C012. FinEvo now includes skill-only evolution and partial token costs, distinguishes alternative-system scores from expert-initialized learning, and explicitly interleaves tasks. The cross-study interpretation separates recurrence from mixing. The practical-value discussion includes recurring expenses and the value of outcomes.

The user's criticism of the ending exposed a further writing problem: its first paragraph recapped papers, its second listed controls, and its last restated conditions without developing a consequence. “What should an agent stop having to relearn?” now argues from recurring needs to selective updating, explains why acquired expertise may be worth preserving without constant revision, and identifies the possibility of learning how to adapt to unfamiliar work. Periodic reuse is labeled a design hypothesis with a specific comparison in C012; the evidence does not establish an optimal update schedule or economic return.

Read the complete essay, then checked section openings and endings together. The other developed mechanism sections retain their arguments; the targeted revision changes the practical-value section, the memory section's final inference, and the conclusion. Reopened FinEvo v1's official HTML and retained harness-evaluation v2 §4.4; no new discovery, freshness update, or reproduction. Source selection remains 26 directly cited families. Historical findings and locations below are preserved to make the resolution reviewable.

## Original review

Review of the current 89-line `thesis.md`, after the architecture and terminology revisions. This is an argument review, not a rewrite. Locations below refer to that version. The earlier architecture review concerns an older essay; its resolved findings should not be treated as outstanding findings against this one.

The central argument is defensible: experience can improve subsequent work, while practical payoff, retention, learned adaptation, and sustained acceleration require different evidence. The current essay distinguishes those claims, develops mechanisms, and qualifies cross-study inference. Three substantive revisions would improve its evidential balance and explanatory precision. None requires abandoning the central thesis.

## 1. Restore the strongest FinEvo alternative before interpreting the expert-skill comparison

**Priority: high. Location: thesis lines 31–33; claim C005.**

The essay reports reset 71.58, fixed expert skill 86.67, and full evolution 89.47. But the same table reports skill-only evolution at 93.71 and memory-only at 90.42. Thus the strongest tested adaptive configuration exceeds the expert skill by 7.04 points, rather than the full-evolution margin of 2.80. The comparison is confined to Claude Code, and lacks across-run uncertainty. [FinEvo v1, §4.4, Table 5](https://arxiv.org/html/2608.06144v1#S4.T5).

The quoted numbers are correct, and expert guidance still accounts for much of the improvement over reset. The omission nevertheless understates the adaptive alternative precisely where the essay evaluates it. It also loses a useful mechanism result: combining memory and skills need not outperform a more constrained update design.

**Repair:** retain the expert control and add skill-only evolution. Describe the result as a comparison of final systems. It does not establish how much further learning would help an agent *already initialized with* the expert skill; that requires an expert-initialized learning condition. Update C005 alongside the prose.

## 2. Make clear that FinEvo also interleaves its tasks

**Priority: medium. Location: thesis lines 31, 39, 47, and 53; claims C007/C011.**

FinEvo uses three globally interleaved streams spanning 20 scenes across six financial domains. Interleaving and recurring procedures coexist in its design. [FinEvo v1, §4.1](https://arxiv.org/html/2608.06144v1#S4.SS1).

The essay contrasts recurring professional work with AgentStream's heterogeneous tasks without making this explicit. Its caveat correctly rules out a causal cross-benchmark comparison, but the explanatory framing can still suggest that recurrence and mixing are opposing conditions. AgentStream also reports retrieval methods doing best under interleaving, which challenges any simple interpretation that mixing itself prevents useful learning.

**Repair:** state FinEvo's interleaving when introducing its protocol. Develop recurrence of reusable structure and diversity of intervening tasks as separate dimensions. Retain the proposed within-protocol experiment; identify feedback, task construction, and method differences as competing explanations. The defensible hypothesis concerns whether relevant procedures recur and can be selected, not whether a stream is simply mixed or unmixed.

## 3. Support the practical-value question with actual costs and separate it from score gains

**Priority: medium. Location: thesis lines 27–39 and 81–85; claims C005/C011/C012.**

The essay makes cost central but supplies no concrete cost comparison. FinEvo Table 5 reports execution-plus-reflection totals of 15.92, 76.50, and 61.56 × 10⁴ tokens/task for expert skill, full evolution, and skill-only evolution respectively. These omit judge costs; expert-skill preparation is not priced. [FinEvo v1, §4.1 and Table 5](https://arxiv.org/html/2608.06144v1#S4.T5).

The essay already qualifies its synthesis as an interpretation, so this is not an unsupported declaration of economic success. It is a gap between the question it foregrounds and the evidence it explains. A higher rubric score does not itself establish that learning repays its cost. Nor does amortizing a fixed harness-development expense describe every system: continued reflection, retrieval, and training can introduce ongoing expenses.

**Repair:** include one scoped quality–cost comparison, explain which costs recur, and state that the cited results establish bounded performance gains without settling net practical value. A payoff comparison needs a reuse horizon and a value assigned to improved outcomes, as well as development and operating costs. Do not present token ratios as dollar ratios or invent a break-even point.

## What does not need a major revision

The introduction now defines the complete learning system and acknowledges outside assistance. WikiSkill's gains are not attributed to its wiki alone. The memory section distinguishes irrelevance, forgetting, and environmental change. R-Zero's decline is not presented as proof that label quality caused it. Hyperagents' positive fixed-method transfer and uncertain continued-evolution endpoint are correctly separated, with whole-implementation transfer qualified. These are substantive strengths; another wholesale structural rewrite is unnecessary.

One smaller clarification would help: explicitly identify each main example as offline development, adaptation across a task stream, or repeated training when introducing its protocol. The introduction states the distinction, but readers must sometimes reconstruct it later.

## Review scope and next steps

Read the complete thesis and consulted the README, workflow, landscape, claim ledger, source register, current coverage reconciliation, prominent-citation aggregate, acquisition manifest, previous architecture review, and relevant reading notes. Reopened retained harness-evaluation v2, Hyperagents v1, and R-Zero v4 PDF passages through text extraction. Reopened FinEvo v1's official HTML because its acquisition record marks retention restricted; checked §§4.1–4.4 and Table 5 without retaining a copy. Other source findings retain their recorded prior review depth. No new discovery, freshness claim, visual PDF audit, or experiment reproduction.

Reuse the September 16 research cutoff. Thesis, claims, and presentation remain unchanged. Recommended next step: a targeted revision addressing findings 1–3, followed by reconciliation of C005/C007/C011/C012 and the corresponding coverage and presentation records. This review does not reopen the earlier resolved architecture findings.
