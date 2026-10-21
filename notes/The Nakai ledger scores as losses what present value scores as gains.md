---
title: The Nakai ledger scores as losses what present value scores as gains
type: permanent
tags: [ensemble-average, expected-utility, time-average, risk-sharing]
project: HistorEE
source-session: tanomoshi-ko-coding
database: [loss_mitigation_forms]
created: 2026-08-08
status: seed
---

# The Nakai ledger scores as losses what present value scores as gains

The 中井家 kept a 「頼母子出入差引名寄帳」 covering forty-six *tanomoshi-kō* from Bunsei 3 (1820) to Meiji 15 (1882), entering each round's 掛金 and 落札金 as they fell due and recording in a 損金付込口 which associations the house reckoned a loss. Katō recomputed those results by present value and compared them with the house's own. **Four of the five he can check score positive by present value and appear in the house's books as losses.** Only 鎌掛専明寺澗栄講 agrees.

**CORRECTED 2026-10-21, against the page images (Katō 1998, 202, 210, 217, 220–221).** Three statements in the paragraph above are wrong or overstated, and together they shrink the anomaly. (i) The ledger was begun in 天保2 (1831), with earlier associations entered retrospectively. Its first part runs from the 文政3年 大宮頼母子講 to an association *begun* in 明治15; Katō counts it as 46 at 202 and numbers it 1–47 at 210, where the 47 plus the sixteen older associations recovered from the 損金付込口 make the 63 memberships he gives for 文化4 (1807) to 明治15 (1882). (ii) The five are not five he "can check". He discounts 25 associations at seven rates from 2 to 20 per cent; none is positive at every rate, and five are positive at some — 大聖寺頼母子, 西川応助頼母子, 水口松栄講, 鎌掛専明寺澗栄講 and 積金講 (217). Four of those five the house books as losses, and only 鎌掛専明寺澗栄講 agrees (220). The divergence is between a loss in the house's books and a gain at *some* discount rates, not against a clean positive. (iii) One of the four has an ordinary explanation, given by Katō himself: the 積金講's 600 *ryō* drawn in 嘉永1 (1848) left 380 *ryō* 3 *bu* over the contributions, which the house lent to 仙台佐兵衛 on an eight-year instalment schedule; the borrower's distress yielded only about 78 *ryō* of interest, some 2.6 per cent a year, and the association was booked a loss (220 n. 30). That is a default on an onward loan, entered against the *kō*. **The anomaly rests on three associations, not four.** (Katō dates the scheduled repayment 安政5年 (1856); 安政5 is 1858, and eight years from 嘉永1 is 1856, 安政3.)

Katō's own conclusion is the important one and it is a refusal rather than a claim: 評価にねじれがある以上、中井家のくだした評価とは単に現在価値法による収支計算をより甘くしたものであるとみることはできない。何か別の論理がベースにあったとおもわれる — the divergence is a twist, not a laxer version of the same calculation, and some other logic underlies it. He does not say what.

The mechanism is nevertheless traceable, and it is specific. The 「落札金預口」 records the calculation for winnings from Tenpō 14 onward — the 380 *ryō* lent to 仙台佐兵衛 on an eight-year 年賦 returned about 77 *ryō* 2 *bu* in interest, some 2.6 per cent annually, 2.5 per cent from years six to ten and nothing after. But 落札金とはことなり、掛金についてはまったく言及がない: **the house imputed no opportunity cost to its contributions at all.** Only deployed capital was priced. That asymmetry is where the divergence from present value comes from, and it is a bookkeeping fact rather than an inference.

**CORRECTED 2026-10-21.** The paragraph above conflates two things and overstates a third. The 2.5-per-cent schedule is not the 仙台佐兵衛 loan; it is the 落札金預口's standing rule, which credits winnings drawn in rounds 1–10 at 5 per cent, rounds 11–20 at 2.5 per cent and later rounds at nothing (年五朱之定 / 年弐朱半之定 / 無利息, 220), and Katō's 表7-9 shows the rate revised repeatedly between 天保14 and 明治10 (221). The 仙台佐兵衛 loan is the 積金講 case of the correction above. And the asymmetry is Katō's observation but not his reading of it. 掛金についてはまったく言及がない is followed at once by 全体的な利子率の低さは、掛金の機会費用の計算をはぶいたこと埋めあわせるための工夫かもしれない, and his n. 32 draws the inference that a rate on winnings set low to allow for the contributions' opportunity cost would be 中井家なりに時間価値を考慮していた証左 (221). **On Katō's own alternative the house did price time, implicitly, through the schedule on winnings.** "Imputed no opportunity cost at all" is a fact about what the ledger states, not about what the house reckoned, and the divergence from present value is not shown to come from it. The note's narrow claim below survives; its account of the mechanism does not.

What this establishes is narrow and worth stating narrowly. A merchant house kept a systematic, documented reckoning of its position in rotating associations, and that reckoning departs from expected-value maximisation in a traceable way. It does not establish what the house was maximising instead. Reading the asymmetry as a time-average criterion is a hypothesis to be tested against the ledger, not a result read off it — see [[Read the Nakai anomaly against the ie's horizon not the transaction's]] for the form that test would take, and [[Time-average optimization is a survivorship property not an intention]] for why the actors need not have held the criterion for it to operate.

The methodological dividend is separate and immediate. This house calculates constantly, ex ante and ex post, and the associations it calculates over still code `PR1=0` in `loss_mitigation_forms`, because none of the calculation prices a peril. Calculation and peril-pricing come apart inside a single archive, which is the strongest available defence of naming the characteristic for the peril rather than for the endpoint of the shift it measures. Compare [[Pricing is orthogonal to mitigation mechanism not a stage of it]].

## Links

- [[Read the Nakai anomaly against the ie's horizon not the transaction's]]
- [[Time-average optimization is a survivorship property not an intention]]
- [[Pricing is orthogonal to mitigation mechanism not a stage of it]]
- [[Economics had its ensemble moment in 1738 and psychologized it]]
- [[The ensemble average is the local descriptor of a barrier-shielded agent]]
- [[MOC - Risk-sharing vs risk-pricing]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

加藤慶一郎『近世後期における米穀・金融市場の展開』(1998), final chapters on the 中井家 ledger — read in full from the PDF, 2026-08-08. Quotations transcribed from an OCR layer and should be checked against the printed text before publication. The classic study of the house is 江頭恒治『近江商人中井家の研究』 [verify title, publisher and date]. *[Checked 2026-10-21 against the page images. The two Japanese quotations match the printed text (220, 221; Katō writes おもわれるである, sic). Egashira verified from Katō's own citation: 江頭恒治『近江商人中井家の研究』(雄山閣, 1965; repr. 1992) (199 n. 2). Katō used only documents of the 滋賀大学経済学部附属史料館 (201 n. 8): [[Shiga University - the Omi merchant archives]]. Page numbers are printed; the PDF offset is −9 to −10 in this chapter, not the −8 of ch. 5. 田中 2011, n. 87 cites the chapter as ch. 4 (99–125) of 加藤『近世後期経済発展の構造〔米穀・金融市場の展開〕』(清文堂出版, 2001), the thesis in book form ⚠️ one witness, not confirmed; if it exists, cite it and re-page.]*
