# Frozen architecture inspection

| Claim | Lane | Evidence |
|---|---|---|
| Workouts have Date, Workout Notes, Exercise, and Sets fields | Observed | Tag schema |
| Sets link to a workout and an exercise | Observed | Tag schema and representative instances |
| A workout may represent a plan or completed session | Inferred | Names and notes vary |
| PLAN and COMPLETED labels define the demo convention | Owner-confirmed | Demo clarification |
| Whether status should become a field | Unresolved | Requires an architecture decision |
