---
title: A blind is a property of the channel not of the dataset
type: permanent
tags: [verification, provenance, coding-ontology, historiography, tooling]
project: HistorEE
source-session: deed-of-settlement-shielding-recode
database: [organizational_forms]
created: 2026-09-09
status: seed
---

# A blind is a property of the channel not of the dataset

[[A blind re-coding is only blind if the value sets are]] found the leak **inside the vocabulary**:
the `definition` column stated the original codings of the forms under test, so withholding
`data.csv` withheld nothing. The repair was to split the prose into a blinded `exemplar` column and
a `definition` written so that no form's answer could be inferred.

Building a real bundle for the `deed_of_settlement_company` re-coding — rather than a fixture —
found four more leaks, **none of them inside the vocabulary and none addressed by that repair**.

- **A stale `graph.svg` embedding a thousand node and edge titles shipped in every bundle, and it
  was not even in the repository.** The exporter writes `.dot`, `.html` and `.json` and no SVG —
  deliberately, since 2026-08-02: `.gitignore` and the CI workflow both say layout output is
  version-dependent, that nothing consumes it, and that it should be rendered on demand to `/tmp`.
  The file was a **pre-decision leftover** left in the working tree when it was untracked, and
  **`.gitignore` gave no protection, because a bundle copies the working tree and not the git
  tree.** A file can be absent from the repository and present in every bundle.
- **The wikilink dereferencer was line-oriented and this vault hard-wraps.** A link broken across a
  newline was missed, leaving a withheld title standing in a note the coder is told to read.
- **The standing spent-blind table is not a dated section, so nothing scrubbed it.** The built bundle
  contained **the batch's own row**, naming its five cells, both sources and the doctrine under test.
- **The `code-a-form` skill file carries a worked example** reading "as owner shielding did
  throughout 1720–1844" — which is `AP3` of one form and no other, and appears to state a withheld
  value. The channel-check read the coding prompt against the brief and **not the procedure files**.

And one the scrubber could not have caught by pattern, found by hand: `compagnie_antwerpen_1582`'s
`AP2` cell note **stated the withheld form's `AP2` outright**, because a coding note explains itself
by comparison.

## The claim

**The blind's boundary is every artefact the coder is instructed to read** — including the ones
generated *from* the data, the ones that describe the *procedure*, and the ones written in a
neighbouring cell to justify a comparison. Withholding a dataset withholds a file; blinding a
question requires enumerating the channels through which that question has an answer, and the
enumeration is not derivable from the dataset's structure.

Three of the five leaks are of one kind: **a record that is generated is stale the moment it is not
regenerated**, and a stale artefact inside a bundle is indistinguishable from a current one. The
remedy that was adopted is the general one — record mtimes, run every generator, and **delete
whatever the generator did not rewrite**, on the ground that an artefact nothing regenerates cannot
be certified. Note what that remedy does *not* rely on: not the file's tracking status, not
`.gitignore`, and not anyone remembering the file exists.

**CORRECTED 2026-09-09.** The first version of the bullet above called the SVG "committed" and read
the exporter's silence about it as an oversight. Both are wrong: the file is untracked, and not
building it is a documented decision. The mistake made the finding weaker than it is — the leak did
not come through the repository at all.

## The corollary about spending

**Deleting a bundle does not un-spend the blind.** A blind is spent on a *topic* — a form, a set of
cells, a doctrine — by the fact that a session read the material, and no subsequent housekeeping
recovers it. The bundle is a copy; the spend is a fact about who has read what. That is why the
record of it lives in a standing table rather than in the bundle, and why the table's own row was a
leak: the register of spent blinds is itself a description of what is under test.

A second corollary for this vault specifically: **a filename is a claim**, so a note title is
withheld material, and notes are dropped from a bundle by `source-session` slug. A note whose slug
does not match the batch it reports will not be dropped when that batch is blinded.

## Links

- [[A blind re-coding is only blind if the value sets are]]
- [[A prediction is evidence only if its priority is committed]]
- [[The coding commons must record stated rationale not only component presence]]
- [[Count degrees of freedom not cells]]
- [[Refusals are observations of the filter not inferences from survivors]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Operator session for the `deed_of_settlement_company` shielding re-coding, 2026-09-07. Two patches
to `scripts/make_blind_bundle.py`; the second found three of the four defects above by building the
real bundle. The built bundle ran 769 rows and 31 types against 833 and 33 live.
