---
title: Toda's own example makes EE more falsifiable than expected utility
type: permanent
tags: [ergodicity, expected-utility, ergodic-hygiene, time-average, multiplicative-dynamics, historiography]
project: HistorEE
source-session: toda-critique
created: 2026-09-02
status: seed
---

# Toda's own example makes EE more falsifiable than expected utility

[[Toda 2023 on ergodicity economics as pseudoscience]] argues from Popper that ergodicity economics is not falsifiable. On the single worked example the author selects, the comparison runs the other way, and he states the reason himself in a parenthesis.

## The two predictions

Merton's portfolio problem, in Toda's own §III. Risky asset following geometric Brownian motion with drift $\mu$ and volatility $\sigma$, safe asset at $r$, fraction $\theta$ held in the risky asset.

$$\text{EE:}\quad \theta^{*} = \frac{\mu-r}{\sigma^{2}} \qquad\qquad \text{EUT (CRRA }\gamma\text{):}\quad \theta^{*} = \frac{\mu-r}{\gamma\sigma^{2}}$$

Toda then writes that EE is testable because we can gather data on $\mu$, $r$, $\sigma$ and check whether investors hold $(\mu-r)/\sigma^2$; and that EUT is testable by checking whether the chosen portfolio is proportional to $(\mu-r)/\sigma^2$ — **"only proportional, because the relative risk aversion coefficient is not directly observable."**

That parenthesis concedes the argument.

## Why it concedes it

**EE issues a point prediction.** Given $\mu$, $r$ and $\sigma$, the theory names a number. Every other $\theta$ is prohibited, and a single well-measured portfolio falsifies it.

**EUT issues a prediction up to a free positive constant.** $\gamma$ is not observable and is fitted after the fact. The theory therefore prohibits *no* level of $\theta$ whatever — any observed holding is rationalised by the $\gamma$ that produces it — and constrains only the comparative statics.

Popper's criterion, which Toda invokes in his first paragraph, ranks theories by the severity of what they forbid. On that criterion EE is here strictly the more falsifiable of the two, and by a wide margin: one prohibits a continuum minus a point, the other prohibits nothing about the level. **A paper titled "'Ergodicity Economics' is Pseudoscience," arguing from Popper, contains a demonstration that on its own chosen example the accused theory is the more scientific.**

This is not a debating point extracted against the grain of the text. It is the text: Toda sets up the comparison, derives both objective functions, and notes the observability asymmetry in the sentence immediately following.

## The reply available to him, and its cost

A defender would say that $\gamma$ is measurable from independent choice experiments, so EUT's prediction is closed by outside data rather than fitted.

Two costs. First, the measured $\gamma$ is notoriously unstable across elicitation methods and populations — the very literature that Doctor, Wakker and Wang cite approvingly on interpersonal variation, l'Haridon and Vieider's thirty-country study, is a catalogue of that dispersion. A parameter that varies by person, task and instrument is not an outside constant closing the prediction; it is a degree of freedom relocated. Second, and more damaging, the reply concedes the structure of the criticism: EUT requires an auxiliary measurement that EE does not, because in EE the transformation is fixed by the dynamics rather than elicited from the subject. That is the claim at [[Jensen supplies the gap but only the dynamic privileges the logarithm]], arriving from the direction of falsifiability rather than parsimony.

## The scope of the point

Narrow, and it must be stated narrowly. This does **not** show that EE is well corroborated, that its prediction is empirically successful, or that the programme is productive — the portfolio prediction may simply be false, and Toda's real complaint is about domain and progress, which is [[The unfalsifiability charge is really a scope-and-productivity charge]]. It shows only that the demarcation argument, as constructed, fails against the example constructed to carry it.

Used in print: one paragraph, no triumph, and immediately followed by the concession about scope. The observation is strong enough that decorating it would weaken it.

## Links

- [[Toda 2023 on ergodicity economics as pseudoscience]]
- [[The unfalsifiability charge is really a scope-and-productivity charge]]
- [[The selective claim is falsifiable where the prescriptive claim is not]]
- [[Jensen supplies the gap but only the dynamic privileges the logarithm]]
- [[Defending expected utility by axiomatics forfeits its normative claim]]
- [[The Wakker counterexample refutes expected log utility too]]
- [[Nothing in the ergodic theorem fails in geometric Brownian motion]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Toda session, September 2026. The two optimal portfolios were re-derived rather than copied: both objective functions are concave quadratics in $\theta$, and differentiating gives $(\mu-r) - \sigma^2\theta = 0$ and $(\mu-r) - \gamma\sigma^2\theta = 0$ respectively. Toda's algebra is correct and the second solution is Merton's of 1969.
