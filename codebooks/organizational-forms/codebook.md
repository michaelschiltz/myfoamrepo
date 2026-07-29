# Codebook — organizational forms feature coding

Reference for the comparative feature-coding of cooperative / risk-pooling organizational forms (waqf, ie, compagnia, joint-stock corporation, nación, natie, kabu-nakama, and the types to be added). Supports *Clearing and Settling the Realm* / HistorEE.

Deliberately **outside the Foam graph**, like `glossary.md`: it lives under `codebooks/`, which `scripts/export_graph.py` and `scripts/validate_vault.py` do not scan, so nothing here creates edges or trips CI. No wikilinks below — note and term names are in backticks so they cannot resolve to graph edges. When the sibling `HistorEE_codebooks` repo is in play, move the three CSVs there under `organizational-forms/` and have argument notes cite them via the `database:` frontmatter field; this definition file can stay here as documentation.

## Files

- `codebook.md` — this file. The authoritative definitions and coding rules.
- `characteristics.csv` — machine-readable dimension list (`char_id`, facet, name, value type, allowed values, short definition).
- `types.csv` — the organizational forms (`type_id`, name, tradition, period, key source, status).
- `codings.csv` — the data, in **long/tidy** form: one row per `type × characteristic` cell.

## Data model

The instrument is a `type × characteristic` matrix, but it is *stored* long, not wide, so every cell carries its own provenance and confidence. The wide matrix (and any radar, dendrogram, or Hasse view) is a **pivot** of `codings.csv` — never hand-maintained.

`codings.csv` columns:

- `type_id` — foreign key to `types.csv`.
- `char_id` — foreign key to `characteristics.csv`.
- `value` — from the value vocabulary below.
- `confidence` — from the confidence vocabulary below.
- `source` — short citation or `[verify]`. Required for any `value` that is not `na` or `?`.
- `note` — free text: the reasoning, the school that dissents, the caveat.

## Value vocabulary

The substantive coding. Four of these are values a cell can take; keep them strictly distinct — conflating them is the scalar-ranking error the whole project refuses.

- `1` — **present.** The feature obtains.
- `P` — **partial.** A real intermediate degree: attenuated, qualified, or present in some respects but not others. A genuine middle value, *not* a hedge.
- `0` — **absent.** The feature is applicable to this form and does not obtain.
- `na` — **not applicable.** The characteristic does not apply to this form's category (e.g. `entry restriction` on a form with no membership). Distinct from `0`: absence-of-applicability, not absence-of-feature.
- `?` — **unknown.** Not yet coded, or evidence insufficient to code.

For `nominal` and `ordinal` characteristics the `value` is instead one of that characteristic's allowed categories (see `characteristics.csv`); `na` and `?` remain available.

## Confidence vocabulary

Orthogonal to `value`. A cell can be present-but-contested (`1` / `C`) or partial-but-settled (`P` / `E`) — the two axes must not collapse into one.

- `E` — **established.** Scholarly consensus supports the coding.
- `C` — **contested.** The scholarship disputes it; `note` must say who dissents.
- blank — used with `na` and `?`, where confidence does not apply.

## Coding rules

- One row per `type × characteristic`. No cell coded twice.
- Every `value` other than `na` and `?` carries a `source` or an explicit `[verify]`. Unverified references are never laundered into confident cells.
- `P` is for degree, `C` is for dispute, `na` is for inapplicability. If you reach for `P` to mean "the sources disagree," you want `1`/`C` or `0`/`C` instead.
- Coding is per *form as ideal-typed in a stated period*; where a form has sharply divergent variants (charitable vs family waqf; chartered vs unchartered joint-stock), split them into separate `type_id` rows rather than blurring one code.
- Do not sort or rank forms by count of `1`s. The matrix is a morphology, not a league table.

## Facets and characteristics

Granular by design. Codes group into eight facets; the terse machine version is `characteristics.csv`. Parenthetical tags map each dimension to the vault's controlled vocabulary.

### Legal personality and standing

- `LP1` juridical personhood — entity is a legal person distinct from members (`legal-personality`, `persona-ficta`). {1,P,0}
- `LP2` property in own name — holds/owns property as the entity. {1,P,0}
- `LP3` capacity to sue — standing to sue and be sued as an entity. {1,P,0}

### Asset partitioning

Both Hansmann–Kraakman–Squire directions, split (`entity-shielding`, `asset-partitioning`, `limited-liability`).

- `AP1` entity shielding (weak) — entity creditors prioritized over members' personal creditors in entity assets. {1,P,0}
- `AP2` liquidation protection — members/their creditors cannot force partition or withdrawal of entity assets (strong shielding / `capital-lock-in`). {1,P,0}
- `AP3` owner shielding / limited liability — members' personal assets shielded from entity creditors. {1,P,0}
- `AP4` separation from founder estate — corpus leaves the founder's personal patrimony on constitution. {1,P,0}

### Temporal structure

- `TS1` perpetual succession — persists across member death/exit (`perpetual-succession`). {1,P,0}
- `TS2` venture horizon — {open, fixed-term, single-venture} (single-venture: commenda, single voyage).
- `TS3` revocability — dissolvable/unwindable at will by a party (`1` = revocable; cf. the revocable mudaraba). {1,P,0}
- `TS4` mutability of purpose — entity can alter its own rules/purpose by internal decision (adaptation vs petrification; `lindy`). {1,P,0}

### Capital and interest

- `CI1` capital structure — {common, several-accounts, none}.
- `CI2` capital lock-in — contributed capital not withdrawable at will (`capital-lock-in`). {1,P,0}
- `CI3` transferable interest — interest is alienable/tradable (`alleenrecht`, kabu). {1,P,0}
- `CI4` depersonalised interest — interest negotiable independent of holder identity (`decoupling`). {1,P,0}

### Liability and risk exposure

- `LR1` liability extent — {unlimited-joint, unlimited-several, limited, none}.
- `LR2` outcome coupling — {coupled, attenuated, veiled} (`skin-in-the-game`, `outcome-coupling`).
- `LR3` profit-and-loss sharing — returns shared by stake vs fixed/contractual claim (`pls`, `risk-sharing`). {1,P,0}
- `LR4` risk pooling — mutualizes idiosyncratic risk across members vs unshielded. {1,P,0}
- `LR5` pooling correlation — {diversifying, synchronising, na}; the sign of the pooling (`synchrony`, `diversification`).

### Membership and governance

- `MG1` entitlement basis — {membership, contract, beneficiary} (`social-status`).
- `MG2` governance mode — {collective, founder-fixed, single-principal}.
- `MG3` entry restriction — closed/numerically restricted membership (`1` = restricted). {1,P,0}
- `MG4` authorization source — {state-charter, customary, private-contract, religious} (`charter`).

### Function and privilege

- `FP1` purpose orientation — {pious-charitable, commercial-profit, mutual-provision, mixed}.
- `FP2` monopoly franchise — holds an exclusive right/franchise as property (`monopoly-franchise`). {1,P,0}
- `FP3` identity wrapper — form confers legal-status/access arbitrage for its principals (`identity-wrapper`). {1,P,0}
- `FP4` legibility / registration — entity registered and legible to authority (`legibility`). {1,P,0}

### Contractual form

For the Islamic/Inner-Asian partnership types to be added (commenda, mudaraba, qirad, ortoq).

- `CF1` capital–labour asymmetry — one party supplies capital, another labour/enterprise (`skin-in-the-game`). {1,P,0}
- `CF2` agent bears capital loss — working party bears loss of principal's capital (`0` = principal bears it; the mudaraba asymmetry). {1,P,0}
- `CF3` principal count — {bilateral, multilateral}.

## Type list — seed and expansion

`types.csv` is a **seed**, not the census. The exhaustive list is a later pass, drawing the Latin/European forms from Harris and adding Asian forms deliberately underrepresented in that literature. Candidate additions to weigh:

- Islamic / Inner-Asian: mudaraba, qirad, ortoq, family waqf (as a row distinct from charitable waqf).
- Latin/European: commenda, fraterna, societas, VOC/chartered company, asiento de avería company, Fugger firm.
- Japanese: ton'ya / toiya, kō / mujin (mutual finance), za (medieval guild), kumi.
- Chinese: huiguan (native-place association), gongsi / kongsi, piaohao and qianzhuang (Shanxi banks), hang guilds.
- South Asian: the joint Hindu family (HUF), and the medieval merchant guilds (Ayyavole, Manigramam).

Splitting the waqf into charitable (`khayrī`) and family (`ahlī`) rows is recommended before coding proceeds — they diverge on purpose, governance, and threat model.

## Open design questions

- Membership-presupposing dimensions (`MG3`, `LR1`, `CF*`) resolve to `na` on non-membership forms like the waqf. Confirm `na` is handled as its own state in every downstream view, never merged with `0`.
- Whether `LR2` outcome coupling should be finer than three levels once the partnership types are coded.
- Whether to add a `provenance` facet (transmission vs independent recurrence) or keep that as an analytic overlay rather than a coded feature.
