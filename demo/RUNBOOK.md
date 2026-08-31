# System Lab 11: Portable Knowledge Core — Presenter Runbook

Operational guidance in this file is presenter-only and is intentionally excluded from
the audience-facing Tana presentation node.

## Prepared ahead

- Public repository and established ChatGPT/Codex connection verified.
- Claude account-level custom-connector flow validated manually with a fresh account;
  the exact Claude Mobile UI and complete workflow remain gated on rehearsal below.
- Sanitized Build Session workspace and exact demo scope verified.
- Planned workout, exercise vocabulary, frozen inspection, and workout report prepared.
- Reset fixtures, exact expected payloads, screenshots, and safe recovery states verified.
- No prerecorded transition clips or substitute demonstration recording prepared.

## Live-only presentation policy

Perform the connector setup, discovery, contract, workout retrieval, logging preview,
approved write, and readback live. Screenshots and frozen fixtures are operational aids
for resetting or confirming state; they are not substitutes for the live demonstration.

## Dual mobile-client rehearsal

The ChatGPT/Codex mobile path through Tana remote MCP is already established. Rehearse
the complete live workflow against the sanitized Build Session fixture.

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
6. Generate the workout logging preview from a fresh live report. Perform the write only
   after explicit confirmation, then read back every created relationship.
7. Record the app version, device, account plan, connector state, result, exact expected
   payload, and reset state. Screenshots may document controls without replacing the
   live rehearsal.

Acceptance requires a fresh Tana read, contract-guided interpretation, and retrieval of
the exact demo workout plan. If any step fails, omit the live Claude Mobile segment and
present it as a future portability path with the captured failure boundary.

Plan assumptions to verify during rehearsal: Anthropic documents custom remote MCP
connectors for Pro, Max, Team, and Enterprise plans. Team and Enterprise organizations
may require an Owner or Primary Owner to add the organization connector.

## Live account and data boundaries

- Use only the Thought of Waves Claude account and the demo Tana account.
- Use only the sanitized public event repository as GitHub context; do not
  connect or reveal a private repository.
- Hide passwords, tokens, authentication screens, account recovery details,
  notifications, private workspaces, and personal data from the shared screen.
- Demonstrate entering the connector name and `https://home.tana.inc/mcp`, then pause or
  hide the shared screen for authentication. Resume only after the connector is enabled.
- If setup does not complete immediately, use the pre-authenticated safe recovery state
  or omit that client segment. Do not troubleshoot credentials on stage.

## Live sequence

1. Run `discover-tana-system` read-only against the fitness-tracker subsystem.
2. Show observed, inferred, owner-confirmed, and unresolved lanes.
3. Generate `TANA_SYSTEM.md` and compare it with the template.
4. In the Thought of Waves Claude account, demonstrate adding the Tana Outliner remote
   MCP custom connector with `https://home.tana.inc/mcp`. Keep authentication off-screen.
5. Give Claude the sanitized public event source and show it combining the
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

If live voice capture is unclear, restate the report live from the exact prepared payload.
Never let either client skip the preview-confirm-write-readback boundary, and never
perform duplicate demonstration writes.

## Full rehearsal acceptance

1. Start from the documented clean demo Tana and repository state.
2. Complete the live ChatGPT/Codex connector, discovery, contract, workout retrieval,
   preview, confirmation, write, and readback sequence.
3. Reset safely, then complete the equivalent Claude account and mobile sequence,
   including live connector setup with authentication hidden.
4. Confirm both clients interpret the same shared contract and retrieve the same plan.
5. Confirm the selected writing client produces the exact expected payload, waits for
   explicit approval, writes once, and reads back every relationship.
6. Confirm the other client can retrieve the newly written workout from Tana.
7. Rehearse notification suppression, screen-hiding during authentication, account
   switching, and recovery from one failed bounded read.

## Operational recovery, not substitute presentation

1. Retry one bounded read once.
2. Restore the documented clean fixture or safe connector state and continue live.
3. Use the exact payload to restate unclear voice input without changing its meaning.
4. Use screenshots only to locate a control or confirm the expected reset state.
5. If Claude Mobile cannot complete the rehearsed workflow, omit that segment and state
   that the account-level connector flow was validated but the event path did not pass.
6. If write safety cannot be established, do not write; explain which acceptance check
   failed rather than showing a prerecorded replacement.

Never troubleshoot authentication, repository indexing, or connector installation on stage.
