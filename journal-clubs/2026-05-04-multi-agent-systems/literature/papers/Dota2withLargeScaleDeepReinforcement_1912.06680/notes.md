# Notes

## Why It Matters
OpenAI Five is one of the clearest demonstrations that large-scale self-play reinforcement learning can master a complex, partially observed, team-based real-time game. Its lasting value is partly empirical, but also practical: the paper documents what mattered when scaling RL beyond clean benchmarks, including rollout freshness, sample reuse, enormous batches, long reward horizons, and tooling for continuing training while the environment and model changed.

## When To Cite
Cite this paper when discussing superhuman esports agents, self-play at extreme scale, multi-agent RL in partially observed team games, PPO systems engineering, credit assignment over long horizons, or continual training across changing environments. It is also useful as a caveated example of benchmark achievement under task restrictions: OpenAI Five did not play every Dota 2 hero/item combination and did not learn directly from pixels.

## Key Terms
OpenAI Five; Dota 2; self-play; Proximal Policy Optimization (PPO); Generalized Advantage Estimation (GAE); recurrent policy; LSTM; distributed rollout workers; forward-pass GPUs; optimizer GPUs; TrueSkill; surgery; continual transfer; data staleness; sample reuse; team spirit; reward shaping; long-horizon credit assignment; semantic observations; restricted hero pool.
