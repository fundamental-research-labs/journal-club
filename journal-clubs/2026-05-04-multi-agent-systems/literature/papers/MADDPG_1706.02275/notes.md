# Notes

## Why It Matters
MADDPG is a canonical deep MARL paper because it made centralized training with decentralized execution concrete for continuous-control, mixed-motive settings. Its key move is pragmatic: do not require each deployed policy to observe everything, but let the training critic condition on joint information so the learning signal is less non-stationary and less ambiguous. It also became a common baseline for multi-agent particle environments, emergent communication, and physical coordination tasks.

## When To Cite
Cite it when discussing centralized critics for decentralized multi-agent policies, actor-critic MARL, DDPG extensions to multiple agents, cooperative-competitive particle-world benchmarks, emergent communication without differentiable communication-channel assumptions, opponent-policy modeling, or robustness through policy ensembles.

## Key Terms
MADDPG; multi-agent deep deterministic policy gradient; centralized training with decentralized execution; centralized critic; decentralized actor; Markov game; non-stationarity; experience replay; deterministic policy gradient; policy ensemble; opponent policy approximation; cooperative communication; physical deception; predator-prey; covert communication.
