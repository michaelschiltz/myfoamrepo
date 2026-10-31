---
title: The hexagon is optimal only among neighbours
type: permanent
tags: [risk-sharing, comparative]
project: erc-synergy
source-session: honeycomb-theorem
created: 2026-10-31
status: seed
---

# The hexagon is optimal only among neighbours

**The regular hexagon is not the best shape for a cell. It is the best shape for a cell among cells. Standing alone, a unit-area cell should be round; inside a comb whose walls are shared, the hexagon is optimal, and every cell in it pays less wax than any solitary cell could. The optimum is defined on the configuration and enjoyed by each member severally. That is *Meditations* 6.54 in geometry — and it is cost-sharing, not risk-pooling, which fixes what the image may be asked to carry.**

## The arithmetic

Wall per unit-area cell:

| Configuration | Wall charged to one cell |
| --- | --- |
| Solitary circle | $2\sqrt{\pi} \approx 3.545$ |
| Solitary regular hexagon | $2\sqrt[4]{12} \approx 3.722$ |
| Solitary square | $4$ |
| Square tiling, walls shared | $2$ |
| Hexagonal tiling, walls shared | $\sqrt[4]{12} \approx 1.861$ |

Taken alone the hexagon loses to the circle. Circles cannot tile, so a comb of circles wastes wax in the interstices and shares no wall. The hexagon wins only because sharing halves its cost, and among the tilings it halves best: about 7 per cent less wall than the square tiling, 18 per cent less than the triangular. **No cell's own geometry recommends the hexagon. Only the comb does.**

## The proof has the same anatomy

Hales's argument (see [[Hales 2001 - the honeycomb theorem and the architecture of its proof]]) bounds each cell separately, and the per-cell bound is useless on its own: it carries a bulge term and a side-count term of either sign. Both vanish only in the sum, and for two reasons that belong to the whole and to no part. A wall bulging out of one cell bulges into its neighbour by the same area, so the bulge terms cancel in pairs across shared walls. And the torus's Euler characteristic forces the mean number of sides to six, so the side-count terms cancel in aggregate. **The individual inequality becomes informative only through the shared boundary and the global constraint.**

## The epigraph reading

*Meditations* 6.54 — τὸ τῷ σμήνει μὴ συμφέρον οὐδὲ τῇ μελίσσῃ συμφέρει [verify] — is retained because it states the alignment of collective and individual advantage directly ([[Stoic loci on cooperation - only two argue from interdependence]]). The comb is the material object behind the image, and it shows the alignment without altruism: no cell sacrifices for the comb; each is cheaper in it. That is the structure of the pooling proposition — the case for cooperation never passes through obligation — and it is cognate with Seneca's arch (*Ep.* 95.53), which also stands by mutual pressure, more than with the membership loci.

## What the image must not be asked to carry

The geometry is additive and static. Wall lengths sum; nothing compounds; there is no time, no trajectory, no absorbing barrier. The comb's economy is the economy of a **shared fixed cost** — one wall serving two cells, as one escort serves a convoy or one warehouse a guild. The project's result is of a different kind: pooling raises the *time-average growth rate* by averaging fluctuations under multiplicative dynamics, and its gain exists only because the dynamics are non-ergodic ([[Time-average optimization is a survivorship property not an intention]], [[Pooling's sign is set by the correlation of its baskets]]). A comb has no correlation structure to get wrong.

So the honeycomb is a sound emblem of 6.54 — alignment of cell and comb — and an unsound figure of the mechanism. Used to illustrate the time-average argument it would decorate, not license, exactly the failure the Stoic-loci note warns against. Deterministic cost-sharing (a convoy's escort, a guild's warehouse) is the one corner of the census it fits literally. *General average* already does not: it apportions a stochastic, realised loss, and that is a pooling question with a correlation structure.

## Links

- [[Stoic loci on cooperation - only two argue from interdependence]]
- [[Hales 2001 - the honeycomb theorem and the architecture of its proof]]
- [[Practice answers the problem as posed and the proof says which problem that was]]
- [[Time-average optimization is a survivorship property not an intention]]
- [[Pooling's sign is set by the correlation of its baskets]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - ERC Synergy Grant]]
- [[MOC - HistorEE]]

## Source

Honeycomb-theorem session, 31 October 2026, from a post on the honeycomb theorem that charged the full hexagon perimeter to each cell and so missed the halving in which the economy consists. Greek of 6.54 from memory; check against Farquharson or the Teubner with the other Stoic loci.
