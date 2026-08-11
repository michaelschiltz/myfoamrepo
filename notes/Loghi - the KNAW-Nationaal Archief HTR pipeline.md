---
title: Loghi - the KNAW-Nationaal Archief HTR pipeline
type: reference
tags: [tooling, htr, ocr]
project: infrastructure
source-session: eic-voc-archives
created: 2026-08-11
status: seed
---

# Loghi — the KNAW / Nationaal Archief HTR pipeline

The engine that transcribed five million VOC pages. Not a competitor to Transkribus in the consumer sense: it is a **modular Linux/Docker pipeline built by an archive for its own mass-digitisation programme**, then released under MIT. That origin explains both its strengths and everything awkward about it.

## Identity

- Repository: <https://github.com/knaw-huc/loghi>, a fork of `rvankoert/loghi` (copyright 2022, Rutger van Koert). **MIT licence** — verified against the repository's `LICENSE`.
- Built at the **KNAW Humanities Cluster** Digital Infrastructure department with the **Nationaal Archief**; the author list spans both.
- Citation: van Koert, Klut, Koornstra, Maas and Peters, "Loghi: An End-to-End Framework for Making Historical Documents Machine-Readable," in *Document Analysis and Recognition — ICDAR 2024 Workshops*, ed. Mouchère and Zhu (Cham: Springer Nature Switzerland, 2024), 73–88. DOI `10.1007/978-3-031-70645-5_6`. Verified against the repository's `CITATION.cff`.

## The three components

**Laypa** — layout analysis and segmentation. ResNet backbone with a feature pyramid network, built on detectron2; pixel-wise classification of regions and, critically, **baselines**. Output converts to PageXML.

**Loghi Tooling** — the unglamorous middle. Cuts images into line images, merges transcriptions back into the PageXML, recalculates reading order. This is the part that determines whether output is usable downstream, and the part nobody markets.

**Loghi HTR** — the recogniser. Line image to text. Handles machine-printed as well as handwritten material, which matters for mixed early modern corpora where print and hand sit in the same volume.

The pipeline is deliberately modular: alternative tools can be substituted at most stages. **Everything ends in PageXML**, which is the open interchange format the rest of the ecosystem reads.

## Reported accuracy

The project's own abstract claims **CER below 3 per cent on handwritten seventeenth-century Dutch** — the States General resolutions, handwritten and printed, seventeenth and eighteenth century.

Treat this as a manufacturer's figure. It is self-reported, on the material the models were trained for, and it is a *corpus-average* CER. Nothing about a 3 per cent average tells you the error rate on the numerals in a ledger column, and for financial series that is the only rate that matters. ⚠️ No published CER for the GLOBALISE OBP output specifically — establish it before any counting claim rests on the transcriptions.

## Practical constraints, stated bluntly

- **Linux only.** Windows via WSL is possible and not recommended. **Mac is not supported**, and the FAQ is explicit that Apple Silicon acceleration is unavailable — emulation only. If the working machine is an M-series Mac this is a Linux box or a server, not a laptop install.
- **NVIDIA GPU with nvidia-docker** for anything resembling throughput. CPU inference works and is described by the developers themselves as very slow; there are `float32-` model variants specifically for CPU.
- Deployment is `docker pull loghi/docker.laypa`, `.htr`, `.loghi-tooling`, then editing paths in `scripts/inference-pipeline.sh`. Straightforward for anyone comfortable at a shell; a genuine barrier for anyone who is not.
- Pretrained Laypa and Loghi-HTR models are distributed via **SURFdrive**, not the repository. The generic HTR model is described by its own authors as working "ok on 17th and 18th century handwritten Dutch" and as a starting point for fine-tuning, not a finished tool.

## The feature that matters most here

`generate-synthetic-images.sh` — **synthetic ground truth generation**. Ground truth production is the dominant cost of any open-stack HTR project and the reason [[Open-source HTR stack - eScriptorium Kraken Loghi]] concludes that the cold start favours a managed platform. Synthetic line images attack exactly that cost.

This is the single reason Loghi is worth evaluating for material it was never trained on. Whether it survives contact with English secretary hand or eighteenth-century ledger hands is an empirical question nobody has answered here. ⚠️ Untested — and the answer sets the price of the EIC option in [[GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC]].

## Where it sits against the alternatives

| | Loghi | Transkribus | Kraken / eScriptorium |
|---|---|---|---|
| Licence | MIT, models yours | Platform-locked | Open |
| Interface | Shell scripts, Docker; Gradio demo and a web service exist | Browser | Browser over engine |
| Infrastructure | Linux + NVIDIA GPU | None | Server or Docker |
| Base models | Strong on Dutch archival hands, weak elsewhere | Super Models, broad | Depends |
| Synthetic ground truth | Built in | No | No |
| Output | PageXML | PageXML export | PageXML / ALTO |

The honest reading: **Loghi is the best available tool for early modern Dutch archival hands and an unknown quantity for everything else.** It does not displace the assessment in [[Open-source HTR stack - eScriptorium Kraken Loghi]] — start managed, keep ground truth portable — except on Dutch material, where the pretrained models and the finished corpus mean the work is already done. See [[VOC digital corpus - what is online and on what terms]].

## Boundary

This note is infrastructure. The *claim* that Loghi's existence restructures the comparative evidence base is an argument and lives in [[GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC]], with concept tags. Do not let the two layers merge — `tags.md` is explicit that tooling tags stay out of the concept graph.

## Links

- [[MOC - Digitisation and text recognition]]
- [[Open-source HTR stack - eScriptorium Kraken Loghi]]
- [[Transkribus - managed HTR platform]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
- [[VOC digital corpus - what is online and on what terms]]
- [[GLOBALISE removes the HTR question for the VOC and leaves it standing for the EIC]]

## Source

EIC/VOC archive-availability session, 11 August 2026. `knaw-huc/loghi` README, `LICENSE` and `CITATION.cff` read directly from the repository; ICDAR 2024 abstract as reproduced in the citation file.
