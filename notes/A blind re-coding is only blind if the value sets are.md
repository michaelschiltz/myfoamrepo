---
title: A blind re-coding is only blind if the value sets are
type: permanent
tags: [coding-ontology, verification, provenance, historiography]
project: HistorEE
source-session: maritime-blind-recoding
database: [loss_mitigation_forms]
created: 2026-08-16
status: seed
---

# A blind re-coding is only blind if the value sets are

A test-retest design withholds the original codings and supplies the instrument. The design assumes
those are separable. In a matrix documented in prose they are not, because the place a project
records *why* a characteristic exists is the same place it records *what the founding forms
answered*.

The maritime re-coding withheld `data.csv`, the generated codebook, the views, the logbook and the
changelog, and supplied `vocabularies/` on the ground that a coder cannot work without the value
sets. The `definition` column of the characteristic vocabulary then stated the original codings of
all three forms under test, for four of the seven decisions under test:

- the security characteristic opened *THE CELL THAT SEPARATES BOTTOMRY FROM RESPONDENTIA: bottomry
  is secured on the ship, respondentia on the goods*
- the market-risk characteristic: *in the sea loan the borrower keeps this while the lender takes
  the peril risk*
- the discharge characteristic: *the sea loan's defining feature*
- the pricing characteristic: *the sea loan prices crudely and sits between*

The type vocabulary compounded it — the forms are **named** "Bottomry (sea loan secured on the
ship)" and "Respondentia (sea loan secured on the goods)" — and the pre-registration entry, which the
coder must read to know what is being tested, restated the same answers in its origin column.

## What the failure revealed

The result is the diagnostic. Every failure condition was phrased as *would a fresh coder reach for
this?*, and on the contaminated characteristics that question became unaskable. Those
characteristics returned **agreement**. The two decisions the leak did not touch returned
**failures** — and the pre-registration had named them as the ones the test was weak on, adding that
if either failed it would be the more important result.

So the contaminated arm produced exactly what an unblinded re-read always produces, and the clean arm
produced the findings. The design was right about its own value and wrong about whether it had
achieved it.

## The repair, and it is cheap

Split the vocabulary's prose into two columns:

- **`definition`** — what the characteristic asks. Written so that no form's answer can be inferred.
- **`exemplar`** — which forms answered what, and why the characteristic was added. Everything now
  doing the work of institutional memory.

Blind the coder to `exemplar`. The rationale survives, the memory survives, and the instrument
becomes testable. Without the split no re-coding test can be run on this matrix at all, which is a
sharper cost than it first appears: a project that cannot re-test its own instrument has no way to
distinguish a coding error from a limit of the matrix, and those are the two things a re-coding test
exists to separate.

## The second lesson, from a withdrawn recommendation

On the first pass the test recommended reversing a widening of the security characteristic, on the
ground that two of its values had zero occurrences two days after being added. Fresh acquisition
then put personal suretyship at 24% of the relevant documents — the commonest specific security
device in the corpus. The recommendation had read an **absence of acquisition** as an **absence in
the world**, which is the precise confusion the blinding exists to catch. It caught it, one pass
late, and only because the acquisition was widened rather than the reasoning sharpened.

Add forms, not features; and before concluding from a zero, ask what has been read.

## Links

- [[Count degrees of freedom not cells]]
- [[The coding commons must record stated rationale not only component presence]]
- [[Refusals are observations of the filter not inferences from survivors]]
- [[The deficit reading of absence is the scalar ranking in evidentiary form]]
- [[Split provenance into priority and independence]]
- [[The notarial security clause is boilerplate and cannot carry a typology]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Maritime blind re-coding, pre-registered in `HistorEE_codebooks/logbook/4` §2026-08-13 (iv), run
2026-08-16. Contamination identified before any cell was coded; the full report is in the project
docs.
