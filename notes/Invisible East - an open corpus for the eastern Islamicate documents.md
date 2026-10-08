---
title: Invisible East - an open corpus for the eastern Islamicate documents
type: reference
tags: [archives]
project: infrastructure
source-session: silk-road-archives-survey
created: 2026-09-12
status: seed
---

# Invisible East — an open corpus for the eastern Islamicate documents

University of Oxford, **funded by the European Research Council under Horizon 2020, grant agreement 851607**. <https://invisibleeast.site.ox.ac.uk/> and a digital corpus at invisible-east.org.

**What it does**: assembles documents from the medieval Islamicate East — **Bactrian, Sogdian, Judaeo-Persian and New Persian** — with editions and translations, and publishes inventories saying **where each original is held**: the BnF, the British Library, the National Library of China, Renmin University's museum, the Afrasiab Museum in Samarkand, the IOM in St Petersburg, the Khalili Collection.

**Why it is useful here, in one sentence: it is the only project found in this pass that treats *documents* — not fragments, not manuscripts — as its unit, across collections and languages, and publishes editions rather than images.** ⚠️ **Licence, corpus size and completeness were not established**; the pages read are inventories and a document-of-the-month piece.

**And it is a second live ERC comparator**, beside [[DHARMA - an ERC Synergy project that produced a TEI corpus of inscriptions]]: a European grant producing an open documentary corpus in exactly the register HistorEE's digitisation strand describes.

## Corpus and search — added 2026-10-08

- **Size**: 1,298 texts at `invisible-east.org/corpus/`, about 515 with transcription or translation. ⚠️ Counts read through a summary.
- **Typology**: Legal, Letter, List/table, Administrative, Literary, Paraliterary, Unknown; Legal has subtypes including sale, rent-hire, loan, debt, guarantee and **Partnership**. Transcribed New Persian Legal: Debt 24, Sale 20, Loan 5, Rent-hire 3, Partnership 1.
- **Search by URL**: `invisible-east.org/corpus/?search=["term"]` (a JSON list), with `search_type` (general, exact, regex) and `search_operator` (or, and); subtype filter `filter_fk_document_subtype=N`, Partnership = 10. Searches metadata, summaries, transcriptions, translations and tags. Parameters read from the site's code at `github.com/invisibleeast/invisible-east-website` (`django/corpus/views.py`).
- **Rate-limited** (HTTP 429): space the queries.

## Links

- [[MOC - Silk Road archives]]
- [[Sogdian commercial documents - thin but not empty]]
- [[The Khalili Bactrian documents - a private collection as the archive]]
- [[DHARMA - an ERC Synergy project that produced a TEI corpus of inscriptions]]
- [[MOC - ERC Synergy Grant]]
- [[The Afghan corpora show partnership as traces because their archives are a landlord's and a granary's]]

## Source

Silk Road archives survey, 12 September 2026. Invisible East project pages (Sogdian and Bactrian inventories; "Document of the Month 1/26"). Read through summaries.
