---
title: Zeutschel book-scanning range - the cradle decides not the camera
type: reference
tags: [tooling, scanning-hardware]
project: infrastructure
source-session: zeutschel-product-range
created: 2026-10-08
status: seed
---

# Zeutschel book-scanning range — the cradle decides not the camera

**Zeutschel's 2026 catalogue lists 54 products; about twenty bear on bound volumes, and they sort into three lines — preservation (OS Q, OS HQ, ScanStudio), production (OS C, OS 15000, OS A) and self-service (zeta, chrome). For this project the camera is the less important variable: what decides whether a volume can be captured as an archival master is the cradle — opening angle, glass contact, pressure control — and whether the line's book-fold handling depends on Perfect Book correction.**

Complements [[Preservation-grade overhead scanners - Zeutschel and i2S]], which sets out the standards vocabulary (FADGI, ISO 19264-1, Metamorfoze) and the record-versus-reconstruct distinction. This note is the model-level register, plus three items that note left open: the current line-up, the Japanese distributor, and the downstream workflow.

## Preservation line

Line-scan RGB cameras (no Bayer interpolation), CRI > 97 LED illumination, 96-bit internal processing. These are the models with the full three-standard compliance claim.

- **OS Q2** — A2+ (635 × 460 mm); up to 600 ppi; 3-channel CMOS RGB line sensor. Claims **ISO 19264-1 Level A, Metamorfoze Full, FADGI 4 Star**. Advanced Plus cradle, 150 mm under glass. ~3 s @ 400 ppi, ~5 s @ 600 ppi (A2).
- **OS Q1** — A1 (zoom A1–A2); up to 600 ppi, MeanMTF10 9 lp/mm at 600 ppi (12 lp/mm zoomed in). A1 at 3.5 s / 200 ppi, 5.9 s / 400 ppi, 7.6 s / 600 ppi. Takes OT 180 H 35 XL700 (350 mm book thickness) or OT 180 H 50 XL (500 mm). ⚠️ The product page as read did not list the three standards; assume conformance only on Zeutschel's written confirmation.
- **OS Q0** — A0+ member of the same series. Not read in detail.
- **OS HQ** — A0+/A1+; **gigapixel** 3-channel CMOS line sensor with optical zoom and mechanical shutter; up to 1000 ppi, MeanMTF10 10 lp/mm at 600 ppi (14 lp/mm zoomed in). Claims ISO 19264-1 Level A, Metamorfoze Full, FADGI 4 Star, and "exceeds" them. 7 s @ 300 ppi, 10 s @ 600 ppi. Accepts the whole cradle range, OT 180 H A0 to Vacuum Table A1.
- **ScanStudio A2** (also A1, A0) — studio camera on a copy stand: medium-format digital backs, interchangeable lenses, up to 150 MP, 16-bit. Claims ISO 19264 > A, FADGI > 4 Star, Metamorfoze Full. Advanced Plus cradle (A2+, 15 cm under glass, automatic, pressure-controlled). 3.4–6 s cycle. Book-curve correction optional.

## Production line

Area or line cameras at lower colour depth (42-bit internal, 24-bit out), standards claimed at a lower level or not at all. Built for throughput on robust material.

- **OS C** (C1 at A1+, C2 at A2+) — up to 600 ppi; **ISO 19264-1 Level B up to 300 dpi / Metamorfoze Light** only (C2 Comfort, Advanced, Advanced Plus). Cradles range from a manual holder (Comfort) to a motorised glass plate with opening angle adjustable up to 90° (Advanced Plus). 3.8 s @ 400 ppi (C2). Output TIFF uncompressed, TIFF G4, JPEG, JP2, multipage TIFF/PDF.
- **OS 15000 Advanced Plus / Comfort** — 460 × 360 mm; 300 dpi, 600 dpi at extra cost; motorised cradle with self-opening glass plate. No standards claim on the page. Still in the current catalogue.
- **OS A1 / OS A2** — modular camera-on-arm system using off-the-shelf bodies, from 24 MP (Canon EOS R10) to 100 MP (Fujifilm GFX100S); A2+; Basic (no cradle) or Advanced (with cradle). Automatic recalibration in OmniScan 12 corrects distortion and chromatic aberration in software — i.e. the geometry is computed, not optical.
- **OS A W "The Wall"** — the OS A calibration carried onto a studio easel for paintings, maps, posters; 4- and 16-shot pixel-shift, stitched tiles. Claims ISO 19264-1, FADGI, Metamorfoze. Not a book device; relevant only for oversize sheets such as maps and broadsheets.

## Self-service line

What a researcher meets in a library's open-access area. Touchscreen PC, output to USB, e-mail, cloud.

- **zeta / zeta Comfort** — 480 × 360 mm (A3+); 300 dpi, 600 dpi optional. Comfort adds a book cradle (100 mm) and a 140°–90° bookholder kit. TIFF, PDF, JPEG, PNG.
- **chrome** — 638 × 445 mm (> A2); 300–600 ppi; 42-bit internal; manual cradle, 100 mm; ~50 mm depth of focus. Runs zeta software with **"3D scan technology"** for book-curve correction. PDF/A, searchable PDF optional.

Every file from this line is a processed derivative by design: curvature correction is the selling point, and no raw master is offered to the user.

## Cradles and holders — the actual decision

| Item | Opening angle | Book thickness | Format | Notes |
|---|---|---|---|---|
| OT 180 H 35 XL700 | up to 115° | 350 mm | A1+ (1025 × 700 mm) | Motorised self-opening glass; constant pressure, infinitely variable, independent of book weight |
| OT 180 H 50 XL | — | 500 mm | — | Not read in detail |
| OT 180 H 90° | 90°, or open without glass | 240 mm | 1025 × 620 mm (special 1025 × 700) | Swing-back glass plate; for "fragile and valuable" originals |
| OT 180 H A0 | — | — | A0 | Not read in detail |
| Kit 90° | 90° | — | A1, A2 | For books that open only to 90° |
| Book holders | 90°–140° | — | A1, A2 | Usable on both sides |
| V-Kit | 180°–140°, four positions | — | A1, A2 | Both pages captured by one camera; **requires Perfect Book**; fits zeta Comfort, OS 15000 Advanced Plus, OS C2 Advanced / Advanced Plus only |

The consequence: the V-Kit, Zeutschel's gentlest single-camera option for half-opened books, is sold only for the self-service and production machines and depends on algorithmic flattening. **On the preservation line, a tight binding is handled by a 90° cradle or a holder, i.e. one page per capture with glass lifted or absent — slower, but recorded rather than reconstructed.**

Thread-bound *wahon* (*fukuro-toji* 袋綴じ) open flat and do not need any of this. The 90°–140° gear matters for Western-bound material: Meiji–Shōwa bank and company reports, bound ledgers, European printed volumes.

## Software

- **OmniScan 12** — capture, processing, indexing, output (TIFF, TIFF-LZW, JPEG, JPEG 2000, PNG, PDF, multipage). ICC colour management throughout. Technical, descriptive and structural metadata capture; ⚠️ the page names no metadata standard (METS/MODS, XMP). OCR and Perfect Book optional.
- **Perfect Book 3.0** (and 2.0) — book-fold distortion correction, fingerprint and Post-it removal, deskew, page-size adjustment. ⚠️ The page does not say whether the uncorrected capture is retained. Ask before any commissioned scan: the uncorrected TIFF is the master.
- **Kitodo.Production / Kitodo.Presentation** — Zeutschel is a development and support partner for this GPL, METS-based workflow suite (the German library standard). Add-ons: ZED Server, zedOCRCloud, ABBYY FineReader runtime. ⚠️ No IIIF mentioned on the page. This is the first concrete lead on the MOC's open question about the downstream pipeline.

## Japan

- **Distributor: Kurabo Industries Ltd (クラボウ), Tokyo** — listed on Zeutschel's partner page as partner for "Flatbed scanner / bookscanner". Contact via `kurabo.co.jp/el/world/en/`. ⚠️ Not confirmed from Kurabo's side; service-engineer coverage for Hokkaido unresearched.
- Korea: Sandol BMT, Seoul. China and Taiwan: direct Zeutschel sales contact only.
- Fujifilm Japan publicises the GFX100S as a camera option for OS A (fujifilm-x.com, ja-jp), which suggests at least OS A has a domestic marketing presence.

## Corrections to the sibling note

- [[Preservation-grade overhead scanners - Zeutschel and i2S]] gives the OS Q series as A2. It is three formats: **Q0 (A0+), Q1 (A1), Q2 (A2+)**.
- The same note names an **OS 16000**; it is not in the 2026 catalogue. The OS 15000 is.
- Its open question "whether OS Q or OS HQ is the current flagship" resolves as: both current, HQ is the top of the line (gigapixel camera, 1000 ppi, A0+).

## Unverified

- ⚠️ Prices: none published for any model.
- ⚠️ OS Q1 standards conformance (see above).
- ⚠️ Specifications were read through page summaries, not from Zeutschel datasheets. Request the PDF datasheet before relying on a figure in a specification or tender.

## Links

- [[MOC - Digitisation and text recognition]]
- [[Preservation-grade overhead scanners - Zeutschel and i2S]]
- [[Robotic V-cradle book scanners - Treventus and Qidenus]]
- [[Desktop and portable capture - CZUR and ScanTent]]

## Source

Products – Zeutschel GmbH, `www.zeutschel.de/en/products/`, read 2026-10-08. Product pages follow `www.zeutschel.de/en/produkte/<slug>/`; read: `os-q1-2`, `os-q2-2`, `os-hq-2`, `scanstudio-a1-2` (covers ScanStudio A2), `os-c-scanner`, `os-15000-advanced-plus-2`, `os-a-overhead-scanner`, `os-a-w-the-wall`, `zeta`, `chrome-2`, `ot-180-h-35-xl`, `ot-180-h-90-2`, `kit-90-2`, `book-holders`, `v-kit`, `perfect-book-3-0`, `omniscan-os12`, `kitodo-2`. Distributors from `www.zeutschel.de/en/partner/`.
