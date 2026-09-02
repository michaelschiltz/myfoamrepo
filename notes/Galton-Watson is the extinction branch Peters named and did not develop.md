---
title: Galton-Watson is the extinction branch Peters named and did not develop
type: permanent
tags: [ergodicity, absorbing-barrier, multiplicative-dynamics, ensemble-average, time-average, ie, entity-shielding, selection]
project: HistorEE
source-session: galton-watson
created: 2026-09-02
status: seed
---

# Galton-Watson is the extinction branch Peters named and did not develop

Peters's own account of the history of ergodicity economics contains a single entry on the ruin limb, and it is exact.

> "In 1875, Galton and Watson published a paper which studies **a different kind of ergodicity breaking, namely the problem of extinction**. The Galton-Watson process has a non-zero probability of continuing forever, and also a non-zero probability of dying out. Expected values in this process mix universes where the process is dead forever with universes where it continues forever, whereas time averages depend on the particular universe one inhabits." (Peters, "Ergodicity economics — a history," 5 February 2024)

*A different kind.* The two-limb division the vault imposes is Peters's own, stated in his own history — and then not used. Every other entry from 1650 to 2020 is on the averaging limb: Fermat and Pascal on expected value, the Bernoullis, Whitworth's multiplicative fair gamble of 1870, Bachelier, Birkhoff and von Neumann, Itô, Kelly, Aitchison and Brown, Samuelson, Bouchaud and Mézard, and his own papers of 2011, 2016 and 2019. The extinction branch is named once, credited to 1875, and left there.

## Why the process is the better formal home

The branching process does what geometric Brownian motion cannot, and does it without any of the machinery the published critics attacked.

Let $Z_n$ be the size of generation $n$ with mean offspring number $m$. In the supercritical case $m > 1$:

$$\mathbb{E}[Z_n] = m^n \to \infty, \qquad \text{while} \qquad P(\text{extinction}) = q > 0$$

where $q$ is the smallest fixed point of the offspring generating function. **The ensemble average diverges while a positive fraction of lineages are extinct and stay extinct.** Extinction is absorbing, the extinction set is invariant, the survival set is invariant, both carry positive probability, and the invariant σ-algebra is therefore non-trivial. Ergodicity fails by decomposition, exactly as [[An absorbing barrier breaks ergodicity by construction]] requires — and it answers the qualification carried there, since the branching case supplies the **two** invariant sets that a single absorbing state does not.

What makes this decisive rather than merely convenient: **no logarithm is taken, no non-linear observable is introduced, and no Jensen gap appears anywhere.** The divergence between the ensemble average and what happens to a lineage is produced by the decomposition alone. This is the cleanest available demonstration that the ruin limb is formally independent of the variance limb — the claim of [[Ergodicity breaking and order-dependence are independent axes]] — and it means the objection catalogued at [[Absorption without ergodicity economics is just ruin theory]] has a sharp boundary: everything Doctor, Wakker and Wang, Toda, and Ford and Kay argue about concerns a limb this process does not use.

## Why it fits the material

The project's units are lineages that either produce successors or do not. Houses, firms, *naties*, chartered companies, the *ie*. A branching process is the natural object for a population of such units, and the historical questions map onto its parameters directly: the offspring distribution is the rate at which a form is reproduced, and $q$ is the probability that a given lineage is not in the record.

**A lead worth following.** Adoption — *yōshi* — is, in these terms, a technology for raising the offspring distribution of a lineage whose biological succession has failed, and therefore for lowering $q$. That is [[The ie as entity-shielding]] restated as a parameter of a branching process rather than as an analogy, and it would give the *ie* argument a formal statement it currently lacks. Whether the demographic record supports estimating anything of the kind is a separate question and probably a hard one [verify].

**The methodological payoff, which is larger.** If extinction probability is the quantity, then survivorship is not a bias to be corrected but the observable itself, and [[Refusals are observations of the filter not inferences from survivors]] becomes a statement about a well-defined object rather than a methodological caution.

## Two cautions

**Do not confuse the two Galtons.** [[Galton's problem]] in this vault is Francis Galton's 1889 question to Tylor about the non-independence of cultural units — an objection to comparative method. The Galton–Watson process is the 1875 extinction model. Same man, unrelated problems, and the vault now contains both. Write *Galton–Watson process* in full, never "Galton's process."

**Priority.** The result is usually credited as **Bienaymé–Galton–Watson**, Bienaymé having stated it in 1845; Watson and Galton's paper is "On the probability of the extinction of families," *Journal of the Anthropological Institute* (1875), and their original solution was famously incomplete on the supercritical case. Cite carefully — this is a well-known priority tangle and getting it wrong in a book about institutional descent would be conspicuous [verify: exact Bienaymé reference and the standard account of the error].

## Links

- [[An absorbing barrier breaks ergodicity by construction]]
- [[Absorption without ergodicity economics is just ruin theory]]
- [[The published critique never engages absorption]]
- [[Ergodicity breaking and order-dependence are independent axes]]
- [[The market selection literature is the project's nearest formal neighbour]]
- [[The ie as entity-shielding]]
- [[Refusals are observations of the filter not inferences from survivors]]
- [[Time-average optimization is a survivorship property not an intention]]
- [[Absorption is a path-dependence mechanism distinct from reinforcement]]
- [[Galton's problem]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Entity-shielding and corporate forms]]
- [[MOC - HistorEE]]

## Source

Galton–Watson session, September 2026. MS pointed to Peters's history-of-EE blog post as likely to overlap with the two-limb argument; the overlap turned out to be one sentence, and it is the sentence that concedes the division.

## Two further facts from the same post, worth holding

**The growth-rate priority runs earlier than Kelly.** Peters credits **W. A. Whitworth, *Choice and Chance* (1870)** with the result that a fair gamble repeated multiplicatively is a losing proposition. [[Nothing in the ergodic theorem fails in geometric Brownian motion]] concedes priority to Kelly, Latané and Breiman; on Peters's own account it should concede it to Whitworth, eighty-six years earlier. **Not in the library** [verify].

**Peters concedes the log-utility mapping himself.** "The Whitworth-Kelly result can be mapped to a basic form of expected-utility theory, assuming logarithmic utility." That is precisely Toda's charge, granted in advance by the author — see [[The three published critiques do not agree with each other]]. He also reports Samuelson calling Kelly's work "a complete swindle," which places the Merton–Samuelson hostility recorded at [[The growth-rate criterion is asymptotic and the horizon comparison cuts both ways]] in its polemical context.
