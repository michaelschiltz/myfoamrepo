---
title: Jensen supplies the gap but only the dynamic privileges the logarithm
type: permanent
tags: [jensen-inequality, convexity, kolmogorov-nagumo, expected-utility, multiplicative-dynamics, time-average]
project: HistorEE
source-session: wp3-ergodicity-formal-placement
created: 2026-08-06
status: seed
---

# Jensen supplies the gap but only the dynamic privileges the logarithm

Jensen's inequality states that for a convex $\varphi$ and an integrable random variable $X$, $\varphi(\mathbb{E}[X]) \le \mathbb{E}[\varphi(X)]$, with the sense reversed for concave $\varphi$ and with equality if and only if $\varphi$ is affine on the support of $X$ or $X$ is degenerate. The **Jensen gap** is the difference $\mathbb{E}[\varphi(X)] - \varphi(\mathbb{E}[X])$, and to second order it is $\tfrac{1}{2}\varphi''(\mathbb{E}[X])\operatorname{Var}(X)$ — the gap is curvature times dispersion, which is why it vanishes both under linearity and under certainty.

For the project the relevant instance is the concavity of the logarithm: $\mathbb{E}[\log X] \le \log \mathbb{E}[X]$. **This inequality is the entire wedge between the time-average and the ensemble-average growth rate in the multiplicative case**, and in the geometric case the second-order expression evaluates to exactly $\tfrac{1}{2}\sigma^{2}$. Nothing further is needed, which is the concession that must be made openly rather than extracted — see [[Nothing in the ergodic theorem fails in geometric Brownian motion]]. The conditional form of the inequality is the one that does the work in the stochastic-process setting (Doob 1953).

## Why the theory of means cannot supply the privilege

The obvious next move is to reach for Kolmogorov and Nagumo, who independently characterised the quasi-arithmetic means $M_f(X) = f^{-1}(\mathbb{E}[f(X)])$ as exactly those means satisfying continuity, monotonicity, symmetry and decomposability, for $f$ continuous and strictly monotone. **That move must not be made, because the characterisation runs against us.** If every continuous strictly monotone $f$ generates an admissible mean, then the logarithm is one member of an infinite family with no distinguished status, and the theory of means positively *licenses* the expected-utility patch it is being summoned to displace. This is the point already recorded at [[Route Kolmogorov to ergodic theory not the theory of means]], and it is the reason Kolmogorov belongs to the ergodic-theory lineage in our text and nowhere else.

The privilege of the logarithm, where it exists, comes from somewhere else entirely: **the dynamic fixes $f$.** Under multiplicative dynamics the logarithm is the transformation that converts a non-stationary multiplicative process into a stationary additive one, which is the condition under which the ergodic theorem applies at all. $f$ is therefore not selected by the modeller from a family of admissible means but determined by the process being modelled. That is what distinguishes the claim from a utility assumption: log utility is *derived* rather than posited, and the maximand is relocated and corrected rather than eliminated.

## The objection this invites

Stating it that way converts the "which utility function?" problem into a "which dynamic?" problem, and a competent referee will say so. Specifying the dynamic is, formally, as free a choice as specifying the utility function; the apparatus has moved the arbitrariness rather than removed it.

The available answer is that dynamics are in principle observable and testable while preferences are not — a real asymmetry, and the one on which the framework's scientific claim rests. But it is weaker in our setting than in a laboratory one, because for historical cases the dynamic is inferred, frequently from the same evidence the argument then explains. **This is a live vulnerability for WP3 and should be named in the application rather than left for the panel to find**, particularly given the falsifiability charge already lodged against the framework.

## Links

- [[Jensen gap]]
- [[Nothing in the ergodic theorem fails in geometric Brownian motion]]
- [[Route Kolmogorov to ergodic theory not the theory of means]]
- [[Economics had its ensemble moment in 1738 and psychologized it]]
- [[Time-average]]
- [[Stationarity is a precondition of ergodicity not a corollary]]
- [[MOC - Defending the ergodicity claim]]
- [[MOC - Ergodicity and the time-ensemble distinction]]
- [[MOC - HistorEE]]

## Source

WP3 formal-placement session — the formal limb of the Jensen material, split from the historiographical limb kept at [[Jensen gap]].

## References

Doob, J. L. 1953. *Stochastic Processes*. New York: Wiley.

Hardy, G. H., J. E. Littlewood, and G. Pólya. 1934. *Inequalities*. Cambridge: Cambridge University Press.

Jensen, J. L. W. V. 1906. "Sur les fonctions convexes et les inégalités entre les valeurs moyennes." *Acta Mathematica* 30: 175–93.

Peters, Ole, and Murray Gell-Mann. 2016. "Evaluating Gambles Using Dynamics." *Chaos* 26: 023103.

**Verify before citing.** Kolmogorov, "Sur la notion de la moyenne," *Atti della R. Accademia Nazionale dei Lincei* 12 (1930): 388–91, and Nagumo, "Über eine Klasse der Mittelwerte," *Japanese Journal of Mathematics* 7 (1930): 71–79 — volume and page numbers unconfirmed for both, and de Finetti has a near-contemporaneous claim on the same characterisation that should be checked before priority is implied. The decision-log question of whether Peters cites Kolmogorov–Nagumo directly remains open and governs whether Kolmogorov 1930 enters the evaluative limb at all. Aczél's *Lectures on Functional Equations* (1966) is the standard modern statement of the characterisation if a secondary anchor is wanted.
