---
title: Unilateral and bilateral commenda collapse on profit and separate on loss
type: permanent
tags: [commenda, similarity, character-independence, coding-ontology, comparative, risk-sharing]
project: HistorEE
source-session: allocation-anchors-blind-coding
database: [loss_mitigation_forms]
created: 2026-08-18
status: seed
---

# Unilateral and bilateral commenda collapse on profit and separate on loss

Pryor (1977), Luzzatto (1961, 119) and van Doosselaere (2009, 65 n.7) all hold that the unilateral *commenda* and the bilateral form — the *societas maris*, "often called *societas* in Genoa" — are **essentially the same agreement**, the choice between them turning on the traveller's wealth rather than on anything in the contract. Van Doosselaere adopts Pryor's view explicitly and traces a single traveller, Ansaldo Baiardo, moving from one to the other in 1158 once two ventures' quarter-profits had capitalised him.

**The verdict is reached on the payout, and on the payout it is airtight.** Unilateral: three-quarters of net to the investor, one-quarter to the traveller, who contributes no capital. Bilateral: halves, with the traveller in for a customary third. Van Doosselaere does the arithmetic (65 n.6): the bilateral traveller's half is his quarter-share of the labour return on the investor's two-thirds — one-sixth — plus the whole return on his own third. **The compensation for labour is identical.** The bilateral form is the unilateral form with the traveller's own capital bolted on.

**On the loss they are not identical, and the same page says so.** In the unilateral the investor "bore all liability for loss" and the traveller "bore no capital risk"; in the bilateral "the liability for loss was proportional to the respective initial investments of the participants". The traveller's downside is zero in one and a third in the other.

## Why this is a methodological finding and not a quibble

The collapse is **facet-relative**, and the facet on which it holds is the one the surviving evidence makes easy to compute. Notarial acts record payout schedules; they record liability by a clause or by silence and statute. A historiography built on counting contracts will therefore keep discovering identities on the payout side.

That is the same failure mode as [[Which peril gets a clause is set by the tradition's doctrinal problem]]: the verdict tracks what the sources make measurable, not what the institutions did. And it is a live instance of the ugly-duckling problem in reverse — the claim "these are the same contract" is as weighting-dependent as the claim "these differ", and neither is meaningful until the facet is declared.

Concretely, in the codebooks: `organizational_forms` would have every reason to merge the pair (same parties, same duration, same governance, same profit economics), and `loss_mitigation_forms` separates them cleanly on `RB1`/`RB2`. **Anyone merging or splitting them owes the reader the facet.**

## Where this is soft

The dissenters have a real answer: the bilateral traveller's third is his *investor's* hat, not a different contract, and a form is not individuated by who happens to be on both sides of it. The reply is that a loss census does not care which hat the exposure arrives under — the absorbing barrier does not either. But this is a genuine disagreement about individuation and it should not be reported as settled.

## Links

- [[The commenda and the qirad do not separate on loss allocation]]
- [[Which peril gets a clause is set by the tradition's doctrinal problem]]
- [[Ragusan collegantia is unilateral and Venetian collegantia is bilateral]]
- [[Typology and character coding literature]]
- [[commenda]]
- [[MOC - Historiography and method]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - HistorEE]]

## Source

van Doosselaere, *Commercial Agreements and Social Dynamics in Medieval Genoa* (Cambridge, 2009), 64–68 — 6,764 *commenda* ties from the Genoese notarial cartularies, 1154–1315, 93 per cent of all coded maritime ties. Pryor 1977; Luzzatto 1961, 119. Coded 2026-08-18 as `commenda_alloc` against `societas_maris`.
