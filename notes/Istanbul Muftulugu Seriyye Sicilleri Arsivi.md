---
title: Istanbul Muftulugu Seriyye Sicilleri Arsivi
type: reference
tags: [archives]
project: infrastructure
source-session: ottoman-archives-survey
created: 2026-09-11
status: seed
---

# İstanbul Müftülüğü Şer'iyye Sicilleri Arşivi

The court-register archive of the Mufti of Istanbul. **The registers of the capital's Islamic courts, about 9,870 volumes from 27 courts, early sixteenth century to 1924.** Founded in 1892 (1310) under Abdülhamid II to gather registers from court offices and stores; passed to the Müftülük when the *Meşihat* was abolished. **The capital's court record stayed with the religious administration when the Republic abolished the courts, while the provinces' went elsewhere** — see [[The Anatolian court registers - museum to National Library to State Archives]].

## The courts

| Court | Registers |
|---|---|
| Kısmet-i Askeriyye (military-class estates) | 2,138 |
| Galata | 1,040 |
| Üsküdar | 801 |
| Havâss-ı Refîa (Eyüp) | 629 |
| Bâb | 544 |
| İstanbul (the *kadılık* proper) | 334 |
| Balat | 154 |
| **Evkâf Muhasebeciliği** | **129** |

Işık 2015. The total is given as 9,872 by Işık, 9,883 in the *TDV İslâm Ansiklopedisi*, and "10,000 volumes from 26 courts" by Aydın and Tak; the Üsküdar count as 801 by Işık and 1,074 by Aydın and Tak. ⚠️ The discrepancy is probably one of counting convention and was not resolved. The oldest Istanbul register is Üsküdar's, from 919/1513–14.

## Why this is the census's archive, not the Ottoman Archive

**Almost every Ottoman row the census carries rests on literature that worked these registers.**

| Census row | Court and registers | Literature |
|---|---|---|
| `avariz_fund`, `avariz_vakfi` | **İstanbul Mahkemesi nrs 3, 10, 12, 18, 20, 22**, 1618–1697 | Kars 2021 |
| `avariz_fund`, `avariz_vakfi` | Evkâf Muhasebeciliği, 1491–1828 | Gürsoy 2019 |
| `cash_waqf` (parked) | Üsküdar, 81 accounts of 1784–86 | Kaya & Akkaya 2017 |
| `cash_waqf` (parked) | Balat, 1555–1838 | Gürsoy & Özdeğer 2022 |
| `cash_waqf` (parked) | Galata, *zimem* entries 1680–1690 | Yıldırım, Yeniyurt & Mete 2026 |
| candidate only | Davutpaşa, cash waqfs 1634–1911 and guild chests | Gürsoy 2017, 2018 |
| `waqf_khayri` | Evkaf Müfettişliği court, waqfs' loan contracts with *sarrafs* 1750–1840 | Pantık 2024 |

⚠️ The Galata and Üsküdar placements are inferred from the census's own descriptions — "Galata *zimem* entries", "Üsküdar accounts" — and not from those articles' apparatus.

**The first row is the important one.** Kars's six registers are a run of the İstanbul court from its register 3 (1027/1618) to its register 22 (1107–08/1695–97), and **at least four of the six are in the published İSAM edition** — see [[Istanbul Kadi Sicilleri - the published transliterations]]. The census's Istanbul *avarız* evidence may therefore sit on registers a publication project chose.

## The vakfiye catalogue — a denominator the census has not used

İSAM's ***İstanbul Şer'iyye Sicilleri Vakfiyeler Kataloğu*** (2015) describes **9,867 endowment deeds registered in the 27 courts, of which 3,950 are cash waqfs** and 5,917 endow real property. Each entry gives court, register, date, founder, property and conditions.

**That is a catalogued population, at item level, of the instrument `cash_waqf` is parked on.** Deniz 2026's 97 deeds and Çizakça's 761 Bursa waqfs are samples; this is the frame they were drawn from, for one city. It does not change the parking — the parking is a boundary decision about purpose, and the catalogue records purpose — but **it makes the purpose question countable for Istanbul**, which it was not before. ⚠️ The catalogue's date range is given as 709–1342 AH, and the early bound must reflect older deeds copied into later registers; not checked.

## Access, layer and script

- **Originals at the Müftülük; researchers work from İSAM's digital copies.** See [[ISAM Library Archive - the court register image collection]]. ⚠️ Direct access to the originals was not established.
- **Layer 2 for all registers, at İSAM; layer 3 for the edited selection.**
- **Language and script:** Arabic predominates in fifteenth- and sixteenth-century registers, Ottoman Turkish thereafter; *ta'lik*, *rik'a* and *dīwānī* hands. **Accounting entries within the registers — the waqf *muhasebe* — are in siyakat.** A register that is transliterated may still not be *read*: a transliteration of a siyakat account is a specialist's product.

## A citation fixed in passing

The census cites "Kars 2020" and its `avariz_vakfi` type row flags that the article's own running head says 2021. **The journal's DergiPark record gives Rümeysa Kars, *Tarih Araştırmaları Dergisi* 40/69 (2021), 160–187.** ⚠️ Read at one remove; not applied to the census, which is the maintainer's to change.

## Links

- [[MOC - Ottoman archives]]
- [[ISAM Library Archive - the court register image collection]]
- [[Istanbul Kadi Sicilleri - the published transliterations]]
- [[Kadijski spisi - the kadi documents at Dubrovnik]]
- [[Orta sandigi records - the guild and Janissary chests]]

## Source

Ottoman archives survey, 11 September 2026. A. Işık, "İstanbul Müftülüğü Şer'iyye Sicilleri Arşivi" (2015, isamveri.org); "Şer'iyye Sicilleri", *TDV İslâm Ansiklopedisi*; B. Aydın and E. Tak, "İstanbul Kadı Sicilleri", *Büyük İstanbul Tarihi* (istanbultarihi.ist); B. Aydın et al., *İstanbul Şer'iyye Sicilleri Vakfiyeler Kataloğu* (TDV/İSAM, 2015), introduction; the census's own `key_source` fields for every placement in the second table; Pantık 2024 read in full text for its apparatus. All but the last read through summaries.
