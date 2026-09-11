---
title: The clearing records dataset has no archive yet
type: reference
tags: [archives]
project: infrastructure
source-session: japanese-archives-survey
created: 2026-09-11
status: seed
---

# The clearing records dataset has no archive yet

**`HistorEE_codebooks/datasets/clearing_records` is synthetic.** Its datapackage calls it an "ILLUSTRATIVE / SYNTHETIC worked example" of Tokugawa money-changer and remittance settlements, built to demonstrate the coding conventions, and **"Not archival data."** The survey of the other two datasets was a search for the archives behind rows that exist; **for this one there are no rows to place, and the survey's job is to say where real ones would come from.** It is the dataset that carries the book's title.

## Where a real one would come from

| Holder | What | Kind of source | Note |
|---|---|---|---|
| [[Mitsui Bunko - the Mitsui house archive]] | *ryōgaeten* ledgers; *Ōmotokata* half-yearly accounts, ~160 years | **one participant, in series** | reading room; not online |
| [[Osaka Museum of History - the Konoike family documents]] | *ryōgae* business, *daimyōgashi* | **one participant, donated selection** | access not established |
| [[Bank of Japan Currency Museum - the Senpeikan documents]] | Edo, Osaka and Kyoto *ryōgae* material, ~2,400 documents catalogued | **a collector's selection across firms** | catalogue published 2000 |
| [[Sumitomo Historical Archives - Kyoto]] | house finance beside copper | one participant | Tue/Thu, reproductions only |
| [[Kyu-bakufu hikitsugisho - the Edo town magistrate records]] | the regulator's compilations; the guild re-establishment of 1851 in print | **the administrator** | digitised; 15 vols in print |

**Three kinds of witness, and they are not interchangeable.** A participant's ledger records the transactions one firm cleared; a collector's documents record what survived and was bought; a regulator's compilation records what came to the magistrate's attention. **A frequency computed across them would mix three survival rules** — the rule [[MOC - European archives and digital collections]] states for national corpora, applied inside one market.

## The recommendation, stated for the maintainer

**Before the synthetic rows are replaced, choose the witness type**, and state it in the datapackage the way the census states `boundary_basis`. **The Mitsui ledgers are the only series** in the list; everything else is a selection. And the Tuesday-and-Thursday regime at Sumitomo, the reading-room regime at Mitsui and the residency wall at the NDL mean **the work is on site in Japan** — see [[NDL transmission service for individuals - the residency wall]].

## Links

- [[MOC - Japanese archives]]
- [[Mitsui Bunko - the Mitsui house archive]]
- [[Kyu-bakufu hikitsugisho - the Edo town magistrate records]]
- [[Refusals are observations of the filter not inferences from survivors]]

## Source

Japanese archives survey, 11 September 2026. `datasets/clearing_records/datapackage.json` (title and description); the linked repository notes.
