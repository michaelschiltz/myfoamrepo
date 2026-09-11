---
title: MOC - European archives and digital collections
type: moc
tags: [moc, archives]
project: infrastructure
source-session: european-archives-survey
created: 2026-09-10
status: seed
---

# MOC — European archives and digital collections

Reference hub for **where the documents are, and whether anyone has already imaged them**. Europe first; the non-European repositories are deliberately out of scope for this pass and are tracked in the ERC budget line instead. **This is an infrastructure layer, not an argument layer.** Notes here are `type: reference`, carry `project: infrastructure`, and are not wired into the concept graph. Nothing below is evidence for a claim about financial history.

It completes a triangle with two existing hubs. [[MOC - Acquisitions and the antiquarian trade]] asks how a text comes within reach at all; [[MOC - Digitisation and text recognition]] asks how to capture and read a document you already have access to; this hub asks the question that sits between them — **which institution holds the series, and at what layer is it already open**. The three meet at the commissioned scan.

## The decision that actually matters

The instinct is to ask *which archive*. The productive question is *which layer*, because European archival material is open at three quite different layers and only one of them is what a researcher usually means by "digitised".

- **Layer 1 — description.** A finding aid, searchable by catalogue metadata. Aggregators live here. Archives Portal Europe alone carries **280+ million descriptive units** from ~7,000 institutions across 30+ countries. Not one of them is a document.
- **Layer 2 — image.** A scan, viewable and usually downloadable, findable only through the layer-1 description that points at it. This is where the bulk of what is genuinely online sits.
- **Layer 3 — text.** Transcribed, full-text searchable, machine-processable. This exists for a **handful** of European corpora and nothing else.

**The failure mode is treating layer 2 as layer 3.** A workflow that assumes "digitised" means "searchable" fails on the overwhelming majority of early modern commercial record. Budget the transcription — see [[Open-source HTR stack - eScriptorium Kraken Loghi]] and [[Loghi - the KNAW-Nationaal Archief HTR pipeline]] — or restrict the claim to what a finding aid can support.

The sharpest instance is the English company record, and it is the project's own: **the constitutional series are not online at any layer below description.** The National Archives states it flatly — none of the company records held at Kew are viewable online. `BT 41` (joint-stock companies registered under the 1844 Act and dissolved before 1860 — prospectuses, capital, share issue and allocation, balance sheets), `BT 31` (dissolved companies from 1856, memoranda and articles, shareholder lists, registers of directors) and `BT 34` (liquidators' accounts, 1890–1932) are exactly the series the deed-of-settlement coding leans on, and they are a Kew trip with a camera, not a download. Plan the batch accordingly.

## Second decision: the coverage map is a funding map

This is the project's own argument turned on its own supply chain, one scale up from where it was first stated. [[The VOC-EIC digital asymmetry is an access regime not a survival difference]] establishes it for two companies; [[The QDL corpus is conditioned on its funder's geography]] establishes it for one selection. Across Europe the same structure holds and is easier to miss because it looks like a map of survival.

- **The Netherlands and the Nordic states** ran state-funded mass digitisation with an open-data mandate. Coverage is near-total for some series and free at point of use.
- **Italy** digitised by project. Notarial material is open where a funded project chose it — Genoa's *Notai Antichi*, Prato's Datini, the Medici correspondence — and closed where none did. The selection tracks scholarly fashion and regional funding, not the density of the record.
- **Britain** left the company record unfunded, so the single richest serial constitutional archive in Europe is invisible from a desk.

The operative rule follows directly and is the same one already in force for the VOC/EIC comparison: **never compute a frequency across national corpora.** Any statement of the form "the Dutch record shows X more often than the Italian" is uninterpretable while one side was counted by machine over millions of transcribed pages and the other by hand over whatever a project imaged. See [[Refusals are observations of the filter not inferences from survivors]] and [[The deficit reading of absence is the scalar ranking in evidentiary form]].

## Third decision: register per source, not per archive

The data management plan already commits the project to an **archival-resources register** with rights status explicit per item before release. Build it from the start, keyed on the *series*, because that is the unit that decides whether a denominator exists. Minimum columns:

| Column | Why it is load-bearing |
|---|---|
| Repository, city, country | Identity; feeds the travel budget |
| Fonds / series and reference code | The unit a frequency claim can have a denominator over |
| Which coded form it witnesses | Links the register to the codebook matrix |
| Layer (description / image / text) | Decides what can be asked without a transcription budget |
| Language and script | Feeds the transcription and translation budget |
| Access conditions and lead time | Reader's ticket, appointment, permission to photograph |
| Reproduction rights | Required before any image is released |
| IIIF / bulk download | Decides whether an HTR pipeline can run against it at all |

## Tier 0 — cross-national aggregators

Descriptions, not documents. Use them to discover that a series *exists* and who holds it; never as a corpus.

| Portal | URL | What it actually is |
|---|---|---|
| Archives Portal Europe | <https://www.archivesportaleurope.net/> | ~7,000 institutions, 30+ countries, 280M+ descriptive units. Filterable to records with linked digital objects — the single most useful discovery move in the whole tier |
| Europeana | <https://www.europeana.eu/> | Cultural-heritage aggregator, gallery-weighted; archives are a minority of it |
| Monasterium.net | <https://www.monasterium.net/mom/home> | ICARUS-run collaborative charter archive; medieval charters with images and editions ⚠️ scale unverified |

## Tier 1 — national portals

| Country | Portal | URL | Note |
|---|---|---|---|
| Netherlands | Nationaal Archief; archieven.nl | <https://www.nationaalarchief.nl/> | Inventories and scans **CC0**, OAI-PMH harvesting, 300 dpi downloads, ~2.8% restricted. No IIIF advertised. See [[Dutch archives online - the access layers]] |
| Belgium | Rijksarchief / Archives de l'État | <https://search.arch.be/> | Millions of scans, free, image-forward ⚠️ figure unverified |
| United Kingdom | TNA Discovery | <https://discovery.nationalarchives.gov.uk/> | Catalogue. Company and friendly-society records are description-only |
| France | FranceArchives + départementales | <https://francearchives.gouv.fr/> | Federated; the *départementales* hold the commercial material and image independently |
| Spain | PARES | <https://pares.cultura.gob.es/> | State archives only — the devolved and corporation-held archives are outside it. See [[PARES - the access layer for the Spanish state archives]] and the Spain section below |
| Portugal | DigitArq / Torre do Tombo | <https://digitarq.arquivos.pt/> | National catalogue with images ⚠️ current URL and scale to confirm |
| Italy | SIAS / SIUSA / SAN | <https://sias-archivi.cultura.gov.it/> | Three overlapping description systems and no image portal at all. State archives in SIAS, bank and corporate archives in SIUSA. See [[SIAS SIUSA and SAN - the Italian access layers]] |
| Germany | Archivportal-D | <https://www.archivportal-d.de/> | Archival section of the Deutsche Digitale Bibliothek |
| Sweden | Riksarkivet, Digitala forskarsalen | <https://sok.riksarkivet.se/en/digitala-forskarsalen> | Heavily imaged; the Riksarkivet also publishes HTR models openly |
| Norway | Digitalarkivet | <https://www.digitalarkivet.no/en/> | Near-total for major series |
| Croatia | ARHiNET | <http://arhinet.arhiv.hr/> | Descriptive; Dubrovnik is `HR-DADU` |

## Tier 2 — city and notarial archives

**This is where the pooling forms actually are.** The commenda, the *collegantia*, the *bodemerij*, the *partenrederij* and the *fraterna* are notarial and municipal instruments; the national archive is the wrong place to look for almost all of them.

| Repository | URL | What is open |
|---|---|---|
| [[Stadsarchief Amsterdam - the notarial archive]] | <https://amsterdam-city-archives.transkribus.eu/> | *Alle Amsterdamse Akten*: hundreds of thousands of pages of 17th–18th c. notarial deeds, HTR-transcribed and free-text searchable. **Layer 3** — the single most valuable European resource for this project after GLOBALISE |
| [[Archivio di Stato di Genova]] | <https://archiviodistatogenova.cultura.gov.it/patrimonio/archivio-digitale/notai-antichi> | *Notai Antichi* — the earliest notarial registers in Europe — digitised via Notariorum Itinera ⚠️ extent unquantified. Also holds [[Casa di San Giorgio - the Genoese public debt archive]] |
| [[Archivio di Stato di Venezia]] | <https://asve.arianna4.cloud/> | *moreveneto* is a re-description of the holdings — layer 1, and excellent. Imaging is thin ⚠️ |
| Arxiu Històric de Protocols de Barcelona | <https://arxiu.colegionotarial.org/> | *Aurora*: images only, no transcription; registration for downloads; research-and-teaching licence, no modification without permission. Corporation-held, in no state catalogue ⚠️ extent unverified |
| [[Archivio di Stato di Prato - the Datini archive]] | <http://datini.archiviodistato.prato.it/en/> | Fondo Datini — letters and books of account, catalogued to item level |
| [[Stadsarchief Rotterdam - the notarial archive and scanning on demand]] | <https://stadsarchief.rotterdam.nl/> | ONA toegang `18`; **free scanning on demand**, three items a day, published publicly |
| Državni arhiv u Dubrovniku | via ARHiNET / APE | Ragusan notarial and *collegantia* material ⚠️ digitisation status unresearched |

## Tier 3 — corpora already transcribed

Where a corpus is at layer 3 the entire calculus above collapses, which is the point of [[GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC]]. Check this tier before spending anything.

- **GLOBALISE** — ≈5 million OBP scans, Loghi-transcribed, Dataverse download. See [[VOC digital corpus - what is online and on what terms]].
- **Alle Amsterdamse Akten** — Amsterdam notarial deeds, HTR, searchable (Tier 2 above).
- **Fondo Datini** — catalogued to item level, letters and account books.
- **Medici Archive Project / BIA** — Mediceo del Principato, document-level annotation ⚠️ current access terms to confirm.
- The English side has no member of this tier at all; see [[EIC digital corpus - what is online and on what terms]].

## Spain — repository notes

The first country worked through at repository level. Each note carries the sections that matter, the digitisation layer, and explicit verify flags where a placement rests on secondary literature rather than a finding aid.

**The structural fact about Spain**, and the one that catches people: archival competence is devolved, so no single catalogue covers the country. [[PARES - the access layer for the Spanish state archives]] holds the state archives; Andalusia, the Basque Country, Valencia and the Balearics run their own; and the richest notarial archive of all is held by a professional corporation and appears in no public system at all. A PARES search that returns nothing is evidence about the Ministry's remit.

**The Atlantic complex**

- [[Archivo General de Indias - Sevilla]] — `CONTRATACION` (1492–1795, 6,337 legajos, 51 series), `CONSULADOS`, `CONTADURIA`, `INDIFERENTE GENERAL`. The *averia* strand
- [[Archivo Historico Provincial de Sevilla - notarial protocols]] — the instruments behind the institution
- [[Archivo Historico Provincial de Cadiz - notarial protocols and the Consulado]] — the Carrera after the 1717 move
- [[Archivo General de Simancas]] — the fiscal archive; the Philip II *asientos*
- [[Archivo Historico Nacional - Madrid]] — councils, charters, and the eighteenth-century privileged companies

**The Crown of Aragon**

- [[Archivo de la Corona de Aragon - Barcelona]] — the legal and institutional frame, from the twelfth century
- [[Arxiu Historic de Protocols de Barcelona]] — the *comandes* themselves; corporation-held, outside every state catalogue
- [[Arxiu del Regne de Mallorca]] — fifteenth-century marine insurance in volume
- [[Arxiu del Regne de Valencia]] — the third royal archive; note the municipal split over the *Taula de Canvis*

**The consulado towns**

- [[Archivo Foral de Bizkaia - the Consulado de Bilbao]] — the Ordenanzas de Bilbao, a merchant body codifying its own rules
- [[Consulado de Burgos - the universidad de mercaderes]] — insurance ordinances of 1538, and an uncoded identity-wrapper at Bruges. Records dispersed; custodial map not yet drawn

## Italy — repository notes

**The structural fact about Italy** is the mirror of Spain's. Spain's catalogue is unified and its custody devolved; Italy's custody is mostly national but its catalogues are not unified — SIAS describes the state archives, SIUSA the bank, corporate and ecclesiastical ones, SAN aggregates both badly, and **the images live on each archive's own website, outside all three**. A bank archive searched only in SIAS does not appear to exist.

**The maritime and notarial core**

- [[Archivio di Stato di Venezia]] — `Notarile`, `Giudici di Petizion`, `Cinque Savi alla Mercanzia`. The *colleganza* and the *fraterna*
- [[Archivio di Stato di Genova]] — *Notai Antichi*, the earliest notarial registers in Europe and the earliest witness to the western commenda
- [[Archivio di Stato di Firenze]] — `Notarile Antecosimiano`, `Mercanzia`, `Arti`, `Monte Comune`, `Monte delle Doti`. The best-digitised of the majors
- [[Archivio di Stato di Prato - the Datini archive]] — one firm observed as a running system rather than reconstructed from its constitutive documents

**Transferable claims on a perpetual fiscal body — four cases**

- [[Casa di San Giorgio - the Genoese public debt archive]] — 1239–1863, c. 40,250 units, `Debito pubblico` from 1346. Felloni's complete inventory is online
- [[Archivio di Stato di Roma - the luoghi di monte]] — `Luoghi di monte` 1532–1824, within the `Camerale` sections
- [[Archivio Storico del Banco di Napoli]] — the Fondo Apodissario, UNESCO Memory of the World; a charitable pool that became a monetary institution
- [[Archivio di Stato di Milano - the Banco di Sant'Ambrogio]] — 1593, the Lombard construction of the same object

Four independent constructions inside one legal culture. Shared ancestral conditions are guaranteed, so the finding can only ever be parallelism — the right claim is about the conditions under which the form recurs, not about independence.

**Doctrine, and the rest**

- [[Archivio Apostolico Vaticano]] — the accommodations rather than the refusals. Severe access regime: no cameras, three units a day
- [[Archivio Storico del Monte dei Paschi di Siena]] — a *monte di pietà* of 1472 that never stopped operating
- [[Archivio di Stato di Napoli]] — the state counterpart to the Banco; note the 1943 destruction and what it does to arguments from absence

## The Netherlands — repository notes

**The structural fact about the Netherlands is that there is no structural obstacle.** Spain's is devolved custody under a unified catalogue; Italy's is unified custody under three catalogues that do not image. The Dutch have neither — and they have what neither of the others has, an **open-data mandate that reaches the scans**: CC0 inventories and scans, OAI-PMH harvesting, 300 dpi downloads. Several archives will also **digitise on request for nothing** and publish the result.

The caution travels with the convenience. This material will be easier to work than anything else in the European set, and that is a fact about Dutch science policy after 2010, not about the seventeenth century.

**The access layers**

- [[Dutch archives online - the access layers]] — the licence position, the harvesting route, and what free scanning on demand does to the acquisitions calculus
- [[Delpher - the full-text layer]] — 18M+ newspaper pages, full-text, with the 1618–1879 texts downloadable as open data. Price currents, shipping intelligence, insurance notices, bankruptcy notices

**Amsterdam — four series, and the richest match in the whole survey**

- [[Stadsarchief Amsterdam - the notarial archive]] — the only notarial archive in Europe at layer 3
- [[Averijgrossen - the general average adjudications]] — 1700–1810, indexed, scans linked, **recording how liability was distributed between skipper and cargo owners**. A coded form with a serial adjudication record
- [[Kamer van Assurantie en Averij - Amsterdam]] — a standing court for marine insurance from **1598**, four years before the VOC charter
- [[Desolate Boedelkamer - Amsterdam]] — the bankruptcy chamber; the best candidate anywhere for the missing creditor limb

**The companies**

- [[Nationaal Archief - The Hague]] — `1.04.02` VOC, `1.05` WIC, the Staten-Generaal
- [[Hof van Holland - the civil litigation record]] — `3.03.01.01`, 1428–1811, *Civiele sententies* separately indexed
- [[Zeeuws Archief - the Zeeland chamber and the MCC]] — toegang `20`, MCC 1720–1889, UNESCO Memory of the World; a complete company archive of modest size
- [[Westfries Archief - the Hoorn and Enkhuizen chambers]] — the small chambers, and locked-in minority participation

**The rest**

- [[Gemeentearchief Zaanstad - the partenrederij country]] — `OA-0020` and `OA-0170`; where a single-witness row could be repaired from instruments
- [[Stadsarchief Rotterdam - the notarial archive and scanning on demand]] — the second maritime notariate, and the cheap independence test
- [[IISG and NEHA - Amsterdam]] — business archives, price currents, and the mutual and cooperative records the entity census is short of

## Where each coded form's records sit

First pass, to be corrected as the register is built. ⚠️ marks a placement that has not been verified against a finding aid.

| Form | Repository | Series | Layer |
|---|---|---|---|
| Commenda / collegantia | [[Archivio di Stato di Venezia]], [[Archivio di Stato di Genova]], DADU | `Notarile`; *Notai Antichi* | 1–2 |
| Fraterna compagnia | [[Archivio di Stato di Venezia]] | `Notarile`, `Giudici di Petizion` ⚠️ | 1 |
| Bodemerij | [[Stadsarchief Amsterdam - the notarial archive]] | Notarieel archief | **3** |
| Partenrederij | [[Stadsarchief Amsterdam - the notarial archive]]; [[Gemeentearchief Zaanstad - the partenrederij country]] | Notarieel archief; `OA-0020`, `OA-0170` | 3 / 1 ⚠️ |
| Begijnhof | Belgian city archives, Rijksarchief, KADOC ⚠️ | unidentified | 1 ⚠️ |
| Naties | Antwerp FelixArchief, Bruges city archives ⚠️ | — | 1 ⚠️ |
| Bazacle | Archives départementales de la Haute-Garonne | ⚠️ series not yet identified | 1 ⚠️ |
| Deed of settlement company | TNA Kew | `BT 41`, `BT 31`, `BT 34` | **1 only** |
| Chartered corporation | TNA Kew | charters; Patent Rolls `C 66` ⚠️ | 1 |
| Mutual pole / friendly societies | TNA Kew | `FS` — Registry of Friendly Societies ⚠️ subseries | 1 |
| General average | [[Averijgrossen - the general average adjudications]] | Schout en Schepenen, *Vonnissen ter zaken van Averij Grosse* 1700–1810 | **2, indexed** |
| Asiento de avería | [[Archivo General de Indias - Sevilla]] | `CONSULADOS`, `CONTADURIA`, `INDIFERENTE GENERAL` ⚠️ | 2 (partial) |
| VOC | [[Nationaal Archief - The Hague]]; [[Zeeuws Archief - the Zeeland chamber and the MCC]]; [[Westfries Archief - the Hoorn and Enkhuizen chambers]] | `1.04.02`; Zeeland, Hoorn and Enkhuizen chambers | 3 / 1 |

## Where this hub meets the others

- [[MOC - Digitisation and text recognition]] — what to do about everything sitting at layer 2; [[Transkribus - managed HTR platform]] and the open stack are the two routes to layer 3
- [[MOC - Acquisitions and the antiquarian trade]] — the commissioned archival scan is an acquisition decision executed against a repository in this hub
- [[MOC - Historiography and method]] — the funding-map argument belongs there as an argument, not here
- [[MOC - ERC Synergy Grant]] — the travel and transcription budget lines are downstream of this register
- [[Le Bris Goetzmann Pouget 2023 on convergent evolution toward the joint-stock company]] — the Bazacle case, whose source base needs pinning to an actual ADHG series
- [[The asiento de averia is the pooling-to-corporation hinge]] and [[Hierro Anibarro 2005 on the asiento de averia and the privileged company]] — the Seville strand
- [[The creditor limb of entity shielding has no witness]] — a gap that may be an archival gap rather than a conceptual one, and this hub is where that gets tested

## Open questions

- **Bazacle is the weakest placement in the table.** The series at the Archives départementales de la Haute-Garonne has not been identified, and the secondary literature is being used as a proxy for a finding aid. Fix this first — it is the project's flagship pre-modern share case.
- **Which portals expose IIIF and permit bulk download.** This decides whether an HTR pipeline can be pointed at a corpus at all, and it is unresearched for every Tier 1 portal above.
- **The begijnhof and *naties* placements are guesses.** Ecclesiastical and civic record in the Low Countries is split across state, municipal and university custody in a way that the aggregators describe badly.
- **Nothing here is costed.** Reproduction fees are per-institution and per-use, and the register's rights column is empty for every row.
- **Non-European repositories are out of scope by decision, not by judgement.** Ottoman, Geniza and Japanese holdings are named in the grant's travel line and need their own pass.

## Tag note

`archives` is a **new coinage and is not yet a concept tag.** It joins `tooling` and `acquisitions` in the quarantined non-concept layer: it labels a repository as a place one goes, not an object of study. Same rule as the other two — never tag an argument note with it, and never tag a note in this hub with a concept tag.

**Watch the same leak the acquisitions hub warns about.** A claim about how *digitisation funding* conditions what comes into view is an argument and belongs in `notes/` under `provenance`, `selection` or `legibility` — [[The VOC-EIC digital asymmetry is an access regime not a survival difference]] is exactly that note and is correctly placed outside this hub. The test is unchanged: if the note would be different had the funding gone elsewhere, it is infrastructure; if it is *about* the fact that the funding went where it did, it is an argument.
