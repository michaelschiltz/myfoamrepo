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

Published 20 July 2026 (received 23 September 2025, accepted 4 June 2026). Checked against the article page 2026-11-22; full text not yet in Zotero.

- **Registered report.** Pre-registered on OSF before data collection as "Are Risk Preferences Optimal?" (doi:10.31219/osf.io/ew2sx, 2023) — so the *To acquire* item at [[Ford and Kay 2023 on growth-optimal decision making]] is this paper's protocol. Stopping rule: Bayes factor above 10, minimum 50, maximum 150 participants.
- **Sample.** 68 recruited, 10 excluded (2 inclusion criteria, 8 below 80% on the no-brainer task), 58 analysed, aged 18–48.
- **Design.** Within participant, additive and multiplicative sessions; order randomised per participant (formal counterbalancing not described); break of more than 10 minutes between sessions. Wealth updated on every learning and decision trial; payment DKK 500 plus DKK 0–5,000 proportional to final in-game wealth. This removes Meder's day-order confound.
- **Hypotheses.** (1) the ergodicity model predicts the quantitative values; (2) weak form: η higher under multiplicative than additive dynamics. Rival: expected utility with a fixed individual utility function.
- **Results.** Group-level multiplicative η: mode 1.062, 95% CI [0.655, 1.463]. Additive η "slightly higher" than 0 (value in a figure, not read). All 58 participants show higher η under multiplicative dynamics. Strong evidence for the weak form and extreme evidence for the quantitative form against fixed-utility EUT (Bayes factors in figures, not read). Model comparison across three datasets: PXP for the ergodicity model 0.999 (this study), 0.982 (pilot), 0.986 (Meder et al. data).
- **What it does not do.** No comparison with prospect theory; Ford and Kay and Doctor, Wakker and Wang not addressed on the article page. The environment-dependent-curvature objection above therefore stands. Authors' own limits: short timeframe, no real losses, unexplained additive estimate above 0, lab-to-world generalisation not established, earlier replication supports the qualitative pattern mainly.

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
