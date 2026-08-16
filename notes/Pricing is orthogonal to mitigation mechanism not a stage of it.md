---
title: Pricing is orthogonal to mitigation mechanism not a stage of it
type: permanent
tags: [risk-pricing, risk-sharing, coding-ontology, comparative, historiography]
project: HistorEE
source-session: tontines-and-annuity-valuation
database: [loss_mitigation_forms]
created: 2026-08-07
status: seed
---

# Pricing is orthogonal to mitigation mechanism not a stage of it

`PR1` was built to test a sequence: if ex-ante pricing of peril is what separates an unquantified conception from a quantified one, then pooling forms should code `PR1=0` and premium forms `PR1=1`, with the transition doing chronological work. The tontine was flagged in the census as the candidate counter-example, and the test was recorded as not yet runnable for want of a source. It is now runnable, and the sequence collapses.

The French royal tontines from 1689 divided subscribers into fourteen age classes in five-year bands — the first to age five accomplished, the last from sixty-five — and declared interest progressive across them, *du denier 20 au denier 8 dans les treizième et quatorzième classes*: five per cent rising to twelve and a half for the oldest. The English tontine of 1693 did not differentiate by nominee age at all, which is why nominees were selected young and why Halley advised against it. Same mechanism, same decade, two polities, different values of `PR1` inside `MC1=pooling`. Pricing therefore varies *within* a mechanism at a fixed date rather than marking a passage between mechanisms. It is a separate axis, not a stage.

**And the axis has three positions, not two.** Coudy's own account forbids reading the French classes as actuarial: the grading is *dans un but d'équité*, and *l'on ne disposait d'aucune table de mortalité. L'on ne s'en souciait guère non plus* — no mortality table existed and nobody much minded. He doubts the Crown understood what the operation cost it. So the peril is priced ex ante by age band and not from any distribution, which is `P` rather than `1` — the reading already given to `sea_loan`, where Harris finds crude categories sufficient. Set against the Scottish Ministers' Widows' Fund, which *was* built on projected mortality, the census now shows **`PR1` running 0, P, 1 inside a single mechanism**: unpriced, crudely graded, table-based. The hazard-to-risk gradient is visible as three coded values rather than asserted as a sequence — and all three coexist.

**The direction of travel is the opposite of the received one.** Deparcieux in 1746 *derived* the survival chances of each class by observing the royal tontines of 1689 and 1696. The actuarial knowledge came **out of** these instruments, not into them. The tontine was the observational substrate for the quantification that would later make it unsellable — which is a sharper statement of the chronology point than the abandonment story alone ([[The tontine's chronology defeats the hazard-to-pricing staging]]).

This is what the census was built to find, and it arrives by the route `CHARACTER-CODING.md` prescribes: **add forms, not features**. The generic `tontine` row could not hold the result because the type spans both values — a doubt already recorded against it. Splitting into `tontine_en_1693` and `tontine_fr_royal` gives the pricing facet its first variance inside a single mechanism, exactly as coding the *asiento* gave the pooling facet its first variance. One form settles what no amount of reasoning could ([[Count degrees of freedom not cells]]).

The consequence for the argument is larger than the cell. If pricing is orthogonal to mechanism, then the ascent from hazard-bearing to risk-pricing cannot be reconstructed as an institutional sequence at all, and Harris's timing argument — general average ancient because nothing is priced ex ante, premium insurance late because everything is — is a claim about *what a mechanism requires*, not about *when societies learned to price*. Those are different propositions and only the first is supported. See [[The tontine's chronology defeats the hazard-to-pricing staging]] for the narrative version of the same result.

Second consequence, for coding hygiene: `PR1`'s definition deliberately says *peril* rather than *risk*, so as not to name the characteristic with the endpoint of the shift it measures. That discipline was correct and is now load-bearing, because the shift it was built to measure turns out not to be a shift. Keep the wording ([[The determinate-contingent typology carries the richness]]).

## The mechanism of the orthogonality

The medieval maritime material supplies a reason for the orthogonality rather than another instance of it. Pricing was gated by canon law; mechanism was not. *Naviganti* reached the priced premium and suppressed it for a century, while the allocation of peril between lender and borrower went on being drafted throughout, unaffected. Two variables under different constraints cannot be stages of one another.

The Hanseatic material makes the independence visible in a single comparison: the Lübeck *Bodmereibrief* of 1431 states its premium openly, at a third of capital for a six-month voyage, while Mediterranean notaries of the same century were burying theirs in freight and exchange rates — with no corresponding difference in mechanism. See [[A concealed premium is evidence about the notary not about the price]].

## Links

- [[Naviganti delayed the priced premium it is credited with dating]]
- [[Insurance is a split-off from the sea loan not a coordinate mechanism]]
- [[A concealed premium is evidence about the notary not about the price]]
- [[The tontine's chronology defeats the hazard-to-pricing staging]]
- [[The tontine is pooling in form and dispersal in function]]
- [[Pricing risk does not remove it]]
- [[Count degrees of freedom not cells]]
- [[The determinate-contingent typology carries the richness]]
- [[Typology and character coding literature]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Tontines and annuity valuation session, 2026-08-07; **French side verified 2026-08-09 against Coudy**, J. 1957. "La « Tontine Royalle » sous le règne de Louis XIV." *Revue historique de droit français et étranger* 35 — now in the Zotero library and read. All French quotations are his, from the section *La répartition par classes* and *L'intérêt servi*. `tontine_fr_royal PR1` **corrected from 1 to P** on that reading, `confidence` raised to high. English 1693 flat structure still to verify against Milevsky (2015). **The load-bearing verification item is Coudy, "La Tontine royale sous le règne de Louis XIV," *Revue historique de droit français et étranger* 35 (1957): 128–**, surfaced from Weir's bibliography and now in Zotero with metadata flagged unverified (no DOI, forename not recorded). Jennings & Trout (1982) and Wyler (1916) are the monograph treatments; Alter, "How to Bet on Lives," *Research in Economic History* 10 (1986) should settle whether the English 1693 scheme was age-graded. Weir 1989 `10.1017/S002205070000735X` and Velde & Weir 1992 `10.1017/S002205070001024X`, both CrossRef-resolved. Zotero collection: *HistorEE — pricing and pooling*.
