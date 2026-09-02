---
title: The Wakker counterexample refutes expected log utility too
type: permanent
tags: [ergodicity, expected-utility, time-average, multiplicative-dynamics, jensen-inequality, ergodic-hygiene]
project: HistorEE
source-session: dww-critique
created: 2026-09-02
status: seed
---

# The Wakker counterexample refutes expected log utility too

The technical heart of [[Doctor Wakker and Wang 2020 on the ergodicity problem]] is a constructed counterexample to the growth-rate criterion. It works. It also destroys the theory it was written to defend, and the authors do not notice.

## The example

Wealth $10{,}000$, three rounds.

**Process A.** Each round, with certainty, wealth is multiplied by $10^{-3}$. Terminal wealth $10^{-5}$ dollars, with probability one.

**Process B.** Each round, with probability $10^{-4}$ wealth is multiplied by $10^{-200{,}000}$; otherwise by $10$. Terminal wealth $10^{7}$ dollars with probability $0.99970$, and essentially zero with probability $0.00030$.

Per-round time-average growth rate, in $\log_{10}$ units: $-3$ for A, and $10^{-4}(-200{,}000) + (1-10^{-4})(1) = -19.0001$ for B. **A has the higher growth rate and B is what anyone would choose.** The criterion returns the wrong answer, exactly as claimed.

## The move they miss

For multiplicative dynamics the time-average growth criterion *is* expected logarithmic utility — this is the identity the vault records at [[Jensen supplies the gap but only the dynamic privileges the logarithm]]. So compute expected log utility of terminal wealth directly:

$$\mathbb{E}[\log_{10} W_3] = -5 \ \text{under A}, \qquad -53.0003 \ \text{under B}$$

**Expected log utility prefers A, by a wide margin.** The counterexample indicts expected utility with a logarithmic utility function precisely as hard as it indicts the growth-rate criterion, because in this setting they are the same object evaluated twice.

What the example therefore establishes is not that time-averaging fails where EU succeeds. It establishes that **any evaluation unbounded below fails on a gamble with a sufficiently deep and sufficiently improbable tail** — which is the old objection to unbounded utility, not a discovery about ergodicity. Accommodating the intuition requires an EU specification with a bounded or otherwise re-curved utility function.

## Why that is fatal to it as a defence

The concession has a price the authors do not pay. Rescuing the intuition inside EU requires *choosing* a utility function with the right curvature — and the freedom to choose is the whole of what makes EU able to rationalise the example. A framework that accommodates any preference by adjusting a free function has not answered a criterion that fixes the function from the dynamics; it has demonstrated the flexibility that made the criticism worth making. §1 and §2 of the same document insist that the utility function is a primitive representing subjective value, which is to say: free. The three sections cannot all be load-bearing at once.

So Example 1 does real damage, but not to the target it was aimed at. It shows that a growth-rate criterion cannot be applied to short-horizon gambles with catastrophic tails, which is the point taken up at [[The growth-rate criterion is asymptotic and the horizon comparison cuts both ways]] and should be conceded there. It does not show that EU is better placed, because at the relevant specification EU makes the identical error.

## What decides the example

Worth noticing what actually drives the intuition that B is obviously right. Process A is **certain ruin**: terminal wealth $10^{-5}$ dollars, no dispersion, no survivors. Process B is near-certain enrichment with a small absorbing tail. The comparison is settled by which process leaves anything alive, which is a barrier consideration and not a curvature consideration — see [[Terminal wealth is permutation-invariant but survival is not]] and [[An absorbing barrier breaks ergodicity by construction]]. The authors' own decisive example turns on the mechanism their critique never names, which is the observation filed at [[The published critique never engages absorption]].

## Links

- [[Doctor Wakker and Wang 2020 on the ergodicity problem]]
- [[The growth-rate criterion is asymptotic and the horizon comparison cuts both ways]]
- [[The published critique never engages absorption]]
- [[Jensen supplies the gap but only the dynamic privileges the logarithm]]
- [[Defending expected utility by axiomatics forfeits its normative claim]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Nothing in the ergodic theorem fails in geometric Brownian motion]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

DWW session, September 2026. Arithmetic recomputed rather than taken from the source: growth rates and the two expected-log-utility values were evaluated directly, including the binomial over three rounds. The authors' own reported probabilities — "exceeding 0.999" and "less than 0.001" — check out at $0.99970$ and $0.00030$.
