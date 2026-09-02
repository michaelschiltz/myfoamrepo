---
title: Nothing in the ergodic theorem fails in geometric Brownian motion
type: permanent
tags: [ergodicity, jensen-inequality, convexity, multiplicative-dynamics, time-average, ensemble-average, ergodic-hygiene]
project: HistorEE
source-session: wp3-ergodicity-formal-placement
created: 2026-08-06
status: seed
---

# Nothing in the ergodic theorem fails in geometric Brownian motion

Geometric Brownian motion is the canonical illustration in the ergodicity-economics literature, and it is stated in a way that invites a fatal objection. The logarithm of the process has stationary, independent increments. Birkhoff therefore applies to those increments and delivers, almost surely, a time-average growth rate of $\mu - \tfrac{1}{2}\sigma^{2}$, while the ensemble average grows at $\mu$. Describing this as "non-ergodicity of geometric Brownian motion" invites the reply that the underlying process satisfies every hypothesis of the ergodic theorem, and that the phrase is a category error.

The defensible restatement is that **nothing in the ergodic theorem fails; what fails is the commutation of the time average with a non-linear transformation of the state.** The gap is [[Jensen gap|Jensen's inequality]] applied to a multiplicatively evolving observable, and $\tfrac{1}{2}\sigma^{2}$ is the size of that gap. Peters's contribution is to make ergodicity a property of an *observable relative to a process* rather than of the process alone — a legitimate move, standard in physics, but one that must be announced rather than smuggled.

Two concessions should be made before a referee extracts them. First, the mathematics is Itô's lemma plus an inequality from 1906, and the growth-rate result was established in the growth-optimal portfolio literature decades before the ergodicity-economics programme (Kelly 1956; Latané 1959; Breiman 1961). Second, the contribution is therefore decision-theoretic reframing rather than new mathematics: the maximand is relocated and corrected — structurally fixed by the dynamics rather than posited as a taste — not eliminated. Conceding both costs nothing we can defend anyway, and it purchases the credibility needed for the claim that *is* ours.

That claim is the historical one. Whether $\tfrac{1}{2}\sigma^{2}$ is a new theorem is irrelevant to whether institutions were selected under it. See [[Time-average optimization is a survivorship property not an intention]].

## Links

- [[Jensen gap]]
- [[Time-average]]
- [[Stationarity is a precondition of ergodicity not a corollary]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Time-average optimization is a survivorship property not an intention]]
- [[The ensemble average is the local descriptor of a barrier-shielded agent]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

WP3 formal-placement session — the defensive restatement, written to foreclose the "category error" objection.

## References

Breiman, Leo. 1961. "Optimal Gambling Systems for Favorable Games." In *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability*, 1: 65–78.

Kelly, J. L. 1956. "A New Interpretation of Information Rate." *Bell System Technical Journal* 35 (4): 917–26.

Latané, Henry A. 1959. "Criteria for Choice among Risky Ventures." *Journal of Political Economy* 67 (2): 144–55.

Peters, Ole. 2019. "The Ergodicity Problem in Economics." *Nature Physics* 15: 1216–21.

Peters, Ole, and Murray Gell-Mann. 2016. "Evaluating Gambles Using Dynamics." *Chaos* 26: 023103.

Peters, Ole, and Alexander Klein. 2013. "Ergodicity Breaking in Geometric Brownian Motion." *Physical Review Letters* 110: 100603.

**Verify before citing.** Doctor, Wakker and Wang, "Economists' Views on the Ergodicity Problem," *Nature Physics* 2020 — volume, page and DOI unconfirmed. This is the published critique flagged in the panel simulation and should be answered in text, not omitted.
