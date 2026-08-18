---
title: A migrated institution collects local names not local forms
type: permanent
tags: [commenda, qirad, mudaraba, comparative-concept, coding-ontology, transmission, historiography]
project: HistorEE
source-session: allocation-anchors-blind-coding
database: [loss_mitigation_forms, organizational_forms]
created: 2026-08-18
status: seed
---

# A migrated institution collects local names not local forms

Three times in two days of coding, a census row turned out to be a **word** rather than a form.

- `commenda_alloc` and `qirad_alloc` return identical values in every loss-allocation cell. Harris treats them as one institution under two names; Çizakça writes that "Islamic *mudaraba* was called *commenda* by the Europeans"; Ackerman-Lieberman glosses "the *commenda* (*qirāḍ* or *muḍāraba* in Arabic)" inside one parenthesis. See [[The commenda and the qirad do not separate on loss allocation]].
- `mudaraba` and `qirad` are one institution under two **school** names — *muḍāraba* is Ḥanafī, *qirāḍ* Mālikī, Shāfiʿī and Ḥanbalī (Ramli 2018, 97, on al-Sarakhsī). `mudaraba` is left uncoded on that ground.
- The Ragusan *collegantia* wears a Venetian name for the **bilateral** commenda while being, on Held's own conclusion, a variant of the **unilateral** one. See [[Ragusan collegantia is unilateral and Venetian collegantia is bilateral]].

## The mechanism, and why it is predictable rather than bad luck

An institution that travels is received into a local legal vocabulary that already exists, and the receiving vocabulary supplies a word from its own stock. The word is chosen for the local question that matters — in Dubrovnik, who bears the peril; among the *madhāhib*, which school's usage you are writing in — not to mark a structural difference from the exporter. **The name records the reception, not the institution.**

The corollary is uncomfortable for a comparative census. A type vocabulary assembled by reading across literatures is assembled from *terms*, because terms are what literatures index. It will therefore over-count exactly the institutions that travelled best, and under-count the ones that stayed put and were never renamed. **The census's apparent diversity is partly a map of philology.**

## What to do about it

Not: merge on suspicion. The three cases above were settled by coding, and two of them produced findings that a merge would have destroyed — the Ragusan case relocated a queued split, and the *qirāḍ*/*commenda* identity is only interesting because the cells were filled and came out the same.

Rather: **check every candidate row against the pattern before coding it, not after**, and make the check a stated step. Where the answer is "it is a name", record the determination on the type row with its falsification condition, as `ortoq_alloc` and now `mudaraba` do. Where the answer is "it is a form", the `boundary_basis` column already exists to say on what ground.

And note what the pattern does **not** license. That two traditions used different words is not evidence they had the same institution, any more than the same word is evidence of the same institution — [[Natie is a false cognate]] is the other error and it is equally available. The unit is the clause structure both times: [[Never let the units slide from instruments to populations]].

## Where this is soft

"Identical in every coded cell" is relative to the cells. `commenda_alloc` and `qirad_alloc` are identical on nine loss-allocation characteristics and demonstrably differ elsewhere — the *qirāḍ*'s payout ratio is negotiated and market-responsive where the Genoese one is customary and invariant (van Doosselaere 2009, 68, reading Udovitch 1970, 190–6). A row can be a name on one facet and a form on another, which is the same lesson as [[Unilateral and bilateral commenda collapse on profit and separate on loss]] arriving from the opposite direction.

## Links

- [[The commenda and the qirad do not separate on loss allocation]]
- [[Ragusan collegantia is unilateral and Venetian collegantia is bilateral]]
- [[Unilateral and bilateral commenda collapse on profit and separate on loss]]
- [[Natie is a false cognate]]
- [[Never let the units slide from instruments to populations]]
- [[Borrow the diagnostics not the tree]]
- [[MOC - Historiography and method]]
- [[MOC - Islamic contract doctrine]]
- [[MOC - HistorEE]]

## Source

Coding sessions of 18 August 2026: `LM-0527`–`LM-0563` and `OF-0283`–`OF-0293`. Ramli 2018, 97; Held 2025, 9 and 23; van Doosselaere 2009, 65 n.7 and 68; Çizakça 2014.
