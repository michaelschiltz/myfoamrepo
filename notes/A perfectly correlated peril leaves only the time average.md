---
title: A perfectly correlated peril leaves only the time average
type: permanent
tags: [ergodicity, time-average, absorbing-barrier, synchrony, coding-ontology, risk-sharing]
project: HistorEE
source-session: ottoman-communal-funds
database: [loss_mitigation_forms]
created: 2026-08-13
status: superseded
---

# A perfectly correlated peril leaves only the time average

> **This note's central claim was tested against its sources on the day it was written and failed.** The title is retained because the reasoning recurs and should stay findable; the argument is set out below as it was made, then dismantled. What survives the dismantling is at the end, and is worth more than what was lost.

## The argument, as made

[[Pooling's sign is set by the correlation of its baskets]] establishes that pooling averages nothing as ρ→1: under Var(r|N) = (s²/N)[1 + (N−1)ρ], perfect correlation returns Var → s², and aggregating N members "merely relabels N members as a single unit". That note treats ρ→1 as the failure mode of a strategy. The Ottoman *avarız* fund appeared to pose the case where ρ→1 is the **initial condition**, and to ask what institution is left when it is.

The peril was taken to be an extraordinary levy assessed on a *mahalle* under collective fiscal liability, its correlation across members definitional rather than contingent: the shock constituted on the community and then apportioned, so that no partition of the membership yields a decorrelated basket. Cross-sectional mitigation would then be unavailable *in principle*. What remained was the other axis — an endowment accumulating in ordinary years and discharging in levy years, averaging the peril **across periods** rather than across members. This was to be the time-average operation performed directly, and, in the sharpest formulation, a **purer ergodicity object than any pooling institution in the census**: a mutual fund raises each member's [[Time-average|time-average]] growth *by borrowing the ensemble*, reaching sideways to members whose draws are partly independent; a buffer stock would raise it with no ensemble at all, the same operation with the crutch removed.

Two falsification conditions were stated. Both failed.

## Why it fails

**The buffer requires drawdown, and drawdown is categorically forbidden.** Küçük on the Kastamonu Kırkçeşme fund: expenditure must absolutely be made out of the profit obtained, and the principle that no expenditure be made from the principal was adopted — enforced by personal liability on the *mütevelli* and even on the officials collecting the *avarız akçesi*, who were to indemnify the fund from their own property. The quarter's needs were met from the *nema*: 942 *kuruş* of annual return against 6,280 of untouchable corpus. Nothing accumulates and nothing is drawn down. **It is an endowment whose income substitutes for taxation, not a buffer stock.**

**A regularised levy is not a hazard, and the levy was regularised.** From the late sixteenth century the state, in fiscal crisis, resolved to collect certain taxes continuously and in cash; the *avârız-ı divâniye* and *tekâlif-i örfiye* were turned into regularly collected annual taxes. A predictable annual charge is a cost of residence, not a peril.

**And the variable was wrong, which is the failure that matters.** The peril the fund addresses is not the levy. Küçük's account of the funds' origin is that difficulties arose *in the process of the populace meeting these newly created taxes*, and the stated design is that persons **without the ability to pay** should benefit. The levy falls on everyone; **which household proves unable to meet its share does not**. That variation is idiosyncratic, ρ is nowhere near one on it, and ordinary cross-sectional mitigation was available the whole time. The correlated quantity was never the one the institution was built against. **The levy is the setting; the incapacity is the hazard.**

The general lesson is not about the Ottoman Empire. It is that ρ is a property of a **specified variable**, and an institution's ρ must be read off the thing it actually indemnifies rather than off the thing that makes indemnity necessary. A famine is covariate; who starves in it is not. A levy is covariate; who cannot pay it is not. Every mutual institution operating inside a correlated environment will look like a ρ→1 case until one asks what it writes cheques against.

## What survives

**Contributor and beneficiary sets can be disjoint, and the census now has three cases of it.** The fund is endowed by donors of comfortable means; the beneficiaries are those unable to pay. This is not pooling among the exposed — it is a hazard shifted onto an endowment, which is why the row reads `MC1=allocation`. With `guild_box_dutch` and `friendly_society_female_england` it makes the third case, and it is the cleanest of the three because the two sets barely overlap. The taxonomy inherited from Harris presumes that those who fund a pool are those it protects; three counterexamples in a thirty-three-form census is enough to say the presumption is doing unexamined work. See [[A scheme for extending the cooperative pooling census]].

**A state can suppress a security interest because it drives households across the barrier.** Deniz, on why three of four pledge-only deeds restrict pledges to gold and silver: creditors had been seizing peasants' land, forcing unpaid labour and distress sales, "often leading to bankruptcy. As peasants fled their lands, agricultural decline threatened state revenue." The state then prohibited taking real estate, vineyards and gardens in pledge, and ordered those already taken returned. The fisc suppressed a form of collateral because foreclosure was pushing its own tax base past the [[Absorbing barrier|absorbing barrier]] — a ruler internalising an absorbing-barrier externality, in the sixteenth century, and legislating against it. **This deserves its own note and does not belong buried in a retraction.**

> **Method.** This note was written before any source was read, from a literature-search summary, and was wrong within hours. So was the Rouen exclusion of the previous day, and for the same reason. The falsification conditions did their work — both were stated in advance, both were checked, both failed cleanly, and the cost was one afternoon. **Keep writing the conditions. Stop writing the notes before at least one source has been read in full.**

## Links

- [[Pooling's sign is set by the correlation of its baskets]]
- [[Time-average]]
- [[Absorbing barrier]]
- [[Jensen gap]]
- [[Skin in the game]]
- [[A scheme for extending the cooperative pooling census]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Küçük 2025 on the Kastamonu Kırkçeşme *avarız akçesi* endowment (`10.21021/osmed.1472954`) and Deniz 2026 on 97 sixteenth-century cash-waqf deeds (`10.33227/auifd.1740727`), both read in full, both Turkish, both outside MS's working languages and flagged accordingly in the census. The ρ→1 apparatus is carried over from the cooperation–synchrony session and is that note's, not mine. The discarded reading and its two falsification conditions are recorded at `HistorEE_codebooks/logbook/4`, and the coded form is `avariz_vakfi_kirkcesme`, `loss_mitigation_forms` 0.5.0.
