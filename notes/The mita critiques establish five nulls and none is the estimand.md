---
title: The mita critiques establish five nulls and none is the estimand
type: reference
tags: [persistence, space-for-time, historiography, provenance, selection]
project: HistorEE
source-session: dell-mita-critique
created: 2026-09-09
status: seed
---

# The mita critiques establish five nulls and none is the estimand

The published criticism of Dell (2010) is cited loosely as "the mita has been challenged."
It is at least five distinct attacks on four different objects, they establish different
nulls, and WP3 has to know which one it is standing beside. Built on the model of
[[The three Kelly critiques establish different nulls]].

## 1. The sample and the boundary — Arroyo Abad and Maurer (2025)

The strongest empirical challenge, and the only one that contests the result rather than the
apparatus. Five hundred indigenous settlements across all of modern Peru, covering the
*encomienda* as well as the *mita*, against Dell's southern band.

- Forced labour severely damaged the communities subjected to it, but the damage **largely
  dissipated before independence**; no significant differences in nineteenth- to
  twenty-first-century literacy, land access, road density or luminosity.
- Colonial provincial boundaries were "remarkably unstable," and mapping them onto modern
  districts — Dell's assignment step — may not be possible at the required precision. At
  settlement level they find a scattered mixture of treated and untreated communities rather
  than a discontinuity, hence false positives and false negatives in treatment status.
- They contest the historical evidence for the hacienda and violence mechanisms.
- Their own mechanisms for the dissipation: out-migration, widening indigenous labour-market
  options, and opposition from Spanish settlers excluded from mita labour.

**Null established:** the treatment leaves no ensemble-level trace in modern district
outcomes. Not a null about trajectories — see
[[A refutation that shares the estimand inherits the defect]].

## 2. Inference under spatial noise — Kelly

The mita is one of Kelly's worked cases. Nominal p of 0.001 moves to roughly 0.19 under
spatial-basis regression with a small-cluster correction, and the synthetic-outcome test
fails to reject that the outcome is trend plus spatial noise. Handled in an appendix rather
than the main text.

**Null established:** the coefficient is not distinguishable from spatially correlated noise.
About the estimator.

[verify] These figures come from the UCD working-paper version. The vault's standing
citation for the standard-error critique is Conley and Kelly 2025 in the *JIE*; establish
whether the mita case appears there, and with what numbers, before any of this is cited.

## 3. Formal identification — Keele and Titiunik (2015), and Woods (2026)

Keele and Titiunik name the paper as an application and mark three distances from a formally
identified geographic RD: identification is discussed informally; the score is a
two-dimensional coordinate pair constant for every household in a district rather than
individually georeferenced; and treatment heterogeneity is absorbed into boundary-segment
fixed effects instead of identified at each boundary point. Their general warning about
**compound treatments** applies directly — the catchment boundary also tracked *reducción*
policy, tribute regime, corregimiento administration and terrain.

Woods (2026) surveys geographic-RD abuse and treats Dell as the *good* case — "an explicit,
coercive labor rule that generated a discontinuous change in obligations at a legally defined
boundary" — while recording the historians' standing doubt that such an assignment sustains
a causal reading across a 200-year horizon. Useful mainly as the checklist of what fails in
the bad cases: smooth rather than discontinuous treatment intensity, endogenous boundaries,
discontinuous unobservables at the border, and the infinitely-many-cutoffs problem in two
dimensions.

**Null established:** none. These are repairs to the design, and a better-identified
between-side comparison is still a between-side comparison.

## 4. Functional form — Karakas (2024)

A double machine-learning re-estimation. Keeps the sign; the interval is the point.
Interactive-regression-model estimates run from about −0.13 to −0.91 against Dell's −0.22 to
−0.36, and the homogeneous-effect assumption is rejected outright. A defence of the direction
and not of the magnitude.

**Null established:** the magnitude is not stable across specifications.

## 5. Mechanism — Ragas (2011)

A historian's assessment, and the earliest of the five. Praises the design, then: the
hacienda channel is specific to the southern sierra, whose estates were subsistence-oriented
rather than market-integrating, so "hacienda implies market access" does not travel; and the
Mantaro valley is a dynamic, market-integrated peasant economy **without** haciendas. Absence
of haciendas cannot by itself carry the underdevelopment result.

**Null established:** the proposed channel does not generalise within Peru.

## The extension that functions as a critique

**Carpio and Guerrero (2021)** run Dell's identification strategy on surname counts from the
2011 electoral roll: roughly 47 log points fewer surnames in mita districts, 65 fewer
district-exclusive and 93 fewer area-exclusive, consistent with the historians' 55 to 80 per
cent male depopulation. They present it as corroboration, and formally it is. Read against
the design it measures the absorbing flow the estimation sample is conditioned on, which is
why it appears in
[[The mita boundary separates two components not two points on a trajectory]] as an
independent objection rather than as support for Dell.

## Adjacent, and not about the mita

- **Bisin and Moro (2021), "LATE for History."** Heterogeneous treatment effects, exclusion
  restrictions, spatial autocorrelation. The worked examples are Acemoglu–Johnson–Robinson
  and Nunn; the mita application has to be made rather than cited.
- **Voth (2021), "Persistence — Myth and Mystery."** A defence: persistence is real,
  misattribution and p-hacking are live, and the field should work on mechanisms and on the
  conditions under which effects decay. The friendly-witness statement of what the genre
  still owes. [verify] whether the chapter treats the mita specifically; it was not confirmed
  in this session.

## The standing historiographical objection, uncited

Toledo drew the catchment on prior Inca *mit'a* obligation, altitude, distance to Potosí and
population density. Dell controls elevation and slope and restricts the band; the exogeneity
of the boundary is assumed rather than demonstrated. This circulates in seminar form and was
**not** traced to a published statement in this session [verify] — do not attribute it.

## Links

- [[The mita boundary separates two components not two points on a trajectory]]
- [[A refutation that shares the estimand inherits the defect]]
- [[The three Kelly critiques establish different nulls]]
- [[Persistence samples are conditioned on non-absorption]]
- [[Sort the persistence objections by what they cost the referee]]
- [[MOC - Historiography and method]]
- [[MOC - ERC Synergy Grant]]
- [[MOC - HistorEE]]

## Source

Dell mita critique session, 2026-09-09. Assembled from a web survey rather than from full
texts: only the Arroyo Abad and Maurer abstract, the Kelly appendix table, the Keele and
Titiunik discussion of Dell, the Karakas results section and the Ragas post were read in any
depth, and several were read through summaries rather than in the original. **No item here
should be cited in print before the source is read whole.**

## References

Arroyo Abad, Leticia, and Noel Maurer. 2025. "The Long Shadow of History? The Impact of
Colonial Labor Institutions on Economic Development in Peru." *Journal of Economic Growth*
30 (4): 521–65. https://doi.org/10.1007/s10887-024-09249-9

Carpio, Miguel Ángel, and María Eugenia Guerrero. 2021. "Did the Colonial *mita* Cause a
Population Collapse? What Current Surnames Reveal in Peru." *Journal of Economic History*
81 (4).

Kelly, Morgan. 2019/2024. "The Standard Errors of Persistence." SSRN 3398303; UCD working
paper 2024/17. Published version: Conley and Kelly 2025, *Journal of International
Economics* 153: 104027.

Keele, Luke J., and Rocío Titiunik. 2015. "Geographic Boundaries as Regression
Discontinuities." *Political Analysis* 23 (1): 127–55.

Woods, Dwayne. 2026. "The Devil Is in the Geography: The Persistent Misuse of Geographic
Regression Discontinuity Design in Political Science." *Chinese Political Science Review*.

Karakas, Alper D. 2024. "The Persistent Effects of Peru's Mining MITA: Double Machine
Learning Approach." arXiv:2506.18947.

Ragas, José. 2011. "Mita minera, colonialismo y subdesarrollo en los Andes." Historia Global
Online, 30 January.

Bisin, Alberto, and Andrea Moro. 2021. "LATE for History." In *The Handbook of Historical
Economics*, 269–96. Amsterdam: North-Holland.

Voth, Hans-Joachim. 2021. "Persistence — Myth and Mystery." In *The Handbook of Historical
Economics*. Amsterdam: North-Holland.
