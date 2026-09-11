---
title: CODH datasets - the open machine-learning layer
type: reference
tags: [archives]
project: infrastructure
source-session: japanese-archives-survey
created: 2026-09-11
status: seed
---

# CODH datasets — the open machine-learning layer

ROIS-DS Center for Open Data in the Humanities, <https://codh.rois.ac.jp/>. The tooling side is at [[Kuzushiji OCR - the NDL and CODH stack]]; this note is about the **data**.

- **日本古典籍データセット**: **3,126 works, 609,631 images** (January 2019), mostly from the NIJL, with metadata, some transcriptions and some named-entity tags. **CC BY-SA 4.0.**
- Derived and related: the *kuzushiji* character dataset, **KMNIST**, *Edo Map*, the collected *bukan* (samurai registers).

## The honest assessment

**Marginal for the census and important for its tools.** These are training and benchmarking sets built from **books**, which is why *kuzushiji* recognition is better on books than on *komonjo* — see [[Books are imaged and documents are not - the Japanese digital split]]. **If the project ever retrains NDL古典籍OCR-Lite on account books, CODH's datasets are the base and the project's own ledger images are the missing half.** The share-alike licence binds anything released from a model fine-tuned on them. ⚠️ Whether share-alike reaches model weights is a legal question not taken here.

## Links

- [[MOC - Japanese archives]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
- [[NIJL Kokusho Database - the classical books union layer]]

## Source

Japanese archives survey, 11 September 2026. CODH, 日本古典籍データセット page. Read through a summary.
