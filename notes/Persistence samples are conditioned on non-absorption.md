---
title: Persistence samples are conditioned on non-absorption
type: permanent
tags: [absorbing-barrier, survivorship-bias, selection, persistence, space-for-time, ergodicity, historiography]
project: HistorEE
source-session: wp3-persistence-hereditarianism
created: 2026-08-11
status: seed
---

# Persistence samples are conditioned on non-absorption

A candidate formal deliverable for WP3, and the one objection in the neighbourhood that is native to this framework rather than borrowed from the existing critical literature.

## The claim

A persistence design estimates a coefficient on a historical treatment using units observed in the present. Where the treatment has an absorbing outcome — annihilation, dissolution, extinction of the unit or of the population whose behaviour is measured — the estimation sample is by construction the set of units that **did not absorb**. The coefficient is estimated on survivors of the very process whose effect it claims to measure.

This is conditioning on a variable causally downstream of the treatment. It is a collider, not an omitted variable, and it follows that the balance tests these papers routinely report cannot detect it: those tests are run *within* the selected sample and are therefore conditioned on the same collider.

## Two designs with identical structure

In Voigtländer and Voth the sample is towns with a documented medieval Jewish community *and* an interwar one with outcome data — 325 of 1,428. Presence in the 1920s is realised six centuries downstream of the treatment, after expulsion, near-disappearance by 1550 and mercantilist resettlement. Towns where the pogrom was terminal, or where hostility was durable enough to prevent return, drop out. See [[Voigtlander and Voth measured the relaxation time and reported a mixture]].

In Nunn's slave-trade design the ethnic groups present in the modern data are those not extinguished, absorbed or dispersed beyond recognition by the trade. Same conditioning, same direction.

Pairing them is the point. One case reads as a quirk of a particular source; two cases sharing the structure read as a property of the design class.

## Why it is not already in the literature

The standing critiques reach other defects. Conley and Kelly 2025 is a precision critique — inference under spatial noise. Bisin and Moro 2021 is about complier-specific effects. Casey and Klemp 2021 is closest, treating the treatment's own dynamics as an exclusion-restriction violation, but frames it as instrument validity. None of them is about absorption.

Absorbing states and survivorship are already named in the project's formal apparatus alongside ergodic decomposition and relaxation times; this deliverable cashes that item rather than adding to it.

## The expected result, which is the interesting part

The conjecture is *not* that the coefficient is attenuated. Where the treatment raises the absorption hazard **and** raises the outcome among survivors, the sign of the bias depends on how the hazard depends on the latent trait, and is therefore indeterminate without a model of the absorption process.

That indeterminacy is the finding. The coefficient is not merely mismeasured; it is **unsigned** absent a model of absorption, and no persistence design supplies one. This is a strictly stronger conclusion than "the standard errors are wrong", and it is the same species of conclusion as [[Deep-roots variables are symplesiomorphies]] reaches by a different route — that a result may be true, precisely estimated and evidentially empty.

## A second face of the same defect

Where the outcome invoked is itself an absorbing event — deportation, extermination, extinction — the estimand compounds the problem. A conditional mean over a cross-section cannot speak to the tail in which the absorbing event lives, so the design is conditioned on non-absorption at the sample boundary while being interpreted as though it explained absorption at the outcome. The two failures are one failure seen from either end.

## Before claiming novelty

[verify] — the epidemiological literature on competing risks, immortal-time bias and index-event bias very likely contains a partial precedent. This must be surveyed before the claim is made in print; the WP3 position is strengthened, not weakened, by finding a precedent and citing it, and badly damaged by a referee finding it first. The same discipline applied in [[Deep-roots variables are symplesiomorphies]] to the Mace and Pagel citation gap.

## Links

- [[Voigtlander and Voth measured the relaxation time and reported a mixture]]
- [[Fat tails do not require fat-tailed inputs]]
- [[Deep-roots variables are symplesiomorphies]]
- [[The three Kelly critiques establish different nulls]]
- [[Refusals are observations of the filter not inferences from survivors]]
- [[Time-average optimization is a survivorship property not an intention]]
- [[Endogenised absorption has a sign]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Ergodicity is indecomposability not randomness]]
- [[Absorbing barrier]]
- [[MOC - Historiography and method]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - ERC Synergy Grant]]
- [[MOC - HistorEE]]

## Source

WP3 persistence/hereditarianism session, from a close reading of the Voigtländer–Voth sample construction. The generalisation to Nunn came from noticing that the two treatments share an absorbing outcome.
