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

**One correction to the word "resets".** *Warichi* does not reverse the loss and does not return a household to a prior level of wealth. The destroyed parcel stays destroyed and the village is permanently poorer; what is re-drawn is the distribution of the *surviving* land. The object being reallocated is the **incidence** of an absorbing event, not its effect — see [[Warichi and general average spread the incidence of an irreversible loss]] for the pairing that formulation opens up. Resetting language is right about the periodicity and wrong about the level.

That points to a formal home better than diversification. Under multiplicative dynamics with an absorbing barrier there is no stationary distribution; **stochastic resetting is what makes one exist**, and the resetting rate is the parameter that governs it. On that reading Brown's chapter-long measurement of *redistribution intervals* is not incidental bookkeeping but the estimation of exactly the free parameter such a model has. Stojkoski and colleagues give the machinery for geometric Brownian motion with resetting, including the non-ergodicity result, and it is a closer fit to what a village was doing every five or ten years than any diversification model.

Two consequences worth keeping separate. The **comparative** one: if *warichi* and scattering answer to different correlation structures, then their coexistence in one society is unremarkable and their distribution across societies should track the *persistence* of the dominant land shock rather than the level of risk. Transient plot-level shocks select scattering; permanent parcel destruction selects reallocation. That is testable and it is a sharper prediction than "high-risk areas get warichi." The **methodological** one: nothing here licenses treating the two as functionally equivalent forms, and the census should not code them as one type.

A caution against over-anchoring on McCloskey. His insurance thesis is contested — Allen and Clark dispute it and the 1991 paper is his reply — so hanging *warichi* on it inherits an unsettled debate for no gain. Argue the resetting mechanism directly, and cite McCloskey as a parallel instance of a land arrangement organised around peril rather than as the model for this one.

## The distinction is what saves the risk account from Brown's test

**Attribute the flood hypothesis correctly.** Spreading the impact of flooding is the *received* reading in the Japanese literature, built on individual village studies; Brown is its sceptic. His 2006 regional test concludes that flood and landslide frequency "must be seen as insufficient causes by themselves, even if scholars ultimately see them as necessary conditions," and that explanation must be sought "more widely… than the threat of natural calamity stressed heretofore."

What he operationalises, though, is hazard **exposure** — elevation, floodplain position, landslide potential — which measures how *often* damage occurs. Resetting predicts from **persistence**: whether a shock permanently destroys a parcel's productive value. The two come apart. An upland terrace stripped to bedrock is rare and irreversible; a lowland paddy that floods most years and drains is frequent and fully recoverable. Diversification answers the second, reallocation only the first.

Brown's anomalies then change sign. Shindōri, Kamegai and Sekiya near the Shinano mouth "cannot be explained by readily apparent natural conditions"; Iwade practises *warichi* while "removed from a large hydrological system and floodplain"; most of the 113-village sample sits above 67.5 metres. Anomalous under frequency, expected under persistence. His residual — "an important role for local, village-level human agency" — is a placeholder where a mechanism should be.

The test this implies is concrete and uses his own data: re-score the villages for irreversibility rather than exposure, and ask whether redistribution interval tracks that instead.

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

Warichi session, 2026-08-08. Brown, Philip C. 2006. "Arable Land as Commons: Land Reallocation in Early Modern Japan." *Social Science History* 30 (3): 431–. `10.1215/01455532-2006-004` — the regional GIS test and the "insufficient causes by themselves" conclusion. Brown, Philip C. 2011. *Cultivating Commons: Joint Ownership of Arable Land in Early Modern Japan*. Honolulu: University of Hawai'i Press — the surviving hypothesis restated in ch. 2 ("warichi is found where natural risks (e.g., floods, landslides) are high"), redistribution intervals measured in ch. 6. **Note on attribution**: the flood-spreading reading is the received view in the Japanese literature, not Brown's; he is its critic. McCloskey, Donald N. 1991. "The Prudent Peasant: New Findings on Open Fields" — "their benefits were those of insurance". Stojkoski, Viktor, et al. 2022. "Income Inequality and Mobility in Geometric Brownian Motion with Stochastic Resetting" — in the Zotero library. **The copy of Brown consulted is a scan with scrambled page order; ch. 6's concluding verdict on the GIS test could not be isolated and is not represented here.**
