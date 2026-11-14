---
title: Agentic research set-ups - the public landscape against the HistorEE protocol
type: reference
tags: [tooling]
project: HistorEE
source-session: agentic-setup-landscape-2026-10-22
database: [organizational_forms, loss_mitigation_forms]
created: 2026-10-22
status: seed
---

# Agentic research set-ups — the public landscape against the HistorEE protocol

**A sweep of the open web and of GitHub code search on 2026-10-22 finds every component of the HistorEE set-up in wide use and the configuration in none.** Zotero MCP servers, Claude Code in VS Code, Markdown vaults and agent-maintained repositories are commodities by now. No public project was found that codes institutional forms from secondary literature held in Zotero into a schema-governed matrix, separates the coding channel from the live values by a blind bundle, adjudicates before write-back, and reserves the commit to the human. The nearest projects each share one or two of these properties and differ on the rest. The difference that cuts deepest is write authority: the two humanities repositories closest in architecture give the agent execution or commit rights that the HistorEE protocol withholds.

## What was searched

- **Web**: five standard searches on Zotero MCP, Claude Code research workflows, historians and economists using Claude Code.
- **GitHub code search**, run signed in through Chrome, because the session's API route to `search/` is closed. Queries and file counts as returned:
  - `zotero path:CLAUDE.md` — 123+ files
  - `zotero path:CLAUDE.md historian` — 6
  - `zotero path:CLAUDE.md "primary sources"` — 41
  - `zotero path:CLAUDE.md archive manuscript` — 42
  - `zotero path:CLAUDE.md "economic history"` — 2
  - `zotero path:CLAUDE.md medieval` — 3
  - `zotero path:CLAUDE.md historiography` — 0
  - `zotero path:CLAUDE.md "data.csv"` — 5
  - `path:CLAUDE.md "secondary literature" coding` — 5, one of them `michaelschiltz/HistorEE_codebooks`
  - `path:CLAUDE.md prosopography` — 3
  - `path:CLAUDE.md "intercoder"` — 21, all qualitative-coding or software projects outside history
  - `codebook path:CLAUDE.md historical` — 102, overwhelmingly unrelated
  - `zotero path:AGENTS.md history` — 110, mostly Zotero plugin development
  - `zotero path:AGENTS.md codebook` — 1, unrelated
  - `zotero path:.mcp.json` — 94
  - `zotero path:.claude/skills` — 173
- `CLAUDE.md` files of the candidates read in full from `raw.githubusercontent.com`.

## Infrastructure — abundant and fragmented

- **kujenga `zotero-mcp`** — Python; `uvx zotero-mcp` installs a three-tool reader against the local or web API. The feature-rich 54yyyu fork ships on PyPI as `zotero-mcp-server`; the name collision is a known trap.
- **piiinpiiins `Zotero-MCP`** — PyPI `zotero-mcp-local`; documents installation under the Claude Code VS Code extension and a macOS defect in which `.mcp.json` `env` fields do not reach the server subprocess.
- **lricher7329 `zotero-mcp-claude-code`** — a Zotero plugin serving MCP over Streamable HTTP from inside Zotero 7–10; `zotero-mcp-plugin/CLAUDE.md` records the Zotero 10 removal of `Zotero.Fulltext.getItemContent`.
- **matthiaskloft `zotero-fulltext-mcp`** (v0.12.2) — converts linked PDFs to Markdown, builds a local index, never writes to Zotero; ships Claude Code and Codex configuration.
- **xiaofei03 `cite-rag-mcp`** — Codex + Zotero + Better BibTeX + Pandoc (`zotero.lua`, `template.docx`) as a citation safety layer: citekey-constrained drafting, DOI lookup without library writes.
- **`research-hub-pipeline`** (PyPI) — Zotero + Obsidian + NotebookLM behind one MCP server (83 tools at v0.55).
- **Galaxy-Dawn `claude-scholar`** — skill and agent bundles for Claude Code, Codex, Kimi and OpenCode with a Zotero import workflow; **HaipingXu `social-science-claude-scholar`** is its social-science fork.

All of these are tools. None is a research project, and none carries a coding protocol.

## Applied economics — the documented practice

- **Paul Goldsmith-Pinkham** (Yale SOM), seven-episode Markus' Academy series on Claude Code for applied economists (2026): EDGAR risk factors into DuckDB; repository wired to Overleaf through GitHub so the agent updates tables and figures; GitHub as the means of verifying agent output.
- **Scott Cunningham**, *Scott's Mixtape* Substack, numbered "Claude Code" series (56+ posts by October 2026). No. 46, "Verification is the new bottleneck"; no. 53, "Applied econometrics will require a detailed checklist".
- **Pedro Sant'Anna**, `pedrohcgs/claude-code-my-workflow` — public skills (`review-paper`, `data-analysis`).

Material: quantitative data, Stata/R/Python pipelines. No Zotero-held secondary corpus. The verification problem is stated as the open one; no blind-channel solution is proposed.

## Humanities and history repositories — the nearest cases

- **anavvanzin `iconocracy-corpus`** and **avmphd `corpus`** — doctoral thesis *ICONOCRACIA: Alegoria Feminina na História da Cultura Jurídica (Séculos XIX–XX)*, Ana Vanzin, PPGD/UFSC, defence 2026. `archive/text-dump/CLAUDE.md`; `CLAUDE.md`.
  - Pipeline: WebScout (Europeana, Gallica, LOC, BnF, Numista, Colnect) → IconoCode (three-level Panofsky reading plus ten *endurecimento* indicators on a 0–3 scale) → `data/processed/records.jsonl` as canonical ledger → `corpus/corpus-data.json` as public export.
  - JSON schemas validated by script; `vault_sync.py` reconciles ledger and Obsidian vault; Zotero PDFs held on an external volume; a Gallica MCP server under `indexing/`.
  - Corpus size: 165 figures in one file, a ~328-record snapshot in the other; N declared deliberately non-fixed.
  - Governance: the agent dispatches on trigger keywords and executes without confirmation.
- **DigitalHumanitiesCraft `mhdbdb-tei-only`** — 667 TEI-encoded Middle High German texts with semantic annotation. `CLAUDE.md` is a pointer into `docs/`; `JOURNAL.md`, `journal-archive.md` and `fehlerjournal.md` keep the session and error record; `sources/INVENTAR-ARCHIV.md` inventories a 9.1 GB legacy archive held outside the repo.
  - Governance: a maintainer ruling dated 2026-10-07 lets the agent commit, push, open and merge pull requests without separate approval once checks pass. No Zotero layer.
- **D3m0sthene5 `Executive-Orders`** — Claude and Codex ("Astra") coordinating on GitHub through `HANDOFF/notes-*.md`, one file per agent, neither editing the other's.
  - `CLAUDE.md` fixes an immutable evidence/legal codebook and separates three layers: AI status hypotheses, source-backed lifecycle dossiers, and independent human certification. It forbids raising the certified count by bulk machine review.
  - No Zotero layer. The nearest case on governance.
- **estebandegetau `Fiscal-shocks`** — Degetau and Samano (World Bank), "Scaling Narrative Fiscal Shock Identification with LLMs". Four codebooks (C1–C4) developed on US budget documents, validated against labelled US shocks, then deployed to Malaysia 1980–2022. It codes primary narrative documents through a pipeline, not secondary literature through an agent. The nearest case on codebook validation.
- **kgeographer `cedop`** — "Computing Place / CEDOP" humanities research platform (EDOP and CDOP components). Codebook versions are kept in `metadata/` (`edops_codebook_v02.tsv` superseded by `v03_draft`); session detail goes to `logs/session_log_YYYYMMDD.md`, and `CLAUDE.md` records current state only.
- **cliodeck `cliodeck-app`** (Frédéric Clavert) and its predecessor **inactinique `cliobrain`** — an Electron writing environment for historians with Zotero, Tropy and Obsidian, MCP in both directions. It replaces the IDE rather than governing a dataset.
- **Florentia-Project `CittaFracta`** — React visualisation of Florentine factions, families and geography. Primary sources (Dante, Dino Compagni, Giovanni Villani) and secondary literature enter through Google Sheets; `CLAUDE.md` is declared binding on all agents.
- **DeepSpawn `ragusa-geneology`** — Python CLI for prosopography of the Republic of Ragusa: GEDCOM → normalised SQLite, with alliance, deduplication and timeline analysis.
- **mancano-tales `Nahoum-Mancano-2026-Antitrust`** — a paper repository that archives its Claude conversations as dated Markdown files under `9-vers/llm-reviews/`, including the sessions that built its Zotero automation. This is a provenance practice: the transcript is committed beside the text it shaped.

## Where the HistorEE set-up differs

| Property | HistorEE | Nearest public case | Status there |
|---|---|---|---|
| Unit coded | Institutional forms, from secondary literature in Zotero | `Fiscal-shocks`, `iconocracy-corpus` | Primary documents or images |
| Coding instrument | Controlled vocabulary and schema, `data.csv` | `iconocracy-corpus` (JSON schemas, 0–3 indicators); `cedop` (versioned codebook) | Present |
| Rater independence | Blind bundle, separate coding chat, `recodings.csv` | `Fiscal-shocks` (validation against labels) | Validation, not blind re-coding |
| Machine output vs certified record | Adjudication before write-back | `Executive-Orders` | Present, without Zotero or a dataset matrix |
| Write authority | Agent proposes, human commits | `mhdbdb-tei-only`, `iconocracy-corpus` | Agent executes or commits |
| Vault linked to dataset | `database:` frontmatter in this vault | `iconocracy-corpus` (`vault_sync.py`) | Present, sync rather than citation |

## Addendum 2026-11-15 — transcription and extraction projects

**A second sweep, on 2026-11-15, aimed at projects that turn primary sources into text or data with a model and publish the output. It confirms the first finding and qualifies it.** Several projects check their output more rigorously than HistorEE does: against a gold standard, by two models disagreeing, or against the source's own internal constraints. None of them codes interpretive characteristics through a blind channel. The protocol leads on governance and lags on measurement.

### Corpus projects with output in the open

- **`professorsolderin/project-lighthouse`.** See [[Model-read mathematical manuscripts - Godel had a proof checker, Lighthouse a false-positive protocol]]. It is the only case found with a ledger of killed candidates and a written false-positive protocol.
- **`fkettelhoit/wittgensteinnachlass`.** Markdown transcriptions of the Wittgenstein Nachlass, served at wittgensteinnachlass.com. The README says the repo was built almost entirely with AI and defers to the Bergen Nachlass Edition as authoritative. Generated files in `md/` are never edited by hand: corrections go to `overrides/`, and every change passes branch → staging site → pull request → production. This separates generated text from human correction in the repo layout itself. ⚠️ Which layers are model-generated, beyond the code and the `md-en/` translations, is not stated.
- **`xieguaiwu/wittgenstein-corpus`.** Derived from the previous repo: 394 coded passages on 447 facsimile pages in seven volumes, 357 of them never printed. It calls itself an independent study edition, not a critical one.
- **`niclasgriesshaber/llm_patent_pipeline`.** Griesshaber & Streb, German patent registers 1877–1918: 306,070 entries from 9,562 scans with Gemini 2.5 Pro and Flash-Lite. Checked against a student-built benchmark (41 images, one per volume) and a separate "perfect" dataset. Pipeline, benchmark and dataset are open. Oxford Economic and Social History Working Paper 228; arXiv 2512.19675. The nearest economic-history case.
- **Crown of Aragon chancery registers.** Jonathan Seyfried, written up by Fred Gibbs (UNM). PARES images; Gemini and Claude transcribe each page in parallel, the outputs are merged, and both raw outputs are kept. A 300-page register takes about 12 h and about $75. Output is published at jonathanseyfried.net (registers 1819 and 2053), not on GitHub. His verdict: good enough for full-text search, not good enough to cite without the manuscript; dates stay unreliable. No error rates.
- **Bäcker-Peral, Meursault & Severen**, US county vehicle-registration tables. Federal Reserve Bank of Philadelphia WP 25-28; arXiv 2505.11599. The gold standard is 694 tables (49,225 data points). LLM output matches it at R² 98.6%, and downstream regression coefficients are statistically indistinguishable. ⚠️ Repository not checked.

### Pipelines with a verification design

- **`ai-historian/chronos`.** Hufe, Griesshaber, Greif, Eck, Torr; arXiv 2604.03553. Claude Opus orchestrates and Gemini extracts. Each prompt is tested on a representative page and shown beside the scan for review before batch extraction is proposed. Sessions are logged as JSONL.
- **`mhumphries2323/Transcription_Pearl`.** Humphries et al., *Historical Methods* 58:3 (2025). CER 5.7–7% raw, 1.8% after LLM correction, on 18th–19th-century English hands. Its successor, Archive Pearl, runs two model families and sends only their disagreements to human review.
- **`Gene-Weaver/VoucherVision`.** University of Michigan Herbarium; specimen labels into Darwin Core records. The finding that matters: zero-trust review, in which every AI suggestion is accepted by hand, is only 10–15% faster than transcribing from scratch. Review, not reading, becomes the bottleneck.
- **`hepplerj/claude-transcribe`.** Batch transcription with Claude or Gemini into Obsidian markdown with YAML frontmatter and wikilinks. The nearest match to this vault's format.
- **`Dieclerc/ArchiveVision-OCR`.** Italian civil-status registers via IIIF; diplomatic and normalised transcriptions side by side; can run locally.
- **Weather records, EGU26-2509.** Outputs checked against physical relationships between meteorological variables; precision up to 97%.

### Benchmarks

- **`RISE-UNIBAS/humanities_data_benchmark`**: 11 datasets, 811 test configurations, Zenodo releases.
- **`stanford-oval/Churro`**: 99,491 documents in 46 language clusters, including the first public Ottoman HTR set and CODH Japanese material.
- **`impresso/llm-transcript-postcorrection`**: LLM post-correction of historical OCR, HTR and ASR output.

### Three kinds of external check, and where HistorEE stands

| Check | Who uses it | HistorEE |
|---|---|---|
| Gold-standard sample, error rate reported | Patents, vehicle registrations, Transcription Pearl | Partial. Rates exist but are one-off and scattered: word recall per engine in `OCR-TEST-madurell-venetian-2026-11-03`, character recall in the Yamamoto pilot, correction counts in the Venetian CORRECTIONS files. Most references are the assistant's own image reads, not independent, and no sample was drawn at random |
| Two model families, review only where they disagree | Archive Pearl, Seyfried | Partial: blind re-coding compares coders, not transcribers |
| Internal constraint of the source | Weather (physical relations); balance-sheet checks (Bessa Ribeiro 2026, via the RF Berlin practitioner's guide) | Unused. Commenda/comanda settlement accounts carry arithmetic of their own (capital returned plus each party's share) where they survive |
| Blind channel for interpretive coding | None found | Present: [[A blind is a property of the channel not of the dataset]] |
| Agent proposes, human commits | Wittgenstein repo (`overrides/`, PR to production) | Present |

**Verdict.** HistorEE leads on rater independence and write authority, and there it has no public counterpart. It lags on measurement, though less than the first draft of this addendum said. Error rates have been measured, but pass by pass, against references that are mostly the assistant's own reads, and they are not collected in one place. There is no randomly drawn, independently read sample. Coverage was audited once (`records/SCRIPTS-venetian-ocr-2026-11-05/cover.py`, ink not covered by the text layer), but no count audit runs in CI. The source's own arithmetic is unused. A panel will ask for the random sample and the standing audit. (Corrected 2026-11-15: the first draft said no error rate had been measured.) The VoucherVision finding also bears on the Resources annex: reading is cheap and review is what costs.

## Flags

- ⚠️ Addendum 2026-11-15: GitHub code search was not available unauthenticated, so the second sweep matched only repository names and descriptions. No Lighthouse-type corpus project was found for Japanese, Chinese or Ottoman documentary material beyond benchmark datasets.
- ⚠️ The code search ran signed in as MS. Other people's private repositories do not appear, so every claim of absence is bounded to public default branches. `HistorEE_codebooks` appeared because it is public: it is the one public instance of the configuration this note describes, and it is excluded from the comparison. (Corrected 2026-10-23: this flag first called it private.)
- ⚠️ The search is keyword-bound. A project whose agent file does not name Zotero, or keeps its instructions outside `CLAUDE.md`/`AGENTS.md`, is invisible to it. The ChatGPT/Codex side is covered only through `AGENTS.md` queries and is thin.
- ⚠️ Counts are files, not repositories; forks and copies inflate several of them.
- ⚠️ Attributions rest on what the repositories state. Handles were not resolved to persons where the repository does not name its author.

## Links

- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]
- [[Blind re-coding workflow - operator, coder, application]]
- [[Primary against secondary coding workflow - three arms, reveal, application]]
- [[Retrieval report workflow - reading the codebooks and the vault back as evidence]]
- [[A blind is a property of the channel not of the dataset]]
- [[Split provenance into priority and independence]]
- [[Model-read mathematical manuscripts - Godel had a proof checker, Lighthouse a false-positive protocol]]

## Source

- GitHub code search, github.com/search (type=code), queries as listed, read 2026-10-22.
- `CLAUDE.md` files read from raw.githubusercontent.com, 2026-10-22: `anavvanzin/iconocracy-corpus` (`archive/text-dump/`), `avmphd/corpus`, `DigitalHumanitiesCraft/mhdbdb-tei-only`, `D3m0sthene5/Executive-Orders`, `estebandegetau/Fiscal-shocks`, `kgeographer/cedop`, `inactinique/cliobrain`, `Florentia-Project/CittaFracta`, `DeepSpawn/ragusa-geneology`.
- pypi.org/project/zotero-mcp-local; pypi.org/project/zotero-fulltext-mcp; pypi.org/project/research-hub-pipeline; mcp.directory/blog/zotero-mcp-complete-guide-2026; glama.ai/mcp/servers/xiaofei03/cite-rag-mcp; dev.co/ai/mcp/claude-scholar; github.com/cliodeck/cliodeck-app/wiki — read 2026-10-22.
- bcf.princeton.edu (Goldsmith-Pinkham series); causalinf.substack.com/s/claude-code/archive; github.com/pedrohcgs/claude-code-my-workflow (via a slide deck citing it) — read 2026-10-22.

- Addendum, read 2026-11-15: github.com/professorsolderin/project-lighthouse; raw.githubusercontent.com READMEs of `fkettelhoit/wittgensteinnachlass`, `xieguaiwu/wittgenstein-corpus`, `ai-historian/chronos`, `Dieclerc/ArchiveVision-OCR`; GitHub repository search (unauthenticated API: names and descriptions only, not code); ora.ox.ac.uk (Griesshaber & Streb WP 228); arxiv.org/abs/2505.11599; philadelphiafed.org; amaranth.unm.edu/ai-workbench/research/atr-paleography.html; tandfonline.com/doi/abs/10.1080/01615440.2025.2500309; midas.umich.edu (VoucherVision talk); meetingorganizer.copernicus.org/EGU26/EGU26-2509.html; rfberlin.com practitioner's guide (2026); zenodo.org (RISE benchmark); arxiv.org/html/2509.19768 (CHURRO).
