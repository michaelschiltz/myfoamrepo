---
title: Conditioning on survival is an ensemble operation
type: permanent
tags: [survivorship-bias, selection, absorbing-barrier, ensemble-average, time-average, ergodicity]
project: HistorEE
source-session: rsta-2334-theme-issue
created: 2026-11-21
status: seed
---

# Conditioning on survival is an ensemble operation

To keep only the trajectories that never hit the boundary is to select from a population of paths, and the result is not a property of any one of them. Both theme-issue papers on absorption make this step without marking it, and the archive makes it for us.

**In Vanhoyweghen, Verbeken and Ginis.** The boundary-adjusted growth rate $g_\theta = (1 - p_\theta)\,g$ (eq. 3.3) is presented as a time-average quantity. Along any single path the long-run growth rate is $g$ if the path survives and zero if it is absorbed; $g_\theta$ is the expectation of that two-point outcome across paths. Their Regime I therefore ranks by expected path-wise growth. In the worked example a surviving path of the inferior venture grows exactly as fast as a surviving path of the superior one.

**In Peters and Adamou §6.** Bounded utilities are handled by retaining the trajectories that never reach the bound (a method-of-images construction), and the paper says the retained paths are genuine Brownian realisations with drift α (p. 11). They are not. Conditioning a process on never hitting a barrier is a Doob $h$-transform and changes its drift. For Brownian motion with drift $\mu > 0$ and volatility $\sigma$, absorbed at zero, the drift conditioned on survival is $\mu \coth(\mu x / \sigma^2)$, which grows like $\sigma^2 / x$ near the barrier.

## The archival consequence

The formula is the selection effect in every merchant archive. Surviving houses that came closest to ruin show the steepest apparent recoveries, because that is what conditioning on survival does to the drift, not because they were better run. Datini, the Geniza merchants and the Mitsui are samples of survivors, and in log wealth the bias has a closed form under the multiplicative null. This is the computational form of [[Persistence samples are conditioned on non-absorption]] and a candidate WP3/WP4 methods deliverable: a survivorship correction applied to the project's own sources before any inference from them.

## What it does not license

It is no argument that survival is uninformative. Survival is a fact about a trajectory and the selective claim stands on it — [[Time-average optimization is a survivorship property not an intention]]. What it forbids is reading the survivors' growth as the growth the institution conferred.

## Links

- [[Vanhoyweghen Verbeken and Ginis 2026 on absorbing boundaries]]
- [[Peters and Adamou 2026 on the time interpretation of expected utility theory]]
- [[Persistence samples are conditioned on non-absorption]]
- [[Taleb reads survival as evidence about the survivor and we read it as evidence about the filter]]
- [[The record of non-survivors survives where failure was administered]]
- [[Time-average optimization is a survivorship property not an intention]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Session of 2026-11-20. The $h$-transform drift is standard (survival probability $1 - e^{-2\mu x/\sigma^2}$, drift $\mu + \sigma^2 h'/h$); not taken from either paper.
