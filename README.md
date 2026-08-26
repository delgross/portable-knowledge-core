# Portable Tana

Portable Tana helps you teach an AI what **your** Tana system means, save that
understanding in a versioned file, and reuse it across AI clients.

It does not install a predefined productivity system. The discovery skill inspects a
bounded workspace, separates observed structure from inferred intent, asks the owner
for clarification, and proposes a client-neutral `TANA_SYSTEM.md`.

## Start here

1. Connect a trusted AI client to Tana through Remote MCP with the narrowest useful permissions.
2. Run [`discover-tana-system`](skills/discover-tana-system/SKILL.md).
3. Review the proposed [`TANA_SYSTEM.md`](TANA_SYSTEM.template.md); correct its meaning and boundaries.
4. Store the approved contract in your own repository.
5. Add small workflow skills that depend on the contract rather than duplicating its architecture.

The included workout example demonstrates the pattern:

- retrieve a plan from Tana;
- capture completed work;
- preview the exact structured write;
- write only after approval; and
- read the result back from Tana.

## Repository map

- `TANA_SYSTEM.template.md` — client-neutral contract template
- `skills/discover-tana-system/` — architecture discovery and contract generation
- `skills/retrieve-workout-plan/` — read-only example workflow
- `skills/log-workout/` — approval-gated write example
- `examples/build-session/` — sanitized example from a public demo workspace
- `fixtures/` — frozen inputs for rehearsal and testing
- `demo/RUNBOOK.md` — live-versus-prepared event sequence

## Safety

- Start read-only and scope discovery to one workspace or subsystem.
- Keep observations, inferences, owner confirmations, and unresolved questions distinct.
- Never publish workspace IDs, node IDs, credentials, or private content.
- Review generated contracts before sharing them.
- Require explicit approval and readback for writes.

See [LICENSE](LICENSE). This starter kit is an educational v0, not a backup or migration tool.
