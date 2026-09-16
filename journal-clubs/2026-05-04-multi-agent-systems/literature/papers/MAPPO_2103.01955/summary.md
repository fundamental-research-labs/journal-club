# The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games

**Authors:** Chao Yu, Akash Velu, Eugene Vinitsky, Jiaxuan Gao, Yu Wang, Alexandre Bayen, Yi Wu
**arXiv:** 2103.01955
**Venue:** NeurIPS 2022 Datasets and Benchmarks Track
**Date:** November 2022

## Problem
On-policy PPO is widely used in single-agent reinforcement learning but is often discounted in cooperative multi-agent reinforcement learning because off-policy methods are assumed to be more sample-efficient. The paper tests whether that assumption still holds when PPO is implemented and tuned carefully for cooperative MARL.

## Method
The authors evaluate PPO-based methods on four cooperative MARL testbeds: MPE, SMAC, Google Research Football, and Hanabi. MAPPO uses a centralized value function during training and decentralized policies during execution, while IPPO uses local inputs for both policy and value function. The study compares these methods with off-policy baselines such as MADDPG, QMix, RODE, CDS, TiKick, SAD, and VDN, then ablates implementation choices including value normalization, critic inputs, sample reuse, clipping, batch size, parameter sharing, and death masking.

## Key Findings
- PPO-based methods are competitive with or stronger than off-policy baselines across the tested cooperative benchmarks, often with comparable sample use.
- In SMAC, MAPPO and IPPO perform at least as well as QMix on most maps, and MAPPO is comparable or superior to RODE on many maps under matched sample budgets.
- In Google Research Football academy scenarios, MAPPO clearly beats QMix in every reported scenario and is competitive with methods that use intrinsic reward or pretraining.
- In Hanabi-Full, MAPPO is comparable to or stronger than SAD and VDN in most reported player counts, with a larger gap over IPPO as the number of players increases.
- Practical PPO details matter: value normalization, informative but compact centralized critic inputs, limited epoch/minibatch reuse, conservative clipping, and sufficiently large batches are key to the reported results.
- The conclusion is intentionally scoped: the study is empirical and focuses on cooperative, discrete-action, mostly homogeneous-agent environments.

## Tags
`multi-agent-rl`, `cooperative-marl`, `ppo`, `mappo`, `ippo`, `ctde`, `sample-efficiency`, `smac`, `hanabi`, `google-research-football`

## Connections
- Complements MADDPG and value-decomposition work by arguing that a well-configured on-policy baseline should not be dismissed in cooperative MARL.
- Useful baseline reference for papers that evaluate multi-agent coordination on SMAC, MPE, GRF, or Hanabi.
- Relevant to later multi-agent-system discussions as an example where simple shared-parameter coordination plus centralized training can be enough before adding more specialized architectures.
