---
title: Ergodicity is indecomposability not randomness
type: permanent
tags: [ergodicity, ergodic-hygiene, time-average, ensemble-average]
project: HistorEE
source-session: wp3-ergodicity-formal-placement
created: 2026-08-06
status: seed
---

# Ergodicity is indecomposability not randomness

Ergodicity is not a property of randomness, and not a property of a process considered on its own. It is a property of a *measure-preserving dynamical system* — a state space, a measure, and a map that preserves it. The system is ergodic if and only if every invariant set has measure zero or one; equivalently, the invariant σ-algebra is trivial. The condition is one of **indecomposability**: the state space admits no non-trivial partition into pieces the dynamics never connect.

This matters because the familiar slogan runs the definition backwards. Birkhoff's pointwise theorem establishes that time averages of an integrable observable converge almost surely to its *conditional* expectation given the invariant σ-algebra. Ergodicity is precisely the condition under which that conditional expectation collapses onto the unconditional one. **Time average equals ensemble average is therefore a consequence of ergodicity, not its definition**, and treating the slogan as the definition is the single most common source of imprecision in the applied literature — including in work sympathetic to us. The ergodic decomposition theorem completes the picture: ergodic measures are the extreme points of the convex set of invariant measures, and every invariant measure is a mixture of ergodic ones.

The payoff for the project is that indecomposability is the formulation that connects directly to the historical argument. A partition of the state space that the dynamics cannot cross is what an [[Absorbing barrier]] *is*. Framing ergodicity as a statement about averages leaves the barrier looking like an application; framing it as indecomposability makes the barrier the central case. See [[An absorbing barrier breaks ergodicity by construction]].

Ergodicity is also the *weakest* member of a hierarchy — ergodic ⊂ weakly mixing ⊂ strongly mixing ⊂ K-system ⊂ Bernoulli — demanding only decorrelation in Cesàro average. The strong law of large numbers is the independent and identically distributed special case; Kolmogorov's zero-one law and Hewitt–Savage are the tail- and exchangeable-σ-algebra analogues. Claiming ergodicity therefore claims very little, and *denying* it claims a great deal.

## Links

- [[Stationarity is a precondition of ergodicity not a corollary]]
- [[The word ergodic carries four incompatible senses]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Route Kolmogorov to ergodic theory not the theory of means]]
- [[Time-average]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

WP3 formal-placement session — locating the ergodicity concept in the theory of stochastic processes to the standard a mathematically literate referee would apply.

## References

Birkhoff, George D. 1931. "Proof of the Ergodic Theorem." *Proceedings of the National Academy of Sciences* 17 (12): 656–60. https://doi.org/10.1073/pnas.17.2.656

Von Neumann, John. 1932. "Proof of the Quasi-Ergodic Hypothesis." *Proceedings of the National Academy of Sciences* 18 (1): 70–82.

Walters, Peter. 1982. *An Introduction to Ergodic Theory*. New York: Springer.

Cornfeld, I. P., S. V. Fomin, and Ya. G. Sinai. 1982. *Ergodic Theory*. Berlin: Springer.
