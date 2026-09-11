---
title: FranceArchives and the French access layers
type: reference
tags: [archives]
project: infrastructure
source-session: french-archives-survey
created: 2026-09-11
status: seed
---

# FranceArchives and the French access layers

<https://francearchives.gouv.fr/>

**France's problem is neither Spain's nor Italy's. It is scale.** Custody is orderly and the classification is uniform — every *archives départementales* in the country uses the same lettered series — but the material is distributed across a hundred departmental services, each with its own portal, its own software and its own digitisation programme, plus the national archives, the overseas archives, the diplomatic archives, the defence archives and the business archives.

**The uniform classification is the thing to exploit.** Because every department uses the same frame, a series letter is a research instrument in its own right: *série B* is the ancien-régime jurisdictions everywhere, *série J* is private archives everywhere, *série E* holds the notaries. **A question can be asked of the whole country at once by asking it of a series**, which is not possible in Spain or Italy. See [[The archives departementales system]] and [[The amirautes - a series across the coastal departments]], which is that move performed.

## The layers

| Layer | Where |
|---|---|
| National aggregation of finding aids | FranceArchives, <https://francearchives.gouv.fr/> — it also publishes its inventory data as open datasets on `data.gouv.fr` |
| National archives, own catalogue | the *Salle des inventaires virtuelle*, see [[Archives nationales - Paris and Pierrefitte]] |
| Departmental portals, ~100 of them | see [[The archives departementales system]] |
| Digitised books, manuscripts and press | [[Gallica and RetroNews - the French full-text layer]] |

## The practical obstacle, and it is real

⚠️ **The French portals are heavily JavaScript-driven and several are behind anti-bot protection.** FranceArchives requires JS to render a description; the Haute-Garonne catalogue refused automated access outright during this survey. The consequence is concrete: **French finding aids are substantially harder to work remotely than Dutch or Italian ones**, not because the data is closed — FranceArchives publishes open datasets — but because the interfaces are built for humans with browsers.

That is worth recording as an access condition in its own right. A register column that assumes a catalogue can be queried programmatically will be wrong for France.

## Links

- [[MOC - French archives]]
- [[Archives nationales - Paris and Pierrefitte]]
- [[The archives departementales system]]
- [[Gallica and RetroNews - the French full-text layer]]
- [[Dutch archives online - the access layers]]

## Source

French archives survey, 11 September 2026. FranceArchives portal and its open-data publications on `data.gouv.fr` and `data.culture.gouv.fr`.
