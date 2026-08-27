# System Lab 11 demo runbook

## Prepared ahead

- Public repository and established ChatGPT/Codex connection verified.
- Claude account-level custom-connector flow validated manually with a fresh account;
  the exact Claude Mobile UI and complete workflow remain gated on rehearsal below.
- Sanitized Build Session workspace and exact demo scope verified.
- Planned workout, exercise vocabulary, frozen inspection, and workout report prepared.
- Successful screenshots or short recordings captured at every tool-dependent transition.

## Dual mobile-client rehearsal

The ChatGPT/Codex mobile path through Tana remote MCP is already established. Rehearse
it against the sanitized Build Session fixture and capture a fresh fallback recording.

The Claude account-level connector flow is validated. Claude Mobile remains a required
rehearsal path: verify the exact mobile UI and complete portable workflow before putting
it on stage.

1. In Claude Desktop or on `claude.ai`, using the same Claude account as Claude Mobile,
   add `https://home.tana.inc/mcp` as a custom connector.
2. Authenticate and enable the connector there.
3. Open Claude for iOS or Android. A new remote server cannot be added directly from
   Claude Mobile.
4. Confirm that the previously configured connector is available on mobile.
5. Run the same bounded architecture discovery, contract-guided interpretation, and
   workout-plan retrieval used in the ChatGPT/Codex mobile path.
6. Generate the same workout logging preview from the frozen report. Do not perform a
   Claude Mobile write unless a separate preview-confirm-write-readback rehearsal passes.
7. Capture screenshots or a short recording and record the app version, device, account
   plan, connector state, and result.

Acceptance requires a fresh Tana read, contract-guided interpretation, and retrieval of
the exact demo workout plan. If any step fails, omit the live Claude Mobile segment and
present it as a future portability path with the captured failure boundary.

Plan assumptions to verify during rehearsal: Anthropic documents custom remote MCP
connectors for Pro, Max, Team, and Enterprise plans. Team and Enterprise organizations
may require an Owner or Primary Owner to add the organization connector.

## Live account and data boundaries

- Use only the Thought of Waves Claude account and the demo Tana account.
- Use only the sanitized public Portable Tana repository as GitHub context; do not
  connect or reveal a private repository.
- Hide passwords, tokens, authentication screens, account recovery details,
  notifications, private workspaces, and personal data from the capture.
- Demonstrate entering the connector name and `https://home.tana.inc/mcp`, then pause or
  hide the shared screen for authentication. Resume only after the connector is enabled.
- If setup does not complete immediately, switch to the pre-authenticated connector and
  the prepared recording. Do not troubleshoot credentials on stage.

## Live sequence

1. Run `discover-tana-system` read-only against the fitness-tracker subsystem.
2. Show observed, inferred, owner-confirmed, and unresolved lanes.
3. Generate `TANA_SYSTEM.md` and compare it with the template.
4. In the Thought of Waves Claude account, demonstrate adding the Tana Outliner remote
   MCP custom connector with `https://home.tana.inc/mcp`. Keep authentication off-screen.
5. Give Claude the sanitized public Portable Tana source and show it combining the
   shared contract with fresh context from the demo Tana account.
6. Ask Claude to explain the demo architecture, then retrieve the planned workout
   through `retrieve-workout-plan`.
7. On ChatGPT/Codex mobile, repeat the discovery/contract-guided workout retrieval and
   produce a logging preview from the workout report.
8. If the Claude Mobile rehearsal passes, repeat the same portable workflow on Claude
   Mobile using the connector already configured on the same account. This is not a
   second connector-setup demonstration.
9. Compare the two results by shared contract and Tana behavior, not by product ranking.
10. Choose one rehearsed client for the single bounded write: show the exact preview,
   obtain explicit confirmation, write, and read back every created relationship.
11. Use the other mobile client to retrieve or summarize the updated workout from Tana.
12. Close on the portable pattern: one Tana source, one shared contract, multiple clients.

Use the frozen voice transcript if live capture is unclear. Never let either client skip
the preview-confirm-write-readback boundary, and never perform duplicate demonstration
writes.

## Fallback order

1. Retry one bounded read once.
2. Use the frozen inspection or report.
3. If the exact Claude Mobile UI or workflow is still incomplete, show its prepared
   fallback and state that mobile remains unrehearsed; the account-level connector flow
   itself has been validated.
4. Continue the live mobile proof with the established ChatGPT/Codex path.
5. Show the prepared write preview without writing.
6. Play the corresponding sub-20-second recording.

Never troubleshoot authentication, repository indexing, or connector installation on stage.
