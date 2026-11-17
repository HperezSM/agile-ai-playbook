#!/usr/bin/env python3
"""Check the playbook's Markdown files. Standard library only.

Checks:
  - every relative link (inline, image or reference-style) points to a file or folder that exists
  - every #anchor points to a heading that exists (GitHub slug rules)
  - no leftover TODO / FIXME / TBD markers
  - templates ship with blank Author / Owner fields

Usage: python3 scripts/check_docs.py [repo_root]
Exit code 0 when clean, 1 when problems are found.
"""

import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", ".github"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
TODO_RE = re.compile(r"\b(TODO|FIXME|TBD)\b")
FILLED_FIELD_RE = re.compile(r"^\*\*(Author|Owner):\*\*[ \t]*(\S.*)$", re.MULTILINE)


def strip_code(text):
    """Return text with fenced blocks blanked out and inline code removed, keeping line numbers."""
    out = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else INLINE_CODE_RE.sub("", line))
    return "\n".join(out)


def slugify(heading):
    text = heading.strip().lower()
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = "".join(ch for ch in text if ch.isalnum() or ch in " -")
    return text.replace(" ", "-")


def anchors(text):
    found = set()
    counts = {}
    for line in strip_code(text).splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = slugify(match.group(2))
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        found.add(slug if n == 0 else f"{slug}-{n}")
    return found


def markdown_files(root):
    for path in sorted(root.rglob("*.md")):
        if not any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            yield path


def check_links(root, path, text, cache):
    problems = []
    rel = path.relative_to(root)
    for lineno, line in enumerate(strip_code(text).splitlines(), 1):
        for target in LINK_RE.findall(line) + REF_DEF_RE.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
                continue  # http:, https:, mailto: and friends
            file_part, _, anchor = target.partition("#")
            dest = (path.parent / file_part).resolve() if file_part else path
            if file_part and not dest.exists():
                problems.append(f"{rel}:{lineno}: broken link to {target}")
                continue
            if anchor and dest.is_file() and dest.suffix == ".md":
                if dest not in cache:
                    cache[dest] = anchors(dest.read_text(encoding="utf-8"))
                if anchor.lower() not in cache[dest]:
                    problems.append(f"{rel}:{lineno}: no heading for #{anchor} in {target or rel}")
    return problems


def check_content(root, path, text):
    problems = []
    rel = path.relative_to(root)
    for lineno, line in enumerate(strip_code(text).splitlines(), 1):
        if TODO_RE.search(line):
            problems.append(f"{rel}:{lineno}: leftover TODO/FIXME/TBD marker")
    if rel.parts[0] == "templates":
        for match in FILLED_FIELD_RE.finditer(text):
            problems.append(f"{rel}: template has a filled-in {match.group(1)} field ({match.group(2).strip()}); leave it blank")
    return problems


def check_repo(root):
    root = Path(root).resolve()
    problems = []
    cache = {}
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        problems += check_links(root, path, text, cache)
        problems += check_content(root, path, text)
    return problems


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    problems = check_repo(root)
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s) found" if problems else "Docs check passed")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
