# Conventions for this Foam vault

Working notes for *Clearing and Settling the Realm* (ergodicity economics + entity-shielding applied to Japanese/comparative financial history). These rules govern any note-writing in this repo.

## Markdown formatting (strict)

- **Always leave one blank line after every heading and subheading** (H1–H6) before the body or list that follows. No heading may be immediately followed by a non-blank line.
- Leave one blank line before any list (CommonMark).
- Keep a blank line between frontmatter (`---`) and the first heading.

## Note model

- **Atomic**: one claim per note. If a note argues two things, split it.
- **Frontmatter schema**:
  ```yaml
  ---
  title: <human-readable title, matches filename>
  type: permanent        # permanent | moc | source | reference
  tags: [concept, concept]
  project: HistorEE   # or erc-synergy
  source-session: <slug of originating conversation>
  database: [dataset]    # optional: HistorEE_codebooks dataset(s) this claim draws on
  created: YYYY-MM-DD
  status: seed           # stub | seed | developed
  ---
  ```
- **`database:` links a claim to its evidence.** Optional. Names one or more dataset folders in the sibling `HistorEE_codebooks` repo (e.g. `clearing_records`). The graph exporter renders each as a database node with a directed edge *from the note to the dataset*, making visible which arguments are anchored in data.
- **Tags name concepts only** — what a note is *about*. Provenance goes in `project:` and `source-session:`, navigation goes in MOC hubs. Never tag by project. Controlled vocabulary: `tags.md`.
- **Preserve citation uncertainty**: keep explicit "verify" flags rather than laundering unverified references into confident claims.

## Structure

- `notes/` — atomic notes and concept stubs. `mocs/` — hub notes (`type: moc`). `tags.md` — controlled vocabulary.
- Filenames are readable (spaces allowed); wikilinks resolve by basename.
- Each atomic note links to at least one thematic MOC and one project MOC.

## Voice

Forensic, precise, argument-led. No hedging, throat-clearing, or excessive signposting. Dense and confident.

## Safety

- Do not delete or rename files without explicit confirmation.
- Git commits/pushes are done by the user in VSCode (the sandbox cannot write to `.git`).
