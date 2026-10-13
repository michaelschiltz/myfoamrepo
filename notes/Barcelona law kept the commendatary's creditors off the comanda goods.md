---
title: Barcelona law kept the commendatary's creditors off the comanda goods
type: permanent
tags: [entity-shielding, commenda, asset-partitioning]
project: HistorEE
source-session: comanda-adjudications-2026-10-11
database: [organizational_forms]
created: 2026-10-11
status: seed
---

# Barcelona law kept the commendatary's creditors off the comanda goods

In the Crown of Aragon the goods a commendatary brought back from a voyage were closed to his own creditors and to his wife's dower claims until the investors had been paid. *Recognoverunt proceres* cap. 69 (Barcelona, 1284) declares void the claims of the commendatary's wife for her *sponsalicium* and of "any creditor of the commendatary" against those goods, and admits them only once those who gave the comandas "recuperaverint illas commandas, vel merces emptas de illa pecunia"; it extends a pragmatic of Jaime I of 1271 against widows seizing comandas *ratione sponsalitiorum* when the commendatary died on the voyage (Martínez Gijón 1966, 421). Martínez Gijón reads the rule as presupposing "una separación tajante entre los bienes recibidos en comenda y el patrimonio del comendatario" (422).

**What it is, in the census's terms.** Weak entity shielding of the venture pool against one member's creditors — the investors, the pool's claimants, rank ahead of the agent's personal creditors in the pool's assets. `comanda AP1 = P`: the investor's own creditors and the rank of third parties who dealt with the venture are not addressed.

**Why it matters against the Italian account.** Harris 2007 describes the commenda pool as reachable by "creditors of the traveling party", and the live `commenda AP1 = P` rests on that. Barcelona barred them by statute in 1284. The Genoese statute Martínez Gijón quotes — commended goods preferred "quibuscumque creditoribus, quantumcumque anterioribus … etiam comprehensis dotibus" — reaches the same solution, but in its 1490/1588 printing, so it cannot date the Italian rule. Whether the twelfth- and thirteenth-century commenda had the protection is open, and it is the cell on which the Italian re-code should look first. *[Superseded 2026-10-12: Genoa had the rule by 1207–1217. See below.]* The wife's dower is the telling detail: the claim most likely to compete with the investors when a traveller died abroad is the one the rule names.

**How it was missed.** On 2026-10-07 the cell was `.NR` because "no source read addresses the commendatary's own creditors"; on 2026-10-11 a ruling classed the comanda–commenda difference on `AP1` as one of evidence on that ground. The source was §C of an article the batch had read only in §§A–B. A `.NR` that rests on "no source read" is a statement about the reading, and should say how far the reading went.


## Genoa by 1207–1217 (2026-10-12)

The Genoese Breve of the consuls of the *placita* (the fragment found at Nice and communicated by Datta, *Atti della Società ligure di storia patria* I, 1858, 81–84), which Desimoni dates to 1207–1217 (99), already has the rule. Chapter VI: the goods of whoever took money *in societate uel mutuo aut accomendatione* are held pledged to the investor, and *accomendator uel socius eius in mobilia preferatur aliis creditoribus. et uxori et nurui*. Movables found with the traveller are presumed bought with the money; in immovables bought after the contract the investors share equally with other creditors; an unpaid seller ranks first. The Pera statutes repeat it (Promis 1871, c. CCXI, 739–740).

So Barcelona in 1284 did not invent the protection; it legislated, for the wife's *sponsalicium*, what Genoa had in its consular breve two generations earlier. And the Italian account in Harris 2007, 11 — the pool "reachable … to creditors of the traveling party" — is wrong for Genoa. Harris restates Hansmann, Kraakman & Squire 2006, whose traveller half is a conjecture in n. 109 and whose cited source, Weber 1889, 77, reports the Genoese rule on the following pages. `commenda AP1` and `societas_maris AP1` stay `P`, now on the statute; `comanda` and `commenda` agree on `AP1` in substance, on evidence of the same kind.

Pisa went further for the *societas maris* in its 1248 revision of the *Constitutum usus*: partners are preferred in the company's goods over creditors *qui non sint creditores eiusdem hentice* (Bonaini II, 839), so the venture's own creditors are not subordinated. That is closer to entity shielding proper than the Genoese or Catalan investor's privilege.

## Links

- [[Comanda capital was kept apart unless the contract said otherwise]]
- [[The Consolat de Mar comanda chapters]]
- [[Martinez Gijon on the comenda in Spanish law]]
- [[A difference between coded forms is a difference of evidence, vocabulary or form]]
- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]
