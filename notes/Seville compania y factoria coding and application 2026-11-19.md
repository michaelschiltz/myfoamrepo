---
title: Seville compania y factoria coding and application 2026-11-19
type: reference
tags: [commenda, principal-agent, coding-ontology, provenance]
project: HistorEE
source-session: compania-sevilla-operator-2026-11-19
database: [organizational_forms]
created: 2026-11-19
status: seed
---

# Seville compania y factoria coding and application 2026-11-19

**Withhold this note by slug (`compania-sevilla-operator-2026-11-19`; the coding chat is `compania-sevilla-coding-2026-11-19`) from any bundle that codes or recodes `compania_factoria_sevilla`, codes a further Seville or Carrera de Indias partnership deed, or codes `CF2` or `LR6` on any commenda-family row.** It states all 33 values of the row and MS's reading of the loss clause of doc. 8.

This note records the first coding of a new `organizational_forms` row, `compania_factoria_sevilla`: a partnership made before a Seville notary for the Indies trade, in which one or more partners supply the capital and another partner travels to the Indies, resides there and manages sale and reinvestment for a share of profit. The source is the Apéndice documental of Martínez Gijón 1970, *Anuario de Historia del Derecho Español* 40, pp. 43–84: ten deeds of the Archivo de Protocolos de Sevilla, Oficio XV, 1516–1550 (Zotero `K36HMDA9`; see [[Martinez Gijon on the comenda in Spanish law]] and [[Archivo Historico Provincial de Sevilla - notarial protocols]]). The full record is in `HistorEE_codebooks/records/*compania-sevilla*-2026-11-19*`; the logbooks carry 2026-11-19 entries in 2, 3, 4 and 5; the CHANGELOG block is `organizational_forms — 2026-11-19`.

## How it was run

- **Operator, blind coder, application**, on the [[Blind re-coding workflow - operator, coder, application]] pattern, with the operator chat also applying. The operator read all ten deeds against the page images, wrote a reading kit and a full translation of doc. 8 (Google Doc "D08 — Martínez Gijón 1970, doc. 8"), put the reading of doc. 8's loss clause to MS (R1), and wrote withheld predictions. The coder worked in `_blind-compania-sevilla-2026-11-19` on the edition alone and read all 41 page images against the text layer.
- **Commit order is the evidence of the blind.** The coder's priors and the operator's predictions went in with `5d1c4f5`, anchored in the research ledger at 2026-11-19T06:01:56Z (`entries/2026/20261119T060156Z-historee_codebooks-5d1c4f59dca1.txt`). The coder confirmed the commit at 15:03 JST before opening the source, and froze its rows before the live tree was granted. The batch was then committed as one commit, `4744283`, under the subject of its script fix; the CHANGELOG records this under Fixed.
- **A leak the operator missed and the coder found.** `CONTRIBUTING.md` §3 already said the edition prints ten Seville deeds of 1516–1550. Recorded in the operator brief, §8.
- **An ordering disclosure.** A format check printed census counts for six characteristics after the coder had fixed every value and before it wrote the rows. Accepted as disclosed (ruling 6).

## The deeds

| doc | year | notary | assignment | why |
|-----|------|--------|------------|-----|
| 3 | 1542 | Alonso de Cazalla | in | factor and partner; 3,000 ducados against his 80; profit ¾–¼ |
| 8 | 1550 | Alonso de Cazalla | in | three capital partners; the factor puts in nothing but his labour; profit ¾–¼ |
| 9 | 1542 | Alonso de Cazalla | in | two brothers; the factor puts in nothing but his labour; profit ¾–¼ |
| 2 | 1516 | Bernal González Vallecillo | out (ruling 1) | equal capital, 158,168 maravedís each, and one partner travels |
| 10 | 1549 | Alonso de Cazalla | corroboration | a power by the principals of doc. 8 to recover an earlier factor-partner's estate; it recites such a company |
| 4, 5 | 1524, 1518 | Vallecillo | out | commission agency, 5 % and 6 % |
| 6, 7 | 1516, 1519 | Vallecillo | out | salaried factors; doc. 7's rubric «COMPAÑÍA» is the editor's and the clauses do not bear it out |
| 1 | 1538 | Cazalla | out | power of attorney |

## The values

Seventeen substantive cells, thirteen `.NR`, three `.NA` (`AP4`, `LR5`, `MG3`). No new value-instance in any column: a new case, not a new state.

| cell | value | confidence | ground |
|------|-------|------------|--------|
| `LP2` | 0 | low | title registered in the partners' names, «por tercias partes» |
| `TS1` | P | low | doc. 8 provides for both deaths, with opposite outcomes |
| `TS2` | fixed-term | high | four or six years, extendable |
| `TS3` | P | medium | the capital partners may recall the factor at will; he may not leave |
| `CI1` | common | high | the contributions are merged in one stock |
| `CI2` | P | low | locked against the factor and heirs, open at the capital side's will; the same clauses as `TS3` |
| `CI5` | segregated | medium | the factor barred from trading on his own account |
| `LR2` | coupled | high | a quarter of the profit in all three |
| `LR3` | 1 | high | — |
| `LR4` | 0 | high | — |
| `LR6` | symmetric | low | 2 of 3; doc. 9 upside-only |
| `MG1` | contract | high | — |
| `MG4` | private-contract | high | notarial deeds |
| `FP1` | commercial-profit | high | — |
| `CF1` | 1 | low | 2 of 3; doc. 3's factor puts in 80 ducados |
| `CF2` | 0 | low | 2 of 3; doc. 8 is P |
| `CF3` | multilateral | low | 2 of 3; doc. 3 has one capital partner |

The silent cells are the questions about default law outside the contract: personhood, creditors' reach, owner shielding (`LP1`, `LP3`, `AP1`–`AP3`, `LR1`), with `TS4`, `CI3`, `CI4` and `FP2`–`FP4`. `MG2` is `.NR` because the deeds divide control by place, Seville and the Indies, and the value set has no state for that.

## Doc. 8: a labour-only factor who bears a quarter of the loss

The clause: «Ytem si pérdida hubiere en esta compañía, lo que Dios no quiera, cargue a todos los compañeros tal y como hereda en la ganancia» (p. 74). The factor, Gonzalo Fernández de Loya, «no mete cosa alguna en esta dicha compañía, salvo el trabajo e industria de su persona» (p. 69). MS's reading (R1): he is liable for one quarter of any loss, out of his own goods. He is received «por factor y compañero» (p. 68), contracts above 100 pesos are made in the name of «todos cuatro compañeros» (p. 69), returns are registered to all four, and he takes a quarter of the profit. The later phrase binding him «como a tal vuestro factor, y persona que no mete … caudal alguno» (pp. 74–75) describes his position, not a cap on his loss. **The blind coder reached the same reading on the clause's words.**

It is the allocation rule of [[The comanda ad societatem shares losses in the proportion of profits]], in a sixteenth-century Castilian deed. Docs. 3 and 9 put the capital loss on the capital partners instead: «que ella corra contra vos los dichos Diego y Pedro Caballero, y no contra mí» (doc. 9, p. 79). At deed level `CF2` does not determine `LR6`: doc. 3 is 0 and symmetric, doc. 9 is 0 and upside-only, doc. 8 is P and symmetric.

## The rulings

All by MS, 2026-11-19, on the operator's recommendations (`records/RULINGS-compania-sevilla-2026-11-19.md`).

1. **Doc. 2 is not an instance.** It lacks the asymmetry between capital and labour that defines the form. A scope ruling: the bundle's scope text admitted it, and the coder assigned it under a test written in its priors. Its removal dissolves the coder's two 2:2 ties (`CF1`, `CF3`).
2. **Variation across deeds is coded by ruling 2 of 2026-10-07**: the modal state, the counts in `notes`, confidence lowered. The operator's proposal of a new `CF2`/`LR6` value for allocation set deed by deed (R2) is withdrawn. It overlooked that ruling, and the coder found it.
3. **No split.** On three deeds every sub-row would rest on one deed.
4. **A split criterion fixed before more deeds are read.** Dimension: loss allocation to a labour-only factor (variant A, the capital partners bear it: docs. 3, 9; variant B, the factor bears a share equal to his profit share: doc. 8). Split only when each variant has at least three deeds, the minority occurs with more than one notary, office or set of principals, and it co-varies with at least one other clause.
5. `LP2` 0 low and `MG2` `.NR` accepted; `TS3` and `CI2` declared one piece of evidence; a `works.csv` row added.
6. The ordering disclosure accepted.

## Scoring

R1 agreed blind. The assignment matched the operator's named likeliest deviation (doc. 2 in). The misfit test on `CF2` and `LR6` failed, and the failure is the operator's: it predicted a misfit report that the existing rule made unnecessary. `CF1` and `CF3` missed because of doc. 2. `MG2` missed toward a weaker claim. `TS3` landed on the named deviation (P); `LR2`, `TS2`, `CI1`, `AP2`, `LR1` and `FP1` were hits. The coder falsified twelve of its own priors, nine of them cell priors, mostly cells it expected silent and the deeds answer. Its `CF1` and `CF3` priors hold on the three deeds that remain.

## Where this is soft

- **One notary.** All three instances are Cazalla's, and docs. 3 and 9 are in one book of 1542: one drafting hand, not three witnesses. See [[Count degrees of freedom not cells]].
- **Four cells hold at 2 of 3**, and `LR6` turns on how doc. 3's factor, who stakes 80 ducados against 3,000 and takes a quarter of the profit, is read. On the stricter reading the modal state is upside-only.
- **One edition, selected by its editor in 1970**, in modernised spelling; quotations reproduce his text. The text layer was read against every page image ([[The OCR text layer evidences a clause's presence, not its absence]]).
- **The coder's stated count was wrong.** Its notes give 13 substantive and 17 `.NR`; its frozen rows have 15 and 15. Corrected at application.

## Open

- **A tie rule (ruled).** Ruling 2 of 2026-10-07 has no answer for an exact tie between deed-level states, which forced the coder to use `.NR` for "answered, but tied". It does not arise in this row after ruling 1. **Ruled by MS the same day:** a tie is answered, not silent; the split is tested first, and failing it the cell takes a new token `.TI`, added to the schema with the first batch that needs it (`records/RULINGS-tie-across-instances-2026-11-19.md`).
- **Acquisitions for the split criterion.** The *Catálogo de los fondos americanos del Archivo de Protocolos de Sevilla* regesta (tomos XV and XVI held), read in full in the archive or in published transcriptions; Gutiérrez García 1998 as a pointer; Martínez Gijón 1979 (on inter-library loan); Martínez Gijón 1966, section D, unread.

## Links

- [[Blind re-coding workflow - operator, coder, application]]
- [[A blind is a property of the channel not of the dataset]]
- [[Comanda primary pass coding and adjudication 2026-10-27]]
- [[The comanda ad societatem shares losses in the proportion of profits]]
- [[The Catalan maritime comanda puts the whole capital loss on the investor]]
- [[Martinez Gijon on the comenda in Spanish law]]
- [[Archivo Historico Provincial de Sevilla - notarial protocols]]
- [[The OCR text layer evidences a clause's presence, not its absence]]
- [[Count degrees of freedom not cells]]
- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]

## Source

Operator and application session `compania-sevilla-operator-2026-11-19`, and blind coding session `compania-sevilla-coding-2026-11-19`, both `claude-opus-5-5` at effort `high`, 2026-11-19. Source: Martínez Gijón, José. 1970. "La práctica del comercio por intermediario en el tráfico con las Indias durante el siglo XVI". *Anuario de Historia del Derecho Español* 40: 5–84 (Apéndice documental, pp. 43–84). Zotero `K36HMDA9`.
