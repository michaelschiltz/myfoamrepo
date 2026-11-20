---
title: Comanda record eyeball check against the print 2026-11-20
type: reference
tags: [commenda, verification, provenance]
project: HistorEE
source-session: madurell-eyeball-check-2026-11-20
database: [organizational_forms, loss_mitigation_forms]
created: 2026-11-20
status: seed
---

# Comanda record eyeball check against the print 2026-11-20

**Withhold this note by slug (`madurell-eyeball-check-2026-11-20`) from any bundle that codes or recodes `comanda` or `comanda_alloc`, and from any blind reading of the Madurell acts.** It names the acts whose dates and parties the record got wrong.

The first error rate in the project that a referee can cite: the comanda instance record (`HistorEE_codebooks/records/instances-2026-11-03.csv`, 118 instances from Madurell Marimón & García Sanz 1973) measured against the printed edition by a reader blind to it. MS read his own copy of the book; 60 fields were drawn by a seed committed and pushed, with the protocol and the assistant's predictions, before he opened a page. His filled sheet was pushed before anything was scored, and he ruled every disagreement against the print. The record is in `records/PROTOCOL-eyeball-madurell-2026-11-19.md` and `records/RULINGS-eyeball-madurell-2026-11-20.md`; register row ER-0025; logbook 4, 2026-11-20.

## Result

- **5 content errors in 60 fields, 8.3%** (95% interval 3.7–18.1%); 8.7% weighted by how many fields each stratum holds.
- **Dates, 4 of 10.** Three dating clauses cut at a printed line break before the year (docs. 15, 84, 162), one dated act coded `.NR` (doc. 16). An extraction failure, not a misreading: no date element was read wrong.
- **Parties, 1 of 10.** Doc. 193 lists 55 investors and omits the two agents they address.
- **Amounts, destinations, clause quotations and coded absences: 0 of 10 each.** The fields the cells rest on most directly, the risk and obligation clauses and their absence, held in every sampled line.
- **Escalation.** The protocol fixed before the draw sends a stratum with two or more content errors to a full census, so the dating clause of all 118 instances is being read. The record is corrected in one successor after the census.

## The reader is not a reference either

MS's reading erred more often than the record: 11 slips in 60. Four came from the sheet's own questions (the risk vocabulary lacked *redegum*; "who entrusts, who receives" invited the roles of the underlying comanda rather than the parties to a receipt; the obligation question admitted a recital). The rest were act 1 read for act 2, another document's parties, a destination missed, the editor's heading read for the act, and the return promise «Quod implicamentum etc.» taken for a risk clause. The rate stands only because each disagreement was ruled against the page. This is the human counterpart of [[Two blind model transcribers agree where both are wrong - agreement is not a reference]]: a blind reading tests a record only when its disagreements are adjudicated, and a reading sheet's questions are themselves a source of error.

## Where this is soft

- One reader, one sample of 60; ten per stratum bounds a clean stratum only below about 28%.
- The scorer passes a shorter excerpt contained in the reading, so form differences in quotations were not measured.
- MS had reviewed the translation Docs earlier in November; he had not seen the record's fields.

## Open

- Whether «Hec igitur etc.» in doc. 174, act [2], abbreviates the risk clause, which the record codes as absent.
- Whether `amount_as_read` should hold doc. 70's total of comandas carried under a partnership over commissions.
- The Venetian acts get their own check, with the questions tightened.

## Links

- [[Comanda primary pass coding and adjudication 2026-10-27]]
- [[Comanda records corrected from the Madurell translation 2026-11-03]]
- [[The OCR text layer evidences a clause's presence, not its absence]]
- [[Two blind model transcribers agree where both are wrong - agreement is not a reference]]
- [[MOC - HistorEE]]

## Source

Eyeball check, protocol 2026-11-19 and adjudication 2026-11-20, session `madurell-eyeball-check-2026-11-20` (`claude-opus-5-5`); reader MS. Source: Madurell Marimón, José María, and Arcadi García Sanz. 1973. *Comandas comerciales barcelonesas de la Baja Edad Media*. Barcelona: Colegio Notarial de Barcelona; CSIC. Zotero `VPX7DFWD`.
