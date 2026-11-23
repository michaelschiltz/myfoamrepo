---
title: The persistence coefficient fails even where the dynamics are ergodic
type: permanent
tags: [persistence, space-for-time, ergodicity, ergodic-hygiene]
project: HistorEE
source-session: kelly-2026-mechanisms
created: 2026-11-23
status: seed
---

# The persistence coefficient fails even where the dynamics are ergodic

Objective 3 states its licence as "the process is ergodic." Stated that way, it is refuted by the friendliest counterexample available. A stable linear system — unique invariant law, geometric relaxation, ergodic in the second and third senses of [[The word ergodic carries four incompatible senses]] — already yields a cross-sectional persistence coefficient that measures neither the system's persistence nor any unit's. **Dynamical ergodicity is necessary for the space-for-time step and nowhere near sufficient.**

## The construction

Let locations evolve as *y*ₜ₊₁ = *c* + *Ay*ₜ + *u*ₜ₊₁, with *A* symmetric, ρ(*A*) < 1 and steady state µ = (*I* − *A*)⁻¹*c*. The expected slope of *y*ₜ₊ₗ on *y*ₜ (Kelly 2026, eq. 5) is

β_L = β_µ + Σₖ ωₖλₖᴸ,

where β_µ projects the steady state onto the demeaned initial configuration, and the weights ωₖ measure the alignment of that configuration with the eigenvectors of *A*. The weights sum to 1 − β_µ and can take either sign, so β_L can lie outside the range of the eigenvalues. Checked numerically against the exact slope, 2026-11-23: see [[Kelly 2026 on the mechanisms of historical persistence]].

One number carries two economically distinct quantities: **between-unit heterogeneity of steady states** (β_µ) and **within-trajectory relaxation, mode by mode** (the sum). This is Heckman's (1991) distinction between heterogeneity and state dependence in cross-sectional form, and the linear case of what [[The mita boundary separates two components not two points on a trajectory]] argues for Dell: a level difference between units is not a rate of propagation within one.

## Where the licence actually fails

Nothing in the dynamics fails. What fails is reading the cross-section as an ensemble. With heterogeneous *c*ᵢ each location has its own stationary law, centred on its own µᵢ; with coupling the *N* coordinates are not *N* realisations but one realisation of an *N*-dimensional process. For the observable "a location's outcome", the distribution across units is not the distribution one unit traces through time. That is the condition the chronosequence literature calls site interchangeability.

The ergodicity Objective 3 needs is therefore **equality between the cross-unit distribution and a single unit's time distribution, for the observable and horizon at issue** — the third sense, which sits within the hierarchy of [[Connaughton Lamb and Paillusson 2026 on what ergodicity is]]. Asserted of "the process", the condition is met by Kelly's construction, and a referee who knows it takes the point.

## Two further conditions

Even with interchangeable steady states (*c* = 0, equal row sums of *A*) the coefficient is a non-negatively weighted average of the eigenvalues of the contrast modes, below ρ(*A*)ᴸ, because the dominant mode is absorbed by the intercept. Only with no coupling and homogeneous dynamics does β = λᴸ exactly. Two conditions beyond dynamical ergodicity follow:

- **homogeneous steady states** across units;
- **no interference** between units.

The five conditions of WP3 (Part 2 §3) contain neither in so many words. "Regime homogeneity" covers a common *A*, not a common *c*, and nothing in the list covers coupling.

## What must be conceded

- **The model is linear-Gaussian.** It says nothing about multiplicative growth, absorbing states or several basins, which are where Objective 3's distinctive claims lie. It is the *a fortiori* benchmark — the coefficient fails even here — not the case.
- **The construction is Kelly's, in an unrefereed working paper.** The algebra is elementary and has been checked independently; the claim does not depend on the paper's standing, and in print it can be carried by Heckman (1991) and a two-line derivation.

## Links

- [[Kelly 2026 on the mechanisms of historical persistence]]
- [[A long-horizon persistence coefficient bounds no relaxation time]]
- [[A significant persistence coefficient is evidence against its own licensing condition]]
- [[The mita boundary separates two components not two points on a trajectory]]
- [[The word ergodic carries four incompatible senses]]
- [[Connaughton Lamb and Paillusson 2026 on what ergodicity is]]
- [[Licensing the ensemble is a dynamical question not a metaphysical one]]
- [[Persistence stationarity and mobility literature]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]
- [[MOC - ERC Synergy Grant]]

## Source

Session of 2026-11-23, reading Kelly (2026) against the licensing sentence of Part 2 §3.

## References

Heckman, James J. 1991. "Identifying the Hand of the Past: Distinguishing State Dependence from Heterogeneity." *American Economic Review* 81 (2): 75–79. Zotero `C9EXVI9Q`.

Kelly, Morgan. 2026. "The Mechanisms of Historical Persistence." Working paper.
