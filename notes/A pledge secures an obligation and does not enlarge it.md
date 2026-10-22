---
title: A pledge secures an obligation and does not enlarge it
type: permanent
tags: [limited-liability, coding-ontology, bottomry]
project: HistorEE
source-session: residual-default-coding
database: [loss_mitigation_forms]
created: 2026-10-22
status: seed
---

# A pledge secures an obligation and does not enlarge it

A borrowing member who pledges his land for his own repayments is no more exposed than he was before: the pledge changes **how** his debt is collected, not **how much** he owes. Coding the pledge as exposure beyond contribution (`LS3 = 1`) confuses security with liability, and the census had done exactly that on three kō rows while reading the same clause as no compulsion at all (`CN3 = .NR`). One instrument cannot be both.

## The two questions the pledge clause answers

- **Can non-payment be compelled?** Yes: the rules create an instrument whose only function is collection. That is `CN3`, and it is now `1` wherever the rules require a bond, pledge or sureties (ruling 1, 2026-10-22).
- **Is the member exposed beyond what he contributed or agreed to contribute?** Not by his own pledge. He agreed to repay; the pledge enforces the agreement. He is exposed beyond it only by one of two routes, which is ruling 2:
  - **the association route**: he answers for obligations not his own — guarantees he must give for other members, his group's advances, an expelled member's share he inherits;
  - **the debtor route**: he is expressly liable beyond the pledge, with his person or his whole estate.

## The maritime precedent fixes the debtor route

The census's sea-loan family already coded this distinction, and it is the one that separates the two forms ([[The Bodmerei shield was a default rule and Amsterdam contracted out of it]]): the ancient sea loan bound the debtor 'unbeschraenkt mit seinem gesamten Vermoegen' (`sea_loan LS3 = 1`), the *Bodmerei* confined liability to the pledged ship (`bottomry LS3 = 0`), and Amsterdam contracts that added 'zijn persoon ende alle sijne goederen' contracted back into personal liability (`bodemerij_amsterdam LS3 = 1`). A contract naming only the pledge was coded `.NR`, not `0`. **The kō rows had drifted from that usage**: they coded a pledge alone as `1`. The ruling brings them back into line, and three `ko_mitarai_*` cells went to `.NR`.

A first wording of the ruling admitted only the association route; it would have made `sea_loan`'s `1` wrong. The correction came from counting the column before entry, not after.

## What it changes

- On the seventeen 1936 reserve kō, `LS3` went from 17 of 17 `1` — a column that merely followed `RB3` — to 8 `1` and 9 `.NR`, separating kō in which members guarantee one another from kō in which each drawer secures himself.
- The comparative concept is the same on both sides of the census: does a participant's downside stop at his own obligation?

## Links

- [[RD-test coding and re-test session 2026-10-22]]
- [[The Bodmerei shield was a default rule and Amsterdam contracted out of it]]
- [[Yui 1934 - the law of ko and who bears a member's default]]
- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]

## Source

Session `residual-default-coding`, 22 October 2026: `HistorEE_codebooks/records/RULINGS-residual-default-2026-10-22.md` (rulings 1 and 2), the `CLARIFIED 2026-10-22` sentences in the `CN3` and `LS3` definitions, recodings `LM-R0076`–`LM-R0079`, and logbook 1, 2026-10-22. The sea-loan quotations are from the census rows' notes (Schuster 2005; Winkelman 1983), not re-read.
