---
title: A constant projection matrix has no ergodicity content
type: permanent
tags: [ergodicity, time-average, ensemble-average, individuation]
project: HistorEE
source-session: hive-report-v3
created: 2026-11-21
status: seed
---

# A constant projection matrix has no ergodicity content

**The dominant eigenvalue that Bourrat et al. 2022 and Clejan, Congleton and Lerch 2022 use as fitness belongs to deterministic dynamics. In a constant environment the ensemble and time averages coincide, so an ergodicity reading of their results has nothing to add. It acquires content only in a random environment, where the time-average growth rate is the top Lyapunov exponent of the random matrix product and lies below the growth rate of the mean dynamics. Stochastic demography has known this since Tuljapurkar and Orzack 1980; it is the ensemble/time gap under another name.**

## What the papers compute

Bourrat et al. (2022, §2.2, read in the bioRxiv version) define collective fitness as the Malthusian parameter of a size-class population projection matrix $\mathbf A$, obtained from the Perron–Frobenius theorem and the strong ergodic theorem of demography. $\mathbf A$ is constant. Clejan et al. take the dominant eigenvalue of linearised invasion dynamics. Neither has noise in the environment.

## What the random case adds

With i.i.d. random matrices $\mathbf A_t$, the growth of one realisation is $\lambda_s = \lim_t \tfrac1t \log \lVert \mathbf A_t \cdots \mathbf A_1 \rVert$ (Furstenberg and Kesten 1960), and $\lambda_s \le \log \rho(\mathbb E\,\mathbf A)$, the growth rate of the expected population. The first is a time average, the second an ensemble average. Where lineages can die out, $\lambda_s$ is defined only on survivors, and [[Conditioning on survival is an ensemble operation]].

## What survives of the horizon proposal

Bourrat et al.'s equality survives. Particle and collective counts are both positive linear functions of the same matrix product, so they grow at the same top Lyapunov exponent: the levels coincide on the time-average horizon. What the restatement adds is a second source of apparent decoupling besides the short window. An experiment that averages collective counts across replicate lines estimates the ensemble rate; one that follows a single line estimates the time-average rate. The two differ by the volatility of the environment. [[Fitness decoupling may be a short-horizon artefact]] is corrected accordingly.

The Black, Bourrat and Rainey 2020 patch cycle is a divergence between horizons. It becomes an ensemble-versus-time divergence only if the patch cycle is random.

## Use

This is item (a) for the note to Peters and Connaughton recommended in the hive report (third version, recommendation 3). It also gives WP3 a citable precedent from outside economics: the demographers distinguished the two growth rates forty years before ergodicity economics named the distinction, and [[Adamou Berman and Peters 2026 on the two growth rates]] is the same pair of rates for wealth.

## Links

- [[Fitness decoupling may be a short-horizon artefact]]
- [[Conditioning on survival is an ensemble operation]]
- [[Adamou Berman and Peters 2026 on the two growth rates]]
- [[The growth-rate criterion is asymptotic and the horizon comparison cuts both ways]]
- [[More than the sum requires a non-additive aggregation rule]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - HistorEE]]

## Source

Session of 2026-11-21. Bourrat et al. 2022 §2.2 reread in Zotero (bioRxiv version). Tuljapurkar, S. D., and S. H. Orzack. 1980. "Population Dynamics in Variable Environments I. Long-Run Growth Rates and Extinction." *Theoretical Population Biology* 18 (3): 314–42. Furstenberg, H., and H. Kesten. 1960. "Products of Random Matrices." *Annals of Mathematical Statistics* 31 (2): 457–69, doi:10.1214/aoms/1177705909. Both cited for standard results, not reread.
