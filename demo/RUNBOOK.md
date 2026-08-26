# System Lab 11 demo runbook

## Prepared ahead

- Public repository and both client connections verified.
- Sanitized Build Session workspace and exact demo scope verified.
- Planned workout, exercise vocabulary, frozen inspection, and workout report prepared.
- Successful screenshots or short recordings captured at every tool-dependent transition.

## Live sequence

1. Run `discover-tana-system` read-only against the fitness-tracker subsystem.
2. Show observed, inferred, owner-confirmed, and unresolved lanes.
3. Generate `TANA_SYSTEM.md` and compare it with the template.
4. Open the same file in a second client and ask it to explain the demo system.
5. Retrieve the planned workout through `retrieve-workout-plan`.
6. Use the frozen voice transcript if live capture is unclear.
7. Run `log-workout`, show the exact preview, approve one bounded write, and read it back.
8. Close by showing that the updated workout can be summarized from Tana.

## Fallback order

1. Retry one bounded read once.
2. Use the frozen inspection or report.
3. Show the prepared write preview without writing.
4. Play the corresponding sub-20-second recording.

Never troubleshoot authentication, repository indexing, or connector installation on stage.
