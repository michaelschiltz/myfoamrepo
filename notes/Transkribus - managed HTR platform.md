---
title: Transkribus - managed HTR platform
type: reference
tags: [tooling, htr, ocr]
project: infrastructure
source-session: digitisation-tooling
created: 2026-08-01
status: seed
---

# Transkribus — managed HTR platform

Operated by **READ-COOP SCE**, a European cooperative based in Innsbruck, successor to the EU READ project. Web platform plus API. Claims 500,000+ users. Corpus of ~7 million pages across ~9,000 archival sources, which is the asset the models are trained on and the reason the cooperative structure matters — members contribute material.

## What it does

Layout analysis, then handwritten and printed text recognition, plus table recognition, field recognition and information extraction as separately priced steps. Browser-based transcription editor with collaboration. Output to PAGE XML, ALTO, TEI, PDF, DOCX.

The pitch is that you do not train anything. **Super Models** are general pretrained models that produce usable output on unseen material with no training data — this is the substantive difference from the open-source stack, where an unfamiliar hand means starting from zero.

## Accuracy — the numbers, correctly framed

Current general model is **Text Titan I ter** (June 2025), trained on 31 million words. Benchmark: 2,000 pages held out from the 7-million-page corpus, 13 languages, printed and handwritten, **measured at full-page level**.

| Material | TTI ter CER |
|---|---|
| Handwritten (overall) | 10.8% |
| Printed (overall) | 3.9% |
| Dutch | 7.2% |
| German | 8.6% |
| French | 9.1% |
| English | 11.5% |
| Other Latin-script | 9.6% |

Transkribus's own reading of these bands: **under 5% CER needs minimal correction; around 10% is readable with corrections; over 20% may be unreadable.** By that scale their flagship handwriting number sits in "readable with corrections" — not "solved". Roughly 30% lower error than the original Text Titan, and it now beats the language-specific Super Models it was meant to complement (English Elder 12.3%, German Genius 9.0%, Dutch Dean 7.4%), which makes the language-specific tier largely redundant.

**Two cautions on these figures.**

First, full-page CER includes layout failures, not just character errors. It is the honest metric and it is *not* comparable to the per-line CER quoted by most academic HTR papers. Do not benchmark against the literature without checking which is being reported.

Second, the LLM comparison is loaded. Transkribus reports TTI ter as 3.2× more accurate than the best LLM on handwriting (Gemini 2.5 Flash, 35.0% CER) — but **they score a refusal to transcribe as 100% CER**. LLMs decline complex historical documents frequently. The comparison therefore measures willingness and accuracy jointly and reports the compound as accuracy. A referee would catch this. The directional claim is probably right; the multiple is not trustworthy.

## Cost

- 50 free credits/month, no card. Text recognition **1 credit per page**; table or field recognition **1 credit each on top**.
- On-demand top-up credits do not expire.
- Plans: Free, Scholar, Team, Organisation.
- **API credits cost 50% less than UI credits.** Organisation subscribers get the 50% reduction applied automatically when using the API. If volume is meaningful, use the API — the discount is large and purely a function of the access route.

Exact currency prices per plan **unverified — check transkribus.org/pricing directly before budgeting.**

## The lock-in problem

**Models trained on Transkribus are not open source and cannot be exported.** They can be shared publicly, but only inside the Transkribus ecosystem. For a project on a book-length timescale this is the material risk: correction effort is the expensive input, corrections become training data, training data becomes a model, and the model is not yours. UB Mannheim documents a Transkribus → eScriptorium model-transfer route, which suggests the wall is not absolute — **verify whether that path still works before relying on it.**

Mitigation is cheap and should be automatic: keep your ground-truth transcriptions and page images in open formats under your own control, independent of the platform. Ground truth is portable even when models are not.

## Relevance to this project

**Latin script only.** Directly useful for European archival material — Dutch VOC records, German and French secondary and primary material. **Useless for *kuzushiji*.** See [[Kuzushiji OCR - the NDL and CODH stack]] for the Japanese side, which is a wholly separate pipeline.

Also sells hardware — see [[Desktop and portable capture - CZUR and ScanTent]] for the ScanTent.

## Links

- [[MOC - Digitisation and text recognition]]
- [[Open-source HTR stack - eScriptorium Kraken Loghi]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
