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

The French royal tontines from 1689 divided subscribers into fourteen age classes carrying differentiated rates. The English tontine of 1693 did not differentiate by nominee age at all — which is why nominees were selected young, and why Halley advised against it. Same mechanism, same decade, two polities, opposite values of `PR1` inside `MC1=pooling`. Pricing therefore varies *within* a mechanism at a fixed date rather than marking a passage between mechanisms. It is a separate axis, not a stage.

This is what the census was built to find, and it arrives by the route `CHARACTER-CODING.md` prescribes: **add forms, not features**. The generic `tontine` row could not hold the result because the type spans both values — a doubt already recorded against it. Splitting into `tontine_en_1693` and `tontine_fr_royal` gives the pricing facet its first variance inside a single mechanism, exactly as coding the *asiento* gave the pooling facet its first variance. One form settles what no amount of reasoning could ([[Count degrees of freedom not cells]]).

The consequence for the argument is larger than the cell. If pricing is orthogonal to mechanism, then the ascent from hazard-bearing to risk-pricing cannot be reconstructed as an institutional sequence at all, and Harris's timing argument — general average ancient because nothing is priced ex ante, premium insurance late because everything is — is a claim about *what a mechanism requires*, not about *when societies learned to price*. Those are different propositions and only the first is supported. See [[The tontine's chronology defeats the hazard-to-pricing staging]] for the narrative version of the same result.

Second consequence, for coding hygiene: `PR1`'s definition deliberately says *peril* rather than *risk*, so as not to name the characteristic with the endpoint of the shift it measures. That discipline was correct and is now load-bearing, because the shift it was built to measure turns out not to be a shift. Keep the wording ([[The determinate-contingent typology carries the richness]]).

## Links

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

Tontines and annuity valuation session, 2026-08-07. French fourteen-class structure from secondary sources surveyed August 2026 — verify against Weir (1989) and Velde & Weir (1992). English 1693 flat structure verify against Milevsky (2015). Both codings entered in `loss_mitigation_forms` at `confidence: medium` pending those checks.
