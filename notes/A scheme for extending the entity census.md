---
title: A scheme for extending the entity census
type: permanent
tags: [corporate-form, entity-shielding, limited-diversity, coding-ontology, comparative-concept, legal-personality]
project: HistorEE
source-session: entity-census-scheme
database: [organizational_forms]
created: 2026-08-29
status: seed
---

# A scheme for extending the entity census

The sibling of [[A scheme for extending the cooperative pooling census]], for the other dataset, and
written on the same principle: **a form gets acquired because a cell needs it, not because the map has
a hole in it.** What follows is readable off `organizational_forms` at 0.8.0 (293 rows, 18 forms,
32 characteristics) and is nobody's judgement but mine as to priority.

## The asymmetry

`loss_mitigation_forms` holds 47 coded forms against 26 characteristics; `organizational_forms` holds
**18 against 32**. Five of the eighteen carry a full row of 32 cells; three carry fewer than three
cells each. Against that, this vault carries **33 notes** under `MOC - Entity-shielding and corporate
forms`.

That ratio is the wrong way round. On the loss side the coding runs ahead of the argument, and the
notes are written to catch up with what the matrix turned out to contain. On the entity side the
argument runs ahead of the coding by an order of magnitude, and the risk this creates is specific:
**claims that cannot be checked against the instrument that is supposed to discipline them.** The
project's own remedy is [[Count degrees of freedom not cells]] — and 18 forms against 32
characteristics is a worse budget than any figure that note contemplates.

## Thirteen values have no instance

Seven of them substantive: `LP3=1` (capacity to sue), `TS3=1` (revocable), `TS4=1` (purpose mutable),
`LR1=none`, `LR2=attenuated`, `LR6=downside-only`, and `FP1=mutual-provision`. Five more are `P`
values never used, which may be honest. One, `LR5=na`, is not a gap but a **defect**: the literal
value is shadowed by the `.NA` sentinel, which eight of ten `LR5` rows use instead.

**`FP1=mutual-provision` is the one that matters.** All eighteen coded entity forms are
`commercial-profit`, `mixed` or `pious-charitable`. *The entity census contains no cooperative* —
while the loss census next door is 47 forms of overwhelmingly mutual institutions, none of which has
ever been coded as an entity. The two datasets have been built as though mutual bodies had no
organisational form at all, which is not a claim anyone in this project would defend if it were
stated out loud.

## The claim worth testing next, and the form that tests it

**Casa di San Giorgio, Genoa, 1407.** Transferable *loca*, the *comperae*, perpetual succession, a
jurisdiction and, from the mid-fifteenth century, territory governed in its own right — two centuries
before the VOC, which this census also does not contain.

If the entity signature of San Giorgio and the VOC is substantially the same, that is a **third
instance of the pattern this vault already has twice**: [[The tontine's chronology defeats the
hazard-to-pricing staging]] and [[Naviganti delayed the priced premium it is credited with dating]].
Both defeat a staging by dating; both do it on the *pricing* axis. San Giorgio would do it on the
**entity** axis, against exactly the account [[Harris 2020 on the late plurality of limited
liability]] and [[The Roman universitas makes the JSC case parallelism not convergence]] are already
circling. That is the most consequential single row available to this dataset.

Two disciplines on it, and both come from the source rather than from us. Taviani's own preface says
San Giorgio "was neither a joint stock company nor a bank," and that it is "difficult to define San
Giorgio with these modern terms" — the nineteenth-century German schema he is describing, not
endorsing. So: **use his evidence, not his subjects' categories**, per
[[The morphological matrix is dictated by the shape of the feature space]] and the `AP4` lesson. And
Taviani argues diffusion from Genoa to London and Amsterdam, which makes San Giorgio and the VOC a
**declared co-occurrence** if adopted, and bars any independence claim across the pair. Descent, not
*genetic*; and if the resemblance runs from a shared ancestral practice, **parallelism**.

## Ordering, by which stuck cell each form moves

1. **`casa_san_giorgio` with `voc`.** `LP3`, `TS1`, `CI3`, `CI4`, `AP2`, `MG4`, `FP2`, and `LR1` at
   both ends. The VOC is mentioned in 65 files here and coded in none.
2. **`fraterna` with `compagnia`.** The entity-side partners of the cluster in
   [[Isqa qirad and commenda are a liability-variable triad]]. Buys `TS2=fixed-term` and
   `LR1=unlimited-joint`, each of which currently has **one** instance.
3. **The cooperative pole**, which needs a row that does not yet exist. The *begijnhof* is the
   candidate already argued for in the pooling scheme note — a lay women's community holding real
   property in perpetuity, and there flagged as belonging in this census more than in that one. The
   Dutch *partenrederij* is the second, and connects the entity census to the maritime block.
4. **Not the umbrellas.** `ie` stands above `nakai_fictive_household`, `piaohao` above `hegu_yingu`
   and `hegu_shengu`, `kabu_nakama` above `kabu_local` and `kabu_edo_export`. Each would enter one
   body of evidence twice. The standing rule — code the class, not the entity, where rights differ by
   class — leaves open whether the entity row is admissible at all, and that is a logbook question
   before it is a coding one.

## A protocol point

**The blind test is only available on forms this vault has not already argued.** `voc` appears in 65
files, `kabu-nakama` in 17; `casa_san_giorgio` in one and `partenrederij` in none. So blindness and
cheapness are inversely ordered here, and the two cannot be had at once. The workable split is to
code the well-argued forms **openly and say so in the header**, as the kō batch did, and to reserve
the bundle for the forms where the coder genuinely meets the material for the first time.

## Links

- [[A scheme for extending the cooperative pooling census]]
- [[Entity-shielding]]
- [[Harris 2020 on the late plurality of limited liability]]
- [[The real cut is shielded-and-pooled versus unshielded]]
- [[Transferable claims reconcile lock-in with member exit]]
- [[Identity-wrapper and perpetual-monopoly are distinct shielding facets]]
- [[Perpetuity splits into adaptation and petrification]]
- [[The Roman universitas makes the JSC case parallelism not convergence]]
- [[Natie and kabu-nakama are a convergence pair]]
- [[Count degrees of freedom not cells]]
- [[The morphological matrix is dictated by the shape of the feature space]]
- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]
- [[MOC - Historiography and method]]

## Source

`organizational_forms` 0.8.0 and `loss_mitigation_forms` 0.6.0 as at `dccf130`, read directly; the
zero-instance list and the density figures are computed from `data.csv`, not asserted. Taviani,
*The Making of the Modern Corporation: The Casa di San Giorgio and its Legacy (1446–1720)* (2022),
preface and contents, held and readable (Zotero `KG9A5SRM`). The priority ordering is proposed here
and is nobody else's; the stuck-cell diagnoses are readable off the data.
