---
title: Modi script and the forty million documents
type: reference
tags: [archives]
project: infrastructure
source-session: south-asian-archives-survey
created: 2026-09-12
status: seed
---

# Modi script and the forty million documents

**Marathi administration from the seventeenth century to the early twentieth was written in Modi**, a cursive script distinct from Devanagari. **The reported stock is about 40 million Modi documents** in archives, temples, private collections and government departments, **"mostly undeciphered and inaccessible, due to the scarcity of expert readers"**. ⚠️ The 40-million figure comes from a press report of the IIT Roorkee work below and was not traced to a survey.

- **The oldest Modi document is dated 1389**, at the Bhārat Itihās Sanshodhak Mandal in Pune.
- **Modi entered Unicode in June 2014** (U+11600–U+1165F).
- **Readers are few and are being trained in small numbers** — "over 400 students" by 2025 on one account. ⚠️ Same caution.

## The machine layer arrived in 2025

**MoScNet**, a vision-language model for transliterating Modi into Devanagari, with **MoDeTrans**, a dataset of **2,043 scanned Modi manuscript images with expert-verified Devanagari transliterations across the seventeenth to nineteenth centuries** (Kausadikar, Kale, Susladkar and Mittal, IIT Roorkee; arXiv 2503.13060). The paper reports a distilled student model outperforming its teacher with **163× fewer parameters**; ⚠️ no character error rate was given in the abstract read, and the arXiv version read is marked as under submission. A press account says dataset and model are **open-sourced on Hugging Face**. ⚠️ Not verified on the repository itself.

## Why this matters to the project

**This is the Modi entry in the same table as kuzushiji and siyakat** — see [[Kuzushiji OCR - the NDL and CODH stack]] and [[MOC - Digitisation and text recognition]]. **The pattern holds across three traditions: the administrative cursive of an early-modern state becomes machine-readable roughly two generations after the state ends**, and the corpus that trains the machine is two thousand images, not two million.

**For the census the script is upstream of everything.** No Maratha fiscal or village record can be read at scale until this stack matures, and the Peshwa's archive is the largest single body of pre-colonial Indian administrative paper — [[Maharashtra State Archives - the Peshwa Daftar]].

## Links

- [[MOC - South Asian archives]]
- [[Maharashtra State Archives - the Peshwa Daftar]]
- [[MOC - Digitisation and text recognition]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
- [[Open-source HTR stack - eScriptorium Kraken Loghi]]

## Source

South Asian archives survey, 12 September 2026. Kausadikar, Kale, Susladkar and Mittal, "Historic Scripts to Modern Vision: A Novel Dataset and A VLM Framework for Transliteration of Modi Script to Devanagari", arXiv:2503.13060 (abstract); *Organiser* report of 19 July 2025; Wikipedia, "Modi script". Read through summaries; the paper itself not read in full.
