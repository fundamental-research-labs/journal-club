# ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration

**Authors:** Andrew Estornell, Jean-Francois Ton, Yuanshun Yao, Yang Liu
**arXiv:** 2411.00053
**Venue:** ICLR 2025
**Date:** March 2025

## Problem
Multi-agent debate and deliberation methods often rely on off-the-shelf LLMs whose collaborative behavior is assumed to emerge from prompting. The paper asks whether collaboration itself can be trained, especially for actor-critic teams where one model answers and another provides feedback.

## Method
ACC-Collab jointly trains a two-agent team: an actor that produces answers and a critic that gives feedback over multiple deliberation rounds. The method alternates training the critic and actor, estimates partial trajectory rewards by rolling out from intermediate conversation states, and builds preference pairs from "guided collaborative trajectories" that steer discussion toward or away from the known answer. The selected positive/negative trajectory pairs are then optimized with DPO. Experiments use Llama-3-8B-Instruct, Mistral-7B-Instruct, and Gemma-2-2B-Instruct on BoolQ, MMLU, BBH, SCIQ, and ARC.

## Key Findings
- Table 1 reports that ACC-Collab or ACC-Collab+ gives the highest five-round accuracy in almost every model/dataset setting, with the main visible exception being Gemma-2 on MMLU.
- Figure 2 shows ACC-Collab+ has the strongest average improvement from the first to fifth deliberation round for all three base model families.
- A single training round often suffices; the paper notes that a second round can sometimes degrade performance, so it uses a hold-out set to decide whether to continue training.
- Table 2 suggests the trained actor is usually stronger than the trained critic when paired with an untrained partner, but pairing trained actor and trained critic generally improves the team.
- Qualitative examples in Figure 4 and Appendix C.2 show trained critics becoming less agreeable and more willing to give detailed corrective feedback.
- The authors explicitly limit the evidence to QA-style tasks with known correct/incorrect answers, same-task train/test splits, and 2B-8B model sizes.

## Tags
`multi-agent`, `actor-critic`, `collaboration-training`, `LLM-debate`, `DPO`, `guided-trajectories`, `question-answering`, `ICLR-2025`

## Connections
- Closely related to multi-agent debate work such as Society of Minds, Persona, DebateTune, and DebateGPT, but shifts from prompting or single-model fine-tuning to training a collaborative two-agent team used at inference.
- Complements papers on multi-agent coordination failure by showing one route to train more useful critic behavior, while still relying on relatively controlled QA settings.
- Relevant to agent-team benchmarks because it separates collaborative improvement across rounds from ordinary single-shot accuracy gains.
