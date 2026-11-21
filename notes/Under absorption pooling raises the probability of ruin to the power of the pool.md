---
title: Under absorption pooling raises the probability of ruin to the power of the pool
type: permanent
tags: [absorbing-barrier, risk-sharing, diversification, synchrony, ergodicity, ensemble-average]
project: HistorEE
source-session: pooling-and-ruin
created: 2026-11-21
status: seed
---

# Under absorption pooling raises the probability of ruin to the power of the pool

Peters and Adamou's cooperation result runs on the variance limb: pooling $N$ members with partly independent multiplicative fortunes raises each member's time-average growth rate from $\mu - \sigma^2/2$ towards $\mu$. **There is a second route to cooperation that runs on the ruin limb and needs neither multiplicative dynamics nor a Jensen gap.** Where there is a point of no return, pooling leaves average earnings where they were and multiplies the chance of survival.

## The algebra

Let a member's wealth move additively, with drift $\mu > 0$ and volatility $\sigma$, from a distance $s$ above ruin. The probability that it ever reaches ruin is

$$p = e^{-2\mu s/\sigma^2}.$$

Pool $N$ members with independent perils and share equally. The pool's wealth starts at $Ns$, drifts at $N\mu$ and has variance $N\sigma^2$, so

$$p_{\text{pool}} = e^{-2(N\mu)(Ns)/(N\sigma^2)} = e^{-2N\mu s/\sigma^2} = p^N.$$

Each member is ruined only if the pool is. **His probability of ruin falls from $p$ to $p^N$; his expected gain is unchanged.** Five partners each facing a 40 per cent chance of ruin alone face about 1 per cent together ($0.4^5 \approx 0.010$).

The result is exact for Brownian motion with drift, and holds to the Lundberg approximation for compound losses: pooling $N$ identical independent portfolios leaves the adjustment coefficient unchanged and multiplies the capital by $N$, so the ruin probability is raised to the power $N$.

## The same algebra in Galton–Watson

$k$ independent lineages are all extinct with probability $q^k$. In the continuous limit, Feller's branching diffusion is extinguished from mass $z$ with probability $e^{-2\mu z/\sigma^2}$ — the same form — and starting mass adds across lineages. **Pooling fortunes against ruin and counting lineages against extinction are one operation on one formula**, which is why [[Galton-Watson is the extinction branch Peters named and did not develop]] belongs in the same argument as the cooperation result rather than beside it.

## What this changes in the vault

[[Cooperation is an averaging puzzle and sovereign repayment is a barrier puzzle]] holds that cooperation is an averaging problem "and nothing else". That is true of Peters and Adamou's resolution, and false of cooperation. Under a barrier, cooperation is also a barrier puzzle, and it is resolved by this formula. The vault already had the empirical form of the barrier route — Aktipis and Cronk's herds removed below 64 head ([[Aktipis and Cronk on need-based transfers and herd survival]]), Scott's peasants minimising the chance of disaster ([[Scott 1976 on the subsistence ethic as safety-first]]) — without its algebra.

## What it requires

- **Independence.** With correlated perils the pool's variance does not fall as $1/N$ and $p$ stays near $p$. Read ρ off the variable the institution actually indemnifies — [[Pooling's sign is set by the correlation of its baskets]], [[A perfectly correlated peril leaves only the time average]].
- **Positive drift.** With negative or zero drift ruin is certain and the formula gives no gain; the regimes are set out at [[Pooling pays only where ventures grow on average]].
- **Equal shares.** Unequal stakes change the arithmetic, not the direction.

## What is not new

The formula is classical: Lundberg and Cramér in actuarial ruin theory, Roy's safety-first criterion (1952) in economics, Feller for branching diffusions. [[Absorption without ergodicity economics is just ruin theory]] applies in full. The contribution is the pairing: the variance limb and the ruin limb as two consequences of one act of pooling, with the Galton–Watson process as the case in which the second appears without the first.

## A caution on what $p$ is

$p$ and $p^N$ are probabilities across paths. For the project that is legitimate — the historian's object is a population of houses, partnerships or lineages, and survival is the observable — but it is an ensemble quantity, and it must not be called a time average. See [[Conditioning on survival is an ensemble operation]].

## Links

- [[Galton-Watson is the extinction branch Peters named and did not develop]]
- [[Cooperation is an averaging puzzle and sovereign repayment is a barrier puzzle]]
- [[Vanhoyweghen Verbeken and Ginis 2026 on absorbing boundaries]]
- [[Pooling's sign is set by the correlation of its baskets]]
- [[Pooling pays only where ventures grow on average]]
- [[Diversification runs across bottoms not across partners]]
- [[Perpetual succession redefines the unit of survival from a line to a union of lines]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - HistorEE]]
- [[Polyandry is pooling under an absorbing barrier]]
- [[Individuation moves the absorbing barrier from the member to the unit]]

## Source

Session of 2026-11-21: a question whether the Vanhoyweghen paper opens a connection between Peters's cooperation result and the Galton–Watson process. The paper does not make the connection; its first-passage quantities and three regimes are what make it statable.
