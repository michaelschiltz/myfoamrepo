---
title: A fair wager lowers both trajectories which maysir forbids and skin in the game permits
type: permanent
tags: [maysir, riba, multiplicative-dynamics, time-average, ensemble-average, skin-in-the-game]
project: HistorEE
source-session: taleb-antifragile-reading
created: 2026-10-01
status: seed
---

# A fair wager lowers both trajectories which maysir forbids and skin in the game permits

**A fair wager is zero-sum in expectation and negative-sum in time average for both parties. *Maysir* forbids it. Taleb's skin-in-the-game criterion cannot, because a fair wager is perfectly symmetric in exposure. On this case the time-average criterion sides with the jurists; on speculation with an edge, it sides with Taleb against them.**

## The arithmetic

Two parties with wealth $W_1$ and $W_2$ each stake $s$ on a fair coin. For either party, $\mathbb{E}[\Delta W_i] = 0$, and

$$\mathbb{E}[\Delta \ln W_i] = \tfrac{1}{2}\ln\!\left(1+\tfrac{s}{W_i}\right) + \tfrac{1}{2}\ln\!\left(1-\tfrac{s}{W_i}\right) = \tfrac{1}{2}\ln\!\left(1-\tfrac{s^{2}}{W_i^{2}}\right) < 0 .$$

Both parties lose growth rate, and the poorer loses more. This mirrors Peters and Adamou's insurance result, where a contract that is zero-sum or negative-sum in expectation is positive-sum in time average for both sides. Priority on the fair-gamble result goes to Whitworth (1870), per [[Galton-Watson is the extinction branch Peters named and did not develop]] [verify].

## Three criteria, three verdicts

- **Taleb, skin in the game** (ch. 23, "The Talker's Free Option"). A free option is condemned. A fair wager is permitted, because exposure is symmetric. Speculation with an edge is "mandatory."
- **Time-average growth.** A free option is condemned for whoever bears the downside. A fair wager harms both parties. Speculation with an edge is permitted at the Kelly fraction.
- **Fiqh.** A free option is *riba* and is condemned. A fair wager is *maysir* and is forbidden. Trade with an edge is permitted where the risk is incidental to the exchange and forbidden where the uncertainty is the object of the contract.

## What follows

- **Skin in the game is a criterion of symmetry of exposure.** It is silent on whether the exposure should exist at all, and a fair wager satisfies it perfectly. Taleb's ethics can condemn *riba* and cannot condemn *maysir*.
- **The time-average criterion condemns the fair wager on dynamics alone**: no utility, no psychology, nothing beyond each party's own growth rate. Of the three criteria, it is the only one that agrees with the jurists on *maysir* without borrowing their premise.
- **The fiqh criterion is neither of the other two.** It asks whether uncertainty is the object of the contract ([[Islamic doctrine refuses risk-commodification at step one]]; [[Gharar excludes designed-in unverifiability]]). On that test it forbids the edge bet that the time-average criterion permits.

The three agree on the free option and differ elsewhere, and the pattern of disagreement exposes each criterion's premise. That makes it a test case, not an illustration. State the fiqh side as revealed preference, never as an anticipation of the growth-rate result; the same caution applies in [[Islamic doctrine refuses risk-commodification at step one]].

## Where this is soft

The arithmetic assumes multiplicative wealth dynamics for both parties over the relevant horizon. A party whose stake is negligible against its wealth loses growth only at second order, $\approx -s^{2}/2W^{2}$. So the time-average objection weakens for the rich party in a way the doctrine's objection does not. Whether the stakes the jurists had in view were large relative to the parties' wealth is an empirical question the argument currently skips. That applies to pre-Islamic *maysir* proper, arrow lots over the shares of a slaughtered camel, and to the later games assimilated to it [verify].

## Links

- [[MOC - Islamic contract doctrine]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]
- [[Islamic doctrine refuses risk-commodification at step one]]
- [[Gharar excludes designed-in unverifiability]]
- [[Entitlement by liability versus entitlement by membership]]
- [[Skin in the game]]
- [[Cooperation is an averaging puzzle and sovereign repayment is a barrier puzzle]]
- [[Taleb 2012 on antifragility - loci for the time-ensemble distinction]]

## Source

Taleb *Antifragile* session, 1 October 2026. MS suggested that Taleb's "no optionality at the expense of others" runs parallel to fiqh contract doctrine. It does on *riba*. It breaks on *maysir*, and the break is where the time-average criterion settles the question.
