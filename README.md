# Journal club

Research, slides, and discussion materials for journal club, together with the
agent tooling used to prepare them.

Current session: [September 18, 2026 — Self-evolving agents](journal-clubs/2026-09-18-self-evolving-agents/README.md).

Archived materials: [May 4, 2026 — Multi-agent systems](journal-clubs/2026-05-04-multi-agent-systems/README.md), imported from `gyyang/Literature` using its repository creation date.

The [complete Literature workspace](journal-clubs/2026-05-04-multi-agent-systems/literature/README.md) includes the [review paper PDF](journal-clubs/2026-05-04-multi-agent-systems/literature/manuscript/multi-agent-review-draft/build/index.pdf), editable manuscript, full paper corpus, and [tooling instructions](journal-clubs/2026-05-04-multi-agent-systems/FULL_IMPORT.md).

- [`AGENTS.md`](AGENTS.md): guidance for agents working in this repository.
- [`journal-clubs/`](journal-clubs/): materials grouped by session.
- [`tools/`](tools/): shared scripts and agent tooling, added as needed.

To start a session, create `journal-clubs/YYYY-MM-DD-short-topic/` (or
`undated-short-topic/`) with a short `README.md` listing the topic, selected papers,
and links to the materials. Keep research notes, editable presentation sources,
and final deliverables together in that directory.

There is no required build system or dependency setup yet. Document any
session-specific generation or analysis commands with that session.

## Journal club skills

Three skills in [`tools/skills/`](tools/skills/) support individual stages or an
end-to-end workflow:

- [`$journal-club-research`](tools/skills/journal-club-research/SKILL.md) maps the
  field, reads primary sources and practitioner work, and organizes evidence,
  emerging trends, and research gaps.
- [`$journal-club-analyze`](tools/skills/journal-club-analyze/SKILL.md) develops and
  challenges a thesis, distinguishes evidence from interpretation, and builds a
  claim ledger and narrative.
- [`$journal-club-present`](tools/skills/journal-club-present/SKILL.md) turns the
  argument into a visual presentation with editable sources, citations, speaker
  notes, and visual review.

For example: “Use $journal-club-research, $journal-club-analyze, and
$journal-club-present to prepare a 30-minute journal club on self-evolving agents.
Iterate when analysis or slide design reveals evidence gaps.” Invoke just one
skill to research, analyze, or revise an existing session independently.

The [shared workflow](tools/skills/journal-club-research/references/workflow.md)
defines source-to-claim-to-slide traceability, handoffs, targeted feedback loops,
and completion criteria. Skills reuse existing materials and create new files
only when needed. They do not require a separate orchestration service.

To make these skills discoverable locally, link all three into your Codex skills
directory. From the repository root, run the following; existing paths are left
untouched. Start a new session if the skill list has not refreshed.

```sh
skill_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skill_dir"
for skill in journal-club-research journal-club-analyze journal-club-present; do
  if [ ! -e "$skill_dir/$skill" ] && [ ! -L "$skill_dir/$skill" ]; then
    ln -s "$PWD/tools/skills/$skill" "$skill_dir/$skill"
  fi
done
```
