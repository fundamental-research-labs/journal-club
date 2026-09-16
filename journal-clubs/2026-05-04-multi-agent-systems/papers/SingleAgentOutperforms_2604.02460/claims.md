# Claims

## Claim 1: Under equal thinking-token budgets, single-agent systems are the strongest default for multi-hop reasoning.

**Evidence:** Across FRAMES and MuSiQue with Qwen3, DeepSeek, and Gemini models, SAS is reported as best or statistically indistinguishable from the best except at very small budgets.

**Caveats/Scope:** The paper focuses on text-only multi-hop reasoning, not tool use, vision, safety workflows, or long-running software tasks.

**Source pointers:** `summary.md`; `source/colm2026_conference.tex`

## Claim 2: Many apparent multi-agent gains can be explained by unnormalized compute.

**Evidence:** The study controls the total thinking-token budget and argues that MAS comparisons are often confounded by multiple calls and longer reasoning traces.

**Caveats/Scope:** Budget accounting for API models can be approximate, especially where visible reasoning and reported thinking tokens diverge.

**Source pointers:** `source/colm2026_conference.tex`; `summary.md`

## Claim 3: The information-theoretic argument favors a single agent with full context under ideal context use.

**Evidence:** The paper uses the Data Processing Inequality to argue that inter-agent messages are lossy functions of the full context and cannot contain more answer-relevant information than that context.

**Caveats/Scope:** This is an idealized argument; it does not rule out MAS benefits when a single model fails to use the full context effectively.

**Source pointers:** `source/colm2026_conference.tex`

## Claim 4: Multi-agent systems become more competitive when single-agent context utilization is degraded.

**Evidence:** Context degradation experiments show Sequential MAS catching up to or surpassing SAS under heavy masking or substitution.

**Caveats/Scope:** Deletion and distractor settings show weaker effects, so the benefit is tied to corrupted or misleading context rather than context length alone.

**Source pointers:** `source/colm2026_conference.tex`; `summary.md`

## Claim 5: Debate and parallel roles are the most competitive MAS variants, but they do not reliably beat SAS.

**Evidence:** The results section describes Debate as the strongest MAS variant and Parallel-roles as often next best, while still framing SAS as the default under matched budgets.

**Caveats/Scope:** Some MAS variants overlap with the best system within confidence intervals on specific model/dataset/budget cells.

**Source pointers:** `source/colm2026_conference.tex`
