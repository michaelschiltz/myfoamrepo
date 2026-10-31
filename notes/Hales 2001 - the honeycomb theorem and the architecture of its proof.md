---
title: Hales 2001 - the honeycomb theorem and the architecture of its proof
type: source
tags: [selection, historiography, survivorship-bias]
project: HistorEE
source-session: honeycomb-theorem
created: 2026-10-31
status: seed
---

# Hales 2001 - the honeycomb theorem and the architecture of its proof

Hales, Thomas C. 2001. "The Honeycomb Conjecture." *Discrete & Computational Geometry* 25 (1): 1–22. doi:10.1007/s004540010071. Preprint arXiv:math/9906042 (v1, 8 June 1999; v2, 20 May 2002, the published text, which admits disconnected cells and gaps between cells).

Prompted by a post of @mathemetica on X, 29 October 2026 (status 2115459455823527946), which states the result and a wax formula and closes on the line that nature solved the problem before the proof existed. The post contains no proof. Its claims are corrected at the foot of this note.

## What is proved

**Theorem 1-A.** Let Γ be a locally finite graph of smooth curves in the plane whose complement has infinitely many bounded components, all of unit area, and let C be their union. Then

$$\limsup_{r\to\infty}\frac{\operatorname{perim}(C\cap B(0,r))}{\operatorname{area}(C\cap B(0,r))}\;\ge\;\sqrt[4]{12}\approx 1.8612,$$

with equality for the regular hexagonal tiling. **Theorem 1-B** drops connectedness and contiguity: for disjoint measurable $R_i$ in a compact set with rectifiable boundaries, $\mathcal{H}^1(\Gamma) > \sqrt[4]{12}\sum_i \alpha_i$, $\alpha_i = \min(1, \operatorname{area} R_i)$. The constant $\sqrt[4]{12}$ is *half* the perimeter of a unit-area regular hexagon: the wall charged to one cell once each wall is shared by two.

## The architecture, in five moves

1. **Existence and regularity first.** Hales recalls that Weierstrass faulted Steiner's isoperimetric proofs for assuming a solution exists. Modern geometric measure theory (Morgan 1994; Taylor; Almgren) supplies minimisers, and they are tame: finitely many circular arcs meeting three at a vertex.
2. **Finite version.** Theorem 2: for $n$ regions with areas at least $\alpha_i \le 1$, $\operatorname{perim}\Gamma > A\sqrt[4]{12}$, $A = \sum\alpha_i$. Morgan's truncation lemma (Morgan 1999) carries the finite case to 1-A. For $A \le 398$ the isoperimetric inequality applied twice suffices. Regions too small for their number of neighbours ($\operatorname{area} < a_0/M^2$) are "popped" into a neighbour, which lowers the target functional.
3. **Transfer to a flat torus.** The cluster is wrapped onto a torus — compact, and with Euler characteristic zero, so that $\sum_P (1 - N(P)/6) = 0$. **Topology alone forces the mean number of sides to six.** Fejes Tóth 1943 had used the sphere for the convex case.
4. **The hexagonal isoperimetric inequality** (Theorem 4), proved cell by cell. Join each cell's $N$ vertices by chords; let $x(e)$ be the signed area of the bulge of edge $e$ over its chord, truncated by $\tau$ at $\pm\tfrac12$, and $T(P) = \sum_e \tau(x(e))$. Then
   $$L(P) \;\ge\; -T(P)\sqrt[4]{12}\;-\;(N(P)-6)\,0.0505\;+\;2\alpha(P)\sqrt[4]{12},$$
   with equality if and only if $P$ is a regular hexagon of area 1. Without the truncation the inequality is false (Hales, Remark 1: three long inverted arcs).
5. **Summation.** A wall bulges into one neighbour exactly as far as it bulges out of the other, so $x(e) + x(e^{op}) = 0$; $\tau$ is odd, so $\sum_P T(P) = 0$. Euler disposes of the $(N-6)$ term. What remains is $2\operatorname{perim}\Gamma \ge 2\sqrt[4]{12}\sum\alpha_i$.

The bulk of the paper (§§5–8, Appendix 1) proves Theorem 4: two cases on the size of the bulges, a stock of lower bounds (the circle bound $L^+$, the reflection bound $L^-$, Dido's semicircle bound $L_D$, and the new chord-length bound $L'$), and interval checks by computer for the two tight windows near $N = 6, 7$.

**Why it took so long.** Fejes Tóth proved the convex case in 1943 and predicted that the general case would involve considerable difficulties. Convexity forces polygonal cells, and so excludes at once the curved-walled cells that isoperimetry identifies as the dangerous candidates. The assumption that made the problem tractable was the assumption that removed the cases that mattered.

## The history Hales gives

- **Varro**, *De re rustica*, c. 36 BC [verify book and section]: the geometers were already said to *prove* the hexagon's capacity — a proof that did not exist.
- **Pappus**, *Collection* V (drawing on Zenodorus, c. 180 BC): compares only the three regular tilings, and restricts himself to them on non-mathematical grounds — bees avoid dissimilar figures, and gaps between cells would admit foreign matter and defile the honey. The stated rationale is purity; the operative quantity is wax.
- **MacLaurin 1743**, Lhuilier 1781 on the rhombic base; eighteenth-century readings of the comb as evidence of design; **Darwin** recasting the same economy of wax as the outcome of selection among swarms.
- **Kelvin 1887** on the three-dimensional analogue; Weaire and Phelan's 1994 counterexample; **Morgan 1999** recording that even the planar case remained open.

## Adjacent literature

- **Fejes Tóth 1964**, "What the Bees Know and What They Do Not Know," *Bull. AMS* 70 (4): 468–482, doi:10.1090/S0002-9904-1964-11155-1. Constructs a cell base of two hexagons and two rhombi that beats the bees' three-rhombus base; the saving is of the order of 0.35 per cent [verify the base of the percentage].
- **Weaire and Phelan 1994a**, "Optimal Design of Honeycombs," *Nature* 367: 123. In a two-layer liquid foam the interface adopts Fejes Tóth's structure while the films are thin and switches abruptly to the bees' three-rhombus base as they thicken. The bees' "error" is optimal for a wall of real thickness.
- **Weaire and Phelan 1994b**, "A Counter-Example to Kelvin's Conjecture on Minimal Surfaces," *Phil. Mag. Lett.* 69 (2): 107–110. Found by simulated relaxation (Brakke's Surface Evolver); about 0.3 per cent less area than Kelvin's cell; optimality unproven.
- **Mechanism.** Karihaloo, Zhang and Wang 2013, *J. R. Soc. Interface* 10: 20130299 [verify]: cells are laid as circles and pulled into hexagons by flow of heated wax at the triple junctions, as Bartholin and D'Arcy Thompson had argued. Bauer and Bienefeld 2013, *Naturwissenschaften* [verify]: the wax is not hot enough for a liquid equilibrium; the shaping is mechanical. Nazzi 2016, *Sci. Rep.* 6: 28341: whatever the mechanism, hexagons follow only from a prior regular arrangement of the cylinders. Natural combs contain a minority of Fejes Tóth cells (up to roughly 18 per cent in *Apis cerana* and *A. mellifera*, *Apidologie* 2022 [verify authors]).
- **Philosophy of mathematical explanation.** Lyon and Colyvan 2008, *Philosophia Mathematica* [verify] made the honeycomb the standard case of a mathematical explanation of a physical fact; Baker 2009 and Pincock 2012 extended the debate. Räz 2013 (*Phil. Math.* 21 (3): 351–360) objected that the comb is three-dimensional; Räz 2017 ("The Silent Hexagon," *Synthese* 194 (5): 1703–1724, doi:10.1007/s11229-016-1014-3) concludes that **an optimal structure does not uniquely determine the optimisation that produced it**. That sentence is the vault's filter discipline in another discipline's words.

## Corrections to the post

- *Proved in 1999.* Preprint 1999; published 2001.
- *Wax ∝ 4√3 r t.* The formulae $A = 2\sqrt3 r^2$, $P = 4\sqrt3 r$ for inradius $r$ are right, but charging the whole perimeter to each cell counts every wall twice. The wax per cell is $2\sqrt3\, r t$. The halving is not a detail: it is where the economy lies (see [[The hexagon is optimal only among neighbours]]).
- *Stores the most honey with the least wax.* The theorem is planar. The comb is three-dimensional, and under the thin-wall idealisation its cell base is not optimal (Fejes Tóth 1964).
- *Nature solved it before the proof.* Soap froth and cooling basalt reach the same tiling with no history of selection, and how the bees' hexagon arises is still disputed. See [[The optimum does not identify the route that reached it]].

## Links

- [[The hexagon is optimal only among neighbours]]
- [[Practice answers the problem as posed and the proof says which problem that was]]
- [[The optimum does not identify the route that reached it]]
- [[Stoic loci on cooperation - only two argue from interdependence]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Honeycomb-theorem session, 31 October 2026. Hales read in full from arXiv v2; the 3D, mechanism and philosophy-of-explanation items located by search and not yet read in full — flagged where details are unconfirmed.
