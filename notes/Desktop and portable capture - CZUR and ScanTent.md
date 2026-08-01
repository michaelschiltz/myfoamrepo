---
title: Desktop and portable capture - CZUR and ScanTent
type: reference
tags: [tooling, scanning-hardware]
project: infrastructure
source-session: digitisation-tooling
created: 2026-08-01
status: seed
---

# Desktop and portable capture — CZUR and ScanTent

The tier a working historian actually buys. Two devices, two different jobs: CZUR for material you can bring to your desk, ScanTent for material you cannot remove from a reading room.

## CZUR ET25 Pro

Overhead desktop scanner, A3 capture area.

- **25 MP** sensor, 5,824 × 4,368 px, **~330 dpi native** across the full A3 area. Output selectable 75–600 dpi (interpolated above native).
- **~1.5 seconds per two-page spread.**
- **Laser-assisted curve flattening** — projected laser lines measure the 3D curvature of the open page, and the software reprojects to a flat plane. This is the feature that distinguishes CZUR from a camera on a copy stand, and it works well.
- Auto page-turn detection for continuous scanning.
- Handles loose sheets, bound books, spiral notebooks, periodicals.
- Export to searchable PDF, Word, TIFF, Excel; bundled OCR claims 180+ languages.
- Windows/macOS/Linux, USB, HDMI out.

**Price for the ET25 Pro not reliably established across regions; the entry-level Aura Pro is around USD 269. ⚠️ Verify current Japanese pricing.**

**Do not use the bundled OCR for research material.** It is generic commercial OCR and will not touch *kuzushiji*. Use CZUR purely as a capture device and send images to [[Kuzushiji OCR - the NDL and CODH stack]] or [[Transkribus - managed HTR platform]]. Configure it to export **images, not searchable PDF** — the PDF path bakes in an OCR layer you do not want and complicates handing images to a real HTR pipeline.

**Two limits worth naming plainly.** Native resolution is fixed by the capture area, not by the size of what you put under it: 5,824 px across A3 is ~350 ppi, and a smaller page gains nothing because there is no optical zoom. That sits below the ~400 ppi floor a preservation specification asks for, though it is ample for reading and for HTR input. And the curve flattening is *reconstruction*: pixels are moved by an algorithm. Excellent for legibility, inadmissible as evidence about the physical object. See [[Preservation-grade overhead scanners - Zeutschel and i2S]].

## Transkribus ScanTent + DocScan

Sold by READ-COOP alongside [[Transkribus - managed HTR platform]].

**ScanTent** — a lightweight foldable fabric tent that sets up in seconds. Phone mounts at the apex; the document sits at the base. The fabric **diffuses ambient light** and built-in LEDs give consistent illumination. It solves the two problems that ruin reading-room phone photography: uneven light and unstable camera position.

**DocScan** — companion app, Android and iOS, free. **Detects page turns and fires automatically**, so you handle the document with both hands and never touch the phone.

Together: **a 300-page book in roughly 12–15 minutes.** Adopted at the Bibliothèque nationale de France. Price not published.

## Why the portable tier deserves more attention than it gets

For archive fieldwork the binding constraints are not resolution — they are **permission, time, and hands**.

- Most Japanese archives permit self-photography under conditions but do not permit you to bring equipment resembling a scanner. **A fabric tent and a phone read as photography, not scanning.** This is a real distinction in practice, not a technicality.
- Reading-room access is often limited to a few hours. 300 pages in 15 minutes changes what a single visit can accomplish, and turns a return trip into a non-event.
- No power, no laptop, no cables, no setup negotiation.
- **No cloud step.** Images stay on the device, which matters where permission conditions restrict reproduction and transmission.

**Ask the holding institution before assuming any of this is allowed.** Rules vary institution to institution and change; flash is almost universally prohibited, self-photography frequently requires an application, and some collections forbid it outright. The ScanTent's built-in LED is continuous rather than flash, but a curator who has not seen one before may not immediately read it that way — worth explaining in advance rather than at the desk.

## Recommendation

**Both, and neither is expensive.** CZUR at the desk for material you can borrow or own; ScanTent-and-phone in the archive for everything else. Combined cost is a rounding error against the tiers in [[Robotic V-cradle book scanners - Treventus and Qidenus]], and for a single-researcher project this pairing removes capture from the critical path entirely — which is the point, because capture was never the bottleneck.

## Links

- [[MOC - Digitisation and text recognition]]
- [[Kuzushiji OCR - the NDL and CODH stack]]
- [[Preservation-grade overhead scanners - Zeutschel and i2S]]
