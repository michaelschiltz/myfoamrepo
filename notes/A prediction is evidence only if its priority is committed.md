---
title: A prediction is evidence only if its priority is committed
type: permanent
tags: [verification, provenance, historiography, coding-ontology, meta]
project: HistorEE
source-session: records-directory
database: [organizational_forms]
created: 2026-09-09
status: seed
---

# A prediction is evidence only if its priority is committed

A blind coding batch earns its keep by falsifying something: the operator writes down what the cells
will do, the coder reaches them without seeing that, and the two are compared. The whole design
rests on **the prediction having been written first**, and an audit found that the project could not
show this.

Counted across the tracked record: **one `PRIORS` file against four blind coding batches**, while
the word `falsif` appears **67 times**. Three of the four scored their falsifications from **the
coder's own narrative, written in the same session as the coding** — a document in which the
prediction and the result are separated by paragraphs rather than by evidence.

And the one priors file proved nothing either, because it was untracked. **An mtime is mutable and
carries no commitment**, so a priors file written after the reading is indistinguishable from one
written before it. Keeping the folder ignored on the ground that its contents were evidentially
precious was the worst of both worlds: the preservation burden without the evidential value.

## The claim

**Priority is not a property of a document; it is a property of a record that someone else can
check.** A timestamp is an assertion by the author about the author. A narrative written afterwards
is an assertion about the author's own state of mind at a moment that has passed. Only a commitment
made *to a third party or a tamper-evident log*, before the thing it predicts, converts a prediction
into evidence — which is why the repair is not "write better priors files" but **commit the priors
file before the coding commit it will be scored against.**

This vault makes the same move for arguments and should say so explicitly: `source-session`
frontmatter plus `git blame` is a claim about when a claim was formed, and it is worth exactly as
much as the commit history behind it. A note back-dated in its frontmatter says nothing; a note
whose first commit predates the source it is later confirmed by says something.

## What tracking does not fix

**Tracking today establishes nothing about August.** A commit made now says nothing about what was
written then, so the four archived batches remain assertions, and the finding that stands is the
count: three of four scored themselves from a same-session narrative. The archive is a safe record
of assertions and becomes a chain of commitments only from the first batch that commits its priors
first. **That is a rule about the batch procedure, not about a directory** — which is why moving
files into version control was the smaller half of the repair.

## Links

- [[A blind is a property of the channel not of the dataset]]
- [[A blind re-coding is only blind if the value sets are]]
- [[A claim set chosen after the coding reports the analyst]]
- [[The coding commons must record stated rationale not only component presence]]
- [[Refusals are observations of the filter not inferences from survivors]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Audit behind the creation of `HistorEE_codebooks/records/`, 2026-09-08. The correction was written
back into `logbook/6`, marked, with the count. The batch-procedure change — commit the priors before
the coding — was proposed as a skill revision the same day.
