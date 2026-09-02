---
title: The growth-rate criterion is asymptotic and the horizon comparison cuts both ways
type: permanent
tags: [ergodicity, ergodic-hygiene, time-average, multiplicative-dynamics, expected-utility]
project: HistorEE
source-session: dww-critique
created: 2026-09-02
status: seed
---

# The growth-rate criterion is asymptotic and the horizon comparison cuts both ways

A concession the vault owes, and has not yet made explicitly.

The time-average growth rate is justified by the ergodic theorem *in the limit*. Birkhoff delivers almost-sure convergence of $\frac{1}{T}\sum_t \log r_t$ as $T \to \infty$; nothing in the theorem says the limit is the right criterion at $T = 3$. The counterexample in [[Doctor Wakker and Wang 2020 on the ergodicity problem]] is built to exploit exactly this, and the construction announces it: the authors observe that for any starting wealth and any *finite* number of rounds they can produce a case as extreme as desired by choosing the disaster probability $10^{-m}$ and the disaster factor $10^{-n}$ with $n$ far exceeding $m$. The example works because an event of probability $10^{-m}$ contributes $-n$ to the log average while contributing almost nothing to what happens over three rounds. Let $T$ grow past the recurrence time of that event and B becomes the catastrophe the growth rate says it is.

**So the criterion fails when the horizon is short relative to the recurrence time of the process's rare events.** That is a real boundary condition and should be stated as one rather than defended around.

## The objection is fifty years old and already conceded elsewhere

This is not a new result. Merton and Samuelson made the same point against the Kelly criterion in 1974, and the library holds it. [[Nothing in the ergodic theorem fails in geometric Brownian motion]] already concedes the Kelly–Latané–Breiman priority on the growth-rate result; consistency requires conceding the standard objection to it in the same breath. Presenting the criterion without the finite-horizon caveat and then meeting this example in a referee report is the avoidable version of the exchange.

## Why the concession costs less than it appears

Because the same comparison, run in the other direction, is already the vault's own instrument.

[[Distinguish strong from weak ergodicity breaking]] holds that weak breaking is a divergence of timescales — the horizon over which ensemble equivalence would be recovered vastly exceeds the horizon any historical agent occupies, so finite-time averages never reach ensemble values. The Wakker example is the mirror image: a horizon so short that the *asymptotic* average never reaches the finite-time outcome. Both are statements about the same quantity, the ratio of the relevant horizon to the relevant relaxation time, and the framework that makes the first argument is committed to accepting the second.

That symmetry is worth stating in print rather than conceding under pressure. It converts an apparent inconsistency into a single discipline: **name the horizon, name the relaxation time, and use whichever criterion the comparison licenses.** [[A significant persistence coefficient is evidence against its own licensing condition]] is the same inequality doing work against the persistence designs; there is no reason to hold it only when it is convenient.

## The historical cases sit on the right side

The project's material — merchant houses, lineages, credit relationships, polities — involves horizons long relative to the recurrence of the perils in question. Ships were lost routinely, not once in $10^{-4}$ of voyages; sovereign payment stops recurred twice in one reign. The regime where the growth-rate criterion applies is the regime the sources describe. That is a defence of scope, and it should be made as one rather than by disputing the mathematics.

## Links

- [[Doctor Wakker and Wang 2020 on the ergodicity problem]]
- [[The Wakker counterexample refutes expected log utility too]]
- [[Distinguish strong from weak ergodicity breaking]]
- [[Nothing in the ergodic theorem fails in geometric Brownian motion]]
- [[A significant persistence coefficient is evidence against its own licensing condition]]
- [[A single throw of dice cannot be evaluated by its expectation]]
- [[Time-average]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

DWW session, September 2026 — the concession half of the reply, written alongside the rebuttal so the two are filed together.

## A tension to resolve before print

[[A single throw of dice cannot be evaluated by its expectation]] argues *against* evaluating the Armada by its expectation precisely because it was a single throw — a short horizon. This note concedes that short horizons are where the growth-rate criterion loses its warrant. **The two are compatible only because the Armada argument runs on exposure and non-replenishment of the stake rather than on the asymptotic growth rate**, but the compatibility is not currently stated in either note and a referee reading both together would press it. Resolve explicitly [verify].
