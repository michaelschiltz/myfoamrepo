#!/usr/bin/env python3
"""
Validate the Foam vault against the conventions in CLAUDE.md.

Checks (errors fail the run, exit code 1):
  1. Frontmatter present with required keys, and `type` in the allowed set.
  2. Every heading (H1-H6) is followed by a blank line.
  3. Every [[wikilink]] resolves (case-insensitively) to an existing note/MOC.
  4. Every frontmatter tag appears in the controlled vocabulary (tags.md).

Used by both the pre-commit hook and CI. Pure standard library.
Run from the repo root:  python3 scripts/validate_vault.py
"""

import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTE_GLOBS = ["notes/*.md", "mocs/*.md"]
ALL_GLOBS = NOTE_GLOBS + ["tags.md"]

WIKILINK = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
REFDEF = re.compile(r"^\[[^\]]+\]:\s")
HEADING = re.compile(r"^#{1,6}\s")
ALLOWED_TYPES = {"permanent", "moc", "source", "reference"}
REQUIRED_KEYS = ("title", "type", "tags")

errors, warnings = [], []


def frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[3:end].strip(), text[end + 4:]


def parse_tags(fm):
    m = re.search(r"^tags:\s*\[(.*?)\]", fm, re.M)
    if not m:
        return []
    return [t.strip() for t in m.group(1).split(",") if t.strip()]


def controlled_vocab():
    path = os.path.join(ROOT, "tags.md")
    if not os.path.exists(path):
        return None
    return set(re.findall(r"`([^`]+)`", open(path, encoding="utf-8").read()))


# collect existing basenames (case-insensitive)
basenames = {}
for pat in ALL_GLOBS:
    for f in glob.glob(os.path.join(ROOT, pat)):
        b = os.path.splitext(os.path.basename(f))[0]
        basenames[b.lower()] = b

vocab = controlled_vocab()

for pat in NOTE_GLOBS:
    for path in sorted(glob.glob(os.path.join(ROOT, pat))):
        rel = os.path.relpath(path, ROOT)
        text = open(path, encoding="utf-8").read()
        fm, body = frontmatter(text)

        # 1. frontmatter
        if fm is None:
            errors.append(f"{rel}: missing YAML frontmatter")
        else:
            for key in REQUIRED_KEYS:
                if not re.search(rf"^{key}:", fm, re.M):
                    errors.append(f"{rel}: frontmatter missing `{key}`")
            mt = re.search(r"^type:\s*(\w+)", fm, re.M)
            if mt and mt.group(1) not in ALLOWED_TYPES:
                errors.append(f"{rel}: type `{mt.group(1)}` not in {sorted(ALLOWED_TYPES)}")
            # 4. tags in controlled vocab
            if vocab is not None:
                for t in parse_tags(fm):
                    if t not in vocab:
                        errors.append(f"{rel}: tag `{t}` not in tags.md controlled vocabulary")

        # 2. heading blank lines
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if HEADING.match(line) and i + 1 < len(lines) and lines[i + 1].strip() != "":
                errors.append(f"{rel}:{i+1}: heading not followed by a blank line")

        # 3. wikilink resolution
        for line in text.split("\n"):
            if REFDEF.match(line):
                continue
            for m in WIKILINK.finditer(line):
                tgt = m.group(1).strip()
                if tgt.lower() not in basenames:
                    errors.append(f"{rel}: unresolved wikilink [[{tgt}]]")

# report
for w in warnings:
    print(f"WARN  {w}")
if errors:
    print(f"\n✗ {len(errors)} error(s):")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
print(f"✓ vault valid — {len(basenames)} notes, all wikilinks resolve, headings & schema OK")
