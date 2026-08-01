---
title: Robotic V-cradle book scanners - Treventus and Qidenus
type: reference
tags: [tooling, scanning-hardware]
project: infrastructure
source-session: digitisation-tooling
created: 2026-08-01
status: seed
---

# Robotic V-cradle book scanners — Treventus and Qidenus

The top of the market: machines that turn the pages themselves. Both are Austrian, both use a V-shaped cradle, and both quote up to 2,500 pages/hour.

## Treventus ScanRobot 2.0 MDS

Treventus Mechatronics GmbH, Vienna. The distinctive engineering is a **transparent V-prism that is lowered into the open book**: the prism flattens both pages against its two faces while air suction lifts and turns the leaf. Capture is through the prism, so the page is imaged flat without a glass platen pressing down on it.

- **Automatic page turning**, up to **2,500 pages/hour**.
- **Opening angle adjustable 60°–100°** — advertised as the smallest opening angle of any automatic book scanner, which is the substantive preservation claim: tight-bound volumes are not forced open past their hinge.
- Optical **300 dpi** standard, **400 dpi optional**. 36-bit colour depth.
- Output: JPEG, JPEG 2000, TIFF, TIFF G4, PNG, GIF, BMP, PDF with OCR layer, XML, DjVu.

**Price: reported ~USD 30,000 base, USD 45,000–50,000 fully configured. ⚠️ Unverified — this figure comes from a low-quality aggregator page, not from Treventus. Treventus does not publish prices. Treat as an order-of-magnitude indication only and request a quotation for anything real.**

## Qidenus

Qidenus Technologies, Vienna. Also V-shape, distributed by Crowley (US) and Iguana. Two relevant tiers:

- **Robotic** — fully automatic page turning, up to 2,500 pages/hour, A3+/A2.
- **Mastered** — semi-automatic; operator turns pages, machine does the rest. Up to **1,500 pages/hour**, available A3+ through A1, **up to 1,000 ppi**.

The Mastered tier is the more interesting product. It concedes the page-turning automation — the fragile, failure-prone part — and keeps most of the throughput. **1,500 pp/h with a human handling the paper is a better proposition for heterogeneous archival material than 2,500 pp/h with a suction arm**, and the resolution ceiling is far higher than the ScanRobot's.

Prices not published.

## Why this tier is almost certainly wrong for this project

**Automatic page turning requires paper that tolerates being handled by a machine.** Suction-driven leaf-turning assumes single-leaf pages of consistent weight and surface. Early modern Japanese material fails this on nearly every count:

- ***Fukurotoji* 袋綴じ (pouch binding)** — the folded double leaf is the standard early-modern format. Suction on a folded leaf risks separating or tearing at the fold, and the machine has no way to know it has grabbed two surfaces.
- **Washi** varies enormously in weight and surface within a single volume.
- ***Kansubon*** scrolls and folded *orihon* formats are simply outside the machine's premise.
- Repairs, inserts, tipped-in slips and irregular sizes — routine in domain administrative records — all defeat the automation.

Add the institutional constraint: **you will not be permitted to bring a robot into a Japanese archive, and archives will not put uncatalogued or fragile holdings into one.** These machines live in digitisation units and process the institution's own material on the institution's own schedule.

Add the economics: at 2,500 pp/h, a €40,000 machine pays back only against a queue that never empties. A book project does not generate that queue.

**Conclusion: this tier is relevant to you as something to know about and possibly to advocate for at the institutional level — Hokkaido University Library, or a funded digitisation programme — not as a purchase.** If a Japanese archive holding material you need is considering digitisation, knowing the difference between the Robotic and Mastered tiers is worth having. If you are buying for yourself, see [[Desktop and portable capture - CZUR and ScanTent]].

## Unresearched

**Japanese distribution and service.** Decisive for any institutional recommendation and entirely unknown to me. A Viennese robot with no service engineer reachable from Sapporo is a capital write-off waiting to happen — and the page-turning mechanism is the part that breaks.

## Links

- [[MOC - Digitisation and text recognition]]
- [[Preservation-grade overhead scanners - Zeutschel and i2S]]
- [[Desktop and portable capture - CZUR and ScanTent]]
