---
title: Model-read mathematical manuscripts - Godel had a proof checker, Lighthouse a false-positive protocol
type: reference
tags: [tooling]
project: HistorEE
source-session: llm-manuscript-reading-precedents-2026-11-15
created: 2026-11-15
status: seed
---

# Model-read mathematical manuscripts — Gödel had a proof checker, Lighthouse a false-positive protocol

**Two public cases from November 2026 put language models to work on the unread papers of mathematicians, and both give the HistorEE B2 methodology an outside precedent.** In the Gödel case the model did not read the manuscripts. It synthesised a human transcription, and Coq judged the output. Project Lighthouse has the model transcribe as well as read, and it puts in writing the twelve ways a model-generated "find" turns out to be nothing. For HistorEE the transferable element is the external judge, not the model. The project works on material with no formal verifier, so the blind-coding and adjudication design has to do the work Coq does for von Plato.

## Gödel's workbooks — Jan von Plato, University of Helsinki

- **Corpus**: Kurt Gödel's 16 workbooks from the early 1940s, 1,009 pp., in Gabelsberger shorthand. Von Plato's transcription project dates from 2017; the ERC Advanced Grant behind it is project 787758, Helsingin yliopisto (CORDIS).
- **Model input**: von Plato's own transcriptions, six of his books on Gödel, and secondary literature. Claude was used from September 2026, after computer scientists proposed it at an August 2026 conference in France on AI and theorem proving.
- **Model output**: a 650-page analysis produced within days, listing 663 theorems for which Gödel had a proof, a proof sketch or an idea for one. On the axiom of choice it found a near-proof of independence that fails on one definition, which Gödel had stated correctly two years earlier.
- **Verification**: in Coq, about 400 hold as stated, about 200 needed correction and about 50 are false.
- **Objection on record**: Joel David Hamkins (Notre Dame) said the line between Gödel's notes and Claude's reconstruction is still for historians to draw.
- **What the model did not do**: it did not decipher the shorthand. ⚠️ Several outlets report that it did, and their own accounts of the inputs contradict them.
- **The decipherment line proper**: Vincent Christlein (FAU Erlangen, Pattern Recognition) and Nikolaus Weichselbaumer (Mainz) are training handwriting recognition on Gabelsberger (Gödel, Schrödinger, Schmitt, Kästner, Faulhaber). Funded by the Schmidt Sciences HAVI Award 2025.

## Project Lighthouse — `github.com/professorsolderin/project-lighthouse`

- **Corpus**: Gauss, Riemann, Hilbert and Dedekind (scans from SUB Göttingen / GDZ) and Grothendieck (Université de Montpellier); about 12,000 pp. deep-read. Scans are linked, not hosted. Planned next: Euler's 866 works and Ramanujan's notebooks.
- **Pipeline**: page image → verbatim transcription (formulas in LaTeX, deletions marked) → deep read of each mathematics page together with its neighbours, scored 0–10 for how surprising it would be → candidate protocol (human reads the scan; code re-derives the mathematics from the scan; literature search; reviewer who never sees the claim) → `ledger/LEADS.md`. Dead candidates stay in the ledger together with the source that killed them.
- **Cost**: about $0.25 per page for transcription plus deep read with Claude Opus 5.5 (the repo's own estimate).
- **Status labels**: `transcribed` · `read` · `self-checked` · `reviewed` (independent of the finder) · `expert` (signed off by a named specialist). A label records what was done, not what anyone believes. Votes set review priority and never set a label.
- **Lead**: L-019, Riemann's unpublished shock-wave sheets, rated 7/10, which the repo dates to 1856–1866. ⚠️ Not yet confirmed by a palaeographer.
- **Writer identification**: `docs/WRITER_ID_RESULTS.md`, `src/writer_id.py`. A classical pipeline (SIFT/RootSIFT, bag-of-visual-words k = 200 and VLAD k = 64, logistic regression, no API calls) trained on six writers and 164 pages. Cross-validated page accuracy is 160/164 (97.6%). When the Riemann class is trained on Cod. Ms. B. Riemann 19 alone, it recognises only 12–13 of the 20 known Riemann pages in Cod. Ms. B. Riemann 26. The repo states this itself: across volumes and styles the method is much weaker. ⚠️ The README describes this as an "AI handwriting comparison".
- **Licence**: transcriptions and analyses CC BY 4.0, code MIT. For Grothendieck the repo holds analyses and short quotations only, per his 2010 declaration.

## The false-positive protocol against the HistorEE coding

`docs/FALSE_POSITIVES.md` lists twelve failure modes. The checklist must be completed before a candidate can be labelled `self-checked`. Below are the modes that carry over to coding contract forms, each with the vault note it bears on.

| Mode | HistorEE exposure | Vault note |
|---|---|---|
| 2. The result exists only in the transcription | OCR passes on Venetian, Madurell and Yamamoto material | [[The OCR text layer evidences a clause's presence, not its absence]] |
| 3. The editors already published it | Source editions and their apparatus | [[MOC - Source editions]] |
| 4. Known under another name | *commenda* / *comanda* / *qirāḍ* / *muḍāraba* / *ʿisqa* | [[MICOLL - Padua ERC tracing commercial-law terms is a transmission control not a rival]] |
| 7. Anchoring | The coder told what the form is supposed to show | [[A blind is a property of the channel not of the dataset]] |
| 8. Hand and date assumed | Formulary against executed deed; register copy against original | [[Doctrine, deed and conduct are three layers and the time-average test needs all three]] |
| 9. "Not found" means "didn't look well" | Absence claims from a search or a text layer | [[The OCR text layer evidences a clause's presence, not its absence]] |
| 10. "Fully read" when pages were skipped | Batch OCR and batch coding runs | none ⚠️ |
| 11. The surprise score is a model opinion | Model confidence entering a coded value | none ⚠️ |
| 12. Modern restatement imports structure not on the page | Reading entity shielding or risk pooling into a contract | [[Typology and character coding literature]] (`comparative-concept`) |

The wording rule worth adopting as it stands: "the Nachlass contains" is allowed; "the author wrote" waits for the palaeographer. Every rating carries its conditions.

## For the application

- **B2 methodology / risk**: give two precedents for two layers. Christlein-type HTR for reading; Gödel/von Plato and Lighthouse for synthesis under external verification. HistorEE's own claim is to apply the same discipline where no formal verifier exists.
- **Resources annex**: $0.25 per page for transcription plus reading is an outside benchmark, not a quote.

## Flags

- ⚠️ The Guardian article of 2026-11-13 was not read; the fetch was blocked. All Gödel figures come from secondary reports of it. 400 + 200 + 50 does not add up to 663. Read the original before citing any figure.
- ⚠️ The X post (`x.com/Salim_AIi/status/2119447102958752038`) was not read; the fetch was blocked.
- ⚠️ Lighthouse is run by an anonymous handle, has had no review, and reports no error rate for transcription or screening. Cite it as practice, not as evidence that the method works. The repo had 52 stars and 2 forks when read.

## Links

- [[MOC - Historiography and method]]
- [[MOC - ERC Synergy Grant]]
- [[MOC - HistorEE]]
- [[Agentic research set-ups - the public landscape against the HistorEE protocol]]
- [[Blind re-coding workflow - operator, coder, application]]
- [[MiDRASH - the machine transcription of the Geniza]]

## Source

- *The Guardian*, 2026-11-13, "Kurt Gödel notebooks: AI helps unlock hidden discoveries" (theguardian.com/science/2026/nov/13/…), not read. Reported via newsbytesapp.com, mezha.net, archyde.com, mlq.ai, explainx.ai, positron.today, themyersreport.substack.com, read 2026-11-15.
- cordis.europa.eu/project/id/787758; lme.tf.fau.de/?p=26985 (HAVI award), read 2026-11-15.
- github.com/professorsolderin/project-lighthouse at commit `c65be885` (2026-11-10). Read: README, `docs/FALSE_POSITIVES.md`, `docs/WRITER_ID_RESULTS.md`, 2026-11-15.
