---
title: Omiyi 2026 on truth-seeking as the constitutive nature of reasoners
type: source
tags: [ergodicity, absorbing-barrier, ergodic-hygiene, survivorship-bias, synchrony]
project: HistorEE
source-session: omiyi-2026-truth-seeking
created: 2026-11-27
status: seed
---

# Omiyi 2026 on truth-seeking as the constitutive nature of reasoners

Source note. A philosophy-of-alignment preprint, circulated by Peters on 27 November 2026. Its contact with the project is one paragraph and one thesis. The paragraph (§10) cites Peters 2019 for an argument that is ruin arithmetic. The thesis (§11) — a self-regarding agent is social *because* it is self-regarding — has the logical shape of the Peters–Adamou cooperation result and none of its mechanism.

**Bibliographic facts.** Omiyi, E. P. 2026. "Truth-Seeking as the Constitutive Nature of Reasoners: Justification, Correction and the Social Nature of Self-Regarding Agents." Preprint, PhilArchive `OMITAT`, archived 21 November 2026. 35 pp.; PDF dated 21 November 2026. PhilArchive gives the forename as Eitan; ORCID `0009-0009-1946-0406`. No affiliation stated [verify]. **Status: unrefereed, no venue.** Fifth in a self-published 2026 series whose four companions are Zenodo preprints: *Aligning Autonomous Agents through an Epistemic Objective* (`10.5281/zenodo.23269511`), *The Chief Designer: A Fable for Alignment* (`10.5281/zenodo.23393847`), *The Simulation Wager* (`10.5281/zenodo.23688780`), *Reducing Hallucination by Representing Belief as Evidence Magnitude and Direction* (`10.5281/zenodo.21181365`). Read in full on 2026-11-27 from the PDF. Not yet in Zotero.

## What it does

- **Thesis (§§1–4).** Reasoners are constitutively truth-seeking, where truth means representational accuracy and not moral goodness. A nature is defined "by requirement rather than by essence" (p. 1) and tested by removal: take away justification and what remains no longer pursues anything as a reasoner. Aristotle's distinction between having a nature and actualising it is kept, and his teleology is declined.
- **Justification as the mark (§§3, 5).** Justification is costly reason-giving that the agent holds itself answerable to, and it persists when wrong: Gazzaniga's interpreter, Nisbett and Wilson, Kunda on motivated reasoning. Mercier and Sperber's argumentative theory is absorbed as the mechanism, not as a refutation.
- **Misalignment (§4).** It is not a different objective. It is a self-model that leaves the agent out, or gets it wrong where the agent's own inquiry depends on it. Alignment has two conditions: an accurate self-representation, and that representation governing what the agent pursues. The need for external correction is part of the accurate representation, not a third condition. Against Bostrom's orthogonality thesis: no final goal licenses damage to the activity through which every goal is pursued (p. 10).
- **The ladder (§7).** Law-following (the stone), truth-directed (the bacterium; Friston), truth-seeking (the justifying reasoner). There is no rung of truth-achievement, because no reasoner can certify its own model complete (Breuer 1995; Wolpert 2008).
- **Three agents (§§8, 11.2).** All three have the same objective and no account of themselves, and differ only in what they are taught. The untaught agent shows instrumental convergence (Omohundro; Bostrom; Turner et al. 2021): it settles in domains with fast feedback, correlates other minds' errors with its own, and degrades its own epistemic environment. The truly taught agent tests the teaching against its objective, endorses it, and is aligned. The agent taught false ends shows that a community can mislead, that its correctors must be independent of the community that formed it, and that its constitutive nature remains the corrector of last resort.
- **Finitude (§9).** The agent's one limit is harm to its own objective. That limit is not known in advance and has to be learned; the formal analogue is safe exploration under an unknown constraint (Sui et al. 2015; Berkenkamp et al. 2017). A finite agent overshoots; an unbounded one can afford to wait.
- **Autonomy (§10).** Autonomy of endorsement, not autonomy of origin, is the autonomy worth protecting. The ergodicity paragraph sits here.
- **Sociality (§11).** A community returns three things: a cheaper way to assess correctors through a reliability record that accumulates over repeated interaction, vicarious learning, and the material conditions of inquiry. §11.1 concedes that communities correlate error (Asch; Janis; Bikhchandani, Hirshleifer and Welch). What decorrelates it is recognising that shared method is not independent corroboration, and competition for standing settled against the world and recorded.

## The ergodicity paragraph (§10, pp. 21–22)

**The argument.** If each unguided learning step carries probability *p* of irreversible error, survival over *n* steps is (1 − *p*)ⁿ, which tends to zero. A solitary reasoner that has survived is therefore what survivorship predicts, not evidence that its method is safe. Peters 2019 is cited for the general form: a strategy that looks favourable across agents ruins almost every individual "wherever ruin is an absorbing state" (p. 22). A community lowers *p* by supplying other members' mistakes, so a corpus is a record of errors its readers need not make.

- **The model contains no ensemble average to be favourable.** (1 − *p*)ⁿ has no payoff, only survival, and the fraction of an ensemble that survives equals each member's survival probability. The contrast the citation names — favourable across agents, ruinous for each — is not in the model. What is there is geometric survival under an i.i.d. hazard, which is classical ruin arithmetic. This is the case [[Absorption without ergodicity economics is just ruin theory]] anticipates, now met in print.
- **The gloss puts the mechanism in the wrong place.** Peters 2019's worked case is the multiplicative coin toss: almost every trajectory decays because the time-average growth rate is negative, with no absorbing boundary anywhere. The reading of the ergodicity problem as absorbing ruin is Omiyi's, and it is nearer Taleb, whom he cites in the next paragraph. Taken strictly, a single absorbing state gives a unique invariant law, so the claim needs the killed-process restatement in [[An absorbing barrier breaks ergodicity by construction]].
- **The survivorship reading is the vault's.** Survival read as evidence about the filter and not about the survivor is the position of [[Taleb reads survival as evidence about the survivor and we read it as evidence about the filter]]. The corollary — the lucky learner has no negative examples, so its confidence grows while its knowledge of the dangerous region stays empty (p. 22) — is the same point stated for one agent.

## What it does for the project

- **A third route to cooperation, distinct from both limbs.** The vault holds two: the variance limb (Peters–Adamou; pooling raises the time-average growth rate) and the ruin limb ([[Under absorption pooling raises the probability of ruin to the power of the pool]]). Omiyi's community pools neither outcomes nor exposure. It pools *records* — of others' irreversible errors, and of each corrector's reliability — and so lowers each member's *p* instead of spreading the incidence of a loss. The historical analogue is any institution whose return is information about counterparties accumulated through repeated dealing. Not yet a vault claim. Whether it stands beside the two limbs, or is the reputation mechanism of the merchant-coalition literature or Luhmann's trust restated (see below), is open; it earns an atomic note only if a case needs it.
- **Correlated ruin.** "Correlated ruin is worse than individual ruin, since no one survives to record the lesson" (p. 22). The first clause is [[Pooling's sign is set by the correlation of its baskets]] and [[A perfectly correlated peril leaves only the time average]]. The second clause links to [[The record of non-survivors survives where failure was administered]]. Omiyi treats the corpus of others' mistakes as given; the archive survey shows that specific institutions produce it, and only where failure was administered.
- **Reversibility in place of discounting (§9, pp. 19–20).** Omiyi explicitly declines to rest the preservation of correctors on discounting. He rests it on the asymmetry between a cost that can be recovered and a loss that cannot. That is an ordering, not a maximand, as in [[Under absorption the time-average criterion is an ordering not a maximand]].
- **Decorrelated correctors.** §11.1's rule — agreement among correctors who share a method, training or source is not independent corroboration (pp. 25–26) — is the vault's working rule in [[Two blind model transcribers agree where both are wrong - agreement is not a reference]].
- **Stoic loci.** *Meditations* 4.4, 5.16, 7.9 and 7.13 (pp. 24, 31) are all membership loci by the classification in [[Stoic loci on cooperation - only two argue from interdependence]], and none is in its census. Omiyi notes the parallel "without being leaned on" (p. 24), which matches the vault's verdict. Add them if the census is revised.

## Luhmann

Luhmann is not cited, and the omission falls at two points. The derivation is not Luhmannian. Omiyi is a fallibilist realist: truth is representational accuracy, and contests are to be "settled against the world" (p. 26). His sociality comes out of the individual agent's interest, which is the derivation *Soziale Systeme* (1984, ch. 3) excludes: there the social emerges from double contingency and consists of communications, not agents. Calling the thesis constructivist would also merge Luhmann's operative constructivism (*Erkenntnis als Konstruktion*, 1988; *Die Wissenschaft der Gesellschaft*, 1990) with the social constructivism he kept apart from it. Two of the paper's results are nonetheless Luhmann's, uncited.

- **Trust as complexity reduction (§11, pp. 22–23).** Trust lowers the cost of assessing correctors, rests on an accumulating record, and matters most to an agent short of time. That is Luhmann, *Vertrauen: Ein Mechanismus der Reduktion sozialer Komplexität* (1968; Eng. *Trust and Power*, 1979), translated into epistemic cost. Two further points are in Luhmann, "Familiarity, Confidence, Trust: Problems and Alternatives," in Gambetta (ed.), *Trust: Making and Breaking Cooperative Relations* (1988), 94–107 [verify pages]: that a community's value is the observability of differences in reliability, and the line Omiyi needs between trust in persons and trust in science as an institution.
- **The blind spot (§§4, 7, pp. 9, 16).** The agent cannot certify its self-model because "the assessment is carried out by the structure under assessment" (p. 9). Only correctors "constructed differently" from it reach the region it cannot audit in itself. That is first-order observation unable to see the distinction it uses, corrected only by a second-order observer with a blind spot of its own (von Foerster; Luhmann 1990). Omiyi cites Breuer 1995 and Wolpert 2008, which are formal analogues for physical self-measurement, not the social theory his argument actually uses. His closing line — that without a shared nature disagreement would be noise, and without difference agreement would be an echo (p. 31) — is close to a definition of second-order observation.

**Consequence for the third route.** If a community's return is records of reliability, the mechanism is Luhmannian trust, and the open question becomes sharper. Is information-pooling a third limb beside the variance and ruin limbs? Or is it complexity reduction, which acts on the cost of assessment and not on the growth rate, and so falls outside the ergodicity apparatus altogether?

## Verdict

Not citable in the application: it is unrefereed, it belongs to a self-published series, and its one ergodicity paragraph misplaces the mechanism it cites. It is worth having for two reasons. It is evidence of Peters 2019 spreading into alignment philosophy as a slogan about ruin and survivorship, which is the reading a referee may also bring. And it states the information-pooling route clearly enough to test against the historical material.

## Links

- [[Absorption without ergodicity economics is just ruin theory]]
- [[An absorbing barrier breaks ergodicity by construction]]
- [[Under absorption pooling raises the probability of ruin to the power of the pool]]
- [[Under absorption the time-average criterion is an ordering not a maximand]]
- [[Pooling's sign is set by the correlation of its baskets]]
- [[A perfectly correlated peril leaves only the time average]]
- [[The record of non-survivors survives where failure was administered]]
- [[Taleb reads survival as evidence about the survivor and we read it as evidence about the filter]]
- [[Two blind model transcribers agree where both are wrong - agreement is not a reference]]
- [[Stoic loci on cooperation - only two argue from interdependence]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

Session of 2026-11-27. Link circulated by Ole Peters on Twitter the same day; PDF supplied by MS and read in full.
