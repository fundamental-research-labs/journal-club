# Double-recursive RSI with Simple-SciBuddy

This document describes the algorithm implemented in `src/simple_scibuddy/`.
It explains how scientific interactions guide harness changes, how the selected
harness supplies fresh experience for model training, and how the updated model
returns to the next harness stage.

[Overview](#overview) · [Inner recursion](#inner) · [Outer recursion](#outer) · [Execution contract](#execution) · [Evaluation](#evaluation) · [Handoff and continuation](#handoff) · [Code map](#code)

For runnable configuration and commands, see the [experiment guide](experiments.md).
For the researcher-facing product and demonstration, see the
[ScienceBuddy overview](../README.md#sciencebuddy).

<a id="overview"></a>

## 1. Algorithm overview

The learned system has two components:

- A **task model** $M_k$ generates the agent's responses and tool-use decisions.
- A **harness** $H_{k,j}$ is a Python program that organizes prompts, model calls,
  tool execution, context and answer submission.

Here $k$ indexes model-learning cycles and $j$ indexes harness updates within one
cycle. An independent auxiliary model proposes harness changes. Its parameters
remain fixed while the task model and harness evolve.

The inner recursion fixes $M_k$ and searches for a better harness. The outer
recursion fixes the selected harness and updates $M_k$ through reinforcement
learning. The selected harness is inherited by the next cycle:

$$
H_{k,j+1} = \mathrm{Select}(H_{k,j},\ \mathcal{C}_{k,j};\ M_k,D_{\mathrm{val}}),
$$

$$
M_{k+1} = \mathrm{GRPO}(M_k;\ H_{k,J},D_{\mathrm{train}}),
\qquad H_{k+1,0}=H_{k,J}.
$$

$\mathcal{C}_{k,j}$ denotes the candidates proposed from the current interaction
evidence. $J$ is the number of harness steps per phase. A change in the harness
changes how the model collects experience; a model update changes which harness
procedures are effective in the next phase.

<p align="center">
  <img src="../assets/sciencebuddy-method.svg" width="1000" alt="Original ScienceBuddy paper method figure, including the inner harness recursion and outer model-learning recursion in panel B.">
</p>

*Original figure from the ScienceBuddy paper. Panel B depicts the coupled learning
processes. The figure also covers the broader product's task construction,
adaptive environments and online deployment. The implemented experiment uses a
frozen task release and sequential harness/RL stages.*

### State carried between stages

| State | Within a harness phase | During RL | Next cycle |
| --- | --- | --- | --- |
| Task model | Fixed | Updated | Export becomes the new task model |
| Harness | Proposed, evaluated and possibly replaced | Fixed | Selected program is inherited |
| Auxiliary model | Fixed | Does not supply RL rewards | Same configured auxiliary model |
| Task assignment and verifier | Fixed | Fixed | Same frozen release and verifier |
| Train cursor and proposal history | Advance with interactions | Preserved | Continue from the preceding boundary |
| Pending public trace evidence | Accumulates until adoption | Not reused as policy training data | Reinitialized for the new model phase |

The default schedule has three complete cycles:

```text
(M0, H0)
   → h0001: harness learning → r0001: model learning → M1
   → h0002: harness learning → r0002: model learning → M2
   → h0003: harness learning → r0003: model learning → M3
```

It ends after `r0003`; it does not add a fourth harness stage. Each harness phase
has three steps and each RL phase has 30 updates in the maintained recipe.

<a id="inner"></a>

## 2. Inner recursion: improve the harness with a fixed model

### 2.1 Collect scientific interactions

At phase start, the inherited harness passes a training-task execution preflight
and receives a baseline Test evaluation. Neither Test outputs nor Test labels
become proposal evidence.

For each harness step, the current program runs on the next 16 Train tasks.
The Train ordering is determined from the configured seed and task IDs. A cursor
continues across phases; it wraps only if the training index is exhausted.

An interaction can contain several model calls and Python tool executions. It
can also contain up to one simulated researcher reply in the current recipe.
The episode's reported reward remains the verifier score of its **first submitted
answer**, even if a follow-up leads to a corrected answer.

### 2.2 Turn feedback into public evidence

The experimental feedback protocol is verifier-assisted:

1. The host grades the submitted answer using the private reference.
2. The host constructs an allowed set of researcher replies. The alternatives
   distinguish acceptance, invalid answer format, a recent tool error and a
   generic request to reconsider.
3. The auxiliary model selects a reply from that allowed set. Invalid output
   falls back to an allowed template and is recorded as such.
4. A PRM-style interpretation request relates the reply to the public execution
   record: model outputs, tool observations, the submitted answer and the reply.

The PRM labels the feedback and identifies relevant fields. Host validation checks
its structure, field addresses and feedback classification. Quote text is not
required to match verbatim. Interpretations remain hypotheses: a generic
correction does not establish a particular scientific cause, and acceptance does
not validate every intermediate step.

The proposal evidence contains public questions, actual model inputs and outputs,
tool calls, observations, valid feedback annotations and execution diagnostics.
Private reference answers and numerical grading outcomes are excluded. Invalid
PRM annotations do not remove the underlying public execution record.

The current step's evidence is combined with a bounded selection of earlier
public failures/corrections and successful controls from the same phase. When a
candidate is adopted, pending evidence is cleared so the next search reflects the
new harness. Aggregate proposal history persists across model updates.

### 2.3 Propose complete Python programs

Each step requests three independent candidate hypotheses from the same parent.
All proposals are generated before the candidate Val results are revealed. Each
candidate can replace the complete `run(task, api)` program, including prompts,
parsing, control flow, memory and tool orchestration.

The improver receives the parent program, public resource inventory, execution
patterns, feedback interpretations, modification history and the task model's
budgets. A proposal must cite evidence from at least two distinct Train tasks.

The structured command interface supports:

| Command | Purpose |
| --- | --- |
| `read` | Inspect an allowed public field, such as an actual model input or tool observation |
| `propose` | Return a complete Python program, hypothesis, rationale and evidence IDs |
| `skip` | Explain why the available evidence does not support a change |

The current protocol permits at most three reads, two repair attempts and six
auxiliary calls per candidate. Reads expose the selected public field from the
requested offset; preview truncation is not a substitute for reading the field.
A repair to an already parsed candidate does not reopen evidence reads.

The host parses candidate Python without executing it. Structural validation
requires a synchronous `run(task, api)` interface and rejects known ineffective
instruction patterns. Execution occurs in an isolated controller container.

### 2.4 Preflight and compare on Val

A structurally valid candidate must first execute on the designated Train
preflight task. Preflight checks execution and answer-format validity; it does
**not** require a correct scientific answer. Byte-identical programs are excluded.

The parent and each remaining candidate are then evaluated on all 90 Val tasks:

- One first-answer attempt per task, without researcher feedback.
- Temperature 0, matched task seeds and the same host budgets.
- Complete task-ID coverage for every program being compared.
- One shared concurrency limit across candidate evaluation jobs.

For a fixed model $M$ and harness $H$, define:

$$
S(H;M,D_{\mathrm{val}})=\frac{1}{|D_{\mathrm{val}}|}
\sum_{x\in D_{\mathrm{val}}}
\mathbf{1}\!\left[\mathrm{Verify}_x(a^{(1)}(M,H,x))=1\right].
$$

$a^{(1)}$ is the first submitted answer. A candidate is eligible to replace the
parent only if its complete Val evaluation has no candidate runtime errors and
its score is strictly higher than the parent's score. Here errors refer to recorded
candidate-program failures (`episode.error`); an ordinary tool error or exhausted
episode budget is a separate recorded outcome, not automatically a controller failure.

Selection retains the parent on a tie. If several candidates tie above the parent,
the earlier candidate wins. The parent is evaluated again at every step rather
than assigned a cached score from a previous comparison.

The selected score, parent score, candidate validity and decision are recorded.
Only aggregate Val comparisons enter subsequent proposal history; Val traces do
not become improver evidence. At the final harness step, the selected program is
evaluated on Test and handed to the outer stage.

<a id="outer"></a>

## 3. Outer recursion: train the model with a fixed harness

### 3.1 Collect fresh policy trajectories

The selected harness is frozen for the entire RL phase. SkyRL samples eight task
instances per batch and eight attempts per instance, giving 64 episodes in the
default recipe. `N_SAMPLES_PER_PROMPT=16` changes the attempt count independently
of rollout concurrency.

These are fresh on-policy attempts generated by the current task model. The
harness-stage conversations supply procedural evidence, not replayed policy
completions for RL. Val tasks are excluded from the RL training index.

Training uses temperature 1 and top-p 1 with thinking disabled. The first answer
submission ends the episode; no simulated researcher reply is provided during RL.

### 3.2 Verifier reward and training targets

The reward is the host verifier's binary outcome for the submitted answer:

$$
R_i=\mathrm{Verify}_{x_i}(a_i^{(1)})\in\{0,1\}.
$$

The verifier parses the required answer format and checks the private reference.
An attempt that never submits an answer has no successful outcome. PRM feedback
labels are not substituted for this reward.

Each model call becomes a training row containing its actual prompt token IDs,
completion token IDs and rollout log probabilities. Calls in one episode share
a trajectory identity. The episode reward is placed once, on the final completion;
earlier calls receive no separate terminal reward.

Only model-generated completion tokens are training targets. Prompt tokens, tool
outputs, simulated researcher text and generated harness Python are not optimized
as model outputs. An episode with no model calls contributes a recorded failure
but cannot supply a policy-gradient row.

### 3.3 Group-relative credit assignment

For attempts $i=1,\ldots,G$ on the same task instance, GRPO compares their terminal
rewards with the group's mean and standard deviation:

$$
\mu_x=\frac{1}{G}\sum_{i=1}^{G}R_i,
\qquad A_i=\frac{R_i-\mu_x}{\mathrm{std}(R_1,\ldots,R_G)+\delta}.
$$

The pinned SkyRL implementation provides the numerical stabilizer $\delta$ and
uses standard-deviation normalization by default. A group with multiple valid attempts and identical rewards
has zero relative advantage. A group containing both outcomes provides positive
and negative relative advantages. The backend has a separate fallback for a
single surviving trainable trajectory; zero-call failures supply no training row,
and an entirely empty batch is rejected.

Step-wise trajectory handling computes the scalar advantage from each episode's
last model call, then broadcasts it to that episode's model-call rows with their
response masks. An episode with several tool-use steps therefore remains one
rewarded attempt rather than several independently graded tasks.

The regular clipped policy objective compares the updated policy with the
recorded rollout policy at generated tokens. Writing this token ratio as
$\rho_{i,t}(\theta)$, the surrogate has the form:

$$
\min\left(\rho_{i,t}(\theta)A_i,
\mathrm{clip}(\rho_{i,t}(\theta),1-\epsilon_{\mathrm{low}},1+\epsilon_{\mathrm{high}})A_i\right).
$$

The pinned backend controls clipping and loss reduction; its default reduction is
a mean over valid tokens. The maintained recipe uses a learning rate of `1e-6`,
one update epoch per batch, and disables both KL loss and KL reward penalties.
The default stage has 30 optimizer updates.

### 3.4 Export and return to harness learning

After the final update, the worker exports model weights, configuration and
tokenizer files. It loads that export in a separate evaluation process and checks
complete Test coverage and nonempty model generation before accepting the stage.
A checkpoint directory or a successful training-process exit is insufficient on
its own.

The verified export becomes $M_{k+1}$, and the selected Python program becomes
$H_{k+1,0}$. Optimizer/trainer state is not retained in these exports. The next
stage starts from the exported model weights.

<a id="execution"></a>

## 4. Fixed execution contract

The generated harness can organize the agent's behavior, but the host retains
control of the scientific environment and training contract:

| Component | Responsibility |
| --- | --- |
| Harness controller | Execute the candidate's standalone Python program |
| `api.generate(messages)` | Request a task-model completion under the host budget |
| `api.execute(code)` | Run Python in a separate persistent scientific execution container |
| `api.submit(answer)` | Submit text to the host verifier |
| Host broker | Enforce provenance, limits, grading and episode termination |
| Training adapter | Preserve actual model contexts, log probabilities and completion masks |

The controller and execution containers have no network access. Only the scientific
execution container receives the public task assets and frozen data lake. Private
references and service credentials stay on the host.

Messages identify their source as task, model, tool, feedback or harness. The host
validates this metadata, applies tool-history budgets and removes the metadata
before tokenization. Task questions and feedback must match their actual source;
user-role harness instructions and budget notices must be explicitly identified.

The host clips tool responses and older tool history within the configured token
budgets. Clipping preserves recorded provenance and the actual shortened model
input. A new harness cannot escape these budgets by renaming a tool observation.

Candidate controller errors make a program ineligible. A confirmed memory failure
in the scientific execution container stops the affected episode with zero reward.
Unrecognized solver/runtime infrastructure failures remain explicit errors rather
than scientific evidence for a new procedure. Auxiliary proposal failures are
recorded as failed or skipped proposal attempts.

<a id="evaluation"></a>

## 5. Evaluation and interpretation

The three splits serve different purposes:

| Split | Count | Use | Feedback available to learning |
| --- | ---: | --- | --- |
| Train | 715 | Harness interactions and fresh RL attempts | Public interaction evidence for harness proposals; verifier rewards for RL |
| Val | 90 | Parent/candidate harness selection | Aggregate selection comparison only |
| Test | 90 | Stage-boundary measurement and export checks | No proposal traces, researcher feedback or RL updates |

The same Test assignment is used in both learning phases. Task IDs are disjoint,
but material groups overlap across Train–Val and Train–Test as declared in the
frozen release. This is not a claim that the Test material is independent or
previously unseen.

The maintained `always_debug` trigger runs the fixed stage schedule whether or not
the harness improved its Test score. The optional `improvement` trigger uses the
stage's changed harness and Test gain to control handoff; reporting an unbiased final assessment under
that alternative requires a separate final holdout.

The default measurement schedule is:

1. Harness stage baseline Test evaluation.
2. Full Val comparison at every harness step.
3. Harness stage-end Test evaluation of the selected program.
4. RL baseline Test evaluation under the inherited harness.
5. Test evaluation from the actual stage-end model export.

During co-evolution, the trainer suppresses post-update in-trainer evaluation so
the worker's export-load evaluation supplies the stage-end measurement. The
standalone model mode can use its configured periodic evaluation schedule.

Training accuracy measures changing sampled batches. Val scores are used for
selection. Neither should be presented as an independent Test curve. Report
first-answer accuracy, attempt budgets and task denominators together; pass@k
coverage is a different metric and requires the corresponding repeated attempts.
Use only recorded measurements for results, and retain the original run provenance
when a stage was inherited through continuation.

<a id="handoff"></a>

## 6. Stage handoff and continuation

The experiment pins the identities of the dataset, verifier, runtime, model and
harness. A harness stage publishes an immutable request containing the selected
program and RL execution contract. A worker claims the request, trains the model,
validates its export and publishes a matching result. The next stage consumes only
a validated result.

Continuation always starts a new run directory. It can resume from a completed
RL stage using its verified model export. If RL failed after a fully completed
harness phase, it can reuse that harness and restart the RL stage from the pinned
base model. Unsaved optimizer updates are not restored or counted as part of the
new model's learning history.

The continuation validator checks experiment settings and dataset/runtime/verifier
identities, the selected harness hash, the published handoff, and the appropriate
base checkpoint. A still-running source experiment cannot be restarted through
the failed-stage recovery path.

### Default algorithm in pseudocode

```text
model, harness = M0, H0
history, train_cursor = empty, 0

for cycle in 1..3:
    keep model fixed
    preflight inherited harness; measure baseline Test
    pending_evidence = empty

    for step in 1..3:
        collect 16 Train interactions with current harness
        advance train_cursor; accumulate public evidence
        propose 3 candidates from the same parent and evidence
        preflight valid, distinct candidate programs
        evaluate parent and valid candidates on all 90 Val tasks
        adopt the earliest strictly better error-free candidate, or retain parent
        record the selection and aggregate Val history
        clear pending_evidence after adoption

    measure selected harness on Test
    publish immutable model/harness/runtime handoff
    release harness-stage inference services

    keep selected harness fixed
    measure RL baseline Test
    for update in 1..30:
        collect fresh grouped Train attempts
        compute first-answer verifier rewards and GRPO advantages
        update task-model parameters from actual generated tokens

    export model; load and evaluate export on Test
    publish and consume validated stage result
    inherit selected harness and exported model for the next cycle
```

This pseudocode describes a fresh run with the fixed `always_debug` schedule.
Continuation and the optional improvement-triggered stop follow the rules above.

<a id="code"></a>

## 7. Implementation map

| File | Algorithm responsibility |
| --- | --- |
| [coevolve/loop.py](../src/simple_scibuddy/coevolve/loop.py) | Alternating stages and experiment state |
| [coevolve/phase.py](../src/simple_scibuddy/coevolve/phase.py) | Train interactions, candidate search and phase evaluations |
| [coevolve/feedback.py](../src/simple_scibuddy/coevolve/feedback.py) | Simulated researcher replies and PRM interpretation |
| [coevolve/evidence.py](../src/simple_scibuddy/coevolve/evidence.py) | Public evidence extraction and execution diagnostics |
| [coevolve/context.py](../src/simple_scibuddy/coevolve/context.py) | Readable trace fields, evidence context and annotation checks |
| [coevolve/program.py](../src/simple_scibuddy/coevolve/program.py) | Full-program proposals and bounded repair |
| [coevolve/selection.py](../src/simple_scibuddy/coevolve/selection.py) | Complete paired Val scoring and tie rules |
| [harness/broker.py](../src/simple_scibuddy/harness/broker.py) | Scientific episode execution and first-answer reward |
| [training/generator.py](../src/simple_scibuddy/training/generator.py) | Fresh policy rollouts and trajectory identities |
| [training/trajectory.py](../src/simple_scibuddy/training/trajectory.py) | Model-call training rows, terminal reward and completion masks |
| [training/entrypoint.py](../src/simple_scibuddy/training/entrypoint.py) | SkyRL trainer extension and evaluation/export behavior |
| [coevolve/worker.py](../src/simple_scibuddy/coevolve/worker.py) | Training, export checks and result publication |
| [coevolve/continuation.py](../src/simple_scibuddy/coevolve/continuation.py) | Verified boundary recovery |

GRPO advantage computation and clipped policy optimization are delegated to the
pinned upstream code in `skyrl/`, including `skyrl/train/trainer.py` and
`skyrl/backends/skyrl_train/utils/ppo_utils.py` within that submodule. The owned
adapter preserves their step-wise trajectory contract.
