#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "TANA_SYSTEM.template.md",
    "skills/discover-tana-system/SKILL.md",
    "skills/retrieve-workout-plan/SKILL.md",
    "skills/log-workout/SKILL.md",
    "examples/build-session/TANA_SYSTEM.md",
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

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"PASS: {len(REQUIRED)} required files; public-safety patterns clean")
