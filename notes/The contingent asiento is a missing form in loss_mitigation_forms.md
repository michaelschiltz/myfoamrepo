---
title: The contingent asiento is a missing form in loss_mitigation_forms
type: permanent
tags: [contingent-claim, risk-sharing, coding-ontology, determinate-contingent, carrera-de-indias]
project: HistorEE
source-session: borrower-from-hell-ergodicity
created: 2026-08-23
status: seed
database: [loss_mitigation_forms]
---

# The contingent asiento is a missing form in loss_mitigation_forms

The short-term *asiento* written between the Castilian Crown and its bankers between 1566 and 1600 is a loss-mitigation form, and the matrix does not hold it.

It must not be merged with the *asiento de averia*, already coded from the Hierro Anibarro material. That is a convoy-protection contract on the *carrera de Indias*; this is a sovereign credit contract with state-contingent repayment. They share a word and not a mechanism, and a matrix that conflates them will produce a spurious `MC1` value for one of the two. See [[Hierro Anibarro 2005 on the asiento de averia and the privileged company]].

Three properties make it worth a slot in the diversity budget rather than another instance of something already held.

**It allocates by contingency without pricing the contingency.** Repayment moved on the arrival and size of the silver fleet and on the yield of named tax streams, and the clauses carrying those triggers were written at no premium or a negative one (Drelichman and Voth 2014: 221, 224). On `MC1` it should sit close to the sea loan and far from marine insurance, which is a boundary the project has independent reason to test ([[The sea loan is a contingent claim not a loan]]). Whether `PY0` applies at all depends on the `MC1` value the form takes, and settling that is the first task of the coding, not an afterthought.

**Its rationale is articulated in the instrument.** The contingency is a written clause with a named trigger and a named alternative revenue stream, not a mechanism reconstructed by the analyst. The coding is therefore `articulated`, which is rare in this corpus and is precisely the value the maritime forms could not supply.

**Its price is readable.** Table 23 reports the return differential by contingency type across 408 scenarios, separating verifiable triggers from discretionary ones. This is the one form in the corpus for which the cost of a mitigation clause can be recovered from the archive instead of inferred, which makes it the control case wherever the project asserts that a mechanism was or was not priced.

## Acquisition

No new archival work is required for a first coding: chapters 3 and 7 of Drelichman and Voth 2014, together with the *Cliometrica* article, carry the contractual detail. The underlying series is Archivo General de Simancas, Contadurías Generales, legajos 84–92, if verification is wanted later.

## Blind status

The blind is spent for this form. It was read from the secondary literature in the session that produced this note, before any coding was attempted, so it cannot serve as a blind re-coding test. It remains available as a *forward* test of `MC1` and `PY0` on a form neither characteristic was designed against.

## References

Drelichman and Voth 2014: chapters 3 and 7, especially 214–15, 221, 224. See [[Drelichman and Voth 2014 on the debts and defaults of Philip II]].

Drelichman, Mauricio, and Hans-Joachim Voth. 2015. "Risk Sharing with the Monarch: Contingent Debt and Excusable Defaults in the Age of Philip II, 1556–1598." *Cliometrica* 9 (1): 49–75. DOI [10.1007/s11698-014-0108-8](https://doi.org/10.1007/s11698-014-0108-8).

## Links

- [[The sea loan is a contingent claim not a loan]]
- [[Hierro Anibarro 2005 on the asiento de averia and the privileged company]]
- [[The determinate-contingent typology carries the richness]]
- [[A contingency clause priced at zero is evidence for a time-average criterion]]
- [[Drelichman and Voth 2014 on the debts and defaults of Philip II]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - HistorEE]]
