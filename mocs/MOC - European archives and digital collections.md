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

**Belgium qualifies this, and the qualification is the more important half.** Its infrastructure is clearly the worse — images behind a registration wall, a press corpus a fifteenth the size of the Dutch one — and its holdings are, for this project's central question, the best in the survey. Until that pass every country confirmed the funding map in the same direction, which made it easy to read as a description of where the evidence is. **It is not. It is a description of where the evidence is *legible*, and the two come apart.** See [[Belgian archives online - the access layers]].

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
| Belgium | Rijksarchief / Archives de l'État | <https://search.arch.be/> | Millions of images via AGATHA, free — but **registration required to view**, and no CC0, OAI-PMH or bulk route advertised. See [[Belgian archives online - the access layers]] |
| United Kingdom | TNA Discovery | <https://discovery.nationalarchives.gov.uk/> | Catalogue. Company and friendly-society records are description-only |
| France | FranceArchives + départementales | <https://francearchives.gouv.fr/> | Federated; the *départementales* hold the commercial material and image independently |
| Spain | PARES | <https://pares.cultura.gob.es/> | State archives only — the devolved and corporation-held archives are outside it. See [[PARES - the access layer for the Spanish state archives]] and the Spain section below |
| Portugal | DigitArq / Torre do Tombo | <https://digitarq.arquivos.pt/> | National catalogue with images ⚠️ current URL and scale to confirm |
| Italy | SIAS / SIUSA / SAN | <https://sias-archivi.cultura.gov.it/> | Three overlapping description systems and no image portal at all. State archives in SIAS, bank and corporate archives in SIUSA. See [[SIAS SIUSA and SAN - the Italian access layers]] |
| Germany | Archivportal-D | <https://www.archivportal-d.de/> | Archival section of the Deutsche Digitale Bibliothek |
| Sweden | Riksarkivet, Digitala forskarsalen | <https://sok.riksarkivet.se/en/digitala-forskarsalen> | Heavily imaged; the Riksarkivet also publishes HTR models openly |
| Norway | Digitalarkivet | <https://www.digitalarkivet.no/en/> | Near-total for major series |
| Croatia | ARHiNET | <http://arhinet.arhiv.hr/> | Descriptive; Dubrovnik is `HR-DADU` |

## Tier 3 — corpora already transcribed

Where a corpus is at layer 3 the entire calculus above collapses, which is the point of [[GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC]]. Check this tier before spending anything.

- **GLOBALISE** — ≈5 million OBP scans, Loghi-transcribed, Dataverse download. See [[VOC digital corpus - what is online and on what terms]].
- **Alle Amsterdamse Akten** — Amsterdam notarial deeds, HTR, free-text searchable. See [[Stadsarchief Amsterdam - the notarial archive]].
- **Haarlem** — the whole notarial archive reported word-searchable ⚠️ transcription basis unconfirmed. See [[Noord-Hollands Archief - Haarlem]].
- **Itinera Nova** — Leuven aldermen's registers, 14th–18th c., volunteer-transcribed. See [[Itinera Nova - the Leuven aldermen's registers]].
- **Delpher** — 18M+ newspaper pages, 1618–1879 downloadable as open data. See [[Delpher - the full-text layer]].
- **Sound Toll Registers Online** — every passage of the Danish straits, 1497/1557–1857, transcribed into a database. See [[The Sound Toll Registers]]. **The only genuine denominator in the survey**, and an interpretation rather than a copy.
- **Fondo Datini** — catalogued to item level; layer 1 at fine grain rather than layer 3.
- **Medici Archive Project / BIA** — a scholar-annotated *selection*, not a transcribed series. See [[Medici Archive Project - the BIA platform]].
- The English side has no member of this tier at all; see [[EIC digital corpus - what is online and on what terms]].

**Every transcribed *notarial* corpus in this tier is in the Low Countries.** The exception is the Sound Toll series, which is Danish, fiscal, and not a corpus of instruments at all. **That is not a fact about where early modern Europe wrote things down**, and a comparative corpus assembled from what is searchable will be a corpus about the Low Countries with illustrations from elsewhere.

## Country hubs

Repository-level notes live in country MOCs, each carrying that country's structural fact. **The structural facts are different in each case, and the differences are the substance** — this hub exists to hold what is common, not to list what is not.

| Country | Hub | The structural fact |
|---|---|---|
| Spain | [[MOC - Spanish archives]] | Unified catalogue, devolved custody. A null result in PARES is a fact about the Ministry's remit |
| Italy | [[MOC - Italian archives]] | Mostly national custody, three unreconciled catalogues, images outside all of them. No layer 3 |
| Netherlands | [[MOC - Dutch archives]] | No obstacle: CC0 scans, OAI-PMH, free scanning on demand. The easiest country, and the most biasing |
| Belgium | [[MOC - Belgian archives]] | Worse infrastructure, better holdings. The country that breaks the proxy |
| France | [[MOC - French archives]] | Scale, against one uniform classification. A question can be put to a *series* nationwide — and the interfaces are the least remotely-workable in the survey |
| Germany | [[MOC - German archives]] | No frame and no national archive for the period. Competence is civic, and the cities are where the material is |
| Nordics | [[MOC - Nordic archives]] | Best infrastructure in Europe, thinnest institutional variety — Belgium's mirror. The one absence in the survey that is probably evidential |
| Britain | [[MOC - British archives]] | Excellent description, thin imaging where it matters. Three major corpora opened by foreign or commercial money, none of it British |
| Croatia | [[MOC - Croatian archives]] | One frame, many custodians — and at Dubrovnik the **whole archive of a commercial republic**, all 73 Republic fonds on the Memory of the World register |
| Ottoman (non-European) | [[MOC - Ottoman archives]] | The court record divided by the Republic and by the successor borders and reunited only as images, in one reading room; the central archive classified by subject before provenance; the waqf's deeds held by the waqf's administrator. **Script decides the layer**, and the census's rows are accounts in siyakat |
| Geniza (non-European) | [[MOC - Geniza archives]] | Not an archive but a deposit, emptied by dealers and an expedition into sixty collections — and **reunited online at every layer**, down to a machine transcription of the whole. The survival rule is a script rule, and so is the machine's accuracy |
| Japan (non-European) | [[MOC - Japanese archives]] | Custody follows the house, and dispersal is policy. **Books are imaged; the documents the census needs are not** — they are at layer 3 in print, in municipal histories. The binding constraint is permission and residency, not script |
| China (non-European) | [[MOC - Chinese archives]] | The Qing central record is divided by a sale and a strait, under opposite access regimes — and **is not where the census's evidence is**. The census's Chinese rows are private contracts read through one compilation by one article; the associations' operating record survives mostly abroad |

**The European survey is complete.** Non-European repositories — Ottoman, Geniza, Japanese, South and East Asian — are named in the grant's travel line and need their own pass; see [[Handoff - the non-European archive survey]]. **The Ottoman, Geniza, Japanese and Chinese passes are done** and hang off the table above as the first non-European rows: [[MOC - Ottoman archives]], [[MOC - Geniza archives]], [[MOC - Japanese archives]], [[MOC - Chinese archives]].

## Where each coded form's records sit

First pass, to be corrected as the register is built. ⚠️ marks a placement that has not been verified against a finding aid.

| Form | Repository | Series | Layer |
|---|---|---|---|
| Commenda / collegantia | [[Archivio di Stato di Venezia]], [[Archivio di Stato di Genova]], [[Drzavni arhiv u Dubrovniku]] | `Notarile`; *Notai Antichi*; [[The Ragusan chancery and notarial series]] | 1–2 |
| Fraterna compagnia | [[Archivio di Stato di Venezia]] | `Notarile`, `Giudici di Petizion` ⚠️ | 1 |
| Bodemerij / Bodmerei | [[Stadsarchief Amsterdam - the notarial archive]]; [[Bodmerei - where the German bottomry records are]] | Notarieel archief; Hamburg `Admiralitätskollegium`, Lübeck *Niederstadtbuch* ⚠️ | **3** / 1 ⚠️ |
| Partenrederij | [[Stadsarchief Amsterdam - the notarial archive]]; [[Gemeentearchief Zaanstad - the partenrederij country]] | Notarieel archief; `OA-0020`, `OA-0170` | 3 / 1 ⚠️ |
| Begijnhof | Dispersed — see [[Begijnhof archives - where the beguinages records are]] | unidentified across four custodians | 1 ⚠️ |
| Naties | [[Natie archives - where the Antwerp nations records are]]; [[Stadsarchief Brugge - the Hanse and the nations]] | not located; possibly in successor-company custody | 1 ⚠️ |
| Bazacle | [[The Bazacle records - a custody problem]] | Toulouse, cote unidentified; modern archive plausibly EDF *Fonds Ex-Sociétés* ⚠️ | 1 ⚠️ |
| Deed of settlement company | [[BT 41 BT 31 and the company files]] | `BT 41`, `BT 31`, `BT 34` | **1 only**; `BT 31` is a sample ⚠️ |
| Chartered corporation | [[C 66 - the Patent Rolls and the charters]] | enrolled charters, Patent Rolls `C 66` ⚠️ | 1 |
| Mutual pole / friendly societies | [[FS - the Registry of Friendly Societies]] | `FS` — deposited rules ⚠️ subseries | 1 |
| Entity shielding, creditor limb | [[Insolvente Boedelskamer - Antwerp]]; [[Desolate Boedelkamer - Amsterdam]] | `IB 1`–`IB 3,038` | 1 ⚠️ |
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
- **The `begijnhof` and `natie` records have still not been located**, and both now have notes saying so properly rather than a flag in a table: [[Begijnhof archives - where the beguinages records are]] and [[Natie archives - where the Antwerp nations records are]]. Both are desk tasks and both should precede any citation of those rows in the grant material.
- **Whether the Insolvente Boedelskamer records state reasoning or only outcomes.** It decides whether the census's creditor limb has a witness, and it is the single most consequential unanswered question in the survey.
- **Nothing here is costed.** Reproduction fees are per-institution and per-use, and the register's rights column is empty for every row.
- **Non-European repositories are out of scope by decision, not by judgement.** Ottoman, Geniza and Japanese holdings are named in the grant's travel line and need their own pass.

## Tag note

`archives` is a **new coinage and is not yet a concept tag.** It joins `tooling` and `acquisitions` in the quarantined non-concept layer: it labels a repository as a place one goes, not an object of study. Same rule as the other two — never tag an argument note with it, and never tag a note in this hub with a concept tag.

**Watch the same leak the acquisitions hub warns about.** A claim about how *digitisation funding* conditions what comes into view is an argument and belongs in `notes/` under `provenance`, `selection` or `legibility` — [[The VOC-EIC digital asymmetry is an access regime not a survival difference]] is exactly that note and is correctly placed outside this hub. The test is unchanged: if the note would be different had the funding gone elsewhere, it is infrastructure; if it is *about* the fact that the funding went where it did, it is an argument.
