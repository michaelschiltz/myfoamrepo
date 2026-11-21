---
title: Among isoelastic transforms only the logarithm has no boundary
type: permanent
tags: [expected-utility, multiplicative-dynamics, absorbing-barrier, ergodicity, ergodic-hygiene]
project: HistorEE
source-session: rsta-2334-theme-issue
created: 2026-11-21
status: seed
---

# Among isoelastic transforms only the logarithm has no boundary

Peters and Adamou require the transformed process to be Brownian motion with drift. For the isoelastic transform $u(x) = (x^{1-\eta} - 1)/(1-\eta)$ with $\eta \neq 0, 1$, the range of $u$ on positive wealth is a half-line (their footnote 1, p. 11), and Brownian motion on a half-line reaches its end with positive probability.

- **For $0 < \eta < 1$** (Cramer's square root included) the range is bounded below: reaching the bound means wealth hits zero.
- **For $\eta > 1$** the range is bounded above: reaching the bound means wealth diverges in finite time.
- **For $\eta = 0$** (linear, on all of $\mathbb{R}$) and **$\eta = 1$** (logarithm, on positive wealth) the range is the whole real line, and the correspondence holds without any boundary.

The paper's instruction that "ranges must be adjusted appropriately" does not resolve this, and its §6 repair is an ensemble operation — [[Conditioning on survival is an ensemble operation]]. The general condition is that $u$ maps the wealth domain onto all of $\mathbb{R}$; within the isoelastic family only linear and log satisfy it.

## Why it matters

The vault holds that the logarithm's privilege comes from the dynamic and not from the theory of means — [[Jensen supplies the gap but only the dynamic privileges the logarithm]]. This adds a structural reason the paper does not state: **among concave isoelastic transforms, the logarithm is the only one whose growth-optimal dynamic is defined everywhere without a barrier.** Bernoulli's choice is not one member of a family on equal terms; it is the one member that needs no boundary treatment. That is the precise sense in which a historian may say the logarithm is special, and it is a better sentence than any appeal to its history.

## Links

- [[Peters and Adamou 2026 on the time interpretation of expected utility theory]]
- [[Jensen supplies the gap but only the dynamic privileges the logarithm]]
- [[Route Kolmogorov to ergodic theory not the theory of means]]
- [[The utility mapping fails exactly where absorption begins]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Session of 2026-11-20, on Peters and Adamou 2026, eq. 4.10 and footnote 1.
