---
title: RD-test coding and re-test session 2026-10-22
type: reference
tags: [risk-sharing, coding-ontology, character-independence, limited-diversity]
project: HistorEE
source-session: residual-default-coding
database: [loss_mitigation_forms]
created: 2026-10-22
status: seed
---

# RD-test coding and re-test session 2026-10-22

**Withhold this note by slug (`residual-default-coding`, `residual-default-retest-scan`, `residual-default-retest-operator`) from any bundle that codes kō rulebooks from the 1936 Nōrinshō volume, the 1915 Finance Ministry survey or 『世態調査資料』第三十六號.** It states cell values for thirty-six rulebooks and the operator's predictions.

One chat, five jobs on one test characteristic: the blind coding of the first test, three rulings and their application to the census, a catalogue scan for an independent re-test, the operator's work for the re-test, and its scoring. The re-test itself was coded blind in a separate chat outside the Claude project (`residual-default-retest-coding`). The full record is in `HistorEE_codebooks/records/`; the logbooks carry the 2026-10-22 entries in 1, 4 and 6.

## What was tested

`RD-test` asks: *once a member has drawn from the fund and stops repaying, and his own security is exhausted or fails, who does the instrument make liable for what remains unpaid?* Values `fund`, `all-members`, `standing-subgroup`, `officers`, `deferred`. It was fixed in logbook 6 (2026-10-22 (ii)) from the open half of the 1936 volume ([[Who answers for a ko member's default was drafted not given]]), with the test fixed before the reserve was read: **does `RD-test` take values that `RB3`, `LS1`, `LS3`, `CN3` and `GV1` do not predict?** That is test 4 of `CHARACTER-CODING.md`, discriminant validity.

## First test: seventeen reserved kō of the 1936 volume

- **Coded blind**, 102 cells, priors committed (`d50331a`) before any page was opened. All cells fixed before any comparison, with one recorded incident: two `CN3` cells edited and reverted while kō 18 was coded.
- **`RD-test`:** `.NR` 12; one each of `standing-subgroup` (kō 7, the 講クビリ), `officers` (kō 12, the 世話人 guaranteeing the convener), `all-members` (kō 25, low), `deferred` (kō 26), `fund` (kō 35, low, on the same clause as `LS1 = residual-on-fund`).
- **Scored fail on rule 6's second limb**: four eligible kō in three villages, no pair agreeing on all five predictors, three weak passes.

## Three rulings, agreed by MS and applied

- **`CN3`:** a rule requiring a bond, pledge or sureties is `1`; the census had read one pledge clause as exposure (`LS3 = 1`) and as no compulsion (`CN3 = .NR`) on the same row. `ko_mitarai_mujin_1773 CN3` → `1`.
- **`LS3`:** for a fund that lends to its members, `1` by the association route (a member answers for others' obligations) or the debtor route (a borrower liable beyond his pledge with his person or estate, as `sea_loan` and `bodemerij_amsterdam`); a pledge or surety for one's own repayment alone is `.NR`. **As first argued the ruling admitted only the association route, which contradicted `sea_loan LS3 = 1`; it was corrected before entry.** Three `ko_mitarai_*` cells → `.NR`. See [[A pledge secures an obligation and does not enlarge it]].
- **`deferred`:** only a clause that refers default itself to the members; a general amendment clause would make `deferred` track `GV1 = collective`.

## The re-test: nineteen rulebooks from two other selectors

- **Sources:** [[Okurasho 1915 - a Finance Ministry survey of mujin with eleven rulebooks]] (M01–M11) and [[Seitai chosa shiryo 36 - court-district reports on ko from Aomori, Tokushima and Okinawa]] (Aomori A03–A07, Tokushima T01–T03).
- **Population by structure** (MS): any rotating fund paying a member a pot he must repay, whatever its name; 十錢講 and 信用會 out. The operator had first called 模合 "a different institution", which was wrong and is corrected in the brief.
- **`LS1` coded but not a pass predictor**, because `residual-on-fund` restates `RD-test = fund`.
- **Exposure:** while sizing the set the operator saw clauses of M01 and M02; they stayed in, and the operator's predictions excluded them.
- **Result:** `RD-test` `.NR` 13, `officers` 5, `all-members` 1. Six eligible rulebooks, thirteen eligible pairs, none agreeing on `RB3`, `LS3`, `CN3` and `GV1`; no weak pass. **Fail on rule 6's second limb again**, and the same with `LS1` added, without M01–M02, and without the model texts.
- **Three of the five `officers` share a licensing template** (M08 and M09, 鳥取縣 model rulebooks; M10, 島根縣): see [[Where ko rules name a bearer beyond the drawer's security it follows the drafting regime]].

## Verdict

**`RD-test` is not adopted.** See [[A residual-bearer characteristic failed two blind tests for want of cases not for redundancy]].

## Scores

- **First test, the coder's priors:** falsified on the modal value (no value occurred twice), on `standing-subgroup` (it occurred, at kō 7, not where predicted), on `LS1` (no division value anywhere), `LS3` (17 of 17 `1` as coded) and `CN3` (no `P`), and on most kō-level guesses from names. **The operator's predictions:** the predicted overall pass failed; kō 35 `standing-subgroup` and kō 33 `officers` failed; the predictor counts held.
- **Re-test, the operator's predictions:** substantive `RD-test` and the 1915 count were falsified upward, the Tokushima `officers` prediction (resting on a table of contents) failed, and the overall fail held. The brief's predictor counts were written over 19 despite excluding M01–M02, a defect recorded in logbook 4.
- **Who scored.** The first test was scored by its coding chat, which the brief allowed only to a separate or operator chat; the re-test by the operator, which did not code.

## Defects recorded, not repaired

- **`LS1`'s `residual-on-fund`** duplicates a bearer and entered the first test's scoring.
- **`RB3 = mixed`** carries four mixtures: several kinds of property; property and surety together; property or surety at the drawer's option; surety for one drawer and property for the others.
- **`deferred`** is a governance value in a loss-sharing column.
- **Rule 5** sends an unwon member's default to `CN3`, which asks only whether non-payment can be compelled, so all members inheriting an expelled member's share (1936 kō 39) has no cell.
- **Forfeiture-only `CN3`** is `1` in `guild_box_brabant` and `P` in `ko_usui_bango_1822`.

## Links

- [[Who answers for a ko member's default was drafted not given]]
- [[Norinsho 1938 - forty-three ko rulebooks in print]]
- [[Blind re-coding workflow - operator, coder, application]]
- [[A blind is a property of the channel not of the dataset]]
- [[Split provenance into priority and independence]]
- [[Count degrees of freedom not cells]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - HistorEE]]

## Source

Sessions `residual-default-coding` (coding, rulings, application, scoring), `residual-default-retest-scan` and `residual-default-retest-operator` (one chat, `claude-opus-5-5` at effort `high`), and `residual-default-retest-coding` (a separate chat), 22 October 2026. Records: `PRIORS-residual-default-filled-2026-10-22.md`, `NOTES-residual-default-coding-2026-10-22.md`, `TEST-residual-default-2026-10-22.csv` and its adjudicated copy, `RULINGS-residual-default-2026-10-22.md`, `SHORTLIST-residual-default-retest-2026-10-22.md`, `NOTES-residual-default-retest-operator-2026-10-22.md`, `TEST-residual-default-retest-2026-10-22.csv`, `NOTES-residual-default-retest-coding-2026-10-22.md`. Commits `d50331a` (priors), `4b272a6` (re-test coding), `898906d` (re-test priors).
