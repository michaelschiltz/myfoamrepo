---
title: MOC - Acquisitions and the antiquarian trade
type: moc
tags: [moc, acquisitions]
project: infrastructure
source-session: antiquarian-book-trade
created: 2026-08-13
status: seed
---

# MOC — Acquisitions and the antiquarian trade

Reference hub for getting texts into reach: the rare book trade, want-lists, commissioned surrogates, and the routes between them. **This is an infrastructure layer, not an argument layer.** Notes here are `type: reference`, carry `project: infrastructure`, and are deliberately not wired into the concept graph. Nothing below is evidence for a claim about financial history.

It is the sibling of [[MOC - Digitisation and text recognition]]. That hub asks how to *capture and read* a document you already have access to; this one asks how the document comes within reach at all. The two meet at the commissioned scan, which is an acquisition decision executed with digitisation hardware.

## The decision that actually matters

The trade presents acquisition as a price question — what does the copy cost. It is not. For this project the binding constraint is **discovery, not purchase**: knowing that a text exists, that a copy is on the market, and which dealer's specialism it falls under. Price is downstream of all three and usually the least interesting.

This has a corollary that runs against instinct. The famous houses are organised around objects whose value is already established — Gutenbergs, Caxtons, canonical firsts in fine bindings. The material this project needs is the opposite kind: commercial arithmetic, insurance treatises, guild ordinances, company charters, *averia* documentation. These are cheap and *invisible*, catalogued by a handful of specialists and by nobody else. **The scarce input is the specialist's finding aid, not the budget.** See [[Antiquarian booksellers - the top tier and where economic history sits]] for who those specialists are and why prestige and reliability are separate properties.

## Second decision: the filter is not the record

Every acquisition route is a selection filter, and each filter has a shape that is easy to mistake for the shape of the past.

- **Dealer specialisms are commercial, not historiographical.** A category exists in the trade because it sells. The absence of a trade category is a fact about collectors, not about the survival of documents.
- **Cataloguing conventions determine findability.** [[Isqa reading list to acquire]] records the instance in full: a substring-only search over titles returned nothing for `isqa`, and the absence was read as absence from the library. Six relevant items were already held. The method rule that came out of it — *a search returning nothing is evidence about the query string, not about the corpus* — is an acquisitions rule before it is anything else.
- **Digitisation regimes are funded geographies.** The same error at corpus scale, already argued in the project's own terms: [[The VOC-EIC digital asymmetry is an access regime not a survival difference]] and [[The QDL corpus is conditioned on its funder's geography]].

This is the project's own methodological guardrail applied to its own supply chain. [[The deficit reading of absence is the scalar ranking in evidentiary form]] and [[Refusals are observations of the filter not inferences from survivors]] are the argument-layer statements; the acquisitions consequence is that a want-list which comes back empty has told you about the trade, not about the sixteenth century.

## Third decision: own, borrow, or commission

Purchase is one route among several and rarely the cheapest per unit of access. The routes differ in latency, cost and — decisively — in what they leave you holding afterwards.

| Route | Latency | Indicative cost | What you end up with | When it is right |
|---|---|---|---|---|
| Specialist dealer, want-list | Months to years | Market; often modest for unglamorous material | The object, warranted | The text is uncatalogued elsewhere and you need it repeatedly |
| Dealer, from catalogue | Days | Market | The object, warranted | It has surfaced and will not surface again soon |
| Auction | Fixed calendar | Hammer + premium, no warranty ⚠️ | The object, *as is* | Nothing else is available; bid through a dealer |
| ILL / document supply | Weeks | Low | A reading copy, temporarily | One-off consultation |
| Commissioned archival scan | Weeks to months | Per-page, institution-set | An archival master, permanently | The original is unpurchasable and you need it citable |
| Open digital corpus | Immediate | Free | A file on someone else's terms | It already exists — check first |
| Facsimile / reprint | Days | Low | A derivative | Reading only, never for claims about the artefact |

⚠️ = auction descriptions are not subject to the ILAB code; see the booksellers note.

**Check the open corpora before spending anything.** Where a text is already transcribed the entire calculus above collapses, which is the point of [[GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC]].

## Fourth decision: what a warranty is worth

Buying through an ILAB affiliate converts the transaction from *caveat emptor* into a warranted one — mandatory disclosure of defects, restorations and sophistications; full refund including return shipping on misrepresentation; guaranteed authenticity; clear title. That warranty is the product. It is also **worthless unexercised**: collate on arrival, inside the ten-day window, or the protection is notional.

Provenance deserves the same discipline the project applies elsewhere. A chain of named owners establishes *priority* — that this copy passed through these hands. It does not by itself establish *independence* — that the copy is what the description says it is. [[Split provenance into priority and independence]] is the argument; here it is the buying rule.

## Notes

- [[Antiquarian booksellers - the top tier and where economic history sits]] — the dealers, the ILAB guarantee, and the economic-history specialists
- [[Isqa reading list to acquire]] — the live want-list, and the search-failure post-mortem that generated the method rule above

## Where this hub meets the others

- [[MOC - Digitisation and text recognition]] — the surrogate route; [[Preservation-grade overhead scanners - Zeutschel and i2S]] carries the rule for commissioning (ask for the uncompressed TIFF archival master, not the delivery PDF)
- [[VOC digital corpus - what is online and on what terms]] and [[EIC digital corpus - what is online and on what terms]] — the free tier, and its asymmetry
- [[Van Dam's Beschryvinge - the VOC described by its own advocaat]] — a worked case of a text whose editions and access conditions determine what can be claimed from it

## Open questions

- **The Japanese trade is not covered by any of this.** For Japanese primary material — *kuzushiji* commercial documents, house ledgers of the [[The Nakai ledger scores as losses what present value scores as gains]] kind — the Western antiquarian trade is largely irrelevant. The routes are the ABAJ shops (Jimbōchō, Osaka, Kyoto), institutional holdings, and permission to photograph in situ. That is a separate note and does not yet exist.
- **Whether acquisitions are chargeable.** Unresolved against [[MOC - ERC Synergy Grant]] budget lines; it determines whether the want-list is aspirational or operational.
- **No note on the Zotero sink.** Acquisition ends at a record with a DOI, a key, and a collection — and [[Isqa reading list to acquire]] already documents a duplicate-merge failure where `if_exists: file` matched on a DOI the original record did not carry. Idempotency keys only work on the field they key on. The import pipeline is where this hub leaks and it is unwritten.
- Institutional purchase versus personal is unaddressed throughout. The Hokkaido library's acquisition budget and its ILL reach change every row of the table above.

## Tag note

`acquisitions` and `book-trade` are **new coinages and are not yet in `tags.md`.** They belong in the quarantined non-concept layer beside `tooling`, `htr`, `ocr`, `kuzushiji` and `scanning-hardware` — they label the supply chain, not an object of study. The same rule holds: never tag an argument note with them, and never tag a note in this hub with a concept tag. If a claim about the trade as a *historical* object ever becomes load-bearing, it belongs in `notes/` as a proper atomic note with concept tags, not here.

## Links

- [[MOC - HistorEE]]
- [[MOC - Digitisation and text recognition]]
- [[MOC - Historiography and method]]
