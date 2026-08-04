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

## Terminology (reserved words)

- **`genetic` is reserved for biological heredity.** Never use it for the descent of institutions. The claim that a recurrence is inheritance rather than arrival is the **origination** claim; a set of forms sharing an ancestor is *connected by descent*. The project engages a literature arguing for biological transmission of economic behaviour, and one ambiguous word concedes ground for free. See [[Never let the units slide from instruments to populations]].
- **`convergence` means convergence in the strict cladistic sense** — independent arrival from *different* ancestral conditions. Where a shared ancestral condition is plausible the word is **parallelism**. See [[Homoplasy is the finding not the noise]] and the note in `tags.md`.
- **Units are instruments, not populations.** Institutions are transmitted as texts and drafting practices. Never describe a legal tradition as a population with a heritable disposition.

## Safety

- Do not delete or rename files without explicit confirmation.
- Git commits/pushes are done by the user in VSCode (the sandbox cannot write to `.git`).

[Never let the units slide from instruments to populations]: <notes/Never let the units slide from instruments to populations.md> "Never let the units slide from instruments to populations"
[Homoplasy is the finding not the noise]: <notes/Homoplasy is the finding not the noise.md> "Homoplasy is the finding not the noise"
