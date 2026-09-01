#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "TANA_SYSTEM.template.md",
    "skills/create-tana-system/SKILL.md",
    "skills/discover-tana-system/SKILL.md",
    "skills/retrieve-workout-plan/SKILL.md",
    "skills/log-workout/SKILL.md",
    "examples/build-session/TANA_SYSTEM.md",
    "examples/from-scratch/README.md",
    "fixtures/blank-start-request.md",
    "fixtures/sample-inspection.md",
    "fixtures/sample-workout-report.md",
    "demo/RUNBOOK.md",
]

errors = []
for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        errors.append(f"missing: {relative}")

public_text = "\n".join(
    path.read_text(encoding="utf-8")
    for path in ROOT.rglob("*")
    if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".yaml", ".yml"}
)

for label, pattern in {
    "Tana URI or exported node reference": r"tana:[A-Za-z0-9_-]+",
    "absolute user path": r"/Users/[^/\s]+/",
    "credential-like value": r"(?i)(api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*[^\s<]+",
    "unfinished scaffold": r"\[TODO:",
}.items():
    if re.search(pattern, public_text):
        errors.append(f"public-safety check failed: {label}")

creation_skill = (ROOT / "skills/create-tana-system/SKILL.md").read_text(encoding="utf-8")
for requirement in [
    "Observed`, `Inferred`, `Owner-confirmed`, and `Unresolved",
    "Wait for explicit approval",
    "Direct-read every created or changed",
    "TANA_SYSTEM.md",
    "do not assume automatic repository instruction loading",
    "Guided Discovery — default",
    "Quick Start — explicit option",
    "short, manageable rounds",
    "complete normal workflow",
    "important exceptions",
    "first-version success criteria",
    "owner to confirm or correct that understanding",
    "this is not deep system understanding",
]:
    if requirement not in creation_skill:
        errors.append(f"creation-skill contract missing: {requirement}")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"PASS: {len(REQUIRED)} required files; public-safety patterns clean")
