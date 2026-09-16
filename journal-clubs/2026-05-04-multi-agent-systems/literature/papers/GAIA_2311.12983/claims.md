# Claims

## Claim 1
**Claim:** GAIA is designed as an easy-to-grade benchmark for general AI assistants, not as another expert-exam benchmark.

**Evidence:** The paper defines GAIA as 466 human-crafted real-world questions with short, factual, unambiguous answers that can be scored by quasi-exact match. The questions are conceptually simple for humans but require multi-step execution across tools and information sources.

**Caveats/Scope:** This framing depends on careful human question design and validation; the benchmark does not grade the reasoning trace directly.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 3.1; Section 3.2.

## Claim 2
**Claim:** GAIA exposes a large gap between human annotators and 2023-era frontier assistants.

**Evidence:** The abstract reports human respondents at 92% versus 15% for GPT-4 equipped with plugins. Table 4 reports human scores of 93.9%, 91.8%, and 87.3% across Levels 1-3, compared with GPT-4 plus plugins at 30.3%, 9.7%, and 0%.

**Caveats/Scope:** The GPT-4 plus plugins setup was manually selected and described as oracle-like rather than exactly reproducible; these results reflect the models and tool interfaces available at the time.

**Source pointers:** `paper.pdf`, Abstract; Section 4; Figure 4; Table 4.

## Claim 3
**Claim:** The benchmark targets real assistant capabilities that require tool use, especially web browsing, while also covering coding, multimodality, and diverse file reading.

**Evidence:** Figure 3 counts annotated capability requirements, including 355 questions requiring web browsing, 154 coding, 138 multimodality, and 129 diverse filetype reading. Appendix C defines these capability categories and gives examples of associated tools.

**Caveats/Scope:** The authors note that these are annotator-derived capability labels, not a perfect typology, because a model may solve a question through a different path.

**Source pointers:** `paper.pdf`, Section 3.3; Figure 3; Appendix C.

## Claim 4
**Claim:** GAIA's three difficulty levels are based on practical execution complexity rather than specialized knowledge.

**Evidence:** Section 3.3 defines Level 1 as generally requiring no tools or at most one tool and no more than five steps, Level 2 as roughly five to ten steps with multiple tools, and Level 3 as requiring arbitrarily long sequences, any number of tools, and broad access to the world.

**Caveats/Scope:** The paper states these definitions are loose rather than hard constraints, and levels are based on annotator paths that AI systems may not follow.

**Source pointers:** `paper.pdf`, Section 3.3; Figure 1; Figure 3; Figures 7-8.

## Claim 5
**Claim:** GAIA tries to reduce benchmark gaming and contamination by requiring task completion rather than answer recognition.

**Evidence:** The authors require concise factual answers that are absent in plain text by design, use sources of truth, validate ambiguity with independent annotators, and retain 300 answers for a leaderboard while releasing a 166-question annotated developer set.

**Caveats/Scope:** The paper acknowledges that static benchmarks can decay through pretraining contamination or disappearing/changing web evidence, so GAIA may need year-by-year maintenance.

**Source pointers:** `paper.pdf`, Section 1; Section 3.1; Section 3.4; Section 5.

## Claim 6
**Claim:** GAIA's simplicity of final-answer evaluation trades off against limited diagnostic detail.

**Evidence:** Section 6 says the benchmark does not evaluate the trace leading to the answer, even though different paths can reach the same correct answer. The paper also notes limited linguistic and cultural diversity because questions are in standard English and often rely on English web pages.

**Caveats/Scope:** These limitations are partly intentional choices to keep the benchmark automatic, factual, and easy to run.

**Source pointers:** `paper.pdf`, Section 6.
