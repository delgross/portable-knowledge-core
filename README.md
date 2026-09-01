# Portable Knowledge Core

This starter kit helps you teach an AI what **your** Tana system means, save that
understanding in a versioned file, and reuse the same system across AI clients.

It does not install a predefined productivity system. Start from either an idea or an
existing subsystem: the setup skill designs the smallest owner-approved structure,
while the discovery skill interprets structure that already exists. Both produce a
client-neutral `TANA_SYSTEM.md` and small workflow skills.

## Start here

1. Fork this repository and connect a trusted AI client to the fork and Tana Remote MCP.
2. Run [`create-tana-system`](skills/create-tana-system/SKILL.md) when starting from
   “I want a system for X,” or [`discover-tana-system`](skills/discover-tana-system/SKILL.md)
   when useful Tana structure already exists.
3. Review the proposed [`TANA_SYSTEM.md`](TANA_SYSTEM.template.md); correct its meaning and boundaries.
4. Store the approved contract in your own repository.
5. Add small workflow skills that depend on the contract rather than duplicating its architecture.

`create-tana-system` defaults to a short-round **Guided Discovery** interview that must
be confirmed before architecture is proposed. Ask for **Quick Start** when you want only
a goal, a few examples, and the smallest evolvable first version; its assumptions and
unresolved meaning stay explicit.

The included workout example demonstrates the pattern:

- retrieve a plan from Tana;
- capture completed work;
- preview the exact structured write;
- write only after approval; and
- read the result back from Tana.

## Repository map

- `TANA_SYSTEM.template.md` — client-neutral contract template
- `skills/create-tana-system/` — approval-gated design and setup from an idea, blank workspace, or partial system
- `skills/discover-tana-system/` — architecture discovery and contract generation
- `skills/retrieve-workout-plan/` — read-only example workflow
- `skills/log-workout/` — approval-gated write example
- `examples/build-session/` — sanitized example from a public demo workspace
- `examples/from-scratch/` — neutral proposed system package with no Tana writes
- `fixtures/` — frozen inputs for rehearsal and testing
- `demo/RUNBOOK.md` — live event sequence, rehearsal checks, and safe recovery states

## Safety

- Start read-only and scope discovery to one workspace or subsystem.
- Keep observations, inferences, owner confirmations, and unresolved questions distinct.
- Never publish workspace IDs, node IDs, credentials, or private content.
- Review generated contracts before sharing them.
- Require explicit approval and readback for writes.

## Client entry files

`AGENTS.md` and `CLAUDE.md` are lightweight pointers to the shared contract and Skills.
They do not guarantee that any client will load repository instructions automatically.
Confirm the behavior of the specific GitHub integration, project context, or local
checkout you use; otherwise explicitly ask the client to read the files.

See [LICENSE](LICENSE). This starter kit is an educational v0, not a backup or migration tool.
