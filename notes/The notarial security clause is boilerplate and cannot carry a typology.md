---
title: The notarial security clause is boilerplate and cannot carry a typology
type: permanent
tags: [coding-ontology, sea-loan, verification, provenance]
project: HistorEE
source-session: maritime-blind-recoding
database: [loss_mitigation_forms]
created: 2026-08-16
status: seed
---

# The notarial security clause is boilerplate and cannot carry a typology

A classification that keys on the object of security assumes the object was recorded. In the largest
transactional corpus available for the medieval Mediterranean sea loan, it usually was not — and
where it was, the scribe abbreviated it away.

Zeno's Palermo register, 1286–1350, from the Archivio di Stato and the Archivio Comunale: 189
documents, of which **91 carry a loan or *risicum* clause**. Counted by clause:

| device | documents | share |
|---|---|---|
| personal surety (*fideiussor et principalis pagator*) | 22 | 24% |
| general hypothec (*sub ypotheca*) | 33 | 36% |
| any specific pledge of a named object | ~10 | 11% |
| — ship or galley (± *corredorum et guarnimentorum*) | 4 | 4% |
| — goods (wheat, cheese) | 3 | 3% |
| — freight (*totum naulum quod debet*) | 1 | 1% |
| no security clause at all beyond the risk clause | ~44 | 48% |

**The ship-or-goods choice is made in seven documents out of ninety-one**, no document makes both,
and personal suretyship is three times commoner than any specific pledge. Nearly half the loan
documents say nothing about security whatever.

And the general hypothec is not a description of anything. **Fifty-eight per cent of the *ypotheca*
clauses are abbreviated by the notary to *sub ypotheca etc.***; where written out they read *ypotheca
bonorum suorum*, a charge on the whole estate. The scribe treated the clause as formulary he need not
copy.

## The generalisation

Hoover found the same for Genoa a century earlier and stated it as a contrast with the modern bond:

> There were no such limitations as to the security or the use of the proceeds of a Genoese sea loan
> of the twelfth and thirteenth centuries. The Genoese sea-loan contracts furnish examples of the
> pledge of real property, of ships, of various numbers of shares in ships, and of a general
> hypothecation of all the borrower's goods. In many other cases, in addition to other pledges,
> personal friends or acquaintances of the borrower acted as his sureties.

Three objects recur across corpora and traditions — **ship, freight, cargo**. Zeno's editorial
summary names the security regime as *ipoteca e pegno sulla nave e sul nolo*; Schuster's differentia
runs *Verpfändung … von Schiff, Fracht oder Ladung*. Freight is the third term and it is invisible to
any scheme built on a ship/cargo dichotomy.

## The coding consequence

A characteristic is measuring what the sources record, not what obtained. Where the sources are
formulary, a coded value reports the formulary. The right value for the object of security on a
generic medieval sea loan is `.NR` rather than a choice between two states, and a characteristic
whose modal answer is "the notary wrote *etc.*" is carrying drafting convention into a comparative
matrix.

Two questions are bundled here and they have very different variance: **is there a specific pledge at
all**, and **of what**. In this corpus the first splits 11/89 and the second splits four ways across
ten documents. Bundled, the second question's noise swamps the first question's signal. This is the
well-formedness test — see [[Count degrees of freedom not cells]] — applied to a characteristic
rather than to a pair.

## Method note

Counts are from OCR of the 1936 scan (`tesseract ita+lat`), documents split on roman-numeral
headings, every pledge hit audited by hand. Removed on audit: renunciation clauses caught by a
pledge pattern, and one apparent ship-and-goods pledge that was the phrase "loaded in the ship"
inside a goods pledge. Sound to within a document or two, not to the unit.

## Links

- [[Count degrees of freedom not cells]]
- [[The coding commons must record stated rationale not only component presence]]
- [[Bottomry and respondentia are one institution named twice in English]]
- [[Bottomry separates from the sea loan on recourse not on collateral]]
- [[The deficit reading of absence is the scalar ranking in evidentiary form]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Zeno (1936), 189 documents, counted 2026-08-16. Hoover, QJE 40 (1926) 527–528. Schuster (2005)
211–212.
