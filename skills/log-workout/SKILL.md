---
name: log-workout
description: Convert a completed workout report into the exact Tana workout structure defined by TANA_SYSTEM.md, require review before writing, and read back the result. Use after someone reports completed sets, repetitions, substitutions, or notes.
---

# Log Workout

Read `TANA_SYSTEM.md` first. Treat spoken or typed workout reports as claims to
normalize and confirm, not permission to write immediately.

## Procedure

1. Resolve the authoritative workspace, workout tag, set tag, exercise references,
   fields, ownership hierarchy, and naming convention from the contract and fresh Tana reads.
2. Parse only explicitly completed work: exercise, set order, repetitions or duration,
   variation/load when supported, substitutions, and session notes.
3. Do not infer omitted sets, quantities, completion, dates, or exercise identity.
4. Reconcile exercise names against existing Tana instances. Propose creation only when
   no safe match exists.
5. Present an exact write preview grouped by workout and set. Identify every node that
   would be created or linked.
6. Write only after explicit approval. Keep the write within the contract's allowed scope.
7. Read back the created workout, its sets, and their exercise/workout relationships.
8. Return a compact receipt plus a summary based on readback, not on the original report.

If the contract and schema differ, or a relationship cannot be verified, do not write.
