---
title: Glossary and repo conventions
type: reference
created: 2026-07-22
---

# Glossary and repo conventions

Deliberately outside the graph. `scripts/export_graph.py` scans only `notes/*.md`, `mocs/*.md`, and `tags.md`, so a file at the repo root is excluded from the exported graph — and from `scripts/validate_vault.py` — by construction.

To keep it out of Foam's own graph panel in VS Code as well, add `glossary.md` to the `foam.files.exclude` array in `.vscode/settings.json`. Note that the documented Foam setting is `foam.files.ignore`; if the existing exclusions are not taking effect in the panel, that key is the thing to check [verify].

No wikilinks below: plain backticks are used for note and file names so that nothing here can create an edge.

## Abbreviations

**MOC — Map of Content.** A hub note that indexes and organizes other notes rather than making a claim of its own. Lives in `mocs/`, carries `type: moc`, and is named `MOC - <topic>`. Two kinds are in use: *thematic* MOCs, which gather an argument area (`MOC - Islamic contract doctrine`), and *project* MOCs, which gather an output (`MOC - HistorEE`). Per `CLAUDE.md`, every atomic note links to at least one of each.

**HistorEE.** The ERC Synergy Grant project (2027 call) applying ergodicity economics to the comparative institutional history of cooperative risk-pooling arrangements. Used as the `project:` value on notes belonging to it. The alternative value `erc-synergy` marks notes about the *application* itself rather than its substance.

## Frontmatter fields

- `title` — human-readable, matches the filename.
- `type` — `permanent` | `moc` | `source` | `reference`. Enforced by the validator.
- `tags` — concepts only, drawn from the controlled vocabulary in `tags.md`. Never provenance, never project.
- `project` — provenance: which output the note serves.
- `source-session` — slug of the conversation the note came out of.
- `database` — optional; one or more dataset folders in the sibling `HistorEE_codebooks` repo that the claim draws on. The graph exporter turns each into a database node with a directed edge from the note to the dataset.
- `created` — YYYY-MM-DD.
- `status` — `stub` | `seed` | `developed`.

## Directories

- `notes/` — atomic notes, one claim each.
- `mocs/` — hub notes.
- `graph/` — generated output; do not hand-edit.
- `scripts/` — `validate_vault.py` (run by the pre-commit hook and by CI), `export_graph.py`, `new_note.py`, `normalize_headings.py`.
- `_foam-docs/`, `_layouts/`, `assets/` — Foam template scaffolding, excluded from the workspace.

## Conventions worth remembering cold

Notes are atomic: one claim per note, split if a note argues two things. Citation uncertainty is preserved with explicit `[verify]` flags rather than laundered into confident claims. Filenames are readable and may contain spaces; wikilinks resolve by basename, case-insensitively. Git commits and pushes are done by hand in VS Code.
