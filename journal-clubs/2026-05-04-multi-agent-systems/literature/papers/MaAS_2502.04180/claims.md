# Claims

## Claim 1: Multi-agent system design should be query-adaptive rather than a single static workflow.

**Evidence:** The paper argues that one-size-fits-all workflows waste resources on easy queries and underfit diverse domains, then formulates MaAS as a conditional distribution over architectures.

**Caveats/Scope:** The claim is evaluated on reasoning, coding, and tool-use benchmarks, not every agent deployment setting.

**Source pointers:** `summary.md`; `source/example_paper.tex`

## Claim 2: The agentic supernet represents many possible multi-agent architectures with probabilistic operator choices.

**Evidence:** MaAS defines an agentic supernet over layers of agentic operators and samples a DAG-like multi-agent system conditioned on the input query.

**Caveats/Scope:** The search space depends on the provided operator set and controller design.

**Source pointers:** `source/example_paper.tex`; `summary.md`

## Claim 3: MaAS jointly optimizes architecture probabilities and operator behavior.

**Evidence:** The method uses Monte Carlo gradient estimation for distribution parameters and agent-generated textual gradients for prompts, tools, temperature, and node structure.

**Caveats/Scope:** The operator updates are natural-language approximations rather than ordinary differentiable updates.

**Source pointers:** `source/example_paper.tex`; `summary.md`

## Claim 4: MaAS improves performance while reducing inference cost versus many handcrafted and automated baselines.

**Evidence:** Experiments across math reasoning, code generation, and GAIA tool-use tasks report higher average scores and substantially lower inference cost than existing multi-agent systems.

**Caveats/Scope:** Reported costs depend on the selected LLM backbones, APIs, and benchmark mix.

**Source pointers:** `source/example_paper.tex`; `summary.md`

## Claim 5: Early exit and cost constraints mainly support efficiency, while textual gradients are most important for performance.

**Evidence:** Ablations report that removing textual gradients causes the largest performance drop; removing early exit or cost constraints has less effect on accuracy but raises cost.

**Caveats/Scope:** This component ranking is from the paper's tested setup and operator set.

**Source pointers:** `source/example_paper.tex`; `summary.md`
