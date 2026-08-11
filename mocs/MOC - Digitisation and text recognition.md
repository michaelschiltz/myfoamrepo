---
title: MOC - Digitisation and text recognition
type: moc
tags: [moc, tooling]
project: infrastructure
source-session: digitisation-tooling
created: 2026-08-01
status: seed
---

# MOC — Digitisation and text recognition

Reference hub for capture hardware and text-recognition software. **This is an infrastructure layer, not an argument layer.** Notes here are `type: reference`, carry `project: infrastructure`, and are deliberately not wired into the concept graph. Nothing below should be cited as evidence for a claim about financial history.

## The decision that actually matters

The market presents itself as a hardware question — which scanner. It is not. The binding constraint is **transcription, not capture**, and the two have entirely different cost curves.

Capture is close to solved and close to free. A ¥40,000 desktop scanner or a phone in a fabric tent produces images good enough for research reading at 200–400 pages/hour. Transcription of *kuzushiji* is the step that has been impossible for a century and became tractable only in the last three years.

This has a hard corollary: **the throughput figures that dominate scanner marketing — 2,500 pages/hour — are answers to a question a single researcher does not have.** A robotic V-cradle scanner amortises against a digitisation programme with staff, a queue, and a service contract. It does not amortise against a book project. If Hokkaido's library is buying, the calculus changes entirely; if you are buying, it almost certainly does not.

## Second decision: script

**Transkribus does not read *kuzushiji*.** Its models are Latin-script. The Japanese stack (NDL, CODH) and the European stack (Transkribus, eScriptorium) are non-overlapping tools for non-overlapping corpora, and the only reason to hold both is that your project is genuinely comparative. Given *Clearing and Settling the Realm* spans Japanese and European material, you plausibly do need both — but as two pipelines, not one.

## Third decision: reversibility

Prefer choices you can undo. Three irreversibilities are worth naming because each is a one-way door:

- **Destructive scanning** (guillotining a spine for a sheet-feeder). Obvious, and never appropriate for archival material.
- **Proprietary model lock-in.** Models trained on Transkribus cannot be exported. Ten years of your correction effort accrues to their ecosystem, not to your files.
- **Cloud-only processing.** Material you may not be licensed to upload — much archival material in Japan is exactly this — forecloses the entire managed-service tier before price enters the argument.

Capture at the highest quality you can afford *once*, in an open format, because rescanning means returning to the archive.

## Notes

- [[Transkribus - managed HTR platform]]
- [[Open-source HTR stack - eScriptorium Kraken Loghi]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
- [[Robotic V-cradle book scanners - Treventus and Qidenus]]
- [[Preservation-grade overhead scanners - Zeutschel and i2S]]
- [[Desktop and portable capture - CZUR and ScanTent]]

## Corpora that already exist

Distinct from the tooling layer, and consequential in the other direction: where a corpus has already been transcribed, none of the decisions above apply. Both notes are argument-layer, not infrastructure.

- [[VOC digital corpus - what is online and on what terms]] — five million OBP pages already through Loghi
- [[EIC digital corpus - what is online and on what terms]] — images at best, and mostly behind a subscription
- [[GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC]] — what that means for the project's own transcription budget

## Tiers at a glance

| Tier | Examples | Throughput | Indicative cost | Who it is for |
|---|---|---|---|---|
| Robotic, automatic page-turn | Treventus ScanRobot 2.0 MDS, Qidenus Robotic | up to 2,500 pp/h | tens of thousands USD ⚠️ | Mass-digitisation programmes |
| Semi-automatic V-cradle | Qidenus Mastered | up to 1,500 pp/h | not published | Library digitisation units |
| Preservation flatbed/overhead | Zeutschel OS Q / OS HQ, i2S CopiBook OS | operator-limited | not published | Where the image *is* the deliverable |
| Desktop overhead | CZUR ET25 Pro | ~1.5 s/spread | low hundreds USD | Individual researchers |
| Portable | Transkribus ScanTent + DocScan | ~300 pp in 12–15 min | not published | Archive fieldwork |

⚠️ = unverified, see the individual note.

## Open questions

- **Permission, not equipment, is the real constraint in Japanese archives.** Self-photography rules vary by institution and are frequently the limiting factor. Nothing in these notes substitutes for asking the holding institution first.
- Japanese distribution and service contracts for Treventus, Qidenus, Zeutschel and i2S are unresearched. For an actual purchase this dominates: a European robot with no service engineer in Hokkaido is a liability.
- No note yet on the *downstream* pipeline — PAGE/ALTO XML into a searchable corpus into Zotero. That is where these tools break, and it is a separate question.
