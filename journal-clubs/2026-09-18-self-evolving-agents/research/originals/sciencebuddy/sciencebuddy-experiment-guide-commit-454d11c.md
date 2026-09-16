# Simple-SciBuddy experiment guide

This guide describes the configured double-recursive RSI experiment.
Read the [algorithm guide](algorithm.md) for the learning procedure and evaluation
semantics, or return to the [ScienceBuddy overview](../README.md#rsi).
Commands below run from the repository root.

<a id="recipe"></a>

## Maintained recipe

The checked-in [experiment configuration](../configs/train.toml) and
[SkyRL recipe](../configs/skyrl.json) define the current experiment.

| Component | Setting |
| --- | --- |
| Task model | Qwen3.5-4B |
| Auxiliary improver | Remote Chat Completions model; configured as `gpt-6-astra`, medium reasoning |
| Auxiliary output budget | 8,192 tokens |
| Schedule | `h0001 → r0001 → h0002 → r0002 → h0003 → r0003` |
| Harness steps per stage | 3 |
| Train interactions per step | 16 |
| Proposals per step | 3 from the same parent |
| Candidate selection | Complete 90-task Val comparison against the parent |
| RL updates per stage | 30 |
| RL batch | 8 task instances × 8 attempts |
| Learning rate | `1e-6` |
| Backend | SkyRL, FSDP and vLLM |
| KL loss / KL reward penalty | Both disabled |
| Task-model sampling | Temperature 1, top-p 1, thinking disabled |
| Evaluation sampling | Temperature 0, one attempt per task |
| Rollout concurrency | 64; candidate Val jobs share that limit |
| Evaluation schedule | Harness start/end; RL baseline and stage-end export load |
| Checkpoints | Stage-end HF model/tokenizer export, without optimizer state |

These settings describe the maintained recipe, not measured performance.
A completed fresh run contains three harness stages and three RL stages. A
continuation reuses the validated stages recorded in its source run.

<a id="data"></a>

## Dataset and budgets

The frozen release is `data/releases/id715-val90-test90-v1`:

| Family | Train | Harness Val | Test |
| --- | ---: | ---: | ---: |
| DbQA | 411 | 50 | 50 |
| GWAS | 140 | 20 | 20 |
| LitQA2 | 76 | 10 | 10 |
| ProtocolQA | 88 | 10 | 10 |
| **Total** | **715** | **90** | **90** |

Harness interactions and RL use Train. Harness selection uses Val. Both learning
phases use the same Test assignment for evaluation. Val never enters RL updates.
The split is by task ID; its material-overlap limitations are explained below
and in the [algorithm guide](algorithm.md#evaluation).

| Episode limit | Budget |
| --- | ---: |
| Context | 24,576 tokens |
| Generated tokens per model call | 4,096 |
| Model calls / tool calls | 9 / 9 |
| Visible tool response | 2,048 tokens |
| Total visible tool history | 8,192 tokens |
| Python call timeout | 60 seconds |
| Episode timeout | 900 seconds |
| Researcher replies | At most 1 during harness interaction; 0 during RL/evaluation |

<a id="reproduce"></a>

## Setup and run

Clone this repository as its own checkout, including its pinned SkyRL submodule:

```bash
git clone --recurse-submodules https://github.com/Gen-Verse/ScienceBuddy-RSI.git
cd ScienceBuddy-RSI
```

The training recipe targets Linux, Python 3.12, CUDA 13, Docker and eight A100 GPUs.
Place Qwen3.5-4B at `models/Qwen3.5-4B` and the authorized frozen task release at
`data/releases/id715-val90-test90-v1`. Weights and task assets are supplied
separately. Machine-specific paths can be overridden in the ignored
`configs/local.json`.

1. Set your improver endpoint and a fresh experiment ID in
   [configs/train.toml](../configs/train.toml).
2. Supply `SCIENCEBUDDY_IMPROVER_API_KEY` and `WANDB_API_KEY` through the environment,
   or literal assignments in `.secrets/improver.env` and `.secrets/wandb.env`.
3. Prepare the environment and launch from the repository root:

```bash
bash scripts/setup.sh
python scripts/train.py configs/train.toml
```

For an unattended run, use the exact experiment ID configured in the TOML:

```bash
experiment_id=qwen35-4b-coevolve-YYYYMMDD-01
mkdir -p runs/logs
nohup bash -c 'python scripts/train.py configs/train.toml; status=$?; printf "%s\n" "$status" > "runs/logs/$1.exit"; exit "$status"' _ "$experiment_id" > "runs/logs/$experiment_id.launch.log" 2>&1 < /dev/null &
echo "$!" > "runs/logs/$experiment_id.pid"
```

The defaults in [configs/defaults.json](../configs/defaults.json) are overridden by
`configs/local.json`, then explicit experiment settings. All project paths in
configuration must be relative: TOML paths are relative to the TOML file; JSON
paths are relative to the repository root. Absolute settings and references or
symlinks escaping this repository are rejected. Place the model and data inside
this checkout rather than linking to files in another workspace.
[configs/skyrl.json](../configs/skyrl.json) holds the backend recipe.
`N_SAMPLES_PER_PROMPT=16` selects sixteen attempts instead of eight.

The task release must also be self-contained. Its `environment.lock.json` uses a
relative `data_lake.path` (for example, `resources`) inside the release directory,
and task-index `task_dir` fields are relative to their JSONL file. Keep public
assets, private references and frozen runtime build files inside that release.
The host's installed Python/CUDA/Docker toolchain and fixed paths inside the
container are runtime prerequisites; no sibling project is imported.
The launcher does not force a machine-specific CUDA or shared-library
location. Optional `SIMPLE_SCIBUDDY_CUDA_HOME` and `SIMPLE_SCIBUDDY_CUDA_COMPAT`
overrides must point to relative locations within this checkout.

The frozen task-ID split is 715 Train / 90 Val / 90 Test; Val is excluded from RL.
Related material groups overlap across Train–Val (20 groups) and Train–Test
(18 groups), so task-ID separation is not a claim of independent test material.
All assignments are preserved; setup does not reconstruct or randomly resplit data.

Each experiment records input identities, selected harnesses, model exports and
measurements under `runs/`. Stage-end exports omit optimizer state. An optional
`continue_from` in the TOML starts a new run from a verified completed boundary;
unsaved optimizer updates are not restored.

<details>
<summary><b>CPU checks and repository layout</b></summary>

```bash
python3.12 -m venv .venv-check
.venv-check/bin/python -m pip install -e '.[dev]'
bash scripts/check.sh
```

The default checks use synthetic data and mocked components; they exclude
`tests/integration/` and need no model, task release, GPU or Docker.

```text
assets/                  Paper illustrations and the usage video
docs/                    Algorithm and experiment guides
configs/                 Runtime defaults and experiment recipe
src/simple_scibuddy/      Standalone scientific-agent RSI implementation
scripts/                 Setup, launch and CPU checks
tests/                   Unit tests and explicit integration checks
skyrl/                   Pinned upstream SkyRL submodule
```

</details>

<a id="outputs"></a>

## Inspect a run

The experiment preserves the launch configuration, identities and measurements
under its own directory in `runs/`. The following files are useful for checking
algorithm behavior without starting additional model calls:

| Record | What it establishes |
| --- | --- |
| `config.toml`, `config.json`, `identities.json` | Requested schedule and pinned inputs |
| `harness_evolve/hNNNN/selection-tasks.json` | Fixed Val task membership |
| `harness_evolve/hNNNN/step-NNNN/selection.json` | Candidate validity, paired scores and selection |
| `harness_evolve/hNNNN/summary.json` | Stage-boundary Test measurements and selected harness |
| `harness_evolve-history.json` | Accepted/rejected proposals and aggregate Val comparisons |
| `shared/rounds/rNNNN/request.json` | Frozen model/harness/runtime handoff contract |
| `shared/rounds/rNNNN/rl-train/settings.json` | Effective RL settings and input identities |
| `shared/rounds/rNNNN/rl-train/evaluation-history.jsonl` | In-trainer evaluations, including the RL baseline |
| `shared/rounds/rNNNN/rl-export-eval/evaluation.json` | Test evaluation from the actual exported model |
| `shared/rounds/rNNNN/result.json` | Validated stage completion and model export |
| `continuation.json` | Inherited stage boundary and recovery provenance |

Raw episode records preserve first answers, verifier outcomes, model calls,
observations and termination reasons. Training accuracy describes changing
sampled batches; it should not be treated as a fixed-panel Test curve.

<details>
<summary><b>Other configured modes</b></summary>

- `mode = "harness_evolve"`: one harness-learning phase with the task model fixed.
- `mode = "model"`: train or evaluate with a fixed harness, selected through
  `[model].mode` and optional relative model/harness paths.
- `mode = "coevolve"`: alternate harness and model learning for the configured
  number of complete cycles.

`smoke` and `overfit` model modes execute actual rollouts. The CPU check script
and configuration parsing are separate from these model-executing modes.

</details>
