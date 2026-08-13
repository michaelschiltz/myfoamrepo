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

## Path dependence / sequence

`path-dependence` · `non-commutativity` · `reinforcement` · `attractor-selection`

**Note on the two senses of lock-in.** `capital-lock-in` (below, under corporate form) is the *legal* property — contributed capital non-withdrawable at the member's will. Arthur's *lock-in* is the *dynamic* property — a stochastic process entering one of several stable basins and being unable to leave. They are independent along both axes and the interesting claim lives in their interaction, so the vocabulary keeps them apart: the dynamic sense takes `attractor-selection`, and prose writes *attractor lock-in* or *capital lock-in* in full wherever either could be meant. Never tag a dynamic claim `capital-lock-in`. See [[Arthur's lock-in and capital lock-in are different objects]].

**Note on `path-dependence`.** The tag asserts that the operations are *non-commuting* — that a permutation of the same events yields a different outcome — and is therefore stronger than the ordinary historiographical usage. Where the claim is only that the *set* of past events matters, the phenomenon is Page's **phat dependence** and is compatible with full permutation invariance; do not tag it. Where the claim is that an outcome persists without order-sensitivity, use `persistence`. See [[Path dependence requires naming the non-commuting operation]].

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

## Acquisitions — *not* concept vocabulary

`acquisitions` · `book-trade`

**The second quarantined layer, on the same reasoning as the tooling tags.** They label the supply chain — how a text comes within reach — not an object of study, and they hub at [[MOC - Acquisitions and the antiquarian trade]] with `project: infrastructure`, `type: reference`. `acquisitions` is the general tag for routes to a text (purchase, want-list, ILL, commissioned surrogate); `book-trade` is narrower and names the antiquarian trade as an institution one buys *through*.

Rule, unchanged: **never tag an argument note with an acquisitions tag, and never tag an acquisitions note with a concept tag.**

**Watch this boundary — it is the leakiest one in the vocabulary.** The trade is itself a selection filter, and a claim about how dealer specialisms, cataloguing conventions or digitisation funding condition what survives *into view* is an argument, not infrastructure. Such a claim belongs in `notes/` under `provenance`, `selection` or `survivorship-bias`, never here. The test is whether the note would change if the trade were organised differently: if yes it is infrastructure, if it is *about* the fact that the trade is organised this way it is an argument.
