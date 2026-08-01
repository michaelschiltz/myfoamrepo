---
title: Preservation-grade overhead scanners - Zeutschel and i2S
type: reference
tags: [tooling, scanning-hardware]
project: infrastructure
source-session: digitisation-tooling
created: 2026-08-01
status: seed
---

# Preservation-grade overhead scanners — Zeutschel and i2S

The tier where **image quality rather than throughput is the product**. Operator turns the pages; the machine's job is colour-accurate, geometrically correct, standards-conformant capture. This is what an institution buys when the digital surrogate is meant to substitute for the original.

## Zeutschel

Tübingen. The reference brand where material is rare, fragile, or irreplaceable — the name that appears in preservation specifications.

- **OS Q series** (A2) — current mainstream line; faster capture and new camera hardware over its predecessor.
- **OS HQ** (A1/A0) — Zeutschel's own **Gigapixel camera system**. Stated to **exceed FADGI 4-star, ISO 19264-1 and Metamorfoze** requirements. These are the three imaging standards that matter, and "exceeds" against all three is the strongest quality claim in this market.
- **OS 15000 / OS 16000** — earlier and adjacent models still widely deployed.

Reported characteristics: **true RGB capture, 96-bit internal processing, high-CRI LED illumination**. Motorised book cradles with controlled glass-plate pressure, and lighting engineered to keep UV and IR off the object.

## i2S

French. **CopiBook OS** (A2) is the workhorse — bound and loose material at production speeds, aimed at libraries, archives and service bureaux. i2S positions between Zeutschel's preservation emphasis and higher-volume production; also makes the larger-format **SupraScan** line.

Neither manufacturer publishes prices. Both sell through regional integrators (Crowley and ScannX in the US, Spigraph in Europe).

## What actually distinguishes this tier

Not resolution — a modern desktop scanner has adequate pixels. The differences are the ones that only show up when you try to *use* the image as evidence:

- **Colour fidelity under a known standard.** FADGI/ISO 19264-1/Metamorfoze conformance means the colour in the file is traceable to the object. This matters for ink and paper analysis, seals, and any argument that turns on the physical document rather than its text.
- **Illumination that does not damage.** High-CRI LED with UV and IR excluded, for material that will be imaged once and then not handled again.
- **Geometric accuracy.** No curvature interpolation, no algorithmic flattening. The desktop tier *guesses* the flat page from a curved one; this tier photographs it flat.
- **Controlled cradle pressure.** The binding is not forced.

**The distinction that matters for you: this tier does not reconstruct, it records.** Everything below it applies correction algorithms — curve flattening, contrast normalisation, background removal — that are irreversible and undocumented. For reading, that is fine and often better. For any claim about the artefact, an algorithmically flattened image is a processed derivative and should not be treated as evidence of the object's physical state.

## Relevance

**Institutional purchase, not personal.** The realistic contact point is that this is what a Japanese archive or university library already owns, and what a digitisation request will be fulfilled on. Knowing the standards vocabulary — FADGI 4-star, ISO 19264-1, Metamorfoze — is useful when specifying a commissioned scan: it lets you ask for a conformant archival master rather than accepting a service copy.

**Practical rule when commissioning: ask for the uncompressed TIFF archival master, not the delivery PDF.** The master is what survives; the PDF is a derivative someone chose the parameters for. If you are paying for a scan you should be receiving the master.

## Unverified

- Prices across all models. None published; quotation only.
- Whether the OS Q or OS HQ is the current flagship as of 2026, and Japanese distribution for both brands.

## Links

- [[MOC - Digitisation and text recognition]]
- [[Robotic V-cradle book scanners - Treventus and Qidenus]]
- [[Desktop and portable capture - CZUR and ScanTent]]
