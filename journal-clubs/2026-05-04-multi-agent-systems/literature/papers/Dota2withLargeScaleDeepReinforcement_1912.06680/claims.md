# Claims

## Claim 1: Large-scale self-play RL can reach superhuman Dota 2 performance under OpenAI Five's game restrictions.

**Evidence:** OpenAI Five defeated OG, the reigning Dota 2 world champions, 2-0 in the April 13, 2019 finals and won 99.4% of 7,257 public Arena games against 3,193 teams.

**Caveats/Scope:** The system played a restricted Dota 2 setting: 17 heroes, no items requiring temporary control of multiple units, some scripted mechanics, and semantic observations rather than pixels. Public Arena wins include abandoned games counted as OpenAI Five wins.

**Source pointers:** `paper.pdf`, Abstract; Section 2; Section 4.1; Table 7

## Claim 2: The result primarily demonstrates scaling existing RL techniques, not a fundamentally new RL algorithm.

**Evidence:** The system uses PPO with GAE, self-play, a recurrent policy, and a distributed rollout/optimization architecture. The paper highlights batch sizes of about 1-3 million timesteps, a final model with 158,502,815 parameters, 180 training days spread over 10 months, and an estimate of 770 +/- 50 PFlops/s-days of optimization compute by the OG match.

**Caveats/Scope:** Compute accounting covers optimizer GPU compute and the paper cautions that total project compute and rollout/forward-pass costs are harder to summarize. Many architecture and training details were not exhaustively ablated because experiments were expensive.

**Source pointers:** `paper.pdf`, Sections 3.1-3.2; Section 4; Appendix A; Appendix H; Table 2

## Claim 3: Continual-transfer "surgery" made iterative development feasible in a changing game and code environment.

**Evidence:** The authors report over twenty successful surgeries during the ten-month OpenAI Five run, covering Dota version updates, observation/action changes, new items, and an LSTM-size increase. They argue that restarting after each major change would have been prohibitive; the Rerun experiment took about two months and 150 +/- 5 PFlops/s-days even in the final environment.

**Caveats/Scope:** Surgery was a practical engineering method rather than a solved transfer-learning technique. The paper notes unsuccessful surgery attempts and that the surgery-trained model ultimately plateaued below the from-scratch Rerun model.

**Source pointers:** `paper.pdf`, Section 3.3; Section 4.2; Appendix B; Table 1; Figure 4

## Claim 4: Fresh, low-reuse rollout data was critical for efficient training.

**Evidence:** Early-training ablations show that adding about eight versions of staleness caused significant slowdowns, while reusing samples 2-3 times caused about a factor-of-two slowdown and reuse of 8 could prevent learning a competent policy. The final system targeted staleness between 0 and 1 and sample reuse around 1.

**Caveats/Scope:** These are small-scale early-training experiments, so the exact scaling may differ later in training or under other RL algorithms.

**Source pointers:** `paper.pdf`, Section 4.4; Figure 5; Appendix M

## Claim 5: Longer reward horizons improved high-skill play, supporting the importance of long-term credit assignment.

**Evidence:** Resuming from a trained agent with longer discount horizons improved win rate over the base agent up to the 6-12 minute horizons tested.

**Caveats/Scope:** The horizon experiments resume from a skilled policy rather than training from scratch, and horizon is a proxy for long-term credit assignment rather than direct evidence of explicit planning.

**Source pointers:** `paper.pdf`, Section 4.5; Figure 6

## Claim 6: Dota 2 exposes multi-agent RL difficulty through partial observability, long horizons, and large action/observation spaces.

**Evidence:** The paper reports roughly 45-minute games at 30 FPS, OpenAI Five actions every fourth frame for about 20,000 steps per episode, about 16,000 observed values per timestep, and an average valid action set of roughly 8,000 to 80,000 actions depending on hero.

**Caveats/Scope:** These figures describe the OpenAI Five interface to Dota 2, not the full unrestricted game. The system omits some heroes/items and uses engineered observations.

**Source pointers:** `paper.pdf`, Section 2; Section 3.1; Appendices E-F
