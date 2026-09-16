# Notes

## Why It Matters
VDN is a foundational value-factorization method for cooperative MARL. Its core move is simple and durable: train with a centralized team-value objective, but constrain that value into per-agent components so agents can execute independently from local histories. This makes it a key bridge between independent Q-learning and later CTDE methods such as QMIX.

## When To Cite
Cite when discussing value decomposition, value factorization, cooperative MARL with shared rewards, centralized training with decentralized execution, multi-agent credit assignment, or historical baselines for SMAC/PyMARL-style experiments. It is also useful when explaining why naive independent learners and fully centralized joint-action learners can fail under partial observability.

## Key Terms
VDN; value-decomposition network; cooperative MARL; team reward; Dec-POMDP; centralized training decentralized execution; additive value factorization; `Q_tot`; local action-value function; independent Q-learning; joint action learner; lazy agent problem; spurious rewards; weight sharing; role information; information channels; Switch; Fetch; Checkers.
