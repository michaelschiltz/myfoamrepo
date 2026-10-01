---
title: Antifragility is defined by an ensemble Jensen gap
type: permanent
tags: [jensen-inequality, convexity, ensemble-average, time-average, multiplicative-dynamics, absorbing-barrier]
project: HistorEE
source-session: taleb-antifragile-reading
created: 2026-10-01
status: seed
---

# Antifragility is defined by an ensemble Jensen gap

**Taleb defines antifragility as a positive convexity bias, $\mathbb{E}[f(x)] - f(\mathbb{E}[x]) > 0$, and that is an ensemble quantity. Under multiplicative dynamics the same volatility opens a negative Jensen gap on the logarithm. A position can therefore be antifragile by his definition and still decay along every typical trajectory.**

The definition is in the glossary entry "Philosopher's Stone, also called Convexity Bias", and Book V develops it. The convexity bias is an expectation taken across outcomes. The wedge between the time average and the ensemble average is the same inequality applied to a different function: $\mathbb{E}[\ln(1+r)] \approx \mathbb{E}[r] - \tfrac{1}{2}\sigma^{2}$, the concave case of [[Jensen supplies the gap but only the dynamic privileges the logarithm]]. **Which function Jensen's inequality is applied to decides the sign of volatility's effect.** Taleb applies it to the payoff. A multiplicative dynamic fixes it on the log of the growth factor.

**The counter-case.** Buy an option at its fair price every period. The payoff is convex, and the convexity bias is positive, in every period. The expected edge is zero, so the time-average growth rate is strictly negative: the position adds variance to a multiplicative trajectory without adding drift. It is antifragile in the ensemble and fragile in time.

**What rescues the barbell.** Not convexity, but two properties the main text never names:

- **A capped loss per period** (the 90 percent leg), which keeps the trajectory off the barrier.
- **The fraction placed in the convex leg**, which decides whether the time-average growth rate is positive. That is a Kelly question, and the book raises Kelly only in a note to Appendix II.

**"Time is volatility"** (ch. 25). Under geometric Brownian motion this is exact: the variance of log wealth grows as $\sigma^{2}t$. But time pushes the two averages in opposite directions. It inflates the ensemble's convexity bias and accumulates the drag $\tfrac{1}{2}\sigma^{2}t$ on the trajectory. The slogan is true of both and decides between neither.

## The book against itself

Ch. 11 ("On the Irreversibility of Broken Packages") argues in terms of the trajectory. Survival comes before return, what counts is effective rather than nominal speed, and a strategy carrying a risk of terminal blowup has "totally inconsequential" potential returns. Book V and the glossary define the book's central property in expectation instead. The 2012 text never reconciles the two. The explicit ergodicity vocabulary arrives only with *Skin in the Game* (2018) [verify]. Loci at [[Taleb 2012 on antifragility - loci for the time-ensemble distinction]].

## Rule for the vault

Borrow ch. 11. Do not use "antifragile" or "convexity bias" as if they were time-average concepts. Where the point is volatility's effect on a compounding trajectory, write the log Jensen gap and leave Taleb's term out. This is the rule from "On citing him" in [[Taleb reads survival as evidence about the survivor and we read it as evidence about the filter]] applied to his central term: use his vocabulary where it is clearest, and always attach the formal referent.

## Links

- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - HistorEE]]
- [[Jensen supplies the gap but only the dynamic privileges the logarithm]]
- [[Jensen gap]]
- [[Nothing in the ergodic theorem fails in geometric Brownian motion]]
- [[Absorbing barrier]]
- [[Time-average]]
- [[Taleb 2012 on antifragility - loci for the time-ensemble distinction]]
- [[Taleb reads survival as evidence about the survivor and we read it as evidence about the filter]]

## Source

Taleb *Antifragile* session, 1 October 2026. MS read the book as close to time-average rationality. The reading holds for ch. 11 and fails for the book's defining property.
