---
title: Comanda records corrected from the Madurell translation 2026-11-03
type: reference
tags: [commenda, verification, provenance]
project: HistorEE
source-session: madurell-translation-test
database: [organizational_forms, loss_mitigation_forms]
created: 2026-11-03
status: seed
---

# Comanda records corrected from the Madurell translation 2026-11-03

**Withhold this note by slug (`madurell-translation-test`) from any bundle that codes or recodes `comanda` or `comanda_alloc`.** It states how the comanda sample was reassigned and what the corrected counts are.

The Latin and Catalan acts of Madurell Marimón & García Sanz 1973 (docs 1-255) and the Glosario were transcribed from the page images and translated in 24 chunks (Drive, `translations/Madurell-GarciaSanz-1973/`, L01-L24). Every correction they found is applied to successor records in `HistorEE_codebooks`: `records/act-census-2026-11-03.csv`, `instances-2026-11-03.csv` and `instance-chars-2026-11-03.csv`. The ledger is `records/CORRECTIONS-madurell-translation-2026-11-03.{md,csv}` (1,103 changes) and the rulings are in `records/RULINGS-madurell-translation-2026-11-03.md`. The 2026-10-27 records are untouched.

## What kind of witness

- **Independent on appearance.** 56 amounts were wrong or truncated (doc 204 read 1 lb for 851 lb), and head date lines, declarants and destinations were left empty. On these the page image is the authority and the coding was not. **[Corrected 2026-11-03:** this was first blamed on the text layer. The coder's own source text holds the full amount in 54 of the 56 cases; the coding pass's field extraction lost them. See [[The OCR text layer evidences a clause's presence, not its absence]].**]**
- **Not independent on assignment.** The form changes come from rulings, not from new evidence about any one act. A loss term that is abbreviated, implied by a salvage clause or incorporated by "simile" is read on the notary's own written-out clause. 27 of the 71 sample instances rest on such a reading, and every one is labelled in `loss_rule` so it can be switched off.

## What it found

- **The abbreviation is the notary's pen, not the contract.** In every notary's series with written-out clauses, those clauses name the investor. Jaume Just writes both forms in one entry (doc 129). Doc 179 survives abbreviated (fol. 19) and in full (fol. 52), and the full text names the investor. Census `comanda` goes from 145 to 202, `neither` from 108 to 51, and the mod3 sample from 45 to 71.
- **Errands are not comandas** (D105, D-ERRAND): docs 104, 105, 152 and 207 carry, sell or buy for the principal with no profit allocation, and are `neither` even where the risk clause names him.
- **Misreadings, not OCR:**
  - doc 226 has the roles reversed;
  - doc 191 has no sea;
  - doc 122 has no surety;
  - doc 193 has 55 investors, and "minor diebus" means the younger;
  - doc 255 dates to the editors' second half of the 14th century.
- **One quoted statistic is false:** OF-0853's "all one quarter". Docs 189 (⅛) and 240 (⅓) enter the sample. No cell value moves.
- **The 2026-10-27 sensitivity figure** of 202 `comanda` acts matches the new total by coincidence: the custom-only acts are not in it.

## What changed in the repository

Records only, plus logbooks 2, 4 and 5 and the CHANGELOG of 2026-11-03. No `data.csv` cell. A recount of the statistics quoted in 18 cells waits on MS in `proposed-of/RECOUNT-comanda-madurell-2026-11-03.md`, as note additions only.

## Open

- ~~**The recount tranche** (eight items), for MS.~~ **Ruled and applied 2026-11-05**: 21 cell notes amended, seven OCR quotations corrected, no value moved (`records/RULINGS-madurell-recount-2026-11-05.md`).
- **Pere de Torre's "ad quartum lucri et usum maris"** (docs 75-85): custom, not abbreviation. It stays `neither` as an open theory call.
- **Acts [2]-[n] of entries 81, 97, 99 and 102** (36 acts) are not instanced. 29 of them would enter the sample by D-ABBR.
- **Clauses the census does not record:** cancellations, licences, insurance costs (224, 250, 251), commissions (214, 238), price ceilings.
- **D1 of 2026-11-01** (the abbreviated acts stay `neither`) is superseded by D-ABBR and D-BELL.

## Related

- [[The OCR text layer evidences a clause's presence, not its absence]]
- [[Comanda coding collated with the editors' study 2026-11-01]]
- [[Comanda primary pass coding and adjudication 2026-10-27]]
- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]

## Source

Session `madurell-translation-test`, 2026-11-03, `claude-opus-5-5`. Source: Madurell Marimón, José María, and Arcadi García Sanz. 1973. *Comandas comerciales barcelonesas de la Baja Edad Media*. Barcelona: Colegio Notarial de Barcelona. Zotero `VPX7DFWD`.
