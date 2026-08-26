# Tana system: fitness tracker example

## Scope and purpose

- Scope: a sanitized fitness-tracker subsystem in a public demo workspace.
- Purpose: plan simple workouts, record completed sets, and review workout history.
- This example contains no personal health history or private workspace identifiers.

## Vocabulary

| Concept | Owner-confirmed meaning | Tana representation |
|---|---|---|
| Workout | A dated plan or completed session; the title and notes state which | `workout` tag |
| Exercise | A reusable movement referenced by workouts and sets | `exercise` tag |
| Set | One explicitly completed or planned quantity for one exercise | `set` tag |

## Architecture

### Tags and fields

| Tag | Purpose | Important fields | Evidence status |
|---|---|---|---|
| `workout` | Groups a dated session | Date, Workout Notes, Exercise, Sets | Observed |
| `exercise` | Reusable movement vocabulary | Muscle Group | Observed |
| `set` | Records one quantity | Reps, Workout, Exercise | Observed |

### Relationships and hierarchy

- A workout can reference several exercises.
- Sets are owned beneath the workout's Sets field in the demo convention.
- Every set links back to exactly one workout and one existing exercise.
- Plan and completion status are not separate fields in this legacy demo schema.
  The owner confirmed that titles and Workout Notes must label `PLAN` or `COMPLETED`.

## Source-of-truth rules

- Current Tana fields are authoritative for structure and recorded quantities.
- This file is authoritative for the meaning of the demo conventions and safety boundary.
- If this file and Tana disagree, stop and report drift.

## Retrieval guidance

- A planned workout must be future-dated or explicitly labeled `PLAN` in its title/notes.
- Never treat a completed session as a plan merely because it is the newest workout.
- Reconcile exercises against existing `exercise` instances before proposing new ones.

## Write boundaries

- Default to read-only.
- A workout write requires an exact preview and explicit approval.
- Log only explicitly completed sets; never infer missing quantities.
- Demo writes are limited to the designated System Lab 11 workout branch.
- After writing, read back the workout and every set relationship.

## Client-neutral workflow rules

- Cite whether a statement comes from live Tana evidence or this contract.
- Keep optional coaching separate from the retrieved plan.
- A voice transcript is capture input, not proof that a Tana write succeeded.

## Unresolved questions

- A future version could add an explicit plan/completed status field. The v0 demo does not change the legacy schema.

## Validation receipt

- Structural claims were checked against the sanitized demo schema.
- Meanings and conventions are owner-confirmed for the example only.
- No private identifiers are included.
