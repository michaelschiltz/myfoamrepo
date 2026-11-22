---
title: Connaughton Lamb and Paillusson 2026 on what ergodicity is
type: source
tags: [ergodicity, ergodic-hygiene, space-for-time, persistence]
project: HistorEE
source-session: rsta-2334-theme-issue
created: 2026-11-21
status: seed
---

# Connaughton Lamb and Paillusson 2026 on what ergodicity is

Source note. The theme issue's introduction, co-written by the project's corresponding PI. The citation that lets Objective 3 say "ergodic for the observable at issue" with a co-PI's definition behind it.

**Bibliographic facts.** Connaughton, Colm, Jeroen Lamb, and Fabien Paillusson. 2026. "What Is Ergodicity?" *Philosophical Transactions of the Royal Society A* 384 (2334): 20250153. DOI `10.1098/rsta.2025.0153`. Zotero `JR4YKTPM`; citekey `connaughtonWhatErgodicity2026`. LML, Imperial College London (Lamb, also IRCN Tokyo), University of Lincoln (Paillusson). Keywords: ergodicity, stationarity, infinite ergodic theory, self-averaging. Read in full from page images.

## What it does

- **Poses the ergodicity question as a licensing question.** When may properties of one individual gathered over time be equated with those of a population sampled at one time, in either direction. The answer "it does not always hold" is why the word exists at all.
- **Bridges deterministic dynamical systems and stochastic processes** for the applied papers in the collection.
- **States a hierarchy and makes it operational (p. 14).** Metric indecomposability, equality of distributions for an observable, and equality of averages for an observable form a sequence of successively weaker notions. Indecomposability is close to impossible to establish for a realistic system; equality of distributions or of averages can be tested on finite samples of finite trajectories. For most applications in the issue, equality of averages for specific observables is sufficient, and the interesting questions are which averages are reasonable for which problems and on what assumptions — not whether an invariant measure is ergodic.

## What it does for the project

- **It is the definitional anchor for Objective 3.** Part 2 now reads that which regime obtains is established case by case "for the observable at issue", citing this paper. The persistence critique needs only equality of averages for the coefficient's observable over the design's horizon, the weakest notion, and should claim no more.
- **It aligns the co-PI's published position with the vault's hygiene.** The hierarchy is the formal version of [[Licensing the ensemble is a dynamical question not a metaphysical one]] and of the third, econometric sense at [[The word ergodic carries four incompatible senses]]; the relation between the two classifications is set out there.
- **It strengthens the Synergy section's description of Connaughton.** Part 1 §5 credits him with the apparatus of ergodic decomposition and mixing times; the issue introduction is the published evidence.

## Limits

An introduction, not a result. It supplies vocabulary and a hierarchy, and the test that cashes the hierarchy is Underwood and Paillusson's — [[Underwood and Paillusson 2026 on the ergodicity spectrum]]. The acknowledgements thank Peters and Soysal for comments on the draft.

## Addendum 2026-11-22 — where absorption sits in the paper's framework

Reread in full from page images. The paper names three ways the ergodicity question fails and does not name absorption: "absorbing" never occurs, and Vanhoyweghen, Verbeken and Ginis 2026 appear only in the opening list of contributions, filed under behavioural science (ref. 7, p. 2). Raposo and Pulido (ref. 6), whose subject is additive ruin, are cited in §5 for their transformation of mixed additive–multiplicative increments, not for the ruin (p. 13).

- **§2, decomposition (pp. 3–5).** Several ergodic invariant measures; the time average depends on the initial condition (doubling map). "Every non-ergodic invariant measure is the weighted average of two or more ergodic invariant measures" (p. 4). Kac's lemma ties ergodic measures to recurrence (p. 5).
- **§4, infinite ergodicity (pp. 9–11).** Non-normalisable invariant measure, infinite mean return time, sublinear cumulative sums with a random limit, trajectories keeping order-1 differences forever (simple random walk, $S_N \sim c\sqrt N$; Pomeau–Manneville map with its "sticky" neutral fixed point).
- **§5, non-stationarity (pp. 11–13).** Multiplicative random walk, $\lambda = \mathbb E[\log z] < \mu = \log \mathbb E[z]$ by Jensen; the growth rate is the observable with equality of averages (eq. 5.9); Box–Cox family as the ergodicity transformation (eq. 5.10). The section opens by calling it "arguably misleading" to describe non-stationary processes as "non-ergodic", since ergodicity in §§2–3 is a property of stationary systems (p. 11).

**Absorption mapped onto it (ours, not the paper's).**

1. *Escape possible* (Vanhoyweghen regime I): paths split into an absorbed class, whose time average is the barrier, and an escaped class growing at $g$ — a decomposition in the §2 sense. Vanhoyweghen's $g_\theta = (1-p)g$ is exactly a weighted average of components, with weights $p$ and $1-p$, which confirms that $g_\theta$ is an ensemble quantity ([[Conditioning on survival is an ensemble operation]]). Pooling lowers the weight on the absorbed component from $p$ to $p^N$ ([[Under absorption pooling raises the probability of ruin to the power of the pool]]).
2. *Driftless* (regime III): the §4 random walk with a barrier. First-passage time to the barrier has infinite mean, the same heavy tail that makes the free walk infinitely ergodic.
3. *Absorption certain*: trivially ergodic in the limit, since every path ends at the barrier. The time–ensemble difference exists only over finite horizons, which is where the §6 operational notion applies.

**Consequence for the application.** Both of the project's routes fail ergodicity in the strict §§2–3 sense only loosely: multiplicative growth is non-stationary, absorption ends recurrence. The usage survives in the §6 sense, equality of averages for the observable at issue, which Part 2 already invokes with this citation. Part 1 should not speak of "non-ergodic dynamics" without that anchor where the co-author will read it. For the note to Connaughton and Peters, question (b) is best put in this vocabulary: is absorption a decomposition in the §2 sense, with pooling lowering the weight on the absorbed component?

## Links

- [[The 2026 Phil Trans A theme issue on ergodicity breaking]]
- [[Underwood and Paillusson 2026 on the ergodicity spectrum]]
- [[Soysal 2026 on the ergodicity assumption in climate damages]]
- [[The word ergodic carries four incompatible senses]]
- [[Ergodicity is indecomposability not randomness]]
- [[Licensing the ensemble is a dynamical question not a metaphysical one]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]
- [[Under absorption pooling raises the probability of ruin to the power of the pool]]
- [[Conditioning on survival is an ensemble operation]]
- [[Vanhoyweghen Verbeken and Ginis 2026 on absorbing boundaries]]
- [[The absorbing barrier is a second route to the hypothesis not a sharpening of the first]]

## Source

Session of 2026-11-21, triage of the theme issue.
