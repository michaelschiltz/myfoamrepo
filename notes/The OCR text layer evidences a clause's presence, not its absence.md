---
title: The OCR text layer evidences a clause's presence, not its absence
type: permanent
tags: [ocr, verification, provenance]
project: HistorEE
source-session: madurell-translation-test
created: 2026-11-03
status: seed
---

# The OCR text layer evidences a clause's presence, not its absence

When coding from a printed primary edition, a clause the PDF text layer shows is there. A clause the layer does not show may have been dropped at a line break, split off with a table, scrambled into garbage, or cut by the scribe's own abbreviation. So an absence coded from the layer, whether `.NR`, "not stated" or a neither row for want of a clause, is a claim about the layer until the page image is read.

## The evidence

The comanda pass coded Madurell Marimón & García Sanz 1973 from the text layer on 2026-10-27. The full reading of the page images on 2026-11-03 corrected it ([[Comanda records corrected from the Madurell translation 2026-11-03]]).

- **The layer damaged the verbatim fields.** It produced 56 wrong or truncated amounts of 115, mostly a leading number word lost at a line break: doc 204 read 1 lb for 851 lb. It also lost 52 date lines, 60 declarants and 29 destinations, and left OCR forms in quotations flagged clean.
- **None of that moved a cell**, because no cell drew on those fields. A few cell quotations were damaged.
- **What did move the census was not OCR.** A convention sent abbreviated clauses to the neither row. A notary's full series shows that every written-out clause names the investor, and the corrected reading decided 60 of 202 acts. Misreadings of correct text did the rest: roles taken from a reversed editorial heading, a "sea" and a "surety" that are not in the deeds.

## Consequences

- **Comparing `pdftotext` with Zotero's rendering checks layout, not OCR.** Both read the same embedded layer; only the image, or a second independent OCR, catches its numeral and character errors.
- **A full image reading is the gold standard but not the default.** Measure the layer on about ten pages before coding. Code from the layer, then check against the image:
  - every quotation that carries a cell;
  - every coded absence;
  - every verbatim numeral, date and name;
  - every garbled page.
- **Narrow the image checks by script**, and by a second OCR where one is available. From this edition's counts the targeted checks cover roughly a fifth to a third of the pages. That is an estimate, not a timing.
- **Settle the assignment conventions before any row exists**, by reading one notary's series in full. A convention set during the coding is a reading of the scribe's pen, not of the contract.
- **Headings and regests are editorial.** They are never evidence of who is investor and who is agent.

Recorded as doctrine in `HistorEE_codebooks` CONTRIBUTING §3, "Reading a printed primary edition", and logbook 5, 2026-11-03 (ii).

## Related

- [[Comanda records corrected from the Madurell translation 2026-11-03]]
- [[Comanda coding collated with the editors' study 2026-11-01]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
- [[MOC - HistorEE]]

## Source

Session `madurell-translation-test`, 2026-11-03, `claude-opus-5-5`; ruled by MS the same day.
