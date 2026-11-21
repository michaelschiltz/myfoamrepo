---
title: More than the sum requires a non-additive aggregation rule
type: permanent
tags: [individuation, jensen-inequality, convexity, multiplicative-dynamics, game-theory]
project: HistorEE
source-session: hive-emergence-sweep
created: 2026-11-08
status: seed
---

# More than the sum requires a non-additive aggregation rule

**Three literatures that do not cite one another give "more than the sum of its parts" a formal content, and the content is the same: the rule by which the parts' fortunes combine into the whole's is not additive. Compounding under multiplicative noise, convex trade-offs between components of fitness, and entangled resource flows each make the whole's growth differ from the average of the parts'. Where payoffs add, the whole is the sum by construction. The break with fixed-game explanation is a matter of algebra, not temperament.**

## The three routes

| Route | Source | Non-additivity |
|---|---|---|
| Pooling under multiplicative growth | Peters and Adamou 2022; Fant et al. 2023 | the time average of a product is not the average of the factors: pooled growth $\mu - \sigma^2/2N$ against $\mu - \sigma^2/2$ alone |
| Germ–soma specialisation | Michod 2006 | group fitness $W = VB$ equals mean cell fitness minus $\mathrm{Cov}(v,b)$; under a convex viability–fecundity trade-off the covariance is negative and the group outgrows its average member |
| Emergent group fitness | Clejan, Congleton and Lerch 2022 | density-proportional resource contributions not shared with outsiders entangle members' outcomes until individual fitness is undefined; group fitness is the dominant eigenvalue, "not a sum or average of the constituent parts" (read in full 2026-11-13) |

Michod 2006, *PNAS* 103: 9113–17 (read in full): specialisation costs each cell and benefits the group, so germ and soma are altruists in the accounting (9115–16). Peters and Adamou 2022, *Phil. Trans. R. Soc. A* 380: 20200425 (read in full): the gain $\tfrac{\sigma^2}{2}(1 - 1/N)$ comes from reduced volatility, not higher drift ([[The expectation value describes a pool that re-shares not a population]]).

## Why the payoff matrix rules it out

A standard payoff is a number added to a running total, independent of the history that preceded it. Under that rule the collective total is the sum of the members' totals, and nothing that happens at the level of the group can fail to be the sum of what happens to its members. Fant et al. 2023, 5, say as much against the public-goods framing. The [[Jensen gap]] is the general name for what additivity deletes: the distance between the transform of the mean and the mean of the transform. Convexity in Michod is a Jensen gap across cells; volatility drag in Peters is a Jensen gap along a trajectory.

## What this licenses and what it does not

It licenses the claim that emergence in the strong sense is invisible to an additive accounting, which is a precise version of the proposal's break with the Olson–North–Greif framing. It does not license treating every non-additive gain as a new individual: the pool in the first row raises each member's rate and creates no unit ([[Pooling raises the rate and individuation draws the boundary]]).

## Revision 2026-11-21 — a fourth route, and the root restated

"Where payoffs add, the whole is the sum by construction" is false as worded. Where a loss is final, pooling lowers each member's chance of ruin from $p$ to $p^N$ while expected wealth is unchanged, even when gains merely add ([[Under absorption pooling raises the probability of ruin to the power of the pool]]; Vanhoyweghen, Verbeken and Ginis 2026). No Jensen gap is involved. The claim survives in a sharper form because the standard payoff has two properties, not one: it is additive *and* history-independent. Compounding breaks the first; an absorbing barrier breaks the second, since a ruined player does not play the next round. Either suffices. The root is therefore that the outcome is not a linear sum of per-period payoffs, and the table gains a fourth row: *pooling under an absorbing barrier | Vanhoyweghen, Verbeken and Ginis 2026; Galton–Watson | the outcome stops at first passage.* The note's title now states only the first half; it is kept for link stability. Hive report, third version, §§5.2, 6.5.

## Links

- [[Endogenous games rewrite the rules but never the player]]
- [[Pooling raises the rate and individuation draws the boundary]]
- [[The expectation value describes a pool that re-shares not a population]]
- [[Jensen gap]]
- [[Antifragility is defined by an ensemble Jensen gap]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]
- [[Under absorption pooling raises the probability of ruin to the power of the pool]]
- [[The absorbing barrier is a second route to the hypothesis not a sharpening of the first]]

## Source

Hive-emergence sweep, 8 November 2026. The three-route synthesis is proposed here; no source draws it.
