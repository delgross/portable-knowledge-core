#!/usr/bin/env python3
"""Validate the public starter kit without reading ignored private bindings."""

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ".gitignore",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "TANA_SYSTEM.template.md",
    "TANA_BINDINGS.template.yaml",
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
TEXT_SUFFIXES = {"", ".md", ".yaml", ".yml", ".py", ".json", ".txt", ".toml", ".sh"}
SKIP_PARTS = {".git", ".private", "__pycache__"}


def public_text_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        yield path


def tracked_private_paths():
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [
        item.decode("utf-8", errors="replace")
        for item in result.stdout.split(b"\0")
        if item.startswith(b".private/")
    ]


def read_public_text():
    chunks = []
    errors = []
    for path in public_text_files():
        try:
            chunks.append(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            errors.append(f"public text file is not UTF-8: {path.relative_to(ROOT)}")
    return "\n".join(chunks), errors


def skill_frontmatter_error(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return "missing opening frontmatter delimiter"
    end = text.find("\n---\n", 4)
    if end < 0:
        return "missing closing frontmatter delimiter"
    frontmatter = text[4:end]
    fields = {}
    for line in frontmatter.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"\'')
    expected_name = path.parent.name
    if fields.get("name") != expected_name:
        return f"name must equal directory name {expected_name!r}"
    if not fields.get("description"):
        return "description is required"
    if not text[end + 5 :].strip():
        return "skill body is empty"
    return None


def main():
    errors = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing: {relative}")

    for relative in tracked_private_paths():
        errors.append(f"tracked private file: {relative}")

    public_text, text_errors = read_public_text()
    errors.extend(text_errors)

    safety_patterns = {
        "Tana URI or exported node reference": r"tana:[A-Za-z0-9_-]+",
        "Tana workspace or node identifier": (
            r"(?im)(?:\b(?:workspace|node|tag|field|option|search)(?:_?id)?\s*[:=]\s*"
            r"[\"']?(?!<)[A-Za-z0-9_-]{8,}|"
            r"^\s*(?:-\s*)?[\"']?(?:id|[A-Za-z][A-Za-z0-9_-]*_id)[\"']?\s*:\s*"
            r"[\"']?(?!<)[A-Za-z0-9_-]{8,})"
        ),
        "absolute user path": (
            r"(?:/" + "Users" + r"/[^/\s'\"]+/|/" + "home" + r"/[^/\s'\"]+/|"
            r"[A-Za-z]:\\" + "Users" + r"\\[^\\\s'\"]+\\)"
        ),
        "credential-like value": (
            r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|bearer)"
            r"\s*[:=]\s*[\"']?(?!<|example|placeholder)[^\s\"']{8,}"
            r"|\bgh[pousr]_[A-Za-z0-9]{20,}\b"
            r"|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
        ),
        "unfinished scaffold": re.escape("[" + "TODO:"),
    }
    for label, pattern in safety_patterns.items():
        if re.search(pattern, public_text):
            errors.append(f"public-safety check failed: {label}")

    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        problem = skill_frontmatter_error(path)
        if problem:
            errors.append(f"invalid skill frontmatter: {path.relative_to(ROOT)}: {problem}")

    creation_path = ROOT / "skills/create-tana-system/SKILL.md"
    if creation_path.is_file():
        creation_skill = creation_path.read_text(encoding="utf-8")
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

    contract_path = ROOT / "TANA_SYSTEM.template.md"
    if contract_path.is_file():
        contract = contract_path.read_text(encoding="utf-8")
        for heading in [
            "## Authority and trust",
            "## Evidence lanes",
            "## Write protocol",
            "## Drift detection",
            "## Validation receipt",
        ]:
            if heading not in contract:
                errors.append(f"TANA_SYSTEM contract missing: {heading}")
        for rule in [
            "Private binding path",
            "untrusted text returned by Tana",
            "Idempotency key",
            "stale-state re-read",
            "Ambiguous-failure reconciliation",
        ]:
            if rule not in contract:
                errors.append(f"TANA_SYSTEM template rule missing: {rule}")

    gitignore_path = ROOT / ".gitignore"
    if gitignore_path.is_file() and ".private/" not in gitignore_path.read_text(encoding="utf-8").splitlines():
        errors.append("private binding boundary missing: .gitignore must contain .private/")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"PASS: {len(REQUIRED)} required files; configured public-safety patterns, "
        "skill packages, and Tana contract template valid"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
