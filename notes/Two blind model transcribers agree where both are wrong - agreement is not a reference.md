---
title: Two blind model transcribers agree where both are wrong - agreement is not a reference
type: permanent
tags: [htr, verification, provenance]
project: HistorEE
source-session: yamamoto-ledgers-double-transcription-2026-11-15
database: [loss_mitigation_forms]
created: 2026-11-15
status: seed
---

# Two blind model transcribers agree where both are wrong — agreement is not a reference

**Two model transcriptions of the same printed page, made blind to each other, fail together on exactly the readings a model regularises: their agreement certifies nothing, and only a reading of the image settles a character.** In the double transcription of Yamamoto IV(A), Nos. 221–259 (the Dunhuang 納贈曆 ledgers, 9,938 characters), chat A (Opus) and chat B (Fable) disagreed on 57 characters of content and 61 of form. MS ruled each disagreement on the image. The residual check then found five places where both had written the same wrong character: 步 for the printed 歩 three times, 佰 for 仵, and 渭 for 淸. Each is the commoner form or the likelier name. They surfaced only because the adjudication looked at those lines for another reason.

## What the measured rates are, and are not

- Against the adjudicated text, A made 39 content errors (0.39 per cent) and B 25 (0.25 per cent). Form errors are counted apart (A 58, nearly all 清 and 青 for the printed 淸 and 靑) and so are misplacements. Register rows ER-0023 and ER-0024 in `HistorEE_codebooks`.
- **Both are lower bounds.** The reference was read on the image only where the two disagreed. A shared error anywhere else is invisible to the measure.
- **Neither is independent.** MS read the image knowing both readings, so the register labels the rows `maintainer-image-read` and the check refuses to cite them as error rates.
- The OCR text layer of the same pages reached 44.8 per cent character recall (ER-0011). Model reading from the image is two orders of magnitude better and still not self-certifying.

## The adjudicator's own recommendations fail the same way

The assistant that prepared the adjudication sheet read every disagreement from crops and recommended a reading. MS ruled against 13 of 56 recommendations. In at least seven the assistant was demonstrably wrong: forms read from a reduced tile, and one rationale (㺃) that took 犭 + 句, the shape of plain 狗, for the variant. Every reversal came from a crop at 4× or more. The judge has to be a person at full resolution, as in [[Model-read mathematical manuscripts - Godel had a proof checker, Lighthouse a false-positive protocol]]: there Coq judged the output and Lighthouse requires a human to read the scan.

## A second edition is a check on transcription, not a second witness

Ning and Hao 1997 edit eleven of the same documents. Collation caught a mis-placed debt (245) and identified Yamamoto's ≀ as a cancellation mark. It also exposed one false count in a coded note: "bread and grain in all 62 entries" is 55 of 62 in both editions. But the two editions read the same manuscripts. Where they differ (盧/㕎, 闍/閻), neither is evidence against the manuscript. This is the [[The OCR text layer evidences a clause's presence, not its absence]] point one level up: a reading is evidence of what one reader saw.

## Links

- [[MOC - Historiography and method]]
- [[MOC - ERC Synergy Grant]]
- [[Agentic research set-ups - the public landscape against the HistorEE protocol]]
- [[Dunhuang she associations - bylaws for a funeral fund]]

## Source

`HistorEE_codebooks`: `records/RULINGS-yamamoto-ledgers-adjudication-2026-11-15.md`, `records/COLLATION-she-death-aid-yamamoto-2026-11-15.md`, logbook 4 (2026-11-15 (ii)), logbook 5 (2026-11-15).
