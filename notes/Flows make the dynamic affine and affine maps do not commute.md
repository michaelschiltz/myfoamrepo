---
title: Flows make the dynamic affine and affine maps do not commute
type: permanent
tags: [path-dependence, non-commutativity, multiplicative-dynamics]
project: HistorEE
source-session: path-dependence-sequence
created: 2026-08-05
status: seed
---

# Flows make the dynamic affine and affine maps do not commute

Add a withdrawal or a contribution to a multiplicative process and order begins to matter exactly, generically, and for a reason that can be written down in one line.

With flows the period map is affine rather than linear:

$$f_i(x) = a_i x + b_i$$

Composing two such maps in both orders gives

$$f_1(f_2(x)) = a_1a_2x + a_1b_2 + b_1 \qquad f_2(f_1(x)) = a_1a_2x + a_2b_1 + b_2$$

so the commutator is

$$b_2(a_1 - 1) - b_1(a_2 - 1)$$

which vanishes only if $b_1 = b_2 = 0$ — no flows, back to the permutation-invariant case of [[Pure multiplicative dynamics are permutation-invariant]] — or if $a_1 = a_2 = 1$, no growth. Otherwise the operations do not commute and sequence is consequential.

The historical reach is wide, because almost no financial institution is a closed compounding pot. A state servicing debt through a bad decade is not in the position of one that had the identical decade with payments deferred; the returns are the same multiset, the trajectories are not. Standing obligations — debt service, tribute, garrison costs, dividend expectations — are precisely the $b_i$ terms, and any institution carrying them has an order-sensitive history whether or not anyone modelled it that way.

The pension literature knows this as sequence-of-returns risk. Nobody has written it as a theorem because it is too elementary to publish, which means the citation for the historical application will have to be constructed rather than borrowed. See [[Path dependence literature]].

## Links

- [[Pure multiplicative dynamics are permutation-invariant]]
- [[Path dependence requires naming the non-commuting operation]]
- [[Terminal wealth is permutation-invariant but survival is not]]
- [[Path dependence literature]]
- [[MOC - Path dependence and sequence]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Path-dependence session, August 2026.
