---
title: The expectation value describes a pool that re-shares not a population
type: permanent
tags: [ensemble-average, time-average, risk-sharing, diversification, synchrony, ergodicity]
project: HistorEE
source-session: honeycomb-theorem
created: 2026-10-31
status: seed
---

# The expectation value describes a pool that re-shares not a population

**Two of Peters's results, read together, separate what ordinary language merges. A population of $N$ independent multiplicative trajectories, merely averaged, tracks the expectation value only for a time of order $\ln N$ and then collapses onto the time-average rate. A pool of $N$ members that re-shares every period grows at $\mu - \sigma^2/2N$ for ever. The expectation value is therefore the growth path of no population at all; it is the limit of an institution — a pool with a redistribution rule, made infinitely large and perfectly decorrelated. Membership is not pooling. The rule is the institution.**

## The two results

- **Membership without sharing** (Peters and Klein 2013, *Phys. Rev. Lett.* 110: 100603, arXiv:1209.4517). For the partial ensemble average $\langle x(t)\rangle_N$ of $N$ geometric Brownian motions, the long-time growth rate is $\mu - \sigma^2/2$ for every finite $N$: the time limit and the ensemble limit do not commute. The finite average stays near $e^{\mu t}$ only for a characteristic time $\tau \sim \ln N$ (their fit and their eq. 19; after Redner 1990, holding ensemble behaviour for time $\tau$ requires $N \sim e^{\tau}$), and its early growth is linearly unstable, so it is eventually dominated by time-average behaviour whatever $N$.
- **Membership with sharing** (Peters and Adamou, "An Evolutionary Advantage of Cooperation," arXiv:1506.03414, rev. 2018). Members grow, pool and split equally each period. The pooled share is itself a geometric Brownian motion with amplitude $\sigma/\sqrt{N}$, and its time-average growth rate is $\mu - \sigma^2/2N$ — permanently, not transiently. The cooperators' gain over loners is $\tfrac{\sigma^2}{2}(1 - 1/N)$.

The difference between the two is not $N$. It is the periodic redistribution, which resets the dispersion before the extremes can take over the average.

## What the gap is

The volatility drag $\sigma^2/2$ — the distance between the logarithm of the mean and the mean of the logarithm, the [[Jensen gap]] of the multiplicative process — is growth an unpooled trajectory forgoes. Sharing recovers it at the rate $1/N$. Correlation sets a floor: with pairwise correlation $\rho$ the pooled variance is $\sigma^2[\rho + (1-\rho)/N]$, so even an infinite pool keeps a drag of $\rho\sigma^2/2$ ([[Pooling's sign is set by the correlation of its baskets]], [[Extending a pool along kin proximity buys N without buying decorrelation]]). The expectation value is reached only at $N \to \infty$ *and* $\rho = 0$.

This gives the logarithm a reading alongside Peters's dynamic one. Dynamically, the log is the transform under which multiplicative increments become stationary, so that time and ensemble averages of it coincide. Institutionally, the gap between the log and the expectation is the price of solitude, and a pool is the apparatus that buys it back — at a rate set by its size and a ceiling set by its correlation.

## Consequences for the vault

- It sharpens [[The ensemble average is the local descriptor of a barrier-shielded agent]]. That note has the ensemble average become *locally true* once institutions absorb the barrier. This one names the condition precisely: the institution must re-share, not merely aggregate. A census, a diaspora or a market of independent venturers is an ensemble; it is not a pool.
- It gives the census a coding distinction it should carry: whether a form **redistributes on a schedule** (the *kō* draw, the annual division of a *qirāḍ* or *commenda* fund, general average at each voyage's end) or merely **aggregates exposures** without a sharing rule. Only the first earns the $\sigma^2/2N$ result [check against the HistorEE_codebooks schema].
- It corrects a loose sentence in [[Practice answers the problem as posed and the proof says which problem that was]]: the ensemble average is the limit of *re-sharing* pools, not of pools in general.

## Open question for Peters

Does he treat the partial ensemble average without sharing and the pool with sharing as different *institutional* objects, or only as different calculations? The cooperation paper's protocol is the institution; the 2013 paper's estimator is the population. The historical programme needs the distinction stated, and it should be checked whether his lecture notes already state it [verify].

## Links

- [[The ensemble average is the local descriptor of a barrier-shielded agent]]
- [[Pooling's sign is set by the correlation of its baskets]]
- [[Extending a pool along kin proximity buys N without buying decorrelation]]
- [[Practice answers the problem as posed and the proof says which problem that was]]
- [[Cooperation is an averaging puzzle and sovereign repayment is a barrier puzzle]]
- [[Pooling approaches the infinite ensemble and perpetual succession the infinite horizon]]
- [[Jensen gap]]
- [[Time-average]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - HistorEE]]

## Source

Honeycomb-theorem session, 31 October 2026, follow-up. MS asked whether Peters would be aware of the ensemble-as-pooling-limit reading and what the log transform means in reality. Both papers read from arXiv; the $\tau \sim \ln N$ scaling is Peters and Klein's fit and approximation, not an exact law.
