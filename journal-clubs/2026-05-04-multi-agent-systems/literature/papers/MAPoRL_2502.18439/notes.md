# Notes

## Why It Matters
MAPoRL is useful because it treats collaboration among LLM agents as something to train, not just something to prompt. Its central contribution is a concrete post-training recipe for multi-agent systems: agents receive verifier-based rewards over their own answers and the downstream answers they influence, then co-adapt through multi-agent PPO. This makes it a natural citation when discussing whether multi-agent gains require learned interaction policies rather than more debate turns.

## When To Cite
Cite it for multi-agent LLM post-training, reinforcement learning for collaborative debate, verifier-shaped rewards across multiple discussion turns, empirical comparisons between prompted debate and trained collaboration, transfer of collaboration behavior across GSM8K and ANLI, heterogeneous LLM co-training, and limitations of naive SFT for inducing collaboration.

## Key Terms
MAPoRL; multi-agent post-co-training; collaborative debate; multi-agent reinforcement learning; multi-agent PPO; influence-aware verification reward; verifier model; reward shaping; self-revision incentives; majority-influence incentives; GSM8K; TinyGSM; ANLI; QLoRA; heterogeneous LLM collaboration; reward hacking; verifier-generator alignment.
