---
title: A route clause conditions the investor's peril in three traditions
type: permanent
tags: [commenda, qirad, mudaraba, daman, moral-hazard, principal-agent, risk-sharing, parallelism]
project: HistorEE
source-session: allocation-anchors-blind-coding
database: [loss_mitigation_forms]
created: 2026-08-18
status: seed
---

# A route clause conditions the investor's peril in three traditions

The textbook statement — in the *commenda* and the *qirāḍ* the investor bears the peril — is **conditional in all three of the legal traditions that state it**, and the condition is the same one: the agent must stay inside a stipulated route envelope. Step outside it and the whole peril moves to him.

- **Latin statute.** Statute of Dubrovnik 1272, VII,50: maritime *fortuna* is in principle the *commendator*'s, but if the *tractator* leaves the Adriatic (*Culfum*) without permission, *totum periculum* is his (Held 2025, 12).
- **Ḥanafī ḥadīth-warrant.** Al-Sarakhsī cites al-ʿAbbās b. ʿAbd al-Muṭṭalib giving capital on condition the *muḍārib* "go neither on sea, nor down the oasis, nor buy a live animal", and "if the *muḍārib* did so, he had to guarantee the capital due to the risks involved" — the Prophet is reported to have approved the stipulation (Ramli 2018, 97–98).
- **Mamlūk formulary.** Al-Nuwayrī's model *commenda* clause has the agent travel "wherever he wishes in Islamic lands **on safe routes**" (Ackerman-Lieberman 2011, 664).
- **Genoese notarial practice.** Across 6,764 *commenda* ties, 1154–1315, the traveller "swore to abide by certain instructions concerning the use of the money, such as **restrictions on destinations or goods transacted**" (van Doosselaere 2009, 65).

Latin statute, prophetic report, notarial formulary and the largest surviving corpus of the contracts themselves — four traditions, three centuries, one drafting device. Note that Genoa and the ḥadīth of al-ʿAbbās restrict the **same two things**: where he may go and what he may buy.

## Why the device exists

Because the shield creates the hazard it is drafted against. Ackerman-Lieberman puts it in modern terms: the agent's freedom from liability "could actually encourage him to invest in a suboptimally risky asset", which is the standard adverse-selection problem of a payoff bounded below at zero. The route clause is the cheapest available bound on the agent's choice set — cheaper than monitoring, and verifiable after the fact from the voyage itself.

That is the same reasoning [[Skin in the game is asymmetric in the mudaraba]] finds in the *taʿaddī*/*taqṣīr*/*mukhālafa* doctrine: the tradition noticed that a profit share alone left the agent's skin too thin and built a designed correction. The route clause is the *ex ante* half of that correction and the liability doctrine is the *ex post* half.

## Do not call this convergence

A shared ancestral condition is not merely possible here, it is the majority view — the *commenda* very likely arrives in Italy from the Islamic Mediterranean. The word is **parallelism**, or simply borrowing. See [[Homoplasy is the finding not the noise]] and [[Borrow the diagnostics not the tree]].

## Consequence for the coding

`RB1=capital-provider` is unqualified in every allocation row in `loss_mitigation_forms`, and in every one of them it overstates: the allocation holds *within the mandate*. This is not an argument for a new characteristic — a risk-window cell would read `1` for the whole sea-loan family too, where the deviation rule does the same work, and so would buy no discrimination. It is an argument for never reading `RB1` as unconditional.

## Links

- [[The commenda and the qirad do not separate on loss allocation]]
- [[Skin in the game is asymmetric in the mudaraba]]
- [[The qirad envelops the sea loan]]
- [[Homoplasy is the finding not the noise]]
- [[Borrow the diagnostics not the tree]]
- [[commenda]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Islamic contract doctrine]]
- [[MOC - HistorEE]]

## Source

Blind coding session, 18 August 2026. Held 2025, 12 and 20–22; Ramli 2018, 97–98; Ackerman-Lieberman 2011, 664 (citing al-Nuwayrī, *Nihāyat al-Arab* 9:19).
