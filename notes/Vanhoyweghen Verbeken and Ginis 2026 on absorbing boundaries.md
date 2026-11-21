---
title: Vanhoyweghen Verbeken and Ginis 2026 on absorbing boundaries
type: source
tags: [absorbing-barrier, time-average, ergodicity, expected-utility, survivorship-bias]
project: HistorEE
source-session: rsta-2334-theme-issue
created: 2026-11-21
status: seed
---

# Vanhoyweghen Verbeken and Ginis 2026 on absorbing boundaries

Source note. The Brussels group's formal paper: the time-average decision framework extended to dynamics with ruin. Never mentions Bernoulli, and is nonetheless the paper in the issue that settles the Bernoulli question for the project.

**Bibliographic facts.** Vanhoyweghen, Arne, Brecht Verbeken, and Vincent Ginis. 2026. "Ergodicity Economics beyond Asymptotics: A Time-Average Decision Framework for Dynamics with Absorbing Boundaries." *Philosophical Transactions of the Royal Society A* 384 (2334): 20250167. DOI `10.1098/rsta.2025.0167`. Zotero `ENRE2FVB`; citekey `vanhoyweghenErgodicityEconomicsAsymptotics2026`. Received 31 October 2025, accepted 12 May 2026. VUB Data Analytics Laboratory; Ginis also Harvard SEAS. Code `10.6084/m9.figshare.32159103`. Read in full from page images.

## What it does

- **Absorbing boundaries break ergodicity even under additive dynamics.** Boundary-adjusted growth $g_\theta = (1 - p_\theta)\,g$ (eq. 3.3), multiplicative analogue $G_\theta = G^{1-p_\theta}$ (eq. 3.7).
- **One-boundary axiom, three regimes.** (I) escape possible: rank by $g_\theta$; (II) absorption certain with finite expected hitting time: rank by $\tau_\theta$; (III) driftless with infinite expected hitting time: rank by finite-horizon hitting probability. Two-boundary axiom: probability of favourable absorption, then absorption time, then finite-time growth at the knife-edge.
- **§6.** Ruin carrying an intrinsic negative value $-M$; as $M \to \infty$ preference becomes lexicographic in ruin probability.
- **pp. 9–10.** Any utility representing the ordering must be antisymmetric about the *initial state*, convex towards an unfavourable boundary, concave towards a favourable one. Examples: arctan, a split power function resembling the Tversky–Kahneman value function with loss aversion set to one, a shifted logistic. Presented as consequences of dynamics, not psychology.
- **The worked example.** Two ventures with equal expected gain and ruin probabilities of 2 and 68 per cent; A ≻ B at $g_\theta$ 0.196 against 0.064.

## What it does for the project

- **It is the formal backing for the single-objective wording** of Part 2 §0 and the reconciliation of Observation 5 with WP3, on condition that the wording is an ordering — [[Under absorption the time-average criterion is an ordering not a maximand]]. Cited at Part 2 §0.
- **It formalises the noise–ruin distinction** on which the Objective 1 prediction against Holmström turns, and is cited at the head of the WP1 epistemics paragraph. The worked example is the shape of that prediction: equal expectation, different exposure to ruin. See [[Institutions substitute state-verification for outcome-inference as ruin exposure rises]].
- **It decides the Bernoulli question by implication.** Because the representation depends on the starting point, the boundary and, in two regimes, the horizon, no fixed utility of wealth reproduces it — [[The utility mapping fails exactly where absorption begins]]. The authors do not draw the inference. Cited at Part 1 §1.

- **It makes the barrier an independent route to the hypothesis.** How far it departs from Peters is set out at [[Peters's growth criterion is the boundary-free case of the first-passage ordering]]; why that matters for the application, and the three text changes it prompted on 2026-11-21, at [[The absorbing barrier is a second route to the hypothesis not a sharpening of the first]].

## What must not be cited from it

- **$g_\theta$ is not a time average.** Each path's asymptotic growth is $g$ or zero; $g_\theta$ is the ensemble expectation of that two-point outcome — [[Conditioning on survival is an ensemble operation]]. Cite the paper for boundary-dependence, never for the formula.
- **The prospect-theory resemblance strips out loss aversion**, the feature that defines prospect theory. Do not repeat "remarkably".

## Links

- [[Peters's growth criterion is the boundary-free case of the first-passage ordering]]
- [[The absorbing barrier is a second route to the hypothesis not a sharpening of the first]]
- [[The 2026 Phil Trans A theme issue on ergodicity breaking]]
- [[Peters and Adamou 2026 on the time interpretation of expected utility theory]]
- [[The Brussels experiment - Vanhoyweghen et al 2022 and its sequels]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Absorption without ergodicity economics is just ruin theory]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Session of 2026-11-20. Project doc `claude/ee-log-utility-bernoulli-reading-note-2026-11-20.md`. Peters reported in October 2026 that he was working with Vanhoyweghen on the log-utility question; whether this paper is that collaboration's output is unconfirmed [verify with Peters].
