# Claims

## Claim 1
**Claim:** Multi-agent performance is bounded by usable task information rather than raw agent count.

**Evidence:** The paper defines usable evidence as conditional mutual information between the transcript and answer given the input, then derives architecture-independent information-budget bounds.

**Caveats/Scope:** The formal analysis depends on the paper's information-theoretic abstractions and idealized assumptions in later bounds.

**Source pointers:** `source/main.tex`; `summary.md`

## Claim 2
**Claim:** Homogeneous agent scaling saturates because additional calls tend to contribute redundant outputs.

**Evidence:** Homogeneous voting and debate experiments show fast-then-slow gains, with marginal improvements collapsing as agent count grows; the theory explains this as stagnant effective channel growth.

**Caveats/Scope:** Main experiments use selected 7B-8B open-weight models, seven benchmarks, and vote/debate workflows.

**Source pointers:** `source/main.tex`; `summary.md`; `source/Figure/homo_per_dataset_vote.pdf`

## Claim 3
**Claim:** Diversity can be more efficient than adding more homogeneous agents.

**Evidence:** The experiments compare diversity layers and report that full diversity using model and persona heterogeneity can match or exceed a larger no-diversity baseline with far fewer agents.

**Caveats/Scope:** The benefit is strongest when diversity produces complementary useful evidence, not merely different text.

**Source pointers:** `source/main.tex`; `summary.md`; `source/Figure/Vote_Heatmap_Square_LargerFont_1.pdf`; `source/Figure/Debate_Heatmap_Square_LargerFont_1.pdf`

## Claim 4
**Claim:** The effective channel proxy `K*` is intended to measure non-redundant agent outputs without labels.

**Evidence:** The paper defines `K*` as entropy effective rank of a trace-normalized cosine-similarity Gram matrix over output embeddings and validates that it increases with diversity.

**Caveats/Scope:** `K*` measures semantic embedding diversity, not guaranteed task-relevant information diversity, and depends on the embedding model.

**Source pointers:** `source/main.tex`; `summary.md`

## Claim 5
**Claim:** Not all diversity helps; diversity among correct reasoning paths is the useful signal.

**Evidence:** The paper decomposes `K*` into correct and incorrect channel counts and argues that high-performing configurations concentrate where correct-path diversity dominates incorrect-path diversity.

**Caveats/Scope:** This decomposition requires ground-truth labels and is an analysis tool, not a label-free deployment metric.

**Source pointers:** `source/main.tex`; `summary.md`; `source/Figure/exp1_task_profiles.png`
