---
title: GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC
type: permanent
tags: [legibility, provenance, comparative, verification]
project: HistorEE
source-session: eic-voc-archives
created: 2026-08-11
status: seed
---

# GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC

[[Van Dam's Beschryvinge - the VOC described by its own advocaat]] made the point for one source: an already-transcribed text takes a corpus out of the HTR question altogether — no CER band to negotiate, no correction budget, no model lock-in. GLOBALISE makes the same point at the scale of **five million pages**. The Overgekomen Brieven en Papieren are not a digitisation project waiting to be funded; they are a corpus that already exists.

Nothing equivalent exists on the English side. Any series-level quantitative treatment of the EIC records must **fund its own transcription**, and the cost falls on this project rather than on a Dutch research council.

## What that actually costs, stated rather than waved at

Three things do not transfer from the Dutch case:

1. **Models.** Loghi's models are trained on early modern Dutch chancery and mercantile hands. English secretary hand and eighteenth-century ledger hands are a separate training problem. Ground truth would have to be produced.
2. **Images.** Loghi needs the scans. The EIC constitutional series exists as images inside a commercial platform with no bulk export, which forecloses the pipeline before the model question is reached. This is the **cloud-only / lock-in irreversibility** named in [[MOC - Digitisation and text recognition]] arriving from the supply side instead of the tooling side.
3. **Rights.** Transcribing a subscription platform's images at scale is a licensing question, not a technical one. Ask before building.

The QDL images are the exception on all three counts — freely available, high quality, IIIF-served — and are therefore the only EIC material on which an HTR pipeline could actually be run without negotiation. ⚠️ Confirm IIIF endpoints and bulk-download terms. But see [[The QDL corpus is conditioned on its funder's geography]]: what that pipeline would produce is a Gulf corpus, not an EIC corpus.

## The design decision this forces

Two honest options, and no third:

- **Restrict the English side to what secondary literature and structured datasets support** — Bowen's SN 5690 for the financial series, the existing historiography for the constitutional narrative — and make no claim that requires counting words in the manuscripts. Symmetric in rigour, asymmetric in method, and defensible if stated.
- **Budget for EIC transcription explicitly**, scoped to a named series (IOR/B for the constitutional argument; IOR/L/AG for anything financial), with ground truth, a CER target, and a licence agreed in advance.

The failure mode is the third path nobody chooses deliberately: running corpus-scale queries on the Dutch material because they are cheap, running none on the English material because they are not, and reporting the results side by side. That is [[The VOC-EIC digital asymmetry is an access regime not a survival difference]] converted into a finding.

## Links

- [[VOC digital corpus - what is online and on what terms]]
- [[EIC digital corpus - what is online and on what terms]]
- [[The VOC-EIC digital asymmetry is an access regime not a survival difference]]
- [[Van Dam's Beschryvinge - the VOC described by its own advocaat]]
- [[Open-source HTR stack - eScriptorium Kraken Loghi]]
- [[Transkribus - managed HTR platform]]
- [[MOC - Digitisation and text recognition]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

EIC/VOC archive-availability session, 11 August 2026.
