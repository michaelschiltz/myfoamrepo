---
title: Reinforcement selects an attractor the ensemble average never occupies
type: permanent
tags: [path-dependence, reinforcement, attractor-selection, ensemble-average, ergodicity]
project: HistorEE
source-session: path-dependence-sequence
created: 2026-08-05
status: seed
---

# Reinforcement selects an attractor the ensemble average never occupies

The Pólya urn is the canonical demonstration that an ensemble statistic can describe no realizable history whatever.

An urn holds one red and one blue ball. Draw one at random, return it together with another of the same colour. Let $X_n$ be the red fraction. Then $X_n$ is a martingale,

$$E[X_{n+1} \mid X_n] = X_n$$

bounded and therefore almost surely convergent, with limit $X_\infty \sim \mathrm{Beta}(1,1) = \mathrm{Uniform}[0,1]$.

The ensemble average is $1/2$ at every $n$. No individual history ends at $1/2$; each locks onto its own limit and those limits are spread uniformly across the interval. This is [[Non-ergodicity collapses the likelihood ratio on outcomes]] in its purest form — the expectation is not merely a poor summary of the typical trajectory, it is a value the process does not occupy.

The lock-in mechanism is quantitative. Draw $n$ shifts the fraction by roughly $1/n$: early draws carry enormous leverage, late ones almost none. Since $\sum 1/n^2 < \infty$ the accumulated variance is finite and the fraction settles; since $\sum 1/n$ diverges, no correction is bounded in advance. Early history is therefore never erased, only diluted at a rate too slow to matter.

The general condition, and the one that does the work in historical argument: **increasing returns give the process multiple stable fixed points and the realized path selects one; decreasing returns give a unique fixed point and history washes out.** Path dependence is the multi-attractor case. Ergodicity is the single-attractor case. That dichotomy is the whole of it.

Caution on exchangeability. The Pólya urn is exchangeable, so the probability of a given *count* of red draws is order-independent. What the sequence determines is which basin the process enters, because early draws are a large share of the urn. Anyone treating "path dependent" and "order-of-events matters for the likelihood" as synonyms will get this backwards.

## Links

- [[Non-ergodicity collapses the likelihood ratio on outcomes]]
- [[Absorption is a path-dependence mechanism distinct from reinforcement]]
- [[Arthur's lock-in and capital lock-in are different objects]]
- [[Path dependence requires naming the non-commuting operation]]
- [[Path dependence literature]]
- [[MOC - Path dependence and sequence]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Path-dependence session, August 2026. Result from Arthur, Ermoliev & Kaniovski (1983) and Hill, Lane & Sudderth (1980); see [[Path dependence literature]].
