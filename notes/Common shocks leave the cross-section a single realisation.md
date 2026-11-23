---
title: Common shocks leave the cross-section a single realisation
type: permanent
tags: [persistence, space-for-time, ergodicity, synchrony]
project: HistorEE
source-session: kelly-2026-mechanisms
created: 2026-11-23
status: seed
---

# Common shocks leave the cross-section a single realisation

Kelly's (2026, §3.1) result on inflated *t*-statistics is a cross-sectional failure of ergodicity, stated without the word. Let *y*ᵢₜ = φ*y*ᵢ,ₜ₋₁ + *b*ᵢ*f*ₜ + εᵢₜ, with a common shock *f*ₜ entering each location through a fixed loading *b*ᵢ. Following Andrews (2005), the OLS slope converges in probability not to φ but to φ + *F*ₜ₋₁*f*ₜ / (*F*²ₜ₋₁ + σ²/(1 − φ²)), a random variable fixed by the realised path of the common shock. Under φ = 0 the *t*-statistic grows as √*N*.

## Why this is the ergodic theorem's failure case

Birkhoff's theorem without ergodicity still delivers convergence, but to a conditional expectation given the invariant σ-field rather than to a constant. Andrews's limit has exactly that form, with the common-shock σ-field in the place of the invariant one. The cross-section is **one realisation** of the common shock however many locations it contains: adding locations adds observations of the loadings, never another draw of *f*. The law of large numbers runs across the wrong index. Spurious significance follows with no spatial trend and no omitted variable.

## Spatial and temporal failures: distinct, sometimes coincident

WP3 distinguishes spatial ergodicity (whether spatial averages over one realisation estimate expectations — the Conley–Kelly standard-error problem) from temporal ergodicity (whether the cross-section stands in for a trajectory — space-for-time). Kelly's two sections show both how they come apart and where they meet.

- **They come apart.** With φ = 0 the process forgets every period, so there is no temporal persistence at all, yet the common shock spoils cross-sectional inference completely.
- **They meet in the VAR.** In §2.1 the eigenvectors of *A* are spatial patterns, and the low-frequency ones are the persistent ones: spatial autocorrelation *is* the persistence of the large-scale modes (Kelly 2026, p. 8). Where persistence comes from slow spatial modes, the modes that leave the cross-section few independent observations are the same modes that relax slowly in time.

So the distinction is real and must be kept, but in the coupled models the persistence literature implicitly assumes, one condition cannot be checked without the other. For Connaughton and Peters, with the item of 16 October 2026.

## Links

- [[Kelly 2026 on the mechanisms of historical persistence]]
- [[The persistence coefficient fails even where the dynamics are ergodic]]
- [[A common shock defeats the pool through its mean loading and the cross-section through its dispersion]]
- [[The three Kelly critiques establish different nulls]]
- [[Ergodicity is indecomposability not randomness]]
- [[Stationarity is a precondition of ergodicity not a corollary]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Session of 2026-11-23. The Birkhoff reading is the vault's; Kelly derives the limit and the divergence of the *t*-statistic but does not name the property.

## References

Andrews, Donald W. K. 2005. "Cross-Section Regression with Common Shocks." *Econometrica* 73 (5): 1551–85. [verify] DOI.

Kelly, Morgan. 2026. "The Mechanisms of Historical Persistence." Working paper.
