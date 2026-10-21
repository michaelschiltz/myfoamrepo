---
title: Japan Search - the national metadata aggregator
type: reference
tags: [archives]
project: infrastructure
source-session: japanese-archives-survey
created: 2026-09-11
status: seed
---

# Japan Search — the national metadata aggregator

ジャパンサーチ, <https://jpsearch.go.jp/>. Operated by the National Diet Library under the Cabinet Office's digital-archive promotion framework.

**32,817,120 metadata records from 320 databases and 208 organisations.** By category, among others: books and publications 15.5 million; natural history and science 6.9 million; humanities 5.9 million; **official documents 4.6 million**; cultural heritage 1.7 million; regional resources 1.6 million.

## What it is and is not

**Layer 1, national, with links to layer 2.** It aggregates metadata and points to content held by member institutions; it holds no images of its own. **Japan's Archives Portal Europe** — and like it, a tool for discovering that a thing exists and who holds it, never a corpus.

**Two cautions.**

- **Coverage is by database, not by holder.** An institution appears if one of its databases is connected. The private house archives, most municipal holdings and most village documents are not there. **A null in Japan Search is a fact about which databases are connected.**
- **"Official documents" means the modern state's records**, not early-modern village or merchant papers. ⚠️ Category composition not inspected.

**Its web API was not probed**: the endpoint is disallowed to automated fetching from this session. A term count for 頼母子 or 無尽 across the aggregator is a cheap desk test and should be run by hand. *[Run 2026-10-21, through the public search API called from the site's own origin in MS's Chrome (`/api/item/search/jps-cross`, with the `f-db=` filter per database because deep paging stops at 2,000 records).]*

## The 頼母子 count, 2026-10-21

| Term     | Records | Note                                                                                  |
|----------|--------:|---------------------------------------------------------------------------------------|
| 頼母子   |   2,839 | 2,816 unique harvested across 52 databases; 1,195 carry the term in the title         |
| 頼母子講 |   1,475 |                                                                                       |
| 無尽     |   8,859 | swollen by 無尽蔵, 無尽灯 and the like; not usable as a count                         |
| 無尽講   |     271 |                                                                                       |
| 憑支     |       4 | all OCR noise in 1950s accounting books; the 1275 attestation does not surface        |

**Where 頼母子 sits.** NIJL's archival descriptions 782, NDL Digital 491, Fukui 393, the Tōkai national universities' archive (Nagoya University and Ōgaki) 275, the Tokyo Metropolitan Archives' subject index 177, Rekihaku 124, Kyushu University 73, Kobe University's newspaper-clippings archive 56, Nagoya City Museum 55, the National Archives 38. Access: 644 records with content online, 385 restricted, 1,047 with none.

**None of the census's own sources surfaces.** No 長興寺, 大黒屋, 御手洗, 誉田, 宝光院 or 持寄融通社. **The null is the one this note predicted**: Toyonaka, Kure, Osaka Metropolitan University and the Yamagata holdings are not connected.

**What it does surface is rulebooks.** 64 records have 頼母子 and a rulebook term (仕法, 定, 議定, 規則, 約定, 趣法) in the title, **26 of them imaged online**: a run of Edo 仕法帳 at the Edo-Tokyo Museum (1827–1842, and a Meiji 共救社 申合規則), Sagamihara City Museum (a 頼母子講仕法 convened because the lord's finances were straitened, and a 積金定法帳), and in the Tōkai archive a 仕法帳 spanning 24 villages of six Owari districts (Ōgaki) and a 1859 御奉加 頼母子惣益講仕法帳 (Nagoya University). Rekihaku holds a serial run of 頼母子定書 from 1820 to 1888 in one fonds, not imaged — [[Rekihaku - the National Museum of Japanese History and khirin]]. Many of the Tokyo Metropolitan Archives' hits are magistrates' 申渡書 on 仕法頼母子 and 取退無尽, regulation rather than rulebooks.

**Two primary bases the census has been citing second-hand are online.** The 1935 農林省 survey, 『農村金融資料 第1号 頼母子講ニ関スル調査』, is at NDL Digital with internet access (pid 1077357); the vault's magnitudes come from it through 並松 and 有本ほか. *[Read the same day; see HistorEE_codebooks logbook 5, 2026-10-21 (iv). It is a census of February 1934, published 1935, and its definition of the 講親 changes what the 66.3 per cent means: [[Relief ko for a named person is claimed to be unattested outside Japan]].]* And the 取退無尽禁令 is imaged at the National Archives (item 744923), with the 古事類苑's 法律部四十八 博弈 取退無盡・頼母子講 (pp. 68–74) at NIJL — the primary layer under `torinoke_mujin`.

## Links

- [[MOC - Japanese archives]]
- [[Books are imaged and documents are not - the Japanese digital split]]
- [[MOC - European archives and digital collections]]
- [[NIJL Kokusho Database - the classical books union layer]]

## Source

Japanese archives survey, 11 September 2026. Japan Search "about" and statistics pages. Read through summaries. Counts and record lists of 21 October 2026 from the search API; titles, databases and access flags only, no record opened.
