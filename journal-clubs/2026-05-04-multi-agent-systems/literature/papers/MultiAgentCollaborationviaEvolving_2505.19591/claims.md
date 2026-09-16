# Claims

## Claim 1
**Claim:** A centralized policy can dynamically orchestrate LLM agents without committing to a fixed collaboration topology.

**Evidence:** Section 2 formalizes each step as selecting an agent conditioned on the current global state and task, then updating the state with that agent's output. The serialized activation sequence can later be reconstructed as a directed graph of agent interactions.

**Caveats/Scope:** This is a framework design claim, not by itself proof that centralized control is always better than decentralized coordination. The paper evaluates a fixed family of agents and tools.

**Source pointers:** `paper.pdf`, Sec. 2 and Sec. 2.1; Figure 1.

## Claim 2
**Claim:** Reinforcement learning improves Puppeteer's average benchmark performance over its initialized policy.

**Evidence:** Table 1 compares initialized and evolved phases. In the Titan subspace, Puppeteer improves from 0.6893 to 0.7731 average score; Puppeteer-Mono improves from 0.6671 to 0.7453. In the Mimas subspace, Puppeteer-Mono improves from 0.5068 to 0.6147, and heterogeneous Puppeteer improves slightly from 0.6273 to 0.6324.

**Caveats/Scope:** Individual benchmark scores do not all improve, especially in Mimas where GSM-Hard and SRDD decline for heterogeneous Puppeteer. The claim is about the reported averages under the paper's evaluation setup.

**Source pointers:** `paper.pdf`, Sec. 3.1; Table 1.

## Claim 3
**Claim:** Evolved Puppeteer is competitive with, and by average score outperforms, the listed pure-model, single-agent, and multi-agent baselines in both tested model subspaces.

**Evidence:** Table 1 reports evolved Puppeteer average scores of 0.6324 in Mimas and 0.7731 in Titan. The strongest listed baseline averages are lower in the same table, including AFlow at 0.5364 in Mimas and 0.6899 in Titan.

**Caveats/Scope:** The advantage is clearest on average, not uniformly on every dataset. Some baselines outperform Puppeteer on individual tasks, such as CommonGen-Hard in Titan.

**Source pointers:** `paper.pdf`, Sec. 3.1; Table 1.

## Claim 4
**Claim:** The reward design can reduce token cost while improving task performance.

**Evidence:** Section 3.2 states that token consumption decreases during learning across almost all settings, while Table 1 shows improved evolved performance. Figures 2 and 3 plot declining token use and agent counts through training, and Appendix A.2 reports rising performance-per-cost trends across most tasks.

**Caveats/Scope:** Much of the cost evidence is presented as smoothed training curves rather than exact tabulated token totals. The paper also notes that some settings do not show a consistent downward trend.

**Source pointers:** `paper.pdf`, Sec. 3.2; Figures 2 and 3; Appendix A.1-A.2; Figure 9.

## Claim 5
**Claim:** Puppeteer's learned organizations tend toward compact, cyclic reasoning structures.

**Evidence:** Section 3.3 describes evolution from exploratory disjoint chains toward fewer paths with cycles. Figure 6 reports higher graph density after evolution and increased counts for cycles of several lengths, which the authors interpret as compaction and cyclicality.

**Caveats/Scope:** The observed motifs are empirical patterns from the reported runs, not guaranteed structural outcomes for every task or agent pool. The paper does not prove that cycles are always causally necessary.

**Source pointers:** `paper.pdf`, Sec. 3.3; Figures 4, 5, and 6.

## Claim 6
**Claim:** Wider or deeper orchestration is not automatically better.

**Evidence:** Section 3.4 and Figure 7 show a non-monotonic relationship between topology constraints, token consumption, and accuracy; increasing width or depth can add redundancy, raise cost, and degrade performance relative to the default setting.

**Caveats/Scope:** The best width/depth setting may depend on benchmark difficulty, model capacity, agent design, and optimization budget.

**Source pointers:** `paper.pdf`, Sec. 3.4; Figure 7.
