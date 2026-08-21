---
title: Attractor selection bounds what a persistence design can resolve
type: permanent
tags: [retrodiction, persistence, path-dependence, reinforcement, attractor-selection, space-for-time, historiography]
project: HistorEE
source-session: ice-cube-retrodiction
created: 2026-08-21
status: seed
---

# Attractor selection bounds what a persistence design can resolve

[[Reinforcement selects an attractor the ensemble average never occupies]] states the forward result: increasing returns give multiple stable fixed points and the realised path selects one, decreasing returns give a unique fixed point and history washes out. This note takes the same dichotomy backwards, which is where the persistence design lives.

**Under attractor selection the resolution obtainable about the past is bounded by the number of distinguishable attractors, and by nothing else.** Not by the sample size, not by the precision of the outcome measure, not by the richness of the controls. The terminal state records which fixed point the process reached. Everything finer than that partition was decided by early increments whose signature the terminal state does not carry.

The Pólya urn makes the point without any historical apparatus. Every realisation starts from the same urn; the limits spread uniformly over the unit interval; and observing a limit of 0.31 tells you which draws occurred only through a posterior so diffuse as to be useless. Early history is not erased — it is what fixed the limit — but it is **unreadable from the limit**. Those are different statements and only the second bears on retrodiction.

## Two mechanisms, one cross-sectional signature

The word *persistence* is doing duty for two dynamics that a two-date design cannot separate.

- **Proportional transmission.** The initial condition is attenuated but carried: `x_T = ρ^T x_0 + noise`, `ρ` near one. The map is injective, inversion is a signal-to-noise problem, and a large coefficient really does measure the strength of a channel from the deep past. Retrodiction is licensed, and better outcome data buys more resolution.
- **Attractor selection.** Multiple fixed points, one of them realised. A large coefficient measures the separation and the depth of the attractors. It says nothing about the initial condition beyond which partition element contained it.

Both produce what the regression sees: variation across units today aligned with variation across units then. Nothing in the estimate distinguishes them, and the two license opposite readings of the same number.

## The consequence that is checkable

A continuous deep-roots regressor estimated on an attractor-selection process is **over-resolved**: the estimate has a standard error but no referent at the resolution it is reported to. The usual remedies operate on the standard error, so the defect passes through them untouched — the same structural property that makes [[Deep-roots variables are symplesiomorphies]] unanswerable by a robustness table.

The constructive form, following [[Retrodiction fails on non-invertibility not on induction]]: state, per design, which functionals of the initial condition the dynamics preserve. Under attractor selection the answer is the partition, and a claim pitched finer than the partition is unsupported however well estimated.

## The mechanism the literature invokes is the one that costs it the reading

Arthur's lock-in is cited in the persistence literature to make a distant cause plausible — the reason a medieval condition should still be visible is that the system locked in. But Arthur's lock-in *is* attractor selection, and attractor selection is what bounds the resolution. The story supplied to justify the finding is the story that limits what the finding can say.

Two disciplines apply here and are not optional. The mechanism must be named rather than gestured at, per [[Path dependence requires naming the non-commuting operation]]: the claim above is about reinforcement, and it does not transfer to the absorbing case, which is a distinct mechanism ([[Absorption is a path-dependence mechanism distinct from reinforcement]]). And the word itself must be kept straight, per [[Arthur's lock-in and capital lock-in are different objects]] — this note concerns the first sense only.

## Relation to the absorption objection

[[Persistence samples are conditioned on non-absorption]] and this note are independent and should not be run together. That one is a **selection** argument: the estimation sample is the set of units that did not absorb, so the coefficient is conditioned on a collider and is unsigned absent a model of the absorption hazard. This one is a **resolution** argument, and it bites on the surviving units — those that absorbed nothing and whose data are perfect. The two attack different halves of the design, and their conjunction is stronger than either, but only if each is stated in its own terms.

## The discriminating evidence is a middle

The two mechanisms separate on trajectories, not on endpoints. Under proportional transmission units drift apart smoothly and their ordering is preserved throughout; under attractor selection they converge on a few states and the within-partition ordering is scrambled early, so the cross-sectional ordering at *T* need bear no relation to the ordering at intermediate dates. Any observation between treatment and outcome discriminates; a design with two dates cannot.

That is a positive result rather than only a critical one, and it says where to spend effort in WP3.

## Where this can be resisted

A defender need not accept that the estimand was ever the magnitude of `x_0`. If the claim is a causal contrast identified across units under an exchangeability assumption, the retrodictive reading was never asserted and this note misses its target. The cost of that reply is taken up in [[A significant persistence coefficient is evidence against its own licensing condition]].

Second, real processes are mixtures. Partial reinforcement over a partially transmitting substrate is the normal case, and the two mechanisms above bound a spectrum rather than exhausting it. Locating a given design on that spectrum is work; asserting that everything is attractor selection is the mirror image of assuming everything transmits, and is no better.

## Links

- [[Reinforcement selects an attractor the ensemble average never occupies]]
- [[Retrodiction fails on non-invertibility not on induction]]
- [[A significant persistence coefficient is evidence against its own licensing condition]]
- [[Persistence samples are conditioned on non-absorption]]
- [[Absorption is a path-dependence mechanism distinct from reinforcement]]
- [[Path dependence requires naming the non-commuting operation]]
- [[Arthur's lock-in and capital lock-in are different objects]]
- [[Deep-roots variables are symplesiomorphies]]
- [[Voigtlander and Voth measured the relaxation time and reported a mixture]]
- [[Path dependence literature]]
- [[MOC - Path dependence and sequence]]
- [[MOC - Historiography and method]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]
- [[MOC - ERC Synergy Grant]]

## Source

Ice-cube session, 2026-08-21. MS raised Taleb's melting cube; the transposition is that melting is an attractor-selection process whose fixed point is set by the table rather than by the cube. The note was drafted first in the language of "basins" and rewritten into the vault's existing vocabulary after [[Reinforcement selects an attractor the ensemble average never occupies]] was found to hold the forward half of the argument already.

**Status.** The over-resolution claim has not been checked against an actual continuous deep-roots specification [verify]. It should be before the claim is made in print, and the check is cheap: any deep-roots regressor reported to more resolution than its underlying mechanism admits attractors will do.
