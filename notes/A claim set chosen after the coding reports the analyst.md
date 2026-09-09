---
title: A claim set chosen after the coding reports the analyst
type: permanent
tags: [verification, historiography, coding-ontology, comparative, meta]
project: HistorEE
source-session: codebooks-housekeeping
database: [organizational_forms, loss_mitigation_forms]
created: 2026-09-09
status: seed
---

# A claim set chosen after the coding reports the analyst

The LaTeX view generator framed every appendix with a sentence promising that *"the comparative
reading is confined to Table 2, whose two characteristics were fixed before the coding."* It printed
that sentence unconditionally. Table 2 is gated on a declared claim set, and exactly one dataset has
one — `loss_mitigation_forms`, with `PR1`/`PY0`. So on any other dataset the appendix **promised a
table it did not print, and asserted a pre-registration that did not exist.** The word "two" was
hard-coded for good measure.

The generator now states the absence instead, and the sentence it states it with is the note: **no
comparative table is printed, because the dataset has no claim set declared in advance, and
characteristics picked out after the coding would report a selection made by the analyst rather than
a reading of the forms.**

## Why the obvious repair is the error

The obvious repair is to declare a claim set for `organizational_forms` now. It is wrong for the
reason the loss census's pair is right: `PR1`/`PY0` carries evidential weight **because it was fixed
before anything was coded**, and choosing a pair today against 833 coded rows selects from a
distribution already seen. The resulting table would be indistinguishable in form from the
legitimate one and would carry none of its licence.

This is the same structure as a morphological matrix with too many characteristics. Discriminating
power is free — [[Count degrees of freedom not cells]] — so a comparison chosen after the values are
known is a report on how hard one looked, and the appendix is where that report gets mistaken for a
finding, because a typeset table in a published appendix is read as a result rather than as a
choice.

**The generator's job is to state the absence, not to fill it.** Whether the dataset acquires a
declared claim set is a decision that has to be made before the next batch and recorded where the
ordering can be checked — [[A prediction is evidence only if its priority is committed]].

## The second-order point, which is cheaper and more general

The false sentence survived because **nobody counted it**. It was a claim about the project's own
evidence, written in prose, in a generator, and never tested against the thing it described — the
same failure as a vocabulary definition that says a column carries two instances when it carries
three. **A sentence about the evidence is itself a claim and has to be counted like one.** That is
a check that costs a line of code wherever the prose is generated, and nothing at all wherever it is
not.

## Links

- [[A prediction is evidence only if its priority is committed]]
- [[A blind re-coding is only blind if the value sets are]]
- [[Count degrees of freedom not cells]]
- [[The morphological matrix is dictated by the shape of the feature space]]
- [[The deficit reading of absence is the scalar ranking in evidentiary form]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Housekeeping pass, 2026-09-08, `scripts/build_views.py` `render_tex`. Measured before the fix: two
table environments in the loss census's `.tex`, one in a generated `organizational_forms` one, the
identical sentence in both. The committed loss view is byte-identical after the patch.
