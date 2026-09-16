# Claims

## Claim 1: Self-reflection can suffer Degeneration-of-Thought.

**Evidence:** The paper defines DoT as the case where an LLM, after gaining confidence in an answer, fails to generate novel thoughts through self-reflection even when the initial stance is wrong. Figure 1 compares disagreement across iterations and shows self-reflection has much lower disagreement than debate after early rounds.

**Caveats/Scope:** The disagreement analysis is based on the paper's selected debate/self-reflection setup and manual agreement labels; it should be treated as evidence for the evaluated tasks rather than a universal property of all self-reflection methods.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Figure 1

## Claim 2: Multi-Agent Debate improves commonsense translation in the tested setting.

**Evidence:** Table 1 reports that MAD improves GPT-3.5-Turbo on lexical, contextless syntactic, and contextual syntactic ambiguity subsets of Common MT across automatic and human metrics. The paper also reports that GPT-3.5-Turbo with MAD exceeds GPT-4 on the Common MT evaluation used here.

**Caveats/Scope:** The task is Chinese-to-English commonsense translation on the Common MT test split, and the human metric is direct assessment by professional translators; the result does not imply that MAD always beats stronger models on general translation.

**Source pointers:** `paper.pdf`, Sections 3.1-3.3; Table 1; Table 2; Appendix A.1; Appendix B

## Claim 3: MAD helps counter-intuitive arithmetic reasoning but does not close the gap to GPT-4.

**Evidence:** Table 3 shows GPT-3.5-Turbo with MAD outperforming GPT-3.5-Turbo, CoT, self-consistency, and self-reflection on CIAR accuracy. GPT-4 remains higher on the same table.

**Caveats/Scope:** CIAR is a 200-question dataset created by the authors from elicitation questions, web puzzles, and manual derivatives; results may depend on the dataset's particular intuitive traps and prompting format.

**Source pointers:** `paper.pdf`, Sections 3.1, 3.2, and 3.4; Table 3; Appendix A.2

## Claim 4: MAD mitigates the bias and rigidity symptoms associated with DoT.

**Evidence:** Table 4 compares self-reflection and MAD on Common MT and reports lower ambiguity bias plus substantially higher output diversity for MAD. The authors interpret this as evidence that debate adds external viewpoints and makes the model less likely to repeat a biased initial answer.

**Caveats/Scope:** Bias is measured using human labels for commonsense conformity in translation, and diversity is derived from Self-BLEU between candidates; these are proxies for DoT mechanisms, not direct measurements of model cognition.

**Source pointers:** `paper.pdf`, Section 4.1; Table 4; Appendix B

## Claim 5: Debate control choices matter: adaptive stopping and moderate disagreement help, while extra debaters can hurt.

**Evidence:** Figure 3 shows that some tit for tat disagreement improves ambiguity resolution, but maximal forced disagreement is not best. Figure 5 shows adaptive stopping outperforming fixed-round extraction, and Table 7 reports worse Common MT scores when the number of debaters increases from the default two to three or four.

**Caveats/Scope:** These ablations are reported mainly on Common MT with the paper's prompt design and model choices. The authors attribute failures with more debaters partly to long-context handling limits, which may change with stronger models.

**Source pointers:** `paper.pdf`, Section 4.3; Figure 3; Figure 5; Table 7; Appendix D

## Claim 6: The judge role is useful but can introduce model-backbone bias.

**Evidence:** Table 5 shows stronger debaters with a weaker judge outperform weaker debaters with a stronger judge, suggesting debater quality sets much of the ceiling. Table 6 shows that when debaters use different LLM backbones, the judge tends to choose the side using the same backbone model.

**Caveats/Scope:** The bias analysis is specific to the tested GPT-3.5-Turbo, GPT-4, and Vicuna combinations, and the paper recommends same-backbone roles or fully distinct judge/debater backbones to reduce this issue.

**Source pointers:** `paper.pdf`, Section 4.2; Table 5; Table 6; Limitations
