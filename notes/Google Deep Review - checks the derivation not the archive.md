---
title: Google Deep Review - checks the derivation not the archive
type: reference
tags: [tooling]
project: infrastructure
source-session: google-deep-review-2026-10-15
created: 2026-10-15
status: seed
---

# Google Deep Review — checks the derivation not the archive

**An agentic Gemini pipeline that reads a whole manuscript and returns major and minor issues, suggested fixes and summaries. Google Research released it publicly on 14 October 2026.** Its tested strength is mathematical and logical verification in computer-science papers. For this project it can audit the formal apparatus of a draft (derivations, internal consistency between sections and tables). It cannot audit the archival footing, because its only external grounding is Google Search.

## Provenance

- Google Research with Google DeepMind and Google Cloud. Announcement by Rajesh Jayaram and Vincent Cohen-Addad, 14 Oct 2026.
- Successor to the **Paper Assistant Tool (PAT)**. PAT ran as opt-in pre-submission feedback, decoupled from official review, at STOC 2026, ICML 2026, NeurIPS 2026 and ICLR 2027: 16,000+ manuscripts. The landing page also lists AISTATS.
- Method paper: Rajesh Jayaram, Drew Tyler, David Woodruff, Corinna Cortes, Yossi Matias, Vahab Mirrokni, Vincent Cohen-Addad, *Towards Automating Scientific Review with Google's Paper Assistant Tool*, arXiv 2606.28277 (v1, 26 Jun 2026). Proposes a four-level taxonomy of AI–human collaboration in scientific evaluation. Reports the STOC and ICML pilots only.
- The public version runs on Gemini 4 Argon, newer than the models behind the PAT figures.

## How it works

1. **Segmentation.** A segmenter agent splits the document into logical segments. Segments may overlap and must cover the whole text.
2. **Adaptive budgeting.** Compute is allocated by information density: a proof gets more reasoning budget than a literature review. The user can also set overall effort.
3. **Parallel verification.** One reasoning agent per segment. Each has the full document in context for cross-references but reviews only its own segment.
4. **Synthesis and grounding.** A synthesis agent merges the segment reports, re-runs cross-section consistency checks, and grounds claims through tool calls and Google Search as the anti-hallucination step.

Runtime is about 10–20 minutes per document (Jayaram, quoted by R&D World). The design targets three failure modes Google names in single-call review: the reasoning budget runs out on long documents, cross-section dependencies are missed, and nuanced claims pass unscrutinised.

## Evidence — what the figures measure

- **SPOT benchmark.** PAT recall on mathematical errors is 34% above zero-shot. This is a relative gain over a single model call, on the earlier system, on mathematical errors only. It is not a detection rate.
- **Pilot outcomes (landing page).** Significant mathematical errors found in more than 30% of theoretical papers; 60% of authors ran new experiments after feedback. Self-reported, opt-in population, no control group.
- ⚠️ **"89.7% detection rate"** (DigitalToday headline) and **"35.4% of ML papers"** (Tech Times) appear in neither Google's blog post nor the paper abstract. Do not cite without the primary table.
- ⚠️ One trade report gives the pilot as 15,000+ papers against Google's 16,000+.
- ⚠️ Full paper not read. The SPOT figure and taxonomy come from the abstract.
- Every validation venue is in computer science. No published evaluation on historical argument, on humanities prose, or on non-English sources.

## Access and cost

- Two free reviews per user per week, worldwide. Portal: `research.google/deepreview`.
- Higher volume: connect a Gemini API key. Standard Gemini API charges apply, with no Deep Review fee on top. A Deep Review API exists for programmatic use.
- ⚠️ **Input formats are reported inconsistently.** Blog: PDF and plain text at launch, multi-file input "coming soon". Landing page: PDF, text, Google Docs, Google Slides. R&D World adds PowerPoint, Word and Markdown. Test a .docx before relying on it.
- Antigravity has a derived "Teamwork Deep Document Review Pattern", invoked with `/teamwork-preview`. It is inspired by Deep Review, not the same system.

## Data terms

- Uploads are never used to train, fine-tune or improve Google models (blog).
- Uploads are stored **one year**, for display in the Deep Review interface.
- The landing page offers a separate opt-in letting the research team use data to improve Deep Review. Leave it off.
- A review may run web searches to find related work. Google says the document stays private, but its content drives those queries.

## Relevance to this project

- **Use it on the formal layer.** The time-average and ensemble-average algebra, absorbing-barrier arguments and growth-rate computations in the HistorEE papers and the book are the kind of material the tool was built and validated on.
- **Do not read a clean report as a check on sources.** Grounding is Google Search. It cannot see Japanese archives, *kuzushiji* material or most of the classical Chinese record, so it says nothing about whether a citation or a reading of a document holds.
- **Cloud-only.** Same constraint as the managed HTR tier: unpublished drafts are yours to upload; transcriptions of archival material held under reproduction restrictions may not be. See the third decision in [[MOC - Digitisation and text recognition]].

## Open questions

- Untested on long-form historical argument where the claims are interpretive rather than derivational. One trial on a finished chapter would show whether its major issues are substantive or stylistic.
- A Gemini reviewer reads from a different model family than the codebook coders. Whether that makes it usable as a second reader in the verification layer is untested; see [[Blind re-coding workflow - operator, coder, application]].

## Links

- [[MOC - Digitisation and text recognition]] — nearest tooling hub; no hub yet for AI review of drafts
- [[Blind re-coding workflow - operator, coder, application]]
- [[Transkribus - managed HTR platform]] — the other cloud-only managed service in the reference layer

## Source

- Deep Review landing page, research.google/deepreview, read 2026-10-15. The page body sits behind a Google sign-in; its text was taken from the search index.
- *Analyzing technical documents with Deep Review*, research.google/blog/analyzing-technical-documents-with-deep-review/, 14 Oct 2026, read 2026-10-15. Pipeline, pilots, access, data terms.
- arXiv 2606.28277, abstract page, arxiv.org/abs/2606.28277, read 2026-10-15. SPOT figure, taxonomy, pilot scope.
- Secondary: R&D World (runtime, effort setting, formats); GIGAZINE; Neoteo (API pricing, data opt-in); DigitalToday and Tech Times (the unverified figures above).
