---
title: tags
type: reference
tags: [meta]
created: 2026-07-20
---

# Controlled tag vocabulary

**Rule.** Tags name *what a note is about* (concepts), never *where it came from*. Provenance is the `project:` and `source-session:` frontmatter fields; navigation is the MOC hubs. This keeps the graph clustering by concept, so ideas link *across* projects instead of rebuilding project silos.

Keep tags lowercase, hyphenated, singular. Before coining a new tag, check this list — `entity-shielding`, not `entity-shield`; `risk-pricing`, not `pricing-risk`.

## Ergodicity / dynamics

`ergodicity` · `time-average` · `ensemble-average` · `multiplicative-dynamics` · `absorbing-barrier` · `jensen-inequality` · `convexity` · `diversification` · `synchrony` · `kolmogorov-nagumo` · `expected-utility` · `ergodic-hygiene`

## Instruments & risk

`risk-sharing` · `risk-pricing` · `pls` · `skin-in-the-game` · `contingent-claim` · `sea-loan` · `bottomry` · `foenus-nauticum` · `marine-insurance` · `qirad` · `mudaraba` · `commenda` · `general-average` · `averia` · `carrera-de-indias`

## Corporate form / shielding

`entity-shielding` · `asset-partitioning` · `corporate-form` · `charter` · `capital-lock-in` · `perpetual-succession` · `legal-personality` · `persona-ficta` · `limited-liability` · `decoupling` · `joint-stock` · `force-economizing` · `naties` · `alleenrecht` · `kabu-nakama` · `monopoly-franchise` · `identity-wrapper` · `ie` · `lindy` · `social-status`

## Islamic contract doctrine

`gharar` · `maysir` · `riba` · `salam` · `hiyal` · `ghishsh` · `khiyana` · `waqf` · `maqasid` · `amana` · `daman`

## Jewish contract doctrine

`isqa` · `heter-iska` · `ribbit` · `avak-ribbit`

**Note on `ribbit` vs `riba`.** Kept separate deliberately. The two prohibitions converge on refusing the priced-certain return but diverge in the forms they license — the *qirāḍ* shields the agent, the *ʿisqa* does not. Collapsing them into one tag would hide the divergence that carries the comparative payoff. See [[Ribbit mandates exposure rather than forbidding gain]] and [[The isqa refuses the agent's shield]].

## Legal / jurisdiction

`legal-violence` · `mare-liberum` · `mare-clausum` · `cartaz` · `grotius` · `canon-law` · `naviganti` · `verification` · `moral-hazard` · `principal-agent`

## Method / historiography

`comparative` · `teleology` · `survivorship-bias` · `selection` · `legibility` · `organizational-memory` · `provenance` · `refused-forms` · `transmission` · `whiggism` · `historiography` · `independent-recurrence` · `convergence-pair` · `ortoq` · `sasanian` · `syriac` · `leitfehler` · `qingzhong` · `determinate-contingent` · `legal-consciousness` · `coding-ontology` · `homology` · `homoplasy` · `parallelism` · `cladistics` · `reticulation` · `symplesiomorphy` · `persistence` · `space-for-time` · `heritability` · `character-independence` · `similarity` · `limited-diversity` · `comparative-concept`

**Note on the four coding tags.** `character-independence` marks the redundancy problem — several characteristics recording one fact. `similarity` marks the Watanabe/Goodman problem — that discriminating power is free, so a typology which adds characteristics until forms separate has found nothing. `limited-diversity` marks the case-to-characteristic budget. `comparative-concept` marks Haspelmath's distinction between concepts built for comparison and categories imported from one tradition, which several of our characteristics currently violate. See [[Typology and character coding literature]].

**Note on `convergence-pair`.** The tag asserts convergence in the strict cladistic sense — independent arrival from *different* ancestral conditions — and is therefore stronger than it looks. Where a shared ancestral substrate is plausible, the correct term is `parallelism`. See [[Homoplasy is the finding not the noise]]; existing `convergence-pair` notes need auditing against the distinction.

## Structural

`moc` · `meta`

## Tooling — *not* concept vocabulary

`tooling` · `htr` · `ocr` · `kuzushiji` · `scanning-hardware`

**These are not concepts and must not be treated as such.** They label the infrastructure reference layer (`project: infrastructure`, `type: reference`) hubbed at [[MOC - Digitisation and text recognition]] — what a note is *about* in the sense of which machine, not which idea. They exist so the digitisation notes are findable, and they are quarantined here so they do not enter the concept graph and generate a cluster that clusters on nothing.

Rule: **never tag an argument note with a tooling tag, and never tag a tooling note with a concept tag.** If a claim about, say, source legibility genuinely arises from working with these tools, it belongs in `notes/` as a proper atomic note with concept tags — not in the reference layer.

`kuzushiji` sits here rather than in a Japanese-material section deliberately: it labels *the OCR problem*, not the script as an object of study. If the script itself later needs a concept tag, coin a separate one and note the distinction.
