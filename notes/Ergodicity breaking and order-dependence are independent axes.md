---
title: Ergodicity breaking and order-dependence are independent axes
type: permanent
tags: [ergodicity, ergodic-hygiene, path-dependence, non-commutativity, multiplicative-dynamics, jensen-inequality, time-average, ensemble-average]
project: HistorEE
source-session: static-vs-dynamic-equilibrium
created: 2026-09-02
status: seed
---

# Ergodicity breaking and order-dependence are independent axes

The vault now runs two clusters side by side — the time/ensemble apparatus and the path-dependence apparatus — and a reader will fuse them unless told not to. They are orthogonal, and each direction of the independence has a clean witness.

**Ergodicity breaking without order-dependence.** Take the canonical multiplicative case. Per [[Nothing in the ergodic theorem fails in geometric Brownian motion]] the failure is not in the ergodic theorem but in the commutation of averaging with a non-linear transformation of the state, and the size of the failure is the [[Jensen gap]], $\tfrac{1}{2}\sigma^{2}$. Now observe that both quantities involved are **symmetric functions of the increments**: the realised wealth $\prod_i r_i$ and the realised growth rate $\frac{1}{N}\sum_i \log r_i$ are each invariant under any permutation of the returns. The gap between time and ensemble average is therefore produced by the non-linearity of the observable and by nothing whatever to do with sequence. It cannot be repaired by reordering, and it is not evidence that order matters.

**Order-dependence without any averaging question.** Take two deterministic affine maps, $f_i(x) = a_ix + b_i$, no randomness anywhere. Composition in the two orders differs by $b_2(a_1-1) - b_1(a_2-1)$, per [[Flows make the dynamic affine and affine maps do not commute]]. There is no ensemble, no expectation, no observable to average, and order is decisive. A process can be order-dependent with the ergodicity question not even posed.

## The two-by-two

| | permutation-invariant | order-dependent |
|---|---|---|
| **no time/ensemble gap** | additive i.i.d. increments | deterministic affine composition |
| **gap present** | geometric Brownian motion | absorption; reinforcement |

The cell that matters is the fourth. Absorption sits there because it does both jobs at once: it decomposes the state space, which is ergodicity failure in the strict sense ([[An absorbing barrier breaks ergodicity by construction]]), *and* it makes survival depend on the running minimum, which is order-dependence ([[Terminal wealth is permutation-invariant but survival is not]]). That conjunction is why absorption rather than variance is the strongest card the project holds, and it is a second, independent argument for the preference already recorded in that note.

## The discipline

Do not offer permutation-invariance as a criterion for ergodicity breaking, and do not offer a time/ensemble gap as evidence that sequence mattered. Each is available without the other. Where a historical claim needs both — and the shielding argument does — the two must be established separately, on their own witnesses. This is the same hygiene the vault imposes in [[The word ergodic carries four incompatible senses]] and [[Distinguish strong from weak ergodicity breaking]], extended to the boundary between the two clusters.

## Links

- [[Nothing in the ergodic theorem fails in geometric Brownian motion]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Terminal wealth is permutation-invariant but survival is not]]
- [[Pure multiplicative dynamics are permutation-invariant]]
- [[Flows make the dynamic affine and affine maps do not commute]]
- [[Absorption is a path-dependence mechanism distinct from reinforcement]]
- [[Distinguish strong from weak ergodicity breaking]]
- [[The word ergodic carries four incompatible senses]]
- [[Jensen gap]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Path dependence and sequence]]
- [[MOC - HistorEE]]

## Source

Static-vs-dynamic-equilibrium session, September 2026. Written after the loose formulation "geometric Brownian motion is non-ergodic and permutation-invariant" was checked against [[Nothing in the ergodic theorem fails in geometric Brownian motion]] and found to need the same restatement that note already imposes.
