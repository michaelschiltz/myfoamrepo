---
title: Comanda capital was mixed with the agent's own unless the contract said otherwise
type: permanent
tags: [commenda, coding-ontology]
project: HistorEE
source-session: comanda-crown-of-aragon-2026-10-07
created: 2026-10-07
status: seed
---

# Comanda capital was mixed with the agent's own unless the contract said otherwise

*[RENAMED 2026-10-13, by MS's decision, from "Comanda capital was kept apart unless the contract said otherwise": cap. 215, not cap. 219, is the default (ruling 29).]* *[Corrected 2026-10-12, late: true only for a comanda carried alongside a company's common stock (cap. 219). Mixed with the agent's own money, the default is commingling with gain and loss divided per sou e per liura (cap. 215); `comanda CI5` is now `commingled`. See the last section. The title is now misleading; renaming waits on MS.]* The *Consolat de Mar* makes separate accounting the default for a comanda carried alongside other goods. A comanda taken *sparsa* by someone who also carries the goods of a company is accounted for separately, and is not mixed into the common stock unless the contract says so. Commingling without consent lets the investor claim the highest price obtained (cap. 219; [[The Consolat de Mar comanda chapters]]). Where the agent invests the comanda together with his own money, gain and loss are divided "per sou e per liura" (215).

The notarial acts show three ways of holding the capital, which Hancock takes from Madurell & García Sanz (I, 94–96):

- *a esparç*, managed apart from the traveller's own;
- *simil cum meis mercibus*, used with his goods as one fund;
- a community of all investments in shares.

See [[Hancock 2025 on trust in Barcelona and Mallorca contracts]], 17.

**For the census** *(superseded 2026-10-11; see below)*. `CI1` (capital structure: `common` | `several-accounts` | `none`) can take both of its first two values inside one form, by drafting variant. Under the ruling of 2026-10-07 a minority variant does not make a cell `P`: the cell takes the modal state, and the counts go in the note. That requires counts the held literature does not give, so the cell waits on Madurell & García Sanz 1973. The ruling also logged that the value set has no state for a single investor's capital in a single agent's hands. The *Consolat*'s default, separate accounting, is the case that question is about.

## Superseded 2026-10-11: the question moved to `CI5`

`CI1` was answering two questions: how the contributions of several parties are held within an arrangement, and whether the arrangement's capital is kept apart from the agent's own. The *Consolat*'s default answers the second. MS split the characteristic (`records/RULINGS-comanda-adjudications-2026-10-11.md` in HistorEE_codebooks, ruling 4): `CI1` keeps the first question, and **`CI5`, segregation from the holder's capital** (`segregated | commingled`), takes the second. `comanda CI5 = segregated`, low, on cap. 219; `comanda CI1 = .NR`, because single-investor comandas (`none`) and Hancock's community of investments in shares (`common`) are both attested and neither is counted. The gap logged on 2026-10-07 closes with the split: one investor's capital in one agent's hands is `CI1 = none`. Arm P's Genoese acts are the evidence that the two questions come apart: Scriba and Amalric commingle *per libram cum aliis*, Cassinese keeps capital *separatim*. `CI5` is not shielding; who could reach the segregated account remains `AP1`–`AP4`'s question.


## Genoa and Pisa ran the other default (2026-10-12)

The Italian re-code coded the same question, now `CI5`, for the commenda and the *qirāḍ*, and the family splits on it. In Genoa the commended goods were traded and charged together with the traveller's other capital unless the act said otherwise: Scriba's acts commingle; Cassinese writes *et debet implicare separatim* into eight of the fifteen acts that speak, which is a clause one drafts only against a commingling default. Pisa's *Constitutum usus* joins a valued contribution to the traveller's common stock at once, *cum hentica statim communicet* (Bonaini II, 885). *[Corrected late the same day: Catalonia sides with Genoa and Pisa, not with Ḥanafī law; see the next section.]* Ḥanafī law sides with Catalonia: mixing the capital with his own property without *iʿmal fīhi bi-raʾyika* makes the *muḍārib* liable and voids the *muḍāraba* for that sum (al-Sarakhsī, *al-Mabsūṭ* 22, 48). So `comanda` and `qirad` read `segregated`, `commenda` `commingled` (low).

What travels with the default is how a loss is divided. A mixed stock divides gain and loss *per libram* everywhere it is regulated (Pisa; Cassinese; *Consolat* caps. 215–216; *Mabsūṭ* 22, 48); a segregated or traceable one leaves the loss with the owner (Genoa's own Breve prefers the investor who can trace his goods). Mixing is a way of mutualising an owner's particular loss. ~~Whether the census should read that as `LR4` is open: it has so far coded *per libram* sharing of one venture's outcome as not mutualisation.~~ [CORRECTED 2026-10-12: the definitional half is ruled. `LR4` counts the pooling of members' separate outcomes, and *per libram* division of one stock is `0` (ruling 10 of `records/RULINGS-commenda-italian-recode-2026-10-12.md`). What stays open is whether commingling ever turns separate fortunes into a pool; the one pool found so far, three travellers sharing the profit of all their comandas (Amalric 697, 1248), is a separate contract and is parked as a candidate.]

## Ruled late on 2026-10-12: Catalonia commingles with the agent's own money

Read again for the Italian re-code, the *Consolat* states two rules, and the census had coded the narrower one. Cap. 219 bars mixing a comanda taken *sparsa* into a **company's** common stock without notice. Cap. 215 governs mixing with the agent's **own** money and permits it unless the investor restricted the investment: *E si aquell dit no lo·y havia e ell esmerçarà la comanda ab los seus diners ensemps, lo guany e la pèrdua se partirà per sou e per liura* (Capmany/Font Rius 263, page image). `CI5` asks about the capital the agent himself holds or trades, so 215 is the general case. MS ruled `comanda CI5` `segregated` → `commingled`, low (ruling 29 of `records/RULINGS-commenda-italian-recode-2026-10-12.md`).

The family's `CI5` split is therefore no longer Italy against Catalonia. Genoa, Pisa and Catalonia commingle by default and divide the mixed stock *per libram*; only the *qirāḍ* segregates, mixing without authority making the *muḍārib* liable (*Mabsūṭ* 22, 48). The three Latin cases share a Roman-law substrate and count as one datum against the Ḥanafī one.

## Links

- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]
