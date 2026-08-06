---
title: Time-average
type: permanent
tags: [time-average, ergodicity, multiplicative-dynamics]
project: HistorEE
source-session: concept-anchor
created: 2026-07-20
status: seed
---

# Time-average

The growth rate realized along a *single trajectory* through time, as opposed to the ensemble average taken across many parallel trajectories at one instant. For multiplicative dynamics with an [[Absorbing barrier]] the two diverge, and only the time average describes the fate of the one agent who cannot step outside his own path.

## The equivalence conditions

The object is made precise by Birkhoff's pointwise ergodic theorem: for an integrable observable of a measure-preserving system, the time average converges almost surely to the *conditional* expectation of that observable given the invariant σ-algebra. The equivalence of time and ensemble averages is therefore not a general fact about long runs but the special case in which that σ-algebra is trivial — see [[Ergodicity is indecomposability not randomness]].

Three conditions must hold before the equivalence can even be asserted, and each fails somewhere in our material. The system must be **measure-preserving and stationary**, which is a precondition of the definition rather than a consequence of it ([[Stationarity is a precondition of ergodicity not a corollary]]). The invariant σ-algebra must be **trivial**, which an absorbing state destroys by construction ([[An absorbing barrier breaks ergodicity by construction]]). And the observable must be the one to which the theorem is being applied — the average of a non-linear function of the state is not the function of the average, which is where the multiplicative case actually goes wrong ([[Nothing in the ergodic theorem fails in geometric Brownian motion]]).

The third condition is the one most often skipped. In the geometric case the time-average growth rate is recovered by applying the theorem to the *log-increments*, which are perfectly stationary and independent; the divergence from the ensemble rate is the [[Jensen gap]], not a failure of Birkhoff. Stating it that way keeps the concept usable under review.

## Links

- [[Absorbing barrier]]
- [[Ergodicity is indecomposability not randomness]]
- [[Stationarity is a precondition of ergodicity not a corollary]]
- [[Nothing in the ergodic theorem fails in geometric Brownian motion]]
- [[Jensen gap]]
- [[Pricing risk does not remove it]]
- [[The ensemble average is the local descriptor of a barrier-shielded agent]]
- [[Route Kolmogorov to ergodic theory not the theory of means]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]
