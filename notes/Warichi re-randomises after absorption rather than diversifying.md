---
title: Warichi re-randomises after absorption rather than diversifying
type: permanent
tags: [absorbing-barrier, ergodicity, diversification, risk-sharing, time-average]
project: HistorEE
source-session: warichi-coding
database: [loss_mitigation_forms]
created: 2026-08-08
status: seed
---

# Warichi re-randomises after absorption rather than diversifying

The tempting move is to read *warichi* as the Japanese counterpart of English open-field scattering, and to borrow McCloskey's argument that the benefits of scattering were those of insurance. The two institutions are not variants of one mechanism, and the difference is structural rather than interpretive: **they address opposite correlation structures.**

Scattering is permanent simultaneous fragmentation. A household holds twenty plots at once across the village face, and the variance it removes is idiosyncratic and plot-level — hail on one furlong, pests in one corner, a bad drainage pocket. It is diversification, it operates within a single year, and once the layout exists it requires no further coordination.

*Warichi* is periodic reallocation between households, and it does nothing about within-year variance. What it addresses is a **permanent** change in a plot's quality. When a river avulsion destroys a parcel or a landslide buries it, no amount of holding many plots helps the household whose parcel is gone, because the shock is covariate at village scale and irreversible at plot scale. Only re-drawing the lots restores parity. And the institution is far more expensive than scattering — a recurring collective decision, a lot-drawing, enforcement, disputes — so the premium has to purchase something scattering cannot.

Stated in the project's own terms: **scattering averages across an ensemble of plots at one moment; *warichi* resets a trajectory that a permanent shock has already moved.** It is not a device for reducing the variance of a draw. It is a device for returning a household to the middle of the distribution after the draw has gone against it — which is a response to absorption, not to volatility ([[An absorbing barrier breaks ergodicity by construction]]).

That points to a formal home better than diversification. Under multiplicative dynamics with an absorbing barrier there is no stationary distribution; **stochastic resetting is what makes one exist**, and the resetting rate is the parameter that governs it. On that reading Brown's chapter-long measurement of *redistribution intervals* is not incidental bookkeeping but the estimation of exactly the free parameter such a model has. Stojkoski and colleagues give the machinery for geometric Brownian motion with resetting, including the non-ergodicity result, and it is a closer fit to what a village was doing every five or ten years than any diversification model.

Two consequences worth keeping separate. The **comparative** one: if *warichi* and scattering answer to different correlation structures, then their coexistence in one society is unremarkable and their distribution across societies should track the *persistence* of the dominant land shock rather than the level of risk. Transient plot-level shocks select scattering; permanent parcel destruction selects reallocation. That is testable and it is a sharper prediction than "high-risk areas get warichi." The **methodological** one: nothing here licenses treating the two as functionally equivalent forms, and the census should not code them as one type.

A caution against over-anchoring on McCloskey. His insurance thesis is contested — Allen and Clark dispute it and the 1991 paper is his reply — so hanging *warichi* on it inherits an unsettled debate for no gain. Argue the resetting mechanism directly, and cite McCloskey as a parallel instance of a land arrangement organised around peril rather than as the model for this one.

## Links

- [[Brown tests equality where a risk reading predicts dispersion]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Absorbing barrier]]
- [[Pooling's sign is set by the correlation of its baskets]]
- [[Stationarity is a precondition of ergodicity not a corollary]]
- [[Terminal wealth is permutation-invariant but survival is not]]
- [[Time-average]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Warichi session, 2026-08-08. Brown, Philip C. 2011. *Cultivating Commons: Joint Ownership of Arable Land in Early Modern Japan*. Honolulu: University of Hawai'i Press — hypothesis stated in ch. 2 ("warichi is found where natural risks (e.g., floods, landslides) are high"), redistribution intervals measured in ch. 6. McCloskey, Donald N. 1991. "The Prudent Peasant: New Findings on Open Fields" — "their benefits were those of insurance". Stojkoski, Viktor, et al. 2022. "Income Inequality and Mobility in Geometric Brownian Motion with Stochastic Resetting" — in the Zotero library. **The copy of Brown consulted is a scan with scrambled page order; ch. 6's concluding verdict on the GIS test could not be isolated and is not represented here.**
