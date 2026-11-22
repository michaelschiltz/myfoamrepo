---
title: The Copenhagen experiment - Meder et al 2021 and its pre-registered successor
type: source
tags: [ergodicity, time-average, expected-utility, multiplicative-dynamics]
project: HistorEE
source-session: swarm-epigraph-and-lab-evidence
created: 2026-10-25
status: seed
---

# The Copenhagen experiment - Meder et al 2021 and its pre-registered successor

Source note. **"Copenhagen" is Oliver Hulme's group at the Danish Research Centre for Magnetic Resonance** (Copenhagen University Hospital Hvidovre), and what it manipulates is the *dynamic*. It is not the Brussels experiment, which belongs to a different group, manipulates time pressure, and makes a different claim: see [[The Brussels experiment - Vanhoyweghen et al 2022 and its sequels]], and the side-by-side table at [[The laboratory tests the choice and the archive tests the pool]]. Peters presents Copenhagen often but is not an author of the 2021 paper; he and Connaughton are authors of its successor.

## The paper

Meder, David, Finn Rabe, Tobias Morville, Kristoffer H. Madsen, Magnus T. Koudahl, Ray J. Dolan, Hartwig R. Siebner and Oliver J. Hulme. 2021. "Ergodicity-Breaking Reveals Time Optimal Decision Making in Humans." *PLoS Computational Biology* 17 (9): e1009217. DOI `10.1371/journal.pcbi.1009217`. Zotero `JE86VR89`. Preprint arXiv 1906.04652 (2019) — **the version Doctor, Wakker and Wang attacked**, not the published one. Data, code and codebook on GitHub at `ollie-hulme/ergodicity-breaking-choice-experiment`.

## Design

- **The manipulated variable is the dynamic, within subject.** Each subject plays on two days: one under additive dynamics (gambles add or subtract fixed sums), one under multiplicative dynamics (gambles multiply wealth by factors). There is no time-pressure arm.
- **Small sample.** Eighteen subjects, per LML's report on the preprint [verify against the published methods]. The additive day came first for everyone [verify], so day order is confounded with dynamic.
- **Wealth is consequential and updated.** Each day opens with a passive session in which subjects watch their in-game wealth move under that day's dynamic, followed by an active session of choices between gamble pairs whose outcomes accrue to that wealth [verify the payout rule].
- **The measure is a fitted curvature.** An isoelastic utility with parameter η is fitted per subject per day. Time optimality predicts η = 0 under additive and η = 1 under multiplicative dynamics.

## Result

Risk aversion rises under multiplicative dynamics, and the fitted η cluster near the predicted values; the 2019 CCN proceedings give posterior estimates of about 0.15 additive and 1.15 multiplicative [verify the published figures]. **The testable claim is the shift between dynamics, not any subject's level** — see [[Prospect theory's parameters are neither population constants nor individual traits]].

## Critique

- **Doctor, Wakker and Wang, SI Appendix** (against the preprint): expected utility and prospect theory applied statically to a dynamic task; probability weighting omitted; ambiguity aversion confounds the treatment difference. Whether the 2021 version answers these is unchecked [verify]. See [[Doctor Wakker and Wang 2020 on the ergodicity problem]].
- **Ford and Kay, Appendix B**: myopic EUT and external wealth ignored; and the internal objection that, since laboratory money leaves into a multiplicative world, the framework's own logic should predict η = 1 on the additive day too (they write ρ). See [[Ford and Kay 2023 on growth-optimal decision making]].
- **The objection that matters most here.** An η near 1 under multiplicative dynamics *is* expected log utility conditioned on the dynamic, which an expected-utility theorist absorbs by letting curvature depend on the environment. No individual-choice design escapes this; the argument for where the escape lies is at [[The laboratory tests the choice and the archive tests the pool]].

## The successor

Skjold, Benjamin, Simon R. Steinkamp, Colm Connaughton, Oliver J. Hulme and Ole Peters. 2026. "Ergodicity Transformations Predict Human Decision-Making under Risk." *PLOS Computational Biology* 22 (7). DOI `10.1371/journal.pcbi.1014409`.

Published 20 July 2026 (received 23 September 2025, accepted 4 June 2026). Read in full 2026-11-22, Zotero `PU7HERA8` (citekey `skjoldErgodicityTransformationsPredict2026`); data and code at osf.io/mwe7k.

- **Registered report.** Pre-registered on OSF before data collection as "Are Risk Preferences Optimal?" (doi:10.31219/osf.io/ew2sx, 2023) — so the *To acquire* item at [[Ford and Kay 2023 on growth-optimal decision making]] is this paper's protocol. Stopping rule: Bayes factor above 10, minimum 50, maximum 150 participants.
- **Sample.** 68 recruited, 10 excluded (2 inclusion criteria, 8 below 80% on the no-brainer task), 58 analysed, aged 18–48.
- **Design.** Within participant, additive and multiplicative sessions; order randomised per participant (formal counterbalancing not described); break of more than 10 minutes between sessions. Wealth updated on every learning and decision trial; payment DKK 500 plus DKK 0–5,000 proportional to final in-game wealth. This removes Meder's day-order confound.
- **Hypotheses.** (1) the ergodicity model predicts the quantitative values; (2) weak form: η higher under multiplicative than additive dynamics. Rival: expected utility with a fixed individual utility function.
- **Sample restrictions.** Copenhagen residents aged 18–50; excluded anyone trained in psychology, finance, accounting, mathematics, physics, engineering or computer science (4). Gambles are 50/50 coin tosses between image outcomes, chosen to remove probability weighting and any preference for or against gambling (7); state-wise dominated pairs removed, 126 pairs per condition, 160 decision trials (8). Wealth-control mechanisms keep wealth in an informative range (Appendix B), and trials that could produce negative wealth are dropped (10).
- **Results** (partial pooling, the pre-registered primary analysis). Group η: multiplicative mode 1.062, 95% BCI [0.655, 1.463]; additive mode 0.0987, BCI [−0.0752, 0.2710], so 0 lies inside the interval (17). Weak form against fixed-utility EUT: one-sided Bayesian paired t-test BF > 1.707 × 10^43, effect size ξ = 5.982 [4.795, 7.051]; all 58 participants show higher η under multiplicative dynamics (12–13); hierarchical mixture BF = 6.982 × 10^111. Quantitative form, distance to (0, 1) against distance to the diagonal: BF > 1.999 × 10^36 (exponent read from garbled text), ξ = 3.960 [3.146, 4.689]; mixture BF = 4.014 × 10^121, PXP_EE ≈ 0.999 (14). Group Bayes factors extreme in all three datasets; PXP 0.999 (this study), 0.982 (pilot), 0.986 (Meder data), the Meder participants biased towards more risk aversion than predicted (15–16). Confound regressions (luck, terminal wealth, variances) all BF_incl < 0.115; effect present in both halves of the decision phase (13).
- **Traits survive.** η across conditions correlates, ρ = 0.440 [0.210, 0.626], BF ≈ 139: trait-like differences persist once the dynamic is accounted for, but the dynamic is the dominant source of variation (15, 17–18). The paper says "both dynamics and traits are necessary components."
- **What it answers and what it does not.** It cites Doctor, Wakker and Wang (ref. 16) and Ford and Kay (ref. 17) and answers their *design* points: wealth now visible and updated every trial, all choices consequential, learning trajectories no longer bounded, matched demands, parameter recovery shown (3, 17). It does not answer the *theoretical* objections. Its EUT model is "a specific interpretation of expected utility theory, which we adopt" — stable curvature across environments (2) — so environment-dependent curvature, Ford and Kay's point that lab money leaves into a multiplicative world, and prospect theory are not tested against. Authors' own limits: short timeframe, no real losses, wealth controls; additive offset unexplained (also in Meder); dynamics other than additive and multiplicative untested; lab-to-world generalisation argued from plausibility (10, 17–18). (Correction: the 2026-11-22 morning entry, from the article web page, said Doctor–Wakker–Wang and Ford–Kay were not mentioned; they are, as refs 16–17.)

**Cited in Part 1 §1 beside Meder et al. 2021 (2026-11-22).**

## Links

- [[The Brussels experiment - Vanhoyweghen et al 2022 and its sequels]]
- [[The laboratory tests the choice and the archive tests the pool]]
- [[Ford and Kay 2023 on growth-optimal decision making]]
- [[Doctor Wakker and Wang 2020 on the ergodicity problem]]
- [[Prospect theory's parameters are neither population constants nor individual traits]]
- [[Jensen supplies the gap but only the dynamic privileges the logarithm]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - HistorEE]]

## Source

Session of 2026-10-25 on the *Meditations* 6.54 epigraph and the experimental evidence. Bibliographic data from Zotero `JE86VR89`, PLOS, the 2019 CCN proceedings and LML's August 2019 report; the successor from its RePEc listing.
