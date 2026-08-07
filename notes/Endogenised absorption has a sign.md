---
title: Endogenised absorption has a sign
type: permanent
tags: [absorbing-barrier, risk-sharing, coding-ontology, character-independence]
project: HistorEE
source-session: tontines-and-annuity-valuation
database: [loss_mitigation_forms]
created: 2026-08-07
status: seed
---

# Endogenised absorption has a sign

The absorbing barrier is normally environmental — the ruin risk a venture faces from outside, and the parameter against which variance suppression is judged ([[An absorbing barrier breaks ergodicity by construction]]). A contract can instead *constitute* it: one member's absorption is written into the payoff function of the others, so the barrier stops being a boundary condition and becomes a term of the instrument. Endogenisation as such is not diagnostic, because it runs in two directions with opposite consequences.

**Transfer to survivors.** A member's extinction raises the entitlement of those remaining. Tontines, survivorship annuities, viaticals. The recipients suffered nothing; the draw is funded by the extinction itself.

**Transfer from survivors.** A member's default raises the obligation of those remaining. Joint-and-several liability, mutual-surety pools, guild and village collective-responsibility regimes. Here the transfer is loss-corresponding within a reciprocal pool, so the same structural feature yields the opposite dispersion result.

A coding that recorded only "absorption is payoff-relevant to other members" would place a tontine and a mutual surety pool in one cell. The sign is what carries the content, and it is recoverable from statute, deed or customary compilation without reference to any theoretical apparatus — which is what makes it usable as an independence test rather than an analyst's imputation.

The census does not currently express it. `PY1 payout trigger` allows `realised-loss | life-event | rotation | need-assessed`, which names the *kind* of event and is silent on *whose*. For a tontine the trigger is another subscriber's death; `life-event` is the only available value and it reads identically to a widows' fund, where the trigger is the member's own. This is a Sereno well-formedness failure of exactly the kind `CHARACTER-CODING.md` test 1 describes — one characteristic silently asking two questions — and the repair is a split on the model of `LR2 → LR6`, not an embellishment. It is the one feature addition this material licenses; everything else it suggests is redundant with `PY0` and `PY1` once the locator is present.

Whether the two directions ever coexist in one arrangement is open. Burial societies and the later widows' funds are candidates — survivorship accrual on one limb, mutual assessment on the other — and if such hybrids exist a single row cannot hold them.

## Links

- [[The tontine is pooling in form and dispersal in function]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Absorbing barrier]]
- [[Entitlement by liability versus entitlement by membership]]
- [[Count degrees of freedom not cells]]
- [[Typology and character coding literature]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Tontines and annuity valuation session, 2026-08-07. Proposed `PY1` split recorded in `HistorEE_codebooks` logbook; not yet implemented pending review.
