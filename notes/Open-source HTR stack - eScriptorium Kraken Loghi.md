---
title: Open-source HTR stack - eScriptorium Kraken Loghi
type: reference
tags: [tooling, htr, ocr]
project: infrastructure
source-session: digitisation-tooling
created: 2026-08-01
status: seed
---

# Open-source HTR stack — eScriptorium, Kraken, Loghi

The alternative to [[Transkribus - managed HTR platform]]. Same task, opposite trade: you supply the infrastructure and the training data, and you keep the models.

## The components

**Kraken** — the recognition engine. Open-source OCR/HTR, originally a fork of OCRopus, optimised for historical documents and explicitly built for non-Latin and right-to-left scripts. Full pipeline: binarisation, layout analysis, line segmentation, recognition. Command-line, highly configurable, trains on your own ground truth. Kraken is what does the work; everything else is interface.

**eScriptorium** — the front end over Kraken. Developed in the SCRIPTA project (PSL, Paris). Browser interface for annotation, segmentation, correction and model training with no coding required. Critically, **it is not an application you install but a service you run** — a server or a Docker image. Someone has to administer it. For a single researcher without institutional IT, this is the real cost, and it is paid in your time rather than in credits.

**Loghi** — KNAW Humanities Cluster with the Nationaal Archief. MIT-licensed, end-to-end, Docker-based; Laypa for layout, Loghi Tooling for the middle, Loghi HTR for recognition, PageXML throughout. Oriented to large Dutch archival corpora and the engine behind the five-million-page GLOBALISE transcription of the VOC papers. **Narrower than Kraken in trained models, not in architecture** — it also generates synthetic ground truth, which Kraken does not. Full assessment: [[Loghi - the KNAW-Nationaal Archief HTR pipeline]].

**OCR4all** — Würzburg. Semi-automatic workflow specifically for **early printed books**, where the problem is historical typefaces rather than handwriting. Different problem, and if the material is incunabula-to-18th-century print this is likely the better fit than a handwriting model.

## Trade against Transkribus

| | Transkribus | eScriptorium / Kraken |
|---|---|---|
| Cold start on unfamiliar hand | Super Models give usable output immediately | Needs a fitting base model or you train from scratch |
| Model ownership | Not exportable, ecosystem-locked | Yours, portable, publishable |
| Infrastructure | None — browser | Server or Docker, self-administered |
| Marginal cost per page | 1 credit | Zero |
| Data residency | Uploaded to the platform | Entirely local |
| Non-Latin scripts | Latin only in practice | Architecturally open |

**The cold-start asymmetry is the whole argument.** Transkribus's Super Models are a genuine moat: they are trained on 7 million pages you do not have. Without a fitting base model, eScriptorium requires ground-truth investment before you get a single usable page. If your hands are common European ones, Transkribus wins on day one. If your material is unusual, both require training and the open stack is strictly better.

**Data residency is the underrated axis.** Where an archive's permission conditions forbid uploading images to a third-party service — not exotic in Japan — the managed tier is excluded on legal grounds before cost is discussed. A local Kraken install is then the only option, and the same logic favours the NDL tools on the Japanese side.

## Migration

UB Mannheim publishes documentation on transferring models from Transkribus to eScriptorium. **Verify this is current before treating it as an exit route** — it is exactly the kind of interoperability that platform operators quietly close.

## Assessment

The honest recommendation for a historian rather than a digital-humanities lab: **start on Transkribus, keep your ground truth in open PAGE XML, and treat the open stack as the hedge rather than the plan.** Self-hosting eScriptorium is a real infrastructure commitment and it competes for time with writing the book. The hedge only has to be exercised if the platform's terms, price, or ownership change — and holding portable ground truth costs nothing today.

## Links

- [[MOC - Digitisation and text recognition]]
- [[Transkribus - managed HTR platform]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
