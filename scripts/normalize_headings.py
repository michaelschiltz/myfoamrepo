#!/usr/bin/env python3
"""
Idempotently insert a blank line after every heading (CLAUDE.md convention).
Auto-fix step; safe to run repeatedly. Pure standard library.

Run from the repo root:  python3 scripts/normalize_headings.py
Prints the files it changed (for the pre-commit hook to re-stage).
"""

import os, re, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOBS = ["notes/*.md", "mocs/*.md", "tags.md"]
HEADING = re.compile(r"^#{1,6}\s")

changed = []
for pat in GLOBS:
    for path in glob.glob(os.path.join(ROOT, pat)):
        lines = open(path, encoding="utf-8").read().split("\n")
        out, modified = [], False
        for i, line in enumerate(lines):
            out.append(line)
            if HEADING.match(line) and i + 1 < len(lines) and lines[i + 1].strip() != "":
                out.append("")
                modified = True
        if modified:
            open(path, "w", encoding="utf-8").write("\n".join(out))
            changed.append(os.path.relpath(path, ROOT))

for c in changed:
    print(c)
sys.exit(0)
