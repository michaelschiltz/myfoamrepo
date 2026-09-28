---
title: Blind re-coding workflow - operator, coder, application
type: reference
tags: [verification, provenance, coding-ontology, tooling]
project: HistorEE
source-session: opus55-recode-mutual-pole-application
database: [organizational_forms]
created: 2026-09-27
status: seed
---

# Blind re-coding workflow - operator, coder, application

**What a re-code pass tests.** It tests the coder, not the evidence. A second model re-codes existing cells from the same sources, blind to the live values, and the two readings are compared. The rows go to `recodings.csv`, one per cell per pass. `data.csv` changes only when MS adjudicates `replaced`, and its `coder_model`/`coder_effort` change with it. Re-coding and acquiring new sources are kept in separate passes, because a disagreement produced by both at once cannot be attributed to the model or to the evidence. This note records the procedure as run on 2026-09-26 (pass `opus55-recode-mutual-pole-2026-09-26`: Opus 5.5 at `high` re-coding the two forms of the 2026-09-04 mutual-pole batch), together with the repairs that pass showed were needed. It states no cell value on purpose, so that it can travel into later bundles.

## The sequence

The work runs in **three chats that must never be merged**. Git belongs to MS throughout.

**0. Plan (MS).**

- Draw the sample only from cells whose cited sources are held as PDFs, so the re-coder reads the same pages the original coder read.
- Exclude the `[verify]`-only rows.
- Fix the pass slug.

**1. Operator, Chat A.** It spends the blind and never codes.

- Draft its own standing-table row in logbook 4 *before* reconnaissance; reconcile it after.
- Write the live baseline (all cells: value, confidence, articulation) and a **withheld-predictions** section into `records/NOTES-<pass>.md`. This file is for the maintainer only.
- Decide the withholding explicitly:
  - the types under test;
  - **sibling rows in the other census coded from the same pages**;
  - vault sessions, chosen by slug and count, never by title;
  - logbook dates.
- Build the bundle with `make_blind_bundle.py` in the device VM's scratch space. Redact by hand whatever the manifest's residual-mentions list flags, re-scan to zero, then copy the bundle to `~/GitHub/`.
- **`records/` is copied into bundles, so delete from the bundle every records file carrying the original values.**
- Record both next free ids (`record_id`, `recoding_id`).
- Write an empty priors template and the coder's kickoff prompt.
- Read the prompt *and the loaded skills* back against the withheld predictions. Delete or disclose every overlap.
- Stop.

**2. The hinge (MS).**

- Open Chat B fresh, with only the bundle folder granted, and (proposed) outside the claude.ai Project.
- When B reports that its priors are written, **copy the bundle's filled `records/PRIORS-…md` over the live template and commit it**. Only then does B open a source.
- Before that release, check that the committed blob is the filled file, not the template: B prints the file's sha256, and the commit must hold that hash. (Proposed after 2026-09-26; not yet tried.)

**3. Coder, Chat B.** It works inside the bundle only.

- Fill the priors, including an **exposure section** listing every leak already read, *before* any source.
- Read every source in full and cite printed folios.
- Write rows in the `recodings.csv` schema, leaving `value_at_recoding` and `agreement` empty.
- Give the six answers of `run-a-coding-batch`.
- **Freeze**: write everything to `proposed-of/` and print sha256 hashes before computing anything about the rest of the matrix. Anything computed afterwards goes in a separate post-freeze file that changes no cell.
- No `git`, not even `git status`. No source-finding tool.

**4. Grant (MS).**

- Record the frozen hashes.
- Lift the `data.csv` prohibition *for reading only*.
- Grant the live tree and the bundle to a fresh Chat C.

**5. Application, Chat C.** It neither codes nor adjudicates.

- Verify the frozen hashes, and verify the destination (next section).
- Join each proposed row to the live `(record_id, type_id, char_id)`.
- Fill `value_at_recoding` (the live value, verbatim) and `agreement` (value equality, as `datapackage.json` defines it). Nothing else changes.
- Append after a round-trip `cmp`, and assert that the old file is a byte prefix of the new one.
- Copy the record into `records/`, checking for collisions first and never overwriting.
- Report agreement, write the adjudication worksheet, then the logbooks, the CHANGELOG and the commit message, then run the full check suite.

**6. Adjudication (MS).** Rule on each worksheet entry: re-code right, live stands, definitional, or split. Only a `replaced` ruling touches `data.csv`.

## Verifying the destination without trusting it

The bundle is a scrubbed copy, so it *should* differ from the live tree. Every difference must be classified mechanically. None may be waved through.

- **CSV cells.** Split the bundle's text on its `[withheld …]` markers. The remaining pieces must appear in order in the live text, so that the only gaps are what the markers replaced. Rows of withheld types must be absent. Whole columns may be dropped by design (`exemplar`, unless `--keep-exemplar` was passed).
- **Logbooks.** Every changed line is either a `[withheld …]` marker or a deleted section, standing-table row or table row that names the withheld material.
- **Views.** Run `build_views.py … --mechanism all --check` in a scratch copy of the bundle and in the live tree. If both print `current`, the difference is the data's alone.
- **Expect more than the prompt lists.** On 2026-09-26 the bundle also differed in the *other* census's `data.csv` (the withheld siblings), in a characteristic vocabulary's dropped `exemplar` column, and in two *unmarked* deletions of withheld-form references. All of it was scrub. The next apply prompt should list it, or point Chat C at the bundle's `.redactions.log`.
- **Read Git without running it.** `.git/objects/xx/…` loose objects are zlib-compressed. Decompress the commit, then its tree, then the blob. That establishes what a commit actually holds.

## Scoring, before any adjudication

- **Keep four classes apart:**
  - *exact*: same value and confidence;
  - *confidence-only*: same value, different confidence;
  - *substantive*: two coded values;
  - *missingness*: a value against `.NR`/`.NA`, or `.NR` against `.NA`.
- **Report articulation separately.** Count the direction of the confidence and articulation differences over all cells, never over a sample.
- **For each disagreement:** give both source sets (same works, different works, or a mixture of passages), and check whether its parent disagrees too (`AP3`/`LR1`/`CF2` on `CF1`, `LR5` on `LR4`, `LR6` on `LR2`, `MG3` on `MG1`).
- **Score both sets of predictions:** the coder's own, and **the operator's withheld predictions in the brief**. The 2026-09-26 application scored only the first, because its prompt did not ask for the second. The skill requires both.
- **Say in every write-up that both coders are Claude models.** Agreement between two models of one family is weak evidence of reliability. Disagreement, and a uniform direction in the confidence differences, is the informative result.
- **Never tabulate "nearest neighbours" by raw agreement across all characteristics.** That is an unweighted similarity computation, which `CLAUDE.md` forbids for comparative claims. A post-freeze file did it on 2026-09-26, and the result is flagged in logbook 4 as not citable.

## What the 2026-09-26 pass got wrong, and the proposed repair

- **The priors commit held the empty template.** The live template was committed, and the filled priors existed only in the bundle, so the ordering of priors before sources rests on the coder's narrative. Repair: the hash check at step 2. Chat C also verifies the priors blob in `HEAD`'s tree before trusting any "ordering held" claim. See [[A prediction is evidence only if its priority is committed]].
- **The application licence was too narrow for house practice.** It allowed "new entries at the top" of logbook 4, so Chat C could not file its own standing-table row. Grant that row explicitly next time.
- **The coding chat saw the Project's document titles.** It was attached to the claude.ai Project, which is a channel the bundle cannot scrub. The coder disclosed this and left the call to MS; the proposal is to open Chat B outside the Project.
- **The comparability gap biases toward disagreement.** The original coder had the whole Zotero collection, the sibling rows and the scope decision; the re-coder had five PDFs and a fixed scope. State this beside every agreement figure.

## Tooling facts that cost time

- **`frictionless`.** It is not installed in the device VM. Run `pip install --user frictionless`, then call it as `python3 -m frictionless`.
- **`check_dependence.py`.** It needs the dataset **directory**. It reads `data.csv` only, so it says nothing about `recodings.csv`.
- **`build_codebook.py`.** It counts `resources[0]` only, so appending to `recodings.csv` leaves the codebooks `current`. Regenerating them is neither needed nor licensed.
- **Writing CSV.** Use `csv.writer(lineterminator='\n')`. Round-trip the file and `cmp` it before any write.
- **The PRIORS path.** A filled priors file cannot land on the committed template's path without overwriting it. At application it goes in under a suffix (`-filled-`), and the gap is disclosed.

## Where the 2026-09-26 record lives

- **Codebooks:**
  - `records/NOTES-opus55-recode-mutual-pole-2026-09-26.md` is the operator's brief.
  - `records/PROMPT-…-2026-09-26.txt` and `records/PROMPT-…-apply-2026-09-26.txt` are the two kickoff prompts.
  - `records/PRIORS-…-filled-2026-09-26.md`, the coding and post-freeze notes and `PROPOSED-RECODINGS-…csv` are the coder's record.
  - Logbook 4 2026-09-26 (ii) and logbook 5 2026-09-26 carry the logbook entries; the CHANGELOG entry is `organizational_forms — 2026-09-26 (ii)`.
  - The adjudication worksheet is in `proposed-of/` and is open work.
- **Project docs:** `claude/recode-plan-2026-09-26.md`, `claude/recode-mutual-pole-operator-prompt-2026-09-26.md`, `claude/opus55-recode-mutual-pole-operator-2026-09-26.md` and `claude/opus55-recode-mutual-pole-applied-2026-09-26.md`.
- **Result, as counts only:** 64 cells, 53 agree and 11 disagree, all `pending`.

## Links

- [[A blind is a property of the channel not of the dataset]]
- [[A blind re-coding is only blind if the value sets are]]
- [[A prediction is evidence only if its priority is committed]]
- [[Split provenance into priority and independence]]
- [[Count degrees of freedom not cells]]
- [[Primary against secondary coding workflow - three arms, reveal, application]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]
