---
title: Hold the rater fixed and vary the evidence
type: permanent
tags: [verification, provenance, coding-ontology, selection, historiography, ensemble-average]
project: HistorEE
source-session: recode-methodology-discussion
database: [organizational_forms, loss_mitigation_forms]
created: 2026-09-27
status: seed
---

# Hold the rater fixed and vary the evidence

**A blind re-code of existing cells from the same sources estimates how much the coding depends on the interpreter, with the evidence held fixed.** The project's inferences run the other way: from accumulating, heterogeneous evidence to claims about forms. A reliability test on fixed sources therefore answers the less important question. Once the rater effect is roughly known, the next experiment holds the rater fixed and varies the evidence.

## What the fixed-evidence re-code measured

**A coding depends on three things: the evidence, the interpreter and the instrument** (the codebook's definitions and value sets). The 2026-09-26 pass had Opus 5.5 re-code two forms from the five PDFs Opus 5 had used. With the evidence held fixed, it isolated the interpreter.

**The disagreements were mostly about the instrument and about calibration.** Of 64 cells, 53 agreed and 11 disagreed. Of the eleven:

- **six were missingness disagreements**: where "the source addresses this" begins;
- **most of the rest turned on the instrument**: whether a spiritual hazard counts in `LR4`; where the entity locator sits (`1` or `P` on `LP2`/`LP3`); and whether one row spans two governance regimes (`MG2`).

All nine confidence-only differences ran the same way, one step lower.

**So the pass learned about the instrument and about the new model's calibration, and almost nothing about the evidence.** Both raters are Claude models, so their errors are correlated and the 53 agreements are weak evidence of reliability.

**The evidence findings came as by-products of reading in full, not from the design.** One source reproduces another's general text verbatim; a text layer called unreadable turned out to read cleanly.

## Blinding protects priority and nothing else

**Blinding is not a general epistemic virtue.** It makes an agreement count as a test by securing a prediction's priority over the evidence it is scored against ([[A prediction is evidence only if its priority is committed]]). For accumulating evidence it is harmful: the prior coding is a posterior, and a blind pass restarts from a near-flat prior on the same pages.

**Target new evidence where current belief is most sensitive.** The value of new evidence is highest there: low confidence, a single witness, or a value the working typology finds improbable. Two cautions apply.

- **The winner's curse.** A surprising value is surprising partly because of noise, so revisiting it should shrink it. A coder anchored on the surprising value shrinks it too little, and anchoring is a documented failure of language models.
- **Severity.** A severe test is one the claim would probably fail if it were false. Searching for that evidence requires knowing the claim, so blindness is neither necessary nor sufficient for severity.

**The resolution: open search, protected reading.** The searcher knows the current coding and hunts for disconfirming material. The reader codes new material before the live value is revealed, then reconciles, and both values are kept. Alternatively, the reader pre-registers per cell what finding would move it.

**What blinding should target** is the path from theory to coding: the selection rationale, and which component the argument needs. It should not target the path from a prior coding to the new one. A coder can see earlier readings and their quotations and still be kept blind to what the argument wants.

## Secondary and primary are two filters, not near and far

**A secondary source is a compression.** Primary material has passed through the author's question, framework and citation genealogy. Coding from secondary literature partly codes the historiography.

**A primary source is not closer to the truth, only filtered differently**: by survival, not by authorial selection. A discard deposit is the extreme case.

**Agreement across the two filters is robustness to both.** Where they diverge, the gap has three possible causes:

- **compression error**: the generalisation outruns the documents;
- **within-form heterogeneity**: the documents vary where the author reports a type;
- **selection**: the author studied only some instances.

**"Primary" is three classes, not one:**

- **Normative** texts (codes, sea laws, fatwas, customs) are themselves compressions of practice.
- **Transactional** documents (contracts, acts, ledgers, letters, court entries) are the only instance-level evidence.
- **Institutional** records (charters, minutes, placards) sit in between.

**Notarial acts measure the formulary.** The clauses come from the notary's drafting practice, so at that level the effective sample is the number of notaries, not the number of acts ([[The notarial security clause is boilerplate and cannot carry a typology]]).

## The type row is an ensemble abstraction

**A form-level cell coded from secondary literature describes the modal type.** Primary material gives instances and their trajectories, and can show that the form is not stationary. Two cases from the 2026-09-26 pass show this in miniature:

- a confraternity row whose governance changes regime around 1785;
- a communal fund that is a sub-pool form in one city and an aggregating form in another.

Whether a type row may stand for its instances is the same question as whether an ensemble may stand for a trajectory ([[Licensing the ensemble is a dynamical question not a metaphysical one]]).

**The matrix cannot hold a distribution.** `P` is a structural half-state, not "present in seven deeds of twenty". Primary coding therefore needs an instance layer, with form-level cells derived under an explicit aggregation rule that keeps the spread. **Frequency never becomes `P`.**

## Accumulation is not convergence

**Evidence accumulates, but the posterior need not narrow.** New evidence can widen it, as when a form turns out to be two, and that is a finding, not noise.

**Accumulation also requires tracking dependence.** Otherwise one upstream author counted four times reads as four confirmations ([[Split provenance into priority and independence]], [[Galton's problem applies to the apparatus not only to the institutions]]).

## The design that follows

**Two experiments, one on each side of the decomposition.** The 2026-09-26 pass varied the rater (Opus 5 → 5.5) with the evidence fixed. The next holds the rater fixed and varies the evidence, in three arms, each in its own chat:

- one arm codes from the secondary sources alone;
- one codes from the transactional record alone;
- the primary arm then sees the live values, reconciles, and searches the corpus for evidence against its own coding.

**The first pilot takes the Genoese commenda cartularies.** There, primary and secondary share one evidential base, because the secondary dataset was built from those cartularies. The pilot therefore measures compression, not independent corroboration.

**Decisions of 2026-09-27:**

- wait for OCR of a third notary (Marseille, 1248) before running;
- run the secondary arm, so that evidence and rater are not confounded;
- add a `source_class` column to `recodings.csv`.

## Links

- [[A blind is a property of the channel not of the dataset]]
- [[A blind re-coding is only blind if the value sets are]]
- [[A prediction is evidence only if its priority is committed]]
- [[Split provenance into priority and independence]]
- [[Galton's problem applies to the apparatus not only to the institutions]]
- [[The notarial security clause is boilerplate and cannot carry a typology]]
- [[Refusals are observations of the filter not inferences from survivors]]
- [[The record of non-survivors survives where failure was administered]]
- [[Licensing the ensemble is a dynamical question not a metaphysical one]]
- [[Blind re-coding workflow - operator, coder, application]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

A discussion between MS and Claude on 2026-09-27, after the pass `opus55-recode-mutual-pole-2026-09-26` (`HistorEE_codebooks/records/`, logbook 4, 2026-09-26 (ii)).

- **MS's diagnosis:** the pass tested the model and its effort level, and was blind to the quality of the evidence.
- **MS's proposals:**
  - allow more non-blind sessions, directed at informative results;
  - read secondary codings systematically against primary sources, which the new Zotero primary collections now make feasible;
  - test the Geniza corpora later.
- **Claude's contributions:**
  - the decomposition into evidence, interpreter and instrument;
  - the winner's-curse and severity arguments;
  - the read-then-reveal protocol;
  - the instance layer.
- **Pilot design:** project doc `claude/commenda-pilot-design-2026-09-27.md`.
