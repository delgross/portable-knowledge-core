# System Lab 11 demo runbook

## Prepared ahead

- Public repository and both client connections verified.
- Sanitized Build Session workspace and exact demo scope verified.
- Planned workout, exercise vocabulary, frozen inspection, and workout report prepared.
- Successful screenshots or short recordings captured at every tool-dependent transition.

## Required Claude Mobile rehearsal

Treat this as a validation path to test before the event, not as a capability already
verified in this demo environment.

1. On `claude.ai`, open **Settings > Connectors** on the same Claude account used by
   Claude Mobile.
2. Add and authenticate the Tana remote MCP connector there, then enable it.
3. Open Claude for iOS or Android. A new remote server cannot be added directly from
   Claude Mobile.
4. Confirm that the previously configured connector is available on mobile.
5. Run the same bounded Tana discovery and workout-plan retrieval used in the desktop
   demo. Keep the test read-only; do not use mobile for the live workout write unless a
   separate write rehearsal passes.
6. Capture screenshots or a short recording and record the app version, device, account
   plan, connector state, and result.

Acceptance requires a fresh Tana read, contract-guided interpretation, and retrieval of
the exact demo workout plan. If any step fails, omit the live mobile segment and present
it as a future portability path with the captured failure boundary.

Plan assumptions to verify during rehearsal: Anthropic documents custom remote MCP
connectors for Pro, Max, Team, and Enterprise plans. Team and Enterprise organizations
may require an owner to enable the connector for the organization.

## Live sequence

1. Run `discover-tana-system` read-only against the fitness-tracker subsystem.
2. Show observed, inferred, owner-confirmed, and unresolved lanes.
3. Generate `TANA_SYSTEM.md` and compare it with the template.
4. Open the same file in a second client and ask it to explain the demo system.
5. Retrieve the planned workout through `retrieve-workout-plan`.
6. Use the frozen voice transcript if live capture is unclear.
7. Run `log-workout`, show the exact preview, approve one bounded write, and read it back.
8. Close by showing that the updated workout can be summarized from Tana.

If the Claude Mobile rehearsal passes, insert a short portability proof after step 5:
open the same Claude account on mobile and repeat the read-only workout retrieval using
the already configured connector. This is not a connector-setup demonstration.

## Fallback order

1. Retry one bounded read once.
2. Use the frozen inspection or report.
3. Show the prepared write preview without writing.
4. Play the corresponding sub-20-second recording.

Never troubleshoot authentication, repository indexing, or connector installation on stage.
