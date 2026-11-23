---
title: Kelly 2026 on the mechanisms of historical persistence
type: source
tags: [persistence, space-for-time, ergodicity, historiography]
project: HistorEE
source-session: kelly-2026-mechanisms
created: 2026-11-23
status: seed
---

# Kelly 2026 on the mechanisms of historical persistence

Source note. Kelly's fourth critique of the persistence literature, and the first to address the estimand rather than the estimator. The word *ergodic* appears nowhere in it; its two formal sections are ergodicity results all the same.

**Bibliographic facts.** Kelly, Morgan. 2026. "The Mechanisms of Historical Persistence." Working paper, 41 pp.; PDF compiled 22 November 2026. Later sections draw on his Tawney Lecture to the Economic History Society conference of 2026, "Historical Economics versus Economic History." Thanks Steven Durlauf; states that the results of §§2.2 and 3.1 were "first derived using AI" (p. 1n). **Status: unrefereed. No venue, series or accepted version located as of 2026-11-23.** Cite as a working paper only, and keep it out of the application until it has appeared somewhere. [verify] series and handle once posted. Not yet in Zotero.

## What it does

- **§2 (pp. 6–9).** A latent spatial VAR, *y*ₜ₊₁ = *c* + *Ay*ₜ + *u*ₜ₊₁ with ρ(*A*) < 1. The cross-sectional slope of *y*ₜ₊ₗ on *y*ₜ is β_L = β_µ + Σₖ ωₖλₖᴸ (eq. 5, p. 8): a steady-state term plus a configuration-weighted average of eigenvalues, weights of either sign. As *L* → ∞ it tends to β_µ, of any size or sign (p. 9). One clean case: *c* = 0 and equal row sums of *A*, where the weights are non-negative and β lies below the spectral radius. Appendix: asymmetric *A*, and a two-way fixed-effects panel whose slope is still a configuration-weighted average of eigenvalues (p. 38).
- **§2.1 (p. 8).** Eigenvectors of *A* are spatial modes; spatial autocorrelation is the persistence of the large-scale ones.
- **§3.1 (pp. 11–12).** A common shock with fixed loadings gives OLS a non-degenerate random probability limit (via Andrews 2005), and *t* grows as √*N* even when the shock is small.
- **§4, Table 1 (p. 13).** Eight canonical results lose significance on an obvious control or specification: Acemoglu–Johnson–Robinson, Alesina–Giuliano–Nunn, Ashraf–Galor, Guiso–Sapienza–Zingales, Nunn, Nunn–Qian, Nunn–Wantchekon, Voigtländer–Voth.
- **§5 (pp. 17–19).** Voigtländer–Voth read century by century; see [[Voigtlander and Voth measured the relaxation time and reported a mixture]].
- **§§5.1–6.** Collingwood's *substantialism*; the denial of agency; no organising structure and no account of what persists and what does not (p. 21); McEvedy–Jones and Murdock as data; errors of historical fact.
- **§7 (p. 28).** The way forward is detailed narrative history, with Rowe's *Crimson Rain* as the model.

## What it does for the project

- **The deep-roots critiques still do not name the property.** Zero occurrences of *ergodic*, *time average*, *ensemble*, *path dependence*, *multiplicative*, *survivor*. Confirms [[The persistence literature names non-ergodicity only in its geography branch]].
- **Eq. 5** is the linear case of the Dell distinction, and shows dynamical ergodicity insufficient: [[The persistence coefficient fails even where the dynamics are ergodic]].
- **Its long-run limit** breaks the vault's timescale inequality: [[A long-horizon persistence coefficient bounds no relaxation time]].
- **§3.1** is cross-sectional non-ergodicity unnamed: [[Common shocks leave the cross-section a single realisation]]. The extension to pooling is the vault's, not Kelly's: [[A common shock defeats the pool through its mean loading and the cross-section through its dispersion]].
- **What the model cannot hold** — multiplicative growth, absorbing states, several basins, survivorship — is Objective 3's ground. Eq. 5 is a usable linear benchmark for WP3's first movement, against which the non-linear cases are measured.
- **The agency passage (p. 20)** — switch to oats and rye or "curl up and die" — reads selection at an absorbing barrier as choice. The vault's position is [[Time-average optimization is a survivorship property not an intention]]; the rhetoric is not to be borrowed.
- **The conclusion abandons the substitution;** the chronosequence precedent Part 2 follows specifies the conditions of its validity instead. Kelly's own clean case is such a condition, which is the best reply to the conclusion on his terms.

## Verification

Eq. 5 and the clean-case bound were reproduced numerically on 2026-11-23 (random symmetric network, *N* = 60, γ = 0.9, δ = 0.5): the formula matches the exact conditional slope at *L* = 1, 5, 50, 500 to four decimals, and the weights sum to 1 − β_µ. Under regular coupling with *c* = 0, β = 0.087 for every initial configuration against ρ(*A*)ᴸ = 0.729 at *L* = 3. Outside the clean case the long-run coefficient ranges from −0.70 to +0.71 across random initial configurations with *c* and *A* fixed. The vault's use of eq. 5 rests on this algebra, not on the paper's standing. §3.1 rests on Andrews (2005) and was not re-derived. The appendix constants (0.37, 0.34) differ from the text's (0.4, 0.3) by rounding only.

## Bibliographic cautions

- Kelly's own bibliography gives Conley and Kelly as 2024, *JIE* 151. CrossRef, checked 2026-11-23: 2025, *JIE* 153: 104027. The vault's form stands; do not copy Kelly's.
- Cites Francis (2026, isitcredible.com) and Guinnane and Hoffman (2022) on the data of Voigtländer and Voth.
- Acharya, Blackwell and Sen, "Historical Persistence," in the *Oxford Handbook of Historical Political Economy*, names the conditions under which persistence occurs as the field's open question — the question Objective 3 answers. Kelly attacks the same authors' slavery paper (p. 16). [verify] year and pagination.

## Links

- [[The three Kelly critiques establish different nulls]]
- [[The persistence coefficient fails even where the dynamics are ergodic]]
- [[A long-horizon persistence coefficient bounds no relaxation time]]
- [[Common shocks leave the cross-section a single realisation]]
- [[A common shock defeats the pool through its mean loading and the cross-section through its dispersion]]
- [[Voigtlander and Voth measured the relaxation time and reported a mixture]]
- [[The persistence literature names non-ergodicity only in its geography branch]]
- [[Persistence stationarity and mobility literature]]
- [[MOC - Historiography and method]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Session of 2026-11-23: full read of the PDF, checked against Part 2 §3 and the WP3 notes.

## References

Kelly, Morgan. 2026. "The Mechanisms of Historical Persistence." Working paper.

Andrews, Donald W. K. 2005. "Cross-Section Regression with Common Shocks." *Econometrica* 73 (5): 1551–85. [verify] DOI, believed `10.1111/j.1468-0262.2005.00629.x`.

Becker, Sascha O., and Luigi Pascali. 2019. "Religion, Division of Labor, and Conflict: Anti-Semitism in Germany over 600 Years." *American Economic Review* 109 (5): 1764–1804.
