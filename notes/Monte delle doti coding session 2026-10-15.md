---
title: Monte delle doti coding session 2026-10-15
type: reference
tags: [contingent-claim, risk-sharing, risk-pricing, verification, coding-ontology]
project: HistorEE
source-session: monte-delle-doti-coding
database: [loss_mitigation_forms, organizational_forms]
created: 2026-10-15
status: seed
---

# Monte delle doti coding session 2026-10-15

**Withhold this note by slug (`monte-delle-doti-coding`) from any bundle that codes or recodes the Florentine dowry fund, another Italian *monte*, or any dowry or survivorship form.** It states every cell value of `monte_doti_florence` and the reasoning behind the hard ones.

This note records the blind coding and the same-day application of `monte_doti_florence`, the Florentine *monte delle doti*, into `loss_mitigation_forms`: 26 cells, `LM-0796`–`LM-0821`, tradition `Tuscan (Florentine)`, period `1425-1530`. The full record is in `HistorEE_codebooks/records/`: the coding notes (`NOTES-monte-delle-doti-coding-2026-10-15.md`), the filled priors, the prompt, the rows as proposed, and the operator's brief in two parts. The logbooks carry the 2026-10-15 entries in 2, 4 and 5.

## How it was run

- **Operator and coder in separate chats**, on the [[Blind re-coding workflow - operator, coder, application]] pattern. The bundle was minimal: the doctrine files, both loss vocabularies, the risk-pooling view, the live `data.csv`, and five works in `sources/`. It had no vault, no logbooks and no `records/` beyond the priors template.
- **The priors were written and hashed before any source was opened** (sha256 `b66aa269…817ca`), and MS committed and confirmed them before reading began. All 26 cells were fixed before anything about the matrix was computed. The operator's withheld predictions were read only after the coding record was frozen.
- **One witness.** Molho 1994 chs. 2–3, Kirshner and Molho 1978, Kirshner 2015 ch. 4, and Morrison, Kirshner and Molho 1977 and 1985 are all Kirshner, Molho or their co-authors, working from the fund's own registers. Their agreement is not corroboration, so the cap is `medium` and no cell is `high`. See [[Split provenance into priority and independence]].
- **Figures from the page.** Every figure and every Latin or Italian clause entering a cell was read from the page image, not from the OCR layer. Nine cells are `articulated`, each on a clause printed in the sources: the founding enactment PR 114 of 23 February 1424/5, the 1434 eligibility clause, the 1437 *tamquam vere mortua* clause, a 1477 certificate and law, and two deliberations of the Monte officials.

## The row

| cell | value | conf. | cell | value | conf. |
|------|-------|-------|------|-------|-------|
| `MC1` | spreading | medium (MS) | `PY3` | 1 | medium |
| `MB1` | territorial-subject | medium | `LS1` | pro-rata | low |
| `MB2` | 1 | medium | `LS2` | 0 | medium |
| `MB3` | voluntary | medium | `LS3` | `.NR` | — |
| `CN1` | ex-ante-lump | medium | `VF1` | official-adjudication | medium |
| `CN2` | proportional-to-stake | medium | `VF2` | mixed | medium |
| `CN3` | `.NA` | — | `GV1` | external-administered | medium |
| `HZ1` | mixed | medium | `DR1` | open-ended | medium |
| `HZ2` | P | low | `DR2` | `.NA` | — |
| `PY0` | individual-draw | low | `RB1` | capital-provider | medium |
| `PY1` | life-event | medium | `RB2` | shared | low |
| `PY2` | `.NR` (no fit) | — | `RB3` | `.NR` | — |
| `PR1` | P | low | `RB4` | `.NA` | — |

That is 20 substantive cells. Owner-shielding (`LS3`, `RB3`, `RB4`) learned nothing. **No new value-instance anywhere**: the row adds a case, not a state.

## The finding: a contingent claim sold by the commune, not a pool

**The test that decided `MC1`: does any member's payout depend on another member's fate?** In the tontine it does: the survivors share what the dead leave ([[The tontine is pooling in form and dispersal in function]]). In the dowry fund it does not. A married girl's dowry is fixed by deposit and term whether one girl in five dies or one in two.

The forfeits of the dead do finance the survivors' yield; Molho computes the commune's real cost as reduced by them. But the commune takes those forfeits as its own surplus: the law of 29 March 1452 drew 300,000 florins of credits from the dowry account because "the credits of this account are in great excess because of the girls who have already died". The commune also bears the shortfall. The cross-subsidy therefore runs through an outside party's price and residual, not through a mutual. In Harris's terms that is **spreading**: "a father's material burden shifted to the polity" (Molho 32), bought with "the equivalent of a premium" (43).

The coder's prior was `pooling`; the operator predicted `allocation`. MS confirmed `spreading` and raised it to `medium`.

**Consequence: the row sits outside the committed risk-pooling view**, whose filter is `MC1 = pooling`. That is the filter working, not a gap.

**Pricing is half-present (`PR1 = P`), and the commune said so.** A provision of February 1462/3 calls the longest term of "greater utility" to the fund "per cagione della morte". The price was set before the event and with death in view, but never on the individual girl: no rate varies with age, and the commune acted "in the absence of actuarial tables". This is a fourth datum for [[Pricing is orthogonal to mitigation mechanism not a stage of it]]: a spreading form priced by term alone, beside the tontines priced by class or not at all.

**The hazard is mixed (`HZ1`).** "Recurrent epidemics accounted for 38 per cent of the total mortality experienced by girls enrolled in the Dowry Fund" (Morrison, Kirshner and Molho 1985, 528). The commune's capacity to pay was perfectly covariate across claimants: instalments from 16 August 1441, and one-fifth in cash from 1475. A spreading form whose counterparty is itself exposed to the covariate shock is the case [[Pooling's sign is set by the correlation of its baskets]] does not yet cover.

**Verification is adjudicated and mixed (`VF1`, `VF2`).** *Deliberaverunt quod Baldus supradictus habeat dotem suam, recepta fide quod dictus Baldus consumavit dictum matrimonium*; and *in quantum fuerit consummatum matrimonium et dos confessata et soluta ghabella*. The officials verified the event (a consummated marriage) and the claimant's compliance (the confessio dotis executed, the gabella paid, the father's consent, and later the husband's tax standing). This bears on [[Institutions substitute state-verification for outcome-inference as ruin exposure rises]]: here the state verifies before paying a promise it made, not before relieving a loss.

## Period: one dated change, no split

The fund ran for over a century under changing legislation, so every cell was tested across 1425–1530.

- **April 1433**, the refund of capital on a girl's death, is the principal change. It is **a variant in every cell it touches**, because it changes how much the depositor loses, not who bears the loss. The coder's prior expected a split here; the operator predicted a variant, and the operator was right.
- **Only `RB2` changes value.** The commune alone carried the price of Monte credits until 18 August 1446; claimants shared it thereafter, systematically from 21 May 1472.
- **MS ruled no split.** It is one cell, and its first phase is codable only by borrowing `MC1`'s reading of the commune as the outside party.

## Defects the row exposed, flagged and not repaired

- **`PY0`.** "individual-draw" is glossed as rotation, lot or auction, so a draw triggered by an event has no value.
- **`PY2`.** It has no value for a payout fixed by deposit and term.
- **`RB1`, `RB2`, `RB4`.** The locators presuppose a capital provider and a labour provider. A commune that takes deposits and owes a contingent sum is a counterparty-obligor the vocabulary cannot name. MS kept `RB4`'s `labour-party` locator; the defect waits for a second form that needs it.
- **`CN2`.** It has no value for a contribution the member chooses.
- **`RB3`.** The only security in the sources secures the husband's duty to restore the dowry to his wife: the guarantors in the confessio dotis, and the law of 1441. Nothing secures anything owed to or by the pool.
- **Dating disagreements inside the one witness.** The law of PR 132, ff. 6v–9r is dated a year apart (24 March 1440/1 in Molho against 24 Mar. 1441/2 in Kirshner 2015), and the Seven Percent Fund law is dated 14 November in Molho against 14 October 1478 in Kirshner 2015. No cell depends on the day.

## Scores

- **The coder's own priors** were falsified on `MC1`, `MB1`, `VF1`, `RB1` and `RB2`, and on the predicted 1433 split. They also dated the first payment crisis wrongly: it is 1441, not the 1470s.
- **The operator's withheld predictions** hit on 14 of 23 cell lines. Four of the misses run toward more found: `LS1`, `VF2`, `RB1` and `RB2` took a rule or a value where silence or a simpler state was predicted. One, `LS3`, runs toward the weaker claim.
- **Row level:** the operator's prediction that the coder would flag, unprompted, that an organizational row would code the Monte comune missed. The coder never raised it.
- What these scores are worth, and why counts mislead here: [[Count degrees of freedom not cells]].

## Decided at application (MS)

- **Co-occurrence.** `compagnia@organizational_forms` declared at `same-polity`, in both directions.
- **No organizational row**, on the operator's finding that the fund's administration and assets were the Monte comune's.
- **Kirshner and Klerman, "The Seven Percent Fund"** (Kirshner 2015, ch. 5): a term count first, and an open recoding pass on `RB2`, `LS1`, `LS2` and `PY3` only if it treats dowry claimants. Until 1496 they were the 7 percent fund's only creditors.

## Open

- Acquire the edition of PR 114 in Kirshner, "Pursuing Honor While Avoiding Sin" (pp. 234–239). It would let the articulated cells rest on the enactment rather than on Molho's ellipses, and it is the condition for reopening an organizational row.
- [[Archivio di Stato di Firenze]] still says the *Monte delle Doti* is "not in the census". It now is, as `monte_doti_florence`, and that note also calls it a claim "on a pooled fund", which the coding rejects.

## Where this is soft

- `MC1` turns on Harris's trichotomy, which was drawn for maritime perils and fits a polity's contingent claim badly. Spreading is the least wrong of three, and that is the most this coding claims.
- Every cell rests on one scholarly witness, reading one archive.
- The row stops at 1530 while the fund ran on into the 1570s.

## Links

- [[Blind re-coding workflow - operator, coder, application]]
- [[A blind is a property of the channel not of the dataset]]
- [[The tontine is pooling in form and dispersal in function]]
- [[The tontine's chronology defeats the hazard-to-pricing staging]]
- [[Pricing is orthogonal to mitigation mechanism not a stage of it]]
- [[Insurance is a split-off from the sea loan not a coordinate mechanism]]
- [[Pooling's sign is set by the correlation of its baskets]]
- [[Institutions substitute state-verification for outcome-inference as ruin exposure rises]]
- [[Split provenance into priority and independence]]
- [[Count degrees of freedom not cells]]
- [[Archivio di Stato di Firenze]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - HistorEE]]

## Source

Coding and application session `monte-delle-doti-coding`, 2026-10-15, `claude-opus-5-5` at effort `high`. Sources:

- Molho, Anthony. 1994. *Marriage Alliance in Late Medieval Florence*. Cambridge, MA: Harvard University Press. Chs. 2–3 and App. 1.
- Kirshner, Julius, and Anthony Molho. 1978. "The Dowry Fund and the Marriage Market in Early Quattrocento Florence." *Journal of Modern History* 50: 403–438. `10.1086/241732`.
- Kirshner, Julius. 2015. *Marriage, Dowry, and Citizenship in Late Medieval and Renaissance Italy*. Toronto: University of Toronto Press. Ch. 4 and notes. `10.3138/9781442664517`.
- Morrison, Alan S., Julius Kirshner, and Anthony Molho. 1977. "Life Cycle Events in 15th Century Florence: Records of the Monte delle Doti." *American Journal of Epidemiology* 106: 487–492. `10.1093/oxfordjournals.aje.a112496`.
- Morrison, Alan S., Julius Kirshner, and Anthony Molho. 1985. "Epidemics in Renaissance Florence." *American Journal of Public Health* 75: 528–535. `10.2105/AJPH.75.5.528`.

The DOIs come from the bundle README and were not re-resolved in this session: **verify**.
