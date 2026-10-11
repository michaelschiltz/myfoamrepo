---
title: The commenda family fixes the allocation of loss and varies its proof
type: permanent
tags: [commenda, verification, amana, moral-hazard, comparative]
project: HistorEE
source-session: comanda-commenda-retrieval-report-2026-10-09
database: [loss_mitigation_forms]
created: 2026-10-09
status: seed
---

# The commenda family fixes the allocation of loss and varies its proof

Across the unilateral forms of the western family the allocation of loss is invariant and the machinery for establishing a loss is not. The Italian `commenda_alloc`, the Catalan `comanda_alloc` and `qirad_alloc` agree that peril and market loss fall on the capital provider, that the agent is discharged on total loss, and that he answers only for fault. They disagree on **how** a claimed loss is shown, and that is where each jurisdiction's legal apparatus becomes visible.

**Three modes for one rule.**

- **Dubrovnik: documentary.** The periculum clause carries its own standard, *maris et gentis clarefactum*: the loss must be made clear (Held 2025, 20–21). Live `commenda_alloc VF1 = documentary`, imported from a neighbouring jurisdiction's statute and disputed (pilot worksheet entry 16).
- **Venice: adjudication.** The pilot's arm S read González de Lara (2002, 258–259) as the state generating verifiable information to adjudicate disputes and proposed `official-adjudication`. Unadjudicated.
- **Catalonia: a sworn self-account, rebuttable.** The commendatary's account is received and, on suspicion, sworn, and he is then believed unless the investor proves otherwise (*Consolat de Mar*, cap. 279). A loss he cannot explain with *iustes raons* sends him to prison (cap. 220); a failed purchase is proved by witnesses on the spot (cap. 216). None of `communal-attestation`, `official-adjudication` or `documentary` fits, so `comanda_alloc VF1` was `.NR` as a **value-set misfit**, not as silence *(until 2026-10-11: see below)*. See [[The Catalan maritime comanda puts the whole capital loss on the investor]].

**The missing value may have a second instance.** The Catalan rule is close to the trustee's position in fiqh: *laysa ʿalā al-amīn illā al-yamīn*, nothing is due from the trustee but the oath, with the owner alleging transgression bearing the proof ([[The amana-daman structure refuses to infer fault from loss]]). If that holds for the *muḍārib*, `qirad_alloc VF1`, now `.NR`, would take the same value, and the rule against adding a value before a form instantiates it (the `AP4` lesson) would be met twice. The amana note's caveat binds here too: the attestations traced are Imāmī and Ḥanbalī, not Ḥanafī or Mālikī. *(The Ḥanafī attestation was found on 2026-10-11: see below.)*

**The *ʿisqa* shows the variable running the other way.** The *heter ʿisqa* keeps the loss-sharing term and sets the proof of loss at a bar that cannot be met, so that the nominal residual claim pays as a fixed coupon ([[The heter iska restores the fixed return by evidentiary barrier]]). The Catalan custom lowers the bar to the agent's oath; the *heter* raises it to make loss unprovable. Same allocation on paper, opposite outcomes in payoff, and the difference sits entirely in `VF1`.

**Why it matters.** The project's claim is that institutions substitute verification of a state for inference from outcomes as exposure to ruin rises ([[Institutions substitute state-verification for outcome-inference as ruin exposure rises]]). A family that holds allocation fixed and varies proof is the place to watch that substitution operate, and the Catalan custom's choice, to believe the agent's sworn account rather than read fault off the loss, is the outcome-refusing pole. That *peril* is the explicitly drafted variable in the Latin tradition ([[Which peril gets a clause is set by the tradition's doctrinal problem]]) is the same point from the clause side.

## Where this is soft

The three Latin modes come from three layers: a statute, an economist's reading of state institutions, and a customary compilation. They are not yet comparable as practice. Whether to add a `VF1` value was a theory decision; MS took it on 2026-10-11 (below).

## Ruled 2026-10-11

`VF1` gained `claimant-oath` (`records/RULINGS-comanda-adjudications-2026-10-11.md` in HistorEE_codebooks, ruling 2): the loss is established by the claimant's own account, on oath or subject to oath on demand, with no third-party verifier unless the counterparty contests. **Defined by mode only**: whether the oath is decisive (the bailee's oath of Exodus 22:10–11) or rebuttable (the *Consolat*, cap. 279; the *amīn*'s oath yielding to *bayyina*) is a burden-of-proof question kept in the notes. `comanda_alloc VF1 = claimant-oath` is the first instance. `qirad_alloc` and `isqa_alloc` stay `.NR` until Udovitch 1970, "Theory and Practice of Islamic Law", and Mishnah *Shevuʿot* 7:8 are read [verify both]. The *heter ʿisqa* point above is unaffected: it is the same value-question at the opposite bar.

## Coded 2026-10-11 (iii): three oath instances

The prediction above held. `qirad_alloc VF1 = claimant-oath` from al-Sarakhsī, *al-Mabsūṭ* 22, 27 and 51: the capital is a trust like a deposit, the *muḍārib*'s word is accepted because he is a trustee, and *al-qawl qawl al-muḍārib maʿa yamīnihi* where the amount of capital is disputed; his word is accepted when he says the property perished in his hand, as the sales agent's is. That is the Ḥanafī rule, which the amana note's caveat had said was untraced. `isqa_alloc VF1 = claimant-oath`, low, on the paid bailee's oath (Mishnah *Bava Metzia* 7:8). The family now reads: **oath** (Catalonia, the *qirāḍ*, the *ʿisqa*), **documentary** (Dubrovnik), **official adjudication** (Venice, disputed). The oath instances share a substrate and are parallelism, not three independent findings; the decisive/rebuttable difference — Exodus's "the owner shall accept it" against the *Consolat*'s proof to the contrary — lives in the cell notes, not in the value. [Edition: Dār al-Maʿrifa, Beirut, per the transcription's title page; identified 2026-10-11, below.]

## Coded 2026-10-11 (v): the four branches agree on what is proved

`qirad_alloc VF2 = mixed`. What the *muḍārib* swears to is that he did not consume the capital and did not lose it through neglect (*Mabsūṭ* 22, 108; the edition is Dār al-Maʿrifa, Beirut), so his oath establishes both that the loss happened and that he did not cause it. `commenda_alloc`, `comanda_alloc` and `isqa_alloc` were already `mixed`. **The family therefore holds the object of proof fixed as well as the allocation, and varies only the mode** — a document, a forum, or the agent's oath. That sharpens the title's claim: what varies is who or what attests, not what must be attested. A first recommendation, `loss-occurrence`, read an al-Sarakhsī passage on an alleged loan (p. 94) as putting fault outside what is verified; it was withdrawn before application once p. 108 was found. See [[The amana-daman structure refuses to infer fault from loss]], now with its Ḥanafī attestation.

## Links

- [[Ragusan collegantia is unilateral and Venetian collegantia is bilateral]]
- [[The commenda and the qirad do not separate on loss allocation]]
- [[Skin in the game is asymmetric in the mudaraba]]
- [[commenda]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Islamic contract doctrine]]
- [[MOC - HistorEE]]
