#!/usr/bin/env python3
"""Validate Pragmatic Engineering Skills packaging with the standard library.

This catches deterministic repository errors. It is not a YAML parser or a
behavioral evaluation of an agent.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
SEMVER = re.compile(
    r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?\Z"
)
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
EXPECTED = {
    "pragmatic-engineering",
    "pragmatic-requirements",
    "pragmatic-feasibility",
    "pragmatic-planning",
    "pragmatic-implementation",
    "pragmatic-testing",
    "pragmatic-debugging",
    "pragmatic-review",
    "pragmatic-commits",
    "pragmatic-collaboration",
    "pragmatic-retrospective",
}


def parse_frontmatter(entry: Path, relative: Path, errors: list[str]) -> tuple[str, str, str]:
    content = entry.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
    if not match:
        errors.append(f"{relative}: missing frontmatter")
        return "", "", content

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator or key not in {"name", "description"} or key in fields:
            errors.append(f"{relative}: invalid or duplicate field {key!r}")
            continue
        fields[key] = value.strip()
    return fields.get("name", ""), fields.get("description", ""), content[match.end():]


def validate_openai_yaml(skill_dir: Path, name: str, root: Path, errors: list[str]) -> None:
    metadata = skill_dir / "agents/openai.yaml"
    relative = metadata.relative_to(root)
    if not metadata.is_file():
        errors.append(f"{skill_dir.relative_to(root)}: missing agents/openai.yaml")
        return
    content = metadata.read_text(encoding="utf-8")
    for field in ("interface:", "display_name:", "short_description:", "default_prompt:"):
        if field not in content:
            errors.append(f"{relative}: missing {field.rstrip(':')}")
    prompt = re.search(r'^\s*default_prompt:\s*"([^"]+)"\s*$', content, re.M)
    if not prompt or f"${name}" not in prompt.group(1):
        errors.append(f"{relative}: default_prompt must mention ${name}")
    short = re.search(r'^\s*short_description:\s*"([^"]+)"\s*$', content, re.M)
    if not short or not 25 <= len(short.group(1)) <= 64:
        errors.append(f"{relative}: short_description must be 25-64 characters")


def validate_manifests(project: Path, errors: list[str]) -> None:
    manifests = [project / "plugin.json", project / ".codex-plugin/plugin.json"]
    parsed = []
    for path in manifests:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            errors.append(f"Missing plugin manifest: {path.relative_to(project)}")
            continue
        except json.JSONDecodeError as error:
            errors.append(f"{path.relative_to(project)}: invalid JSON: {error.msg}")
            continue
        parsed.append((path, data))
        if data.get("name") != "pragmatic-engineering":
            errors.append(f"{path.relative_to(project)}: invalid plugin name")
        if not SEMVER.fullmatch(str(data.get("version", ""))):
            errors.append(f"{path.relative_to(project)}: version is not strict semver")
        if not data.get("description"):
            errors.append(f"{path.relative_to(project)}: missing description")
        if "[TODO:" in path.read_text(encoding="utf-8"):
            errors.append(f"{path.relative_to(project)}: contains a TODO placeholder")
    if len(parsed) == 2 and parsed[0][1].get("version") != parsed[1][1].get("version"):
        errors.append("Plugin manifest versions do not match.")
    codex = project / ".codex-plugin/plugin.json"
    if codex.is_file():
        data = json.loads(codex.read_text(encoding="utf-8"))
        if data.get("skills") != "./skills/":
            errors.append(".codex-plugin/plugin.json: skills must point to ./skills/")
        if not data.get("author", {}).get("name"):
            errors.append(".codex-plugin/plugin.json: missing author.name")
        interface = data.get("interface", {})
        for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
            if not interface.get(field):
                errors.append(f".codex-plugin/plugin.json: missing interface.{field}")


def validate_evals(project: Path, names: set[str], errors: list[str]) -> None:
    path = project / "evals/cases.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as error:
        errors.append(f"evals/cases.json: cannot load: {error}")
        return
    identifiers = set()
    for case in data.get("cases", []):
        identifier = case.get("id", "")
        if not identifier or identifier in identifiers:
            errors.append(f"evals/cases.json: missing or duplicate case id {identifier!r}")
        identifiers.add(identifier)
        unknown = set(case.get("skills", [])) - names
        if unknown:
            errors.append(f"evals/cases.json: {identifier} uses unknown skills {sorted(unknown)}")
        fixture = case.get("fixture")
        if fixture and not (project / "evals" / fixture).exists():
            errors.append(f"evals/cases.json: {identifier} has missing fixture {fixture}")
        if not case.get("prompt") or not case.get("checks") or "must_not" not in case:
            errors.append(f"evals/cases.json: {identifier} has incomplete grader data")


def validate_fixture_hashes(project: Path, errors: list[str]) -> None:
    path = project / "evals/baseline-hashes.json"
    try:
        expected = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as error:
        errors.append(f"evals/baseline-hashes.json: cannot load: {error}")
        return
    for raw, digest in expected.items():
        target = (project / raw).resolve()
        if not target.is_relative_to(project) or not target.is_file():
            errors.append(f"evals/baseline-hashes.json: invalid fixture path {raw}")
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != digest:
            errors.append(f"evals/baseline-hashes.json: fixture drift in {raw}")


def validate(root: Path | str) -> tuple[list[str], int]:
    root = Path(root).resolve()
    project = root.parent
    errors: list[str] = []
    entries = sorted(root.glob("*/SKILL.md"))
    if not entries:
        return ["No skill entrypoints found."], 0

    common = root / "pragmatic-engineering/references/working-agreement.md"
    git_guide = root / "pragmatic-engineering/references/git-practices.md"
    if not common.is_file():
        errors.append("Missing shared working agreement.")
    if not git_guide.is_file():
        errors.append("Missing shared Git practices.")

    names: set[str] = set()
    for entry in entries:
        relative = entry.relative_to(root)
        name, description, body = parse_frontmatter(entry, relative, errors)
        if not NAME.fullmatch(name) or len(name) > 64 or name != entry.parent.name:
            errors.append(f"{relative}: invalid name or folder mismatch")
        if name in names:
            errors.append(f"Duplicate skill name: {name}")
        names.add(name)
        if not description or len(description) > 1024:
            errors.append(f"{relative}: invalid description length")
        if not body.strip():
            errors.append(f"{relative}: empty instructions")
        if CJK.search(entry.read_text(encoding="utf-8")):
            errors.append(f"{relative}: public skill content must be English")
        validate_openai_yaml(entry.parent, name, root, errors)

        if name != "pragmatic-engineering":
            targets = [unquote(urlsplit(link).path) for link in LINK.findall(entry.read_text())]
            if not any((entry.parent / target).resolve() == common for target in targets):
                errors.append(f"{relative}: missing shared agreement link")
            if name == "pragmatic-commits" and not any(
                (entry.parent / target).resolve() == git_guide for target in targets
            ):
                errors.append(f"{relative}: missing Git practices link")

    missing = EXPECTED - names
    extra = names - EXPECTED
    if missing:
        errors.append(f"Missing expected skills: {sorted(missing)}")
    if extra:
        errors.append(f"Unexpected skills: {sorted(extra)}")

    for file in sorted(root.rglob("*.md")):
        if CJK.search(file.read_text(encoding="utf-8")):
            errors.append(f"{file.relative_to(root)}: public skill content must be English")
        for raw in LINK.findall(file.read_text(encoding="utf-8")):
            url = urlsplit(raw.strip().strip("<>"))
            if url.scheme or not url.path:
                continue
            target = (file.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{file.relative_to(root)}: local link escapes suite: {raw}")
            elif not target.exists():
                errors.append(f"{file.relative_to(root)}: broken local link: {raw}")

    validate_manifests(project, errors)
    validate_evals(project, names, errors)
    validate_fixture_hashes(project, errors)

    public_markdown = list(project.glob("*.md"))
    for directory in (project / "docs", project / "research", project / "evals"):
        public_markdown.extend(directory.rglob("*.md"))
    for file in public_markdown:
        if CJK.search(file.read_text(encoding="utf-8")):
            errors.append(f"{file.relative_to(project)}: public documentation must be English")
    return errors, len(entries)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "skills",
    )
    args = parser.parse_args()
    errors, count = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {count} skills and plugin packaging are structurally valid.")
    print("Structural validation only; behavioral and routing claims require evals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
