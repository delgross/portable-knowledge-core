---
name: create-tana-system
description: Design and, only after explicit approval, create the smallest useful Tana system for a person's desired behavior, then generate a client-neutral TANA_SYSTEM.md and focused workflow skills. Use when someone starts with “I want a system for X,” including a blank or partial Tana workspace.
---

# Create Tana System

Turn a desired behavior into an owner-shaped, portable Tana system. Do not clone an
example architecture or write to Tana during discovery and design.

## Workflow

1. **Understand the behavior**
   - Ask what the person wants to capture, retrieve, decide, review, or change.
   - Use their vocabulary and concrete examples, including likely mobile or voice use.
   - Identify the smallest successful end-to-end workflow and current write boundary.

2. **Inspect the starting point read-only**
   - Scope the exact workspace or subsystem.
   - Search for relevant tags, fields, relationships, templates, searches/views, and
     representative nodes.
   - A blank result is valid. Preserve useful existing structure when present.

3. **Separate evidence and meaning**
   - Maintain four lanes: `Observed`, `Inferred`, `Owner-confirmed`, and `Unresolved`.
   - Never treat an example, naming guess, or common Tana pattern as owner intent.
   - Ask only questions whose answers materially change the design or its safe operation.

4. **Design the minimum viable system**
   - Propose only the tags, fields, field types, relationships, hierarchy, templates,
     searches/views, and starter nodes required by the first workflow.
   - Define retrieval behavior, source-of-truth rules, duplicate handling, and write
     boundaries.
   - Prefer additions that can evolve; label optional extensions separately.

5. **Preview and stop**
   - Present one complete review package containing:
     - owner-confirmed purpose and vocabulary;
     - observed starting state;
     - exact proposed architecture and relationships;
     - templates, searches/views, starter nodes, and example records;
     - retrieval and write behavior;
     - proposed `TANA_SYSTEM.md` outline;
     - proposed focused Skills; and
     - unresolved questions and excluded extensions.
   - State the exact Tana workspace and proposed mutations.
   - Wait for explicit approval. Discussion, corrections, or approval of the concept is
     not approval to write.

6. **Create only the approved Tana structure**
   - Re-read the target and reconcile the preview with current state.
   - Apply only the approved mutations through Tana Remote MCP.
   - Reuse matching owner-approved structure; do not duplicate it silently.
   - Stop and re-preview if the target or required design materially changed.

7. **Verify Tana**
   - Direct-read every created or changed tag, field, relationship, template,
     search/view, and starter node.
   - Report partial failures literally. A successful tool call is not readback proof.

8. **Generate the portable GitHub layer**
   - Create `TANA_SYSTEM.md` from the owner-approved design and verified Tana state.
   - Generate one small Skill per approved workflow; do not create one giant operator.
   - Keep `AGENTS.md` and `CLAUDE.md` as short pointers to the shared contract and Skills.
   - Do not include credentials, private identifiers, personal records, or unverified
     claims in publishable files.

9. **Cross-validate**
   - Fresh-read Tana and compare it with the GitHub artifacts.
   - Classify each contract claim as structurally verified, owner-confirmed, or unresolved.
   - Confirm the active client can actually access the repository context and Remote MCP;
     do not assume automatic repository instruction loading.

## Output contract

Before approval, return:

- `desired_behavior`;
- `starting_state`;
- `evidence_lanes`;
- `complete_preview`;
- `proposed_contract_and_skills`;
- `unresolved`; and
- `approval_required`.

After approved implementation, return exact created Tana structures, direct-read
verification, generated repository files, cross-validation differences, and remaining
decisions.
