---
title: Count degrees of freedom not cells
type: permanent
tags: [coding-ontology, cladistics, comparative, verification]
project: HistorEE
source-session: isqa-qirad-commenda
database: [organizational_forms]
created: 2026-08-02
status: seed
---

# Count degrees of freedom not cells

A morphological matrix reports how many **cells** separate two forms. What licenses an inference is how many **independent facts** those cells encode. The two diverge, and the gap is where a comparative argument gets overstated without anyone lying.

The *ʿisqa*/*qirāḍ* contrast in `organizational_forms` looks fourfold:

- `AP3` = 0 — the manager's estate is exposed
- `LR1` = unlimited-several — he is severally liable
- `CF2` = 1 — he bears capital loss
- `LR6` = symmetric — his exposure runs both ways

Four cells, one fact: **the manager is a debtor on the loan half.** Each characteristic asks a real and separately-motivated question, and for entity forms they come apart — a limited partner is shielded (`AP3`) with no capital-labour asymmetry (`CF2`) in play at all. But for bilateral capital-labour contracts they collapse to a single degree of freedom, and a reader counting cells reads four times the evidence that exists.

This is character non-independence, and it is the standard objection in the phylogenetic literature the project is already borrowing from — see [[Borrow the diagnostics not the tree]]. Correlated characters inflate apparent support exactly as they do in a cladistic matrix; the remedy there is to weight or merge them, not to pretend the correlation is absent.

## Why adding characteristics does not fix it

Discriminating power in a Zwicky matrix is free. Given enough characteristics **any** two forms become distinguishable, at which point "these forms differ" stops being a finding and becomes a report on how hard one looked. The binding constraint is forms, not features — see [[The morphological matrix is dictated by the shape of the feature space]].

So the rule for adding a characteristic is narrow. Add one when an existing characteristic **answers two questions at once** — that is a conflation, and conflations produce uninterpretable values. `LR2` was such a case: it returned `coupled` for the *muḍāraba*, the *commenda* and the *ʿisqa* alike, erasing the difference between an agent holding a call bounded below at zero and one holding a debt that carries him past it ([[Skin in the game is asymmetric in the mudaraba]]). Do **not** add one merely to sharpen resolution.

## The instrument

Dependence is now recorded in the vocabulary rather than left to a reader's judgement, in two columns that are deliberately not merged:

- **applicability** — whether the cell exists at all (`LR5` is meaningless where `LR4` is 0)
- **redundancy** — whether the cell adds evidence (`AP3`, `LR1`, `CF2`, `LR6` within capital-labour contracts)

Collapsing those two into one column would repeat the very error the columns exist to catch.

`scripts/check_dependence.py` tests both against the coded data. On its first run it caught a live inconsistency in the seed coding — `waqf_khayri` carrying `LR4=P` with `LR5=.NA`, which asserts partial pooling and inapplicable correlation simultaneously.

## The test is determination, not signature count

The instrument was initially wrong in a way worth recording, because the mistake is the natural one. It counted **distinct signatures** across forms and reported collinearity when signatures were few. That tests nothing: *n* forms yielding *n* distinct signatures is equally consistent with total redundancy and with total independence.

The actual test is whether the mapping between members is a **function** — does each value of `AP3` occur with exactly one value of `LR6`? Only if every member determines every other does the group collapse to one degree of freedom.

A second distinction the corrected version enforces: separation via a `.NA` is weaker than separation between two substantive values. `.NA` reports that a cell is out of scope, which is a fact about the characteristic's domain rather than evidence that two characteristics vary independently.

## Coding one more form settled it

`agent-loss-exposure` was grouped on logical grounds with scope `conditional` — asserted to collapse for bilateral capital-labour contracts and to come apart elsewhere. Coding the *asiento de avería*, a multilateral capital-pooling form with no capital-labour asymmetry, tested that assertion and **confirmed it on substantive values**:

- `LR1=limited` occurs with `LR6=symmetric` (the *asiento* *partícipe*, capped in both directions) **and** with `LR6=upside-only` (the *qirāḍ* agent, holding a call)
- `AP3=1` likewise splits across both

So limited liability does not determine the direction of exposure, and the four characteristics are not one fact outside the contract forms. The *ʿisqa*/*qirāḍ* contrast still rests on a single degree of freedom — that stands — but the **group** does not, and the `conditional` qualifier was carrying real weight rather than hedging.

The general lesson is cheap to state and was expensive to reach: **a dependence asserted on logical grounds is a hypothesis, and it takes only one form outside the class to test it.** Adding forms buys more than adding characteristics.

## The symmetric failure

A characteristic returning the **same value for every form** is the mirror image: either genuinely invariant or under-specified, and the two are indistinguishable until a form breaks the tie. `interest-alienability` currently has zero variance across the coded set and carries no information at all. Note also that apparent collinearity at n=2 is not evidence of anything — any two characteristics look collinear across two forms.

## Links

- [[The morphological matrix is dictated by the shape of the feature space]]
- [[Borrow the diagnostics not the tree]]
- [[Isqa qirad and commenda are a liability-variable triad]]
- [[Skin in the game is asymmetric in the mudaraba]]
- [[Divergent arbitrary particulars are the independence diagnostic]]
- [[The coding commons must record stated rationale not only component presence]]
- [[Homoplasy is the finding not the noise]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]

## Source

ʿIsqa session, August 2026. Surfaced while coding the *ʿisqa* against *qirāḍ* and *commenda*, when the contrast appeared in four cells and turned out to rest on one.
