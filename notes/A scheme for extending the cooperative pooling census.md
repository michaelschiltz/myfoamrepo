---
title: A scheme for extending the cooperative pooling census
type: permanent
tags: [coding-ontology, risk-sharing, comparative, limited-diversity, comparative-concept]
project: HistorEE
source-session: shareholding-and-pooling-scheme
database: [loss_mitigation_forms, organizational_forms]
created: 2026-08-12
status: seed
---

# A scheme for extending the cooperative pooling census

The census is not short of forms. It is short of forms **that make a characteristic move**, and after a week of coding it is possible to say which characteristics are stuck and what would unstick them.
The organising principle of this note is therefore not geography but **what a form would test**. A region gets acquired because a cell needs it, not because the map has a hole in it.

## What is stuck, and why

**`VF1 loss verification mode` is `.NA` on nine consecutive East Asian forms.** Every kō, and now `shenhui_gu_alloc`, has a payout trigger that is not a realised loss — rotation, lot, ritual — so nothing is ever claimed and nothing verified. A characteristic with one value across a third of the census is carrying no information. **What unsticks it: any membership fund that indemnifies an attested misfortune.** Richardson's English fraternities pay on fire, murrain, theft and illness; that is `PY1=realised-loss`, which makes `VF1` applicable for the first time in this material.

**`MC1 mitigation mechanism` cannot be set on five forms**, and at five it has stopped being a coding difficulty and become a result. `particular_average`, `warichi_iwade` `ko_daikokuya_1848`, the two Mitarai kō where the fit was already strained, and now `shenhui_gu_alloc`. Allocation, spreading and pooling each presuppose a **peril** moving among parties with a stake. These forms pool assets, liquidity, land or ritual obligation and move no peril at all. The census has accidentally assembled a class — *cooperative arrangements that pool without a hazard* — and the sort key of the whole dataset cannot name it. **This is the most interesting unresolved thing in the repository** and it is not fixed by acquiring anything; it is fixed by deciding whether `MC1` should have a value for "no peril at issue" or whether these forms belong in a different census. See [[Pooling's sign is set by the correlation of its baskets]] for why the pooling facet cannot simply absorb them.

**`RB3 security or pledge` is now repaired but provincial.** `real-estate` is taken by Japanese forms only, and a value one tradition monopolises labels the tradition instead of discriminating within the set. `surety` and `personal` have **zero occurrences each**, so the split made this week is still a hypothesis about where the cut belongs.

**`MB3=compulsory` sits on four forms.** Compulsion is theoretically loaded — if pooling raises each participant's time-average growth rate, compulsion demands an explanation — and four cases cannot carry that argument.

**Labour is invisible.** Not one coded form pools labour, though reciprocal labour is a pooling institution with the same functional profile ([[Labour exchange is the pooling type the census cannot see]]). The standing decision is to code 結 *yui* and 품앗이 *pumasi* together or neither.

**Residence is invisible, and this is the deeper hole.** Every form in the census is a *fund* or an *allocation rule* — something is collected and something is paid, or an existing asset is redistributed. Not one is a **place**. Yet the most common historical answer to catastrophic individual exposure was not a subscription but a household: shocks were absorbed by the unit one lived in, and the people at real risk of ruin were those without one. A census that can only see funds will systematically miss the arrangements that substituted for the household, and will then report — falsely — that such arrangements were rare. `CN1=.NA` is currently a curiosity attaching to `warichi_iwade`; it may turn out to mark a whole class the instrument cannot hold.

## Acquisition priority

Ordered by which stuck cell each would move, not by importance of the tradition.

**1 — English fraternity / guild mutual-aid fund.** Richardson 2005, *JEH* 65:2, "The Prudent Village". The Zotero attachment is a RePEc landing page, not the article; acquire the PDF. Moves `VF1` off `.NA` for the first time in a membership fund, gives `PY1=realised-loss` a second instance outside general average, and supplies the European comparator that tests whether the Japanese kō collapse into one signature is a fact about kō or about the instrument. It also settles a question already flagged as unverified in [[Forms are not independent observations when a village runs a portfolio]] — Richardson argues directly against McCloskey that alternatives to scattering existed. Note the type row `guild_mutual_aid` currently reads "European / Japanese", which is a conflation and must be split before anything is coded against it.

**2 — 會館 *huiguan*, Chinese native-place association.** The East Asian half of the comparison rests entirely on Japan, which is a real weakness for a project claiming cross-civilisational scope, and huiguan hold landed endowments, so they would take `RB3=real-estate` in a non-Japanese tradition and discharge the obligation that value was admitted under. Library holds only Hamilton 1977 on a single Swatow opium guild and Zelin's edited volume — not enough. **Declare co-occurrence with the kō when coded**: China-to-Japan transmission is plausible, so the pair is a Galton's-problem case and no independence claim may run on it.

**3 — Ottoman *avarız-hane* fund, and cash *waqf* alongside it.** The strongest independence candidate in the census: a third bloc, compulsory, sitting directly beside `averia_pool`, which would take `MB3=compulsory` from four instances to five and give the compulsion argument a non-European case. Nothing in the library at all. Yaycıoğlu's territory. Krešić & Pavlović 2020 on *kefalet* — collective surety, distinguishing surety for a person from surety for property — is already held and is the first candidate to test the `surety`/`personal` split, if it can be coded as a form rather than a doctrine.

**4 — 結 *yui* with 품앗이 *pumasi*.** Together or not at all. Would test whether `CN2` can express an equivalence schedule graded by sex and age, and whether the census can represent an arrangement whose unit of account is time rather than value.

**5 — Latin confraternity proper, and the HUF.** `confraternity_fund` and `huf` are both parked; the HUF carries an explicit boundary doubt in its own type row about whether it is a capital vehicle rather than a hazard pool, which the *shenhui_gu* coding has just made a general question rather than a peculiarity of that row.

**6 — Flemish *begijnhof*, the beguinage.** MS's suggestion, 2026-08-13, as a way of pooling labour "and maybe more". **The "maybe more" is where the value is, and the labour reading is the part I would expect not to survive the sources.** Two objections to test before acquiring anything. First, beguines took no vow of poverty — that is the defining contrast with nuns — so they **retained private property, could inherit and could bequeath**. There is no common purse, which is exactly what `MC1=pooling` and `CN1` are built to find, and a beguinage may fail at the same first question that excluded Lavallée's choir school. Second, beguine labour was largely **individual piecework for wages** in the cloth trades, plus nursing, laundering and teaching; output was not obviously pooled, and if it was not, `yui` and *pumasi* remain the better route to the labour cell.

What survives both objections is stronger than the labour claim. **A beguinage pools the absorbing barrier itself.** For an unmarried or widowed woman in a Flemish town, ruin followed from having no household to fall back on; the *begijnhof* supplies the function of one — shelter at below-market cost, work found through the community, care in illness and old age within the court, burial — without marriage, without vows, and without a man. That is loss mitigation whose medium is **residence rather than money**, and per the paragraph above the census has no such form. **It is therefore a test of the instrument, not merely an addition to it:** if the beguinage cannot be coded, the finding is that the census's frame is fund-shaped, which is a referee-facing result and not a defect to hide.

Two further reasons to want it. **It may belong in `organizational_forms` more than in `loss_mitigation_forms`** — a corporate body holding real property in perpetuity, governed by a Grand Mistress under a rule never approved at Rome, which survived condemnation at Vienne in 1311 and persisted for centuries afterwards. Legal personality and perpetual succession arrived at by a lay women's community, outside every actor the entity-shielding literature discusses. Check it against `waqf_khayri` and `nakai_fictive_household` on the WP2 five before assuming it is new. And **it completes a triad that assembled itself today**: three institutional answers to one exposure — the unattached woman — namely `craft_widows_fund_edinburgh` (an annuity), `friendly_society_female_england` (sick pay against inability to work), and the beguinage (a place to live and a way to earn). Same hazard, three media, three traditions. That is the kind of set the census exists to produce, and it was not designed for.

*Sources to check rather than assume.* Walter Simons, *Cities of Ladies: Beguine Communities in the Medieval Low Countries, 1200–1565* is the standard treatment and the first thing to acquire; there is a substantial Dutch-language literature on individual *begijnhoven* that the library may already hold. Citation unverified — confirm before it enters a type row. **The claim to test first is the property one**, since it decides whether this is a pooling form at all.

## Decision rules the week produced

Written down because each was learned by getting it wrong first.

- **Split a type when it spans both values of a characteristic.** `tontine` → `tontine_en_1693` / `tontine_fr_royal`; `ortoq` → `ortoq_equity` / `ortoq_loan`; `kabu_nakama` → `kabu_local` /
  `kabu_edo_export`. One row cannot hold two values and `P` must not be used to make it.
- **Code the class, not the entity, where rights differ by class within one entity.** Chinese silver,body and dry shares. Then code entity-level characteristics on the class that *is* the entity and leave them `.NR` elsewhere with the mismatch named.
- **`P` is structural half-presence.** Never "changed over time", never "differs by class", never "I am unsure" — uncertainty is `confidence`.
- **A source's hedge caps the coding's confidence.* "It can be hypothesized" cannot produce a `high`.
- **Extend a vocabulary in its own commit, never in the batch that motivated it.** Otherwise the falsifiability commitment goes; the `.NR` cells are the recorded motivation.
- **Widening a vocabulary does not license filling a cell the source never filled.** Two `RB3` cells stayed `.NR` after `real-estate` was admitted.
- **Declare co-occurrence.** Forms from one community, one institution or one archive are not independent cases, and `same-institution` now exists in both censuses to say so.

## Links

- [[Forms are not independent observations when a village runs a portfolio]]
- [[Labour exchange is the pooling type the census cannot see]]
- [[Pooling's sign is set by the correlation of its baskets]]
- [[The bidding ko transfers from the liquidity-constrained to the liquid]]
- [[Divergent arbitrary particulars are the independence diagnostic]]
- [[Count degrees of freedom not cells]]
- [[The morphological matrix is dictated by the shape of the feature space]]
- [[Kye is not a ROSCA and the equation is an artefact of comparison with mujin]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

Coding sessions of 2026-08-09 to 2026-08-12: 三浦 1959, 松永 1999 and 加藤 1998 on tanomoshi-kō;
Enkhbold 2019 and Endicott-West 1989 on the ortoq; Zelin 2019 and Nagata 2008 on Chinese and Japanese
shareholding. Extended 2026-08-13 after the guild-and-fraternity reading (Prom, Allen, Rusnock & Dietz coded; Lavallee and Klieber read and excluded) and after MS proposed the beguinage. Census state as at `loss_mitigation_forms` 0.4.0 and `organizational_forms` 0.7.1.
The priority ordering is proposed here and is nobody else's; the stuck-cell diagnoses are readable
off the data.

[Pooling's sign is set by the correlation of its baskets]: <Pooling's sign is set by the correlation of its baskets.md> "Pooling's sign is set by the correlation of its baskets"
[Labour exchange is the pooling type the census cannot see]: <Labour exchange is the pooling type the census cannot see.md> "Labour exchange is the pooling type the census cannot see"
[Forms are not independent observations when a village runs a portfolio]: <Forms are not independent observations when a village runs a portfolio.md> "Forms are not independent observations when a village runs a portfolio"
[The bidding ko transfers from the liquidity-constrained to the liquid]: <The bidding ko transfers from the liquidity-constrained to the liquid.md> "The bidding ko transfers from the liquidity-constrained to the liquid"
[Divergent arbitrary particulars are the independence diagnostic]: <Divergent arbitrary particulars are the independence diagnostic.md> "Divergent arbitrary particulars are the independence diagnostic"
[Count degrees of freedom not cells]: <Count degrees of freedom not cells.md> "Count degrees of freedom not cells"
[The morphological matrix is dictated by the shape of the feature space]: <The morphological matrix is dictated by the shape of the feature space.md> "The morphological matrix is dictated by the shape of the feature space"
[Kye is not a ROSCA and the equation is an artefact of comparison with mujin]: <Kye is not a ROSCA and the equation is an artefact of comparison with mujin.md> "Kye is not a ROSCA and the equation is an artefact of comparison with mujin"
[MOC - Risk-sharing vs risk-pricing]: <../mocs/MOC - Risk-sharing vs risk-pricing.md> "MOC - Risk-sharing vs risk-pricing"
[MOC - Historiography and method]: <../mocs/MOC - Historiography and method.md> "MOC - Historiography and method"
[MOC - HistorEE]: <../mocs/MOC - HistorEE.md> "MOC - HistorEE"
