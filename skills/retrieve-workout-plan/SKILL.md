---
name: retrieve-workout-plan
description: Retrieve and explain the next workout from a Tana system using its TANA_SYSTEM.md contract. Use before a workout or when checking the current plan; do not invent missing programming or treat completed sessions as plans.
---

# Retrieve Workout Plan

Read `TANA_SYSTEM.md` first, then inspect current Tana evidence.

## Procedure

1. Resolve the contract's workout-plan convention and authoritative workspace scope.
2. Find the current or next planned workout using the documented tag, date, naming,
   and status conventions.
3. Read its planned exercises, sets, repetitions, notes, and allowed substitutions.
4. Distinguish exact Tana evidence from interpretation or optional coaching.
5. Return the source workout, the plan in execution order, ambiguities, and a concise
   voice-friendly summary.

If multiple plans qualify, show the candidates and ask which one is intended. If the
contract and Tana disagree, stop and report drift. This skill is read-only.
