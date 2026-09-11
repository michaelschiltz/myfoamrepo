---
title: Dutch archives online - the access layers
type: reference
tags: [archives]
project: infrastructure
source-session: dutch-archives-survey
created: 2026-09-11
status: seed
---

# Dutch archives online — the access layers

**The Netherlands is the easiest country in the European set, and the reason is policy rather than scale.** Spain's obstacle is devolved custody under a unified catalogue; Italy's is unified custody under three catalogues that do not image. The Dutch have neither problem, and they have something none of the others has: **an open-data mandate that reaches the scans themselves.**

## The layers

| Layer | Where |
|---|---|
| Aggregated description and images across regional archives | <https://www.archieven.nl/> |
| National archive, inventories and scans | <https://www.nationaalarchief.nl/> |
| Full text at scale | <https://www.delpher.nl/> — see [[Delpher - the full-text layer]] |
| Transcribed notarial corpus | <https://amsterdam-city-archives.transkribus.eu/> — see [[Stadsarchief Amsterdam - the notarial archive]] |

## The licence position, which is the finding

The Nationaal Archief publishes **inventories under CC0 and scans as public domain / CC0**, with attribution requested but not required, and roughly **2.8% of inventories restricted** for third-party copyright. Harvesting is by **OAI-PMH** (EAD/XML) at `https://service.archief.nl/gaf/oai/!open_oai.OAIHandler`; individual scans download as JPEG or TIFF at 300 dpi print quality.

⚠️ **No IIIF is advertised**, which matters more than the open licence for pipeline purposes: bulk work means METS plus direct download rather than a standard image API. Establish whether a systematic harvest is practical before designing around it.

Set this against [[Arxiu Historic de Protocols de Barcelona]], where the images are usable for research and teaching only, unmodified, with anything else needing the Col·legi's permission. **The same act — putting scans on the web — produces a reusable corpus in one country and a reading room with a longer reach in the other**, and the difference is a licence rather than a technology.

## Free digitisation on demand, and what it does to the acquisitions calculus

Several Dutch archives will scan on request, without charge, and publish the result. Rotterdam's terms are the worked case — **three items per day per person, up to A3, nothing under a hundred years old, published on the website within about a month** — and see [[Stadsarchief Rotterdam - the notarial archive and scanning on demand]].

**Compare the Vatican: three units per day, in person, with no camera.** Identical numbers, opposite meaning. In Rome the three-unit ceiling is what a scholar can consult in a day on site; in Rotterdam it is what a scholar anywhere can have imaged and published for nothing. The commissioned-surrogate row of [[MOC - Acquisitions and the antiquarian trade]] is priced at zero here, and the whole travel-versus-surrogate decision inverts.

⚠️ Establish which other Dutch archives run the same service and on what terms. If the Amsterdam and Zeeland archives do, a large part of the Dutch programme is a desk task.

## The caution that has to travel with all of this

The Dutch material will be easier to work than anything else in the European set, and **that is a fact about Dutch science policy after 2010 and not about the seventeenth century**. [[The VOC-EIC digital asymmetry is an access regime not a survival difference]] states it for two companies; the whole-country version is the same argument and is the one that will quietly bias a comparative corpus toward Dutch evidence. Budget for the resistance, not just for the access.

## Links

- [[MOC - European archives and digital collections]]
- [[Delpher - the full-text layer]]
- [[Nationaal Archief - The Hague]]
- [[The VOC-EIC digital asymmetry is an access regime not a survival difference]]
- [[PARES - the access layer for the Spanish state archives]]
- [[SIAS SIUSA and SAN - the Italian access layers]]

## Source

Dutch archives survey, 11 September 2026. Nationaal Archief open-data pages (licence, OAI-PMH endpoint, 300 dpi downloads, 2.8% restricted); archieven.nl; Stadsarchief Rotterdam's *digitaliseren op verzoek* terms.
