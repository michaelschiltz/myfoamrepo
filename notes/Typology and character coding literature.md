---
title: Typology and character coding literature
type: reference
tags: [coding-ontology, cladistics, similarity, character-independence, limited-diversity, comparative-concept, comparative]
project: HistorEE
source-session: isqa-qirad-commenda
database: [organizational_forms]
created: 2026-08-03
status: seed
---

# Typology and character coding literature

Bibliographic companion to [[Count degrees of freedom not cells]]. Zotero collection `method — typology and character coding`; operational rules in `CHARACTER-CODING.md` in the codebooks repo. All DOIs below verified through CrossRef; items marked **unverified** are from memory and must be checked before they reach a footnote.

## The theorem behind the objection

**Watanabe, *Knowing and Guessing* (1969)** — the **ugly duckling theorem**. Over the set of all possible predicates, any two objects share the same number of predicates. Similarity is constant across every pair unless predicates are weighted, and no weighting is derivable from the objects. *Classification without bias makes all objects equally similar.* This is the formal statement of the intuition that a typology which adds characteristics until forms separate has discovered nothing. **Unverified for edition and pagination; pre-DOI, not yet in Zotero.**

**Goodman, 'Seven Strictures on Similarity'** (in *Problems and Projects*, 1972) — similarity without a specified respect is empty. **Unverified.**

More useful than either, because it is the working discipline arguing with itself rather than philosophers at one remove:

- **Rieppel, 'Similarity', *Biological Journal of the Linnean Society* 75 (2002), 59–82.** `10.1046/j.1095-8312.2002.00006.x`
- **Rieppel, 'The poverty of taxonomic characters', *Biology and Philosophy* 22 (2007), 95–113.** `10.1007/s10539-006-9024-z`

## When a character is well formed

**Sereno, 'Logical basis for morphological characters in phylogenetics', *Cladistics* 23 (2007), 565–587.** `10.1111/j.1096-0031.2007.00161.x` — the central paper. Finds that **character independence is routinely overlooked** and that there is no consensus on what a character is. Decomposes any character statement into locator, variable, variable qualifier, state, and shows the classic controversies — above all the state "absent" — are symptoms of *incomplete character statements*. Gives the operational test: **if one characteristic contains two variables it is ill-formed and must be split.** `LR2` was exactly that.

**Vogt, 'The logical basis for coding ontologically dependent characters', *Cladistics* (2018).** `10.1111/cla.12209` — directly on the `applicability_on` column. Read before defending our implementation.

Supporting: **Hawkins, Hughes & Scotland (1997)** `10.1111/j.1096-0031.1997.tb00320.x` · **Pleijel (1995)** `10.1016/0748-3007(95)90018-7` · **Brazeau (2011)** `10.1111/j.1095-8312.2011.01755.x` · **Strong & Lipscomb, 'Character coding and inapplicable data' (1999)** `10.1111/j.1096-0031.1999.tb00272.x` · **Maddison, 'Missing data versus missing characters' (1993)** `10.1093/sysbio/42.4.576`, whose distinction is the ancestor of the repo's `.NR`/`.NA` split.

**Felsenstein, 'Phylogenies and the comparative method', *American Naturalist* 125 (1985), 1–15.** `10.1086/284325` — non-independence proper; the same animal as [[Galton's problem]].

## The threat to our coding ontology

**Haspelmath, 'Comparative concepts and descriptive categories in crosslinguistic studies', *Language* 86 (2010), 663–687.** `10.1353/lan.2010.0021`

Distinguishes **comparative concepts** — built by the analyst for comparison, belonging to no particular system — from **descriptive categories**, internal to one tradition and not exportable. Equating a descriptive category across traditions is illegitimate.

This is the sharpest external objection available to our matrix, and three characteristics fail it now: `AP4` is written around a *founder* and a *corpus*, which is waqf-shaped; `MG4=religious` for the *ʿisqa* was coded for consistency with `waqf_khayri`, which is precisely the prohibited move; `FP4`'s "political authority" does not map onto a corporate minority community. All three are flagged in the data rather than quietly repaired. The reply literature (Newmeyer, Croft, in *Language*) is worth having for balance. **Replies unverified.**

## Whether two characteristics are one construct

**Campbell & Fiske, 'Convergent and discriminant validation by the multitrait-multimethod matrix', *Psychological Bulletin* 56 (1959), 81–105.** `10.1037/h0046016` — verified, pagination correct. Discriminant validity **cannot be settled analytically** — only by observing cases where the constructs come apart. Which is what coding the *asiento* did to `agent-loss-exposure`.

## How many characteristics one can afford

**Marx & Duşa, 'Crisp-set qualitative comparative analysis (csQCA), contradictions and consistency benchmarks for model specification', *Methodological Innovations Online* 6:2 (2011), 103–148.** `10.4256/mio.2010.0037`

Simulated **over five million random datasets** to locate the point at which configurational analysis returns apparently meaningful results from noise, and produced benchmark tables. Guidance is roughly five cases per condition. The pathology has a name — **limited diversity**: with *k* conditions there are 2^*k* configurations, and where *n* ≪ 2^*k* every case is unique by construction. That is the ugly duckling theorem arriving as a practical problem.

**Contested, and cite it as such:** **Thiem & Mkrtchyan (2024)** `10.1177/1525822X231159458` attack the case-to-factor framing; **Duşa & Marx** reply in the same issue `10.1177/1525822X231159462`.

## Typology construction

**Collier, LaPorte & Seawright, 'Putting typologies to work', *Political Research Quarterly* 65 (2012), 217–232.** `10.1177/1065912912437162` · **Sartori, 'Concept misformation in comparative politics', *APSR* 64 (1970), 1033–1053.** `10.2307/1958356` on the ladder of abstraction and conceptual stretching.

**Elman, 'Explanatory typologies in qualitative studies of international politics', *International Organization* 59:2 (2005), 293–326.** `10.1017/S0020818305050101` — **already in the library** as `B3MFB58X`; I recorded it as absent without checking by surname. Read 2026-08-03.

The operational payoff. Elman gives a **typology of the legitimate ways to shrink a property space**, with the cost of each: *rescaling* (lower the level of measurement), *indexing* (weight and combine into a composite), *logical compression* (delete cells from impossible combinations), *empirical compression* (delete empty cells), *pragmatic compression* (collapse cells whose division serves no purpose). The mapping onto the codebook is close to exact — `applicability_on` plus `.NA` **is** logical compression; `.NR` exists to prevent empirical compression; an unweighted distance metric **is** indexing done implicitly; merging `AP2`/`CI2` would have been pragmatic compression. He also treats *expansion* and the **rediscovery of deleted cells** as first-class, which is why conflating `.NR` with `.NA` is unrecoverable rather than merely untidy — and warns against **reification**, the standing risk for `dependence_group`.

**Lazarsfeld (1937)** on typological procedure and **Barton (1955)** on *property space* — the Zwicky matrix under an earlier name, with explicit operations of **reduction**. **Both unverified and absent from the library** (checked by surname). Barton is cited in Collier et al.'s reference list and could be resolved from there.

## The disciplinary analogue we should be reading

Archaeology had this argument sixty years ago, over material forms, morphological attributes and no direct access to descent — closer to our position than biology is. Historians reach for biology and skip the field that had the argument in the medium closest to theirs.

**Spaulding, 'Statistical techniques for the discovery of artifact types', *American Antiquity* 18:4 (1953), 305–313.** `10.2307/277099`, JSTOR `277099`. Read 2026-08-03. Types are "groups of combinations of attributes favored by the makers of the artifacts, **not an arbitrary procedure of the classifier**"; method is chi square on contingency tables of attribute pairs, so a type is an association recurring beyond random drawing.

**This is an empirical escape from the ugly duckling problem, and it is closed to us.** Watanabe says the weighting cannot come from the objects; Spaulding answers that it comes from the *data* — combinations recurring beyond chance are features of practice, not of the analyst's attention. But chi square needs cases, and at four fully-coded forms there are none to spare. So the Ford–Spaulding debate states our position as a fork: **Spaulding's route needs cases we lack; Ford's route — types as constructs imposed for a stated purpose, the purpose supplying the weighting — needs a declared analytical core we have not written.** We have neither.

The library holds the 1997 reprint (`DJZB7ZUV`, in Lyman, O'Brien & Dunnell's *Americanist Culture History*); the 1953 original is now added as `5GR482JX` and the two are linked `owl:sameAs` rather than merged, since original and reprint are separately citable and the pagination differs.

**Still unread:** Ford's reply (*American Antiquity*, 1954) — the other half of the fork, and my characterisation of it above is secondhand; **Dunnell, *Systematics in Prehistory* (1971)**; **Adams & Adams, *Archaeological Typology and Practical Reality* (1991)**. Ford is now the highest-priority unread item.

Also **Ritchey** on cross-consistency assessment in general morphological analysis, which exists to prune the combinatorial explosion. **Unverified.**

## Links

- [[Count degrees of freedom not cells]]
- [[The morphological matrix is dictated by the shape of the feature space]]
- [[Borrow the diagnostics not the tree]]
- [[Galton's problem]]
- [[Homoplasy is the finding not the noise]]
- [[Never let the units slide from instruments to populations]]
- [[The coding commons must record stated rationale not only component presence]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

ʿIsqa session, August 2026. Assembled after the *asiento* coding falsified an asserted character dependence; 17 items DOI-verified and filed to Zotero, the remainder flagged unverified above.
