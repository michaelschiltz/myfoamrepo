---
title: Terminal wealth is permutation-invariant but survival is not
type: permanent
tags: [path-dependence, absorbing-barrier, multiplicative-dynamics, time-average]
project: HistorEE
source-session: path-dependence-sequence
created: 2026-08-05
status: seed
---

# Terminal wealth is permutation-invariant but survival is not

The barrier is what breaks the symmetry. Terminal wealth does not care about order; the running minimum does.

Given the [[Absorbing barrier]] at $b$, define the hitting time

$$T = \inf\{n : W_n \le b\}$$

$T$ depends on $\min_k \prod_{i \le k} r_i$, the running minimum of the partial products, and the running minimum is *not* permutation-invariant even though the full product is. Front-load the adverse draws and the trajectory is absorbed before the favourable ones arrive. Those favourable draws remain in the multiset — they "happened" in the ensemble — but this trajectory never reached them.

The asymmetry is the cleanest statement of why survivorship is a dynamic property rather than a sampling artefact. Two entities facing an identical distribution of shocks, differing only in the order of arrival, are not facing the same problem. One is a going concern with a bad decade behind it; the other does not exist, and its non-existence is not evidence about its quality. This sharpens [[Refusals are observations of the filter not inferences from survivors]]: the filter operates on orderings, not only on forms.

It also supplies the mechanism that [[Time-average optimization is a survivorship property not an intention]] needs. Time-average optimisation need not be intended by anyone; orderings that cross the barrier are simply removed, and what remains looks like optimisation after the fact.

## Links

- [[Absorbing barrier]]
- [[Pure multiplicative dynamics are permutation-invariant]]
- [[Absorption is a path-dependence mechanism distinct from reinforcement]]
- [[Time-average optimization is a survivorship property not an intention]]
- [[Refusals are observations of the filter not inferences from survivors]]
- [[Time-average]]
- [[MOC - Path dependence and sequence]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Path-dependence session, August 2026.
