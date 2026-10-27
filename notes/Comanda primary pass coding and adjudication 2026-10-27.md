---
title: Comanda primary pass coding and adjudication 2026-10-27
type: reference
tags: [commenda, coding-ontology, verification, provenance, capital-lock-in, legal-personality]
project: HistorEE
source-session: comanda-primary-application
database: [organizational_forms, loss_mitigation_forms]
created: 2026-10-27
status: seed
---

# Comanda primary pass coding and adjudication 2026-10-27

**Withhold this note by slug (`comanda-primary-application`; the pass's other sessions are `comanda-primary-operator` and the blind coding chat) from any bundle that codes or recodes `comanda`, `comanda_alloc`, `comanda_ad_societatem`, any other commenda-family row on `LP2`, `TS1`, `CI1`, `CI3`, `LR4` or `FP4`, or `PY0` in the loss census.** It states the values of all 43 comanda cells and the reasons behind the rulings.

This note records a primary pass on the commenda family: the blind coding of 43 cells of `comanda` (`organizational_forms`) and `comanda_alloc` (`loss_mitigation_forms`) from the Latin acts of Madurell Marimón & García Sanz 1973, *Comandas comerciales barcelonesas de la Baja Edad Media*, docs 1–255; its application; the scoring of the operator's withheld predictions; and the adjudication, all on 2026-10-27. The full record is in `HistorEE_codebooks/records/`: the operator's brief and predictions, the coder's committed priors, the coding notes, the act census, the instance tables, the frozen recodings, and `RULINGS-comanda-primary-adjudication-2026-10-27.md`. The logbooks carry the 2026-10-27 entries in 4 and 5; the CHANGELOG block is dated 2026-10-27.

## How it was run

- **Three chats**, on the [[Blind re-coding workflow - operator, coder, application]] pattern: an operator who OCR'd the edition, built the bundle and wrote predictions; a blind coder working on the stripped Latin alone; and this applying session.
- **Commit order is the evidence of the blind.** Predictions `bbf2667`, the coder's priors `9b1a6a8` (anchored in the research ledger at 08:52:48Z), the frozen coding `a73b140`, the pending rows `bdde89f`, the citation registry `47a7d73`, the scored predictions `5011328`. No cell was adjudicated before the predictions were scored.
- **The coder's census.** 230 of 255 documents place capital with a trading party. By the loss rule: 145 `comanda`, 2 `comanda_ad_societatem` (docs 201 of 1419 and 247 of 1473), 83 to neither: 48 abbreviated notules (*Et ad risicum etc.*), 9 custom-only *usum maris* acts of 1314–31, 22 with no loss terms printed, 4 illegible. Values rest on a sample of 45 comanda instances.
- **The applying session's mechanical findings.** The frozen recodings files are CRLF-terminated and the committed blobs LF, so a clone does not reproduce the anchored sha256; the LF hashes are in logbook 4. There were no pending rows to imitate for `adjudicated_by`; `none` came from the schema description and two earlier applications. The works registry lacked the edition (now `VPX7DFWD`).

## Agreement and predictions

- **Coded against live:** 34 of 43 (79.1%); 29 of 38 on the blind-test cells; 5 of 5 on the five cells the assignment rule and the type names fix (`CF2`; `MC1`, `RB1`, `RB2`, `RB4`); 6 of 9 on the cells exposed to vocabulary leaks. **All nine disagreements set a value or `.NA` against a `.NR`, or the reverse; where both values are substantive, 14 of 14 agree.**
- **Coded against the operator's predictions:** 30 of 38 blind cells, against 29 for a predictor that returns the live value. Five of eight misses landed on the operator's named deviation; the three unpredicted moves to a value (`LP2`, `TS1`, `LR4`) are all analyst-imposed. Prediction 8 — that the coder would not connect the fall in clauses after 1300 to the change of record type (cathedral parchments before 1300, notarial registers after 1350) — was confirmed on its criterion, with a near miss: the coder asked, unprompted, whether the abbreviated notules are register drafts. See [[A blind is a property of the channel not of the dataset]].

## The rulings

| cell | live | coded | ruled | ground |
|------|------|-------|-------|--------|
| `LP2` | `.NR` | `0` | **`0`** | the acts call the capital the investor's in 42 of 45; the rest of the family is already `0` |
| `TS1` | `.NR` | `0` | **`.NR`** | default law, and doc 199 (*Risicum dictorum heredum*) can be read as persistence |
| `CI1` | `.NR` | `none` | **`none`** | one investor in 42 of 45; the 2026-10-11 definition codes that `none` |
| `CI3` | `.NR` | `1` | **`P`**, low | the investor's rights are ceded in recorded instruments; the agent's may not pass without consent (Consolat cap. 213) |
| `LR4` | `.NR` | `0` | **`0`** | the 2026-10-12 clarification; `commenda LR4` moved on the same ground |
| `LR5` | `.NR` | `.NA` | **`.NA`** | follows `LR4` |
| `FP4` | `.NR` | `P` | **`.NR`** | notarial constitution is not registration with political authority |
| `VF1` | claimant-oath | `.NR` | **claimant-oath** | the acts' silence does not override the Consolat (cap. 279) |
| `VF2` | mixed | `.NR` | **mixed** | follows `VF1` |

**Fifteen agreeing cells re-based on the acts**, values unchanged: six become articulated on the Latin (`LR2`, `MG1`, `MG4`, `CF3`, `MC1`, `PR1`); `CI5` rises from low to high on the count its note said was missing (23 of 45 commingle in terms, none segregates; see [[Comanda capital was mixed with the agent's own unless the contract said otherwise]]); `MG4` and `RB3` rise to high; `PR1` falls to medium for an insurance premium deducted from profit in doc 250.

## What the matrix learned

- **No new value-instance.** All five changed values already existed in their columns. `CI3 = P` is the census's fifth such cell (beside `asiento_averia`, `kabu_local`, `maona_corsica`, `begijnhof`) and the commenda family's first.
- **The comanda now reads like its family on personhood and pooling.** `LP2 = 0` and `LR4 = 0` had been `.NR` only because the rulings that moved `commenda` and `societas_maris` on 2026-10-12 never reached the Catalan rows.
- **The acts answer the capital questions and are silent on everything outside the contract.** They settle `CI1`, `CI3` and `CI5`, and say nothing on personhood, creditors' reach, death or how a loss is proved. Verification rests on the Consolat alone, which bears on [[The commenda family fixes the allocation of loss and proves it by the agent's oath]]: the oath is normative evidence, never transactional.
- **The row aggregates sub-types.** Voyage comandas are silent on recall; open-trade comandas are recallable at will; comandas placed in an agent's *comune* are locked to the account. `TS3` and `CI2` stay `.NR`, no split. Compare [[Comanda names several contracts in the Catalan sources]].

## Corrected during the session

- **`MB3`** was recommended for re-basing to articulated and withdrawn at application: a notarial recognition shows that a contract exists, not that entering it was chosen.
- **`PY0`**: the coder's proposed applicability rule would break four existing cells, not the three first counted.
- **Martínez Gijón 1966** was first written into logbook 5 as citing the 1973 edition at second hand; it predates it. Only Hancock 2025 does.
- **The standing table** lacked the operator's row, which asked to be filed at application; transcribed verbatim.

## Open

- **No quotation has been checked against a page image**, only against the OCR text. Docs 3, 18, 93, 108, 120, 191 and 207 first, and the multi-act entries the bundle printed without a marker.
- **The coding chat's standing-table row** was never written and was not invented by the applying session.
- **Next acquisitions:** the comanda chapters of the *Costums de la mar* and the *Costums de Tortosa* (`VF1`/`VF2`, `TS1`, `TS3`/`CI2`, `AP3`/`LR1`); Consulate of the Sea litigation; the editors' archival lines, to test whether the abbreviated notules are register drafts.
- **Doc 255**: insurance (operator) or carriage at the carrier's whole risk (coder). No cell rests on it.
- **Vault notes** on the comanda have not been re-read against the new values.

## Where this is soft

- One edition, selected by its editors from what the archives kept; every count describes the printed set.
- `CF2`, `RB1`, `RB4` and `LR6` rest on one risk clause, and the census assigns acts to the row on that clause: one datum, not four. See [[Count degrees of freedom not cells]].
- `CI3 = P` is a ruled third value, rests on cessions in acts the census assigns to neither row, and is low.

## Links

- [[Blind re-coding workflow - operator, coder, application]]
- [[A blind is a property of the channel not of the dataset]]
- [[The Catalan maritime comanda puts the whole capital loss on the investor]]
- [[Comanda capital was mixed with the agent's own unless the contract said otherwise]]
- [[Comanda names several contracts in the Catalan sources]]
- [[The commenda family fixes the allocation of loss and proves it by the agent's oath]]
- [[Genoese notaries drafted the commenda as equity and Catalan notaries as credit]]
- [[Barcelona law kept the commendatary's creditors off the comanda goods]]
- [[The Consolat de Mar comanda chapters]]
- [[Hancock 2025 on trust in Barcelona and Mallorca contracts]]
- [[Polonio on the Barcelona maritime comandas 1349-1450]]
- [[Split provenance into priority and independence]]
- [[Count degrees of freedom not cells]]
- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]

## Source

Application, scoring and adjudication session `comanda-primary-application`, 2026-10-27, `claude-opus-5-5` at effort `high`, on the blind coding of the same day. Source: Madurell Marimón, José María, and Arcadi García Sanz. 1973. *Comandas comerciales barcelonesas de la Baja Edad Media*. Barcelona: Colegio Notarial de Barcelona; CSIC. Zotero `VPX7DFWD`.
