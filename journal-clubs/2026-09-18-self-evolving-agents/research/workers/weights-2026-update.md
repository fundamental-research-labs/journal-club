# 2026 update: weight-changing and self-evolving agents

Cutoff: 2026-09-16. I ran 12 date-constrained searches (April–September 2026, plus exact-title searches) and expanded primary arXiv/project pages. Entries below are discovery records; only abstracts and selected primary excerpts were inspected unless stated. No secondhand result claims are used.

## Strong additions

### SIA: Self Improving AI with Harness & Weight Updates

Prannay Hebbar et al., arXiv:2605.27276, first submitted 2026-05-26: https://arxiv.org/abs/2605.27276 . The paper's abstract says a Feedback-Agent chooses between harness edits and LoRA/RL weight updates for a task-specific agent, evaluated on Chinese legal charge classification, GPU kernel optimization, and single-cell RNA denoising. Abstract-reported gains over initial baselines are 56.6% LawBench, 91.9% GPU runtime reduction, and 502% denoising; these are author claims pending full-table audit. A primary PDF excerpt confirms the loop: Meta-Agent initializes the scaffold, Task Agent executes, Feedback-Agent selects harness or weight update, with Claude Sonnet 4.6 used for meta/feedback roles. Official project: https://hexolabs.com/sia ; code/download status and license require inspection. **Importance:** strongest 2026 direct match to the lane because both editable harness and weights are selected in one loop; the benchmark gains are domain-specific and do not establish compounding RSI.

### Dream-RSI: Recursive Self-Improvement through Evolving Worlds

Tong Zheng et al., arXiv:2609.14858, first submitted 2026-09-14: https://arxiv.org/abs/2609.14858 ; project/technical report: https://www.dream-rsi.com/ . Abstract and project page inspected. Discovery histories become replay simulators; candidate exploration policies are “dreamed” and scored off-policy before redeployment, expanding the simulator pool each lap. Reports competitive or improved discovery quality in algorithm engineering, mathematical optimization, and GPU kernels while reducing discovery cost. This changes an exploration policy/harness, not necessarily foundation-model weights; classify as recursive policy improvement. Very recent, no peer-review or independent reproduction checked.

### Escher-Loop

Ziyang Liu et al., arXiv:2604.23472, first submitted 2026-04-25: https://arxiv.org/abs/2604.23472 . Abstract inspected. Two populations co-evolve: Task Agents and Optimizer Agents; optimizers recursively refine task agents and themselves, using relative win/loss signals from newly generated agents. Authors report highest absolute peak on mathematical optimization under matched compute and late-stage gains. This is optimizer/harness recursion; weight updates are not established from the abstract. Full methods and independent baselines pending.

### Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration

Qifan Zhang et al., arXiv:2604.18131, first submitted 2026-04-20: https://arxiv.org/abs/2604.18131 . Abstract inspected. Training uses an outcome-based reward for whether self-generated world knowledge improves downstream success; at inference, the agent explores/summarizes unknown environments without external rewards or human instructions. Authors report 20% gains on WebVoyager/WebWalker for Qwen3-30B and Seed-OSS-36B and a 14B Qwen3 comparison against unassisted Gemini-2.5-Flash. This is trained meta-evolution and internal-parameter adaptation at deployment, but exact splits, cost, and whether knowledge is weight-updated versus generated context require full-text inspection.

### Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence

Guanting Dong et al., arXiv:2604.18292, first submitted 2026-04-20: https://arxiv.org/abs/2604.18292 . Abstract inspected. Agentic environment/task discovery synthesizes verifiable tasks with controllable difficulty; continuous self-evolving training uses multi-environment RL and an arena to identify capability gaps and drive targeted learning. Evaluates Agent-World 8B/14B across 23 agent benchmarks and reports gains over environment-scaling baselines. It is a curriculum/environment and policy-training family; parameter-update details and held-out controls require full read.

### In-Place Test-Time Training

Guhao Feng et al., arXiv:2604.06169, first submitted 2026-04-07: https://arxiv.org/abs/2604.06169 . Abstract inspected. Updates final MLP projection matrices as fast weights, with a next-token objective and chunk-wise updates, making test-time adaptation a drop-in enhancement. Authors report a 4B model superior on contexts up to 128k and improvements over TTT baselines. This is a particularly relevant architectural route to continual weight adaptation, but it is not an autonomous agent or self-generated curriculum by itself.

### Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents

Ran Yan et al., arXiv:2607.01120, first submitted 2026-07-01: https://arxiv.org/abs/2607.01120 . Abstract/metadata inspected. Position/architecture paper arguing deployed online RL needs step-level trajectory protocols, governed data proxies, and a control plane deciding weight versus in-context-harness updates; instantiates an AReaL2.0 branch. Treat as infrastructure proposal, not measured evidence of recursive capability.

### Position: Deployed Reinforcement Learning should be Continual

Parnian Behdin et al., arXiv:2606.04029, first submitted 2026-06-01: https://arxiv.org/abs/2606.04029 . Position paper. Identifies four post-deployment non-stationarities and argues evaluative reward makes deployment inherently continual RL. Useful framing and counterpoint to train-then-fix; no new empirical effect estimate.

### Generalized Agent Iteration

Hongyao Tang et al., arXiv:2609.13406, first submitted 2026-09-11: https://arxiv.org/abs/2609.13406 . Abstract inspected. Formalizes iterative policy improvement versus RSI along two axes: whether the improver is inside the agent and whether evaluation is externally anchored. Useful taxonomy for distinguishing SIA/Dream-RSI/Escher-Loop from ordinary policy iteration; no new benchmark evidence.

### Recursive Self-Improvement LLM Agents for Inverter Dynamic Model Identification

Jie Feng et al., arXiv:2609.14260, first submitted 2026-09-13: https://arxiv.org/abs/2609.14260 . Explicitly a position/proof-of-concept paper. Uses ThetaEvolve-style program search with test-time learning; reports NRMSE 0.470→0.0435 and recovery of a 15-module controller on a grid-following inverter benchmark. Relevant as domain-specific program evolution, not weight self-training; result needs full methods and baseline audit.

## Exact-title searches and negative findings

Queries: `SIA self improving agent weights harness 2026 paper`; `Self-Evolving Agent Training 2026 arXiv`; `Agent0 self evolving agent 2026 followup`; `Dream-RSI Escher-Loop 2026 agent`; `site:arxiv.org 2026 continual agent reinforcement learning deployed`; `site:arxiv.org 2026 self-evolving agent training weights`; `site:arxiv.org 2026 in-place test-time training language model`; `site:arxiv.org 2026 AgentGym-RL self evolving`; `site:arxiv.org/abs/260 Escher-Loop`; `site:arxiv.org/abs/260 Dream-RSI`; `site:arxiv.org 2026 self-evolving agents weight`; `site:arxiv.org 2026 recursive self-improvement agent policy`.

Agent0 appeared as an ICLR 2026 under-review paper, “Unleashing Self-Evolving Agents from Zero Data,” at https://openreview.net/pdf?id=OWz5JiJw5M, but the accessible search result did not expose enough primary metadata/method detail to make a verified result claim. Dash0 Agent0 pages are a deployed product, not a research result, and were excluded. No primary 2026 hit named “Self-Evolving Agent Training” was sufficiently identifiable beyond Agent-World and the reward-free world-knowledge paper. No primary Escher-Loop follow-up after April 2026 was found by cutoff.

## Screening cautions

- SIA is the clearest new weight+harness family, but its reported gains span unrelated domain metrics and need compute/evaluator/seed checks; they do not show repeated generations with accelerating returns.
- Dream-RSI and Escher-Loop alter policies/optimizers and evaluation loops; classify their editable state explicitly instead of calling them weight learning.
- Reward-free self-evolution still receives supervised training through an outcome-based reward; “reward-free” applies at inference, not necessarily to the training process.
- In-Place TTT demonstrates fast-weight adaptation but does not establish safe continual deployment, retention, or resistance to drift.
- The 2026 papers are mostly preprints or position/framework papers. Independent replications and long-horizon evidence remain a major gap.
