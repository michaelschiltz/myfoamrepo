---
title: MiDRASH - the machine transcription of the Geniza
type: reference
tags: [archives]
project: infrastructure
source-session: geniza-archives-survey
created: 2026-09-11
status: seed
---

# MiDRASH — the machine transcription of the Geniza

**MiDRASH** — *Migrations of Textual and Scribal Traditions via Large-Scale Computational Analysis of Medieval Manuscripts in Hebrew Script* — an **ERC Synergy Grant** (no. 101071829, €10 million, six years from 2023), led by Daniel Stökl Ben Ezra (EPHE, Paris) with Nachum Dershowitz (Tel Aviv), Avi Shmidman (Bar-Ilan) and Judith Olszowy-Schlanger (Oxford), working with the National Library of Israel.

## What it has released

- **27 November 2025: *MiDRASH Automatic Transcriptions of the Cairo Geniza Fragments*, v0.8** — "the first automatic transcription of the entire collection of digital images of the Geniza at the National Library of Israel". Zenodo record 17734473; one 444.6 MB compressed text file; **CC BY 4.0**. Seventeen contributors, **Marina Rustow among them**.
- **22 February 2026: *MiDRASH Geniza 01 HTR model*, v2** — a Kraken model fine-tuned on Geniza documentary and literary texts, including Judaeo-Arabic. Zenodo record 18732245; **CC BY-NC-SA 4.0**.
- Transcriptions are to be added to Ktiv beside the images. Before the project, **fewer than 10–15 per cent** of the Geniza had been transcribed.

## What the release says about itself

**Preliminary, and says so.** Segmentation and recognition errors; reading order sometimes wrong; vertical text mostly ignored; parallel regions incompletely captured; **"Arabic script recognition is less good than Hebrew script"**. ⚠️ No character error rates are published with the dataset.

## What it does to the layer question

**It moves the whole Geniza to layer 3 — noisy, searchable, and free.** In Europe the survey found a handful of layer-3 corpora, every transcribed notarial one in the Low Countries. **Here a non-European corpus of 400,000 fragments has been machine-read in one pass**, and the census's question — whether a partnership instrument is *ʿisqa*-shaped or *qirāḍ*-shaped — is a clause-structure question a search can begin.

**Two limits, and the first is the survival rule again.** **The script that went into the Geniza by rule is read well; the script that went in by accident of reuse is read worse.** The Fatimid state documents Rustow recovered are exactly the Arabic-script material the model handles least well. **Legibility reproduces the deposit's selection.** Second, noisy text supports *finding*, not *counting*: a missed term is a recognition failure before it is an absence. **Never read a null search of this corpus as a null in the Geniza.**

## Why the grant should know about it

**It is an ERC Synergy grant in the same scheme, funded in an earlier round of the scheme HistorEE is applying to, working on one of HistorEE's named corpora, with a Princeton Geniza scholar among its contributors.** That is a citation for Part B, a possible collaboration, and a reason the Geniza line in Decision_log A6 (transcription) can shrink. ⚠️ Not raised with anyone; stated for the maintainer.

## A test that could not be run from here

**The v0.8 text file is the cheapest possible probe of the `isqa_alloc` dispute**: search it for *ʿisqa* and the Judaeo-Arabic forms of *qirāḍ* and *shirka*, and tabulate hits by collection. **The session's network policy blocked the Zenodo download**, so the probe is left as a desk task.

## Links

- [[MOC - Geniza archives]]
- [[Friedberg Genizah Project and Ktiv - the image union layer]]
- [[Princeton Geniza Project - the documentary database]]
- [[Geniza partnership documents - where the census's isqa and qirad evidence sits]]
- [[MOC - Digitisation and text recognition]]
- [[Open-source HTR stack - eScriptorium Kraken Loghi]]

## Source

Geniza archives survey, 11 September 2026. Zenodo records 17734473 and 18732245 (metadata pages); *Times of Israel*, 25 November 2025, and *Ynet*, 23 November 2025, on the launch. Read through summaries of the pages; the dataset itself not opened.
