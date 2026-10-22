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

## Flags

- ⚠️ The code search ran signed in as MS, so his own private repositories appear in results (`HistorEE_codebooks` did) and other people's private repositories do not. Every claim of absence is bounded to public default branches.
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

## Source

- GitHub code search, github.com/search (type=code), queries as listed, read 2026-10-22.
- `CLAUDE.md` files read from raw.githubusercontent.com, 2026-10-22: `anavvanzin/iconocracy-corpus` (`archive/text-dump/`), `avmphd/corpus`, `DigitalHumanitiesCraft/mhdbdb-tei-only`, `D3m0sthene5/Executive-Orders`, `estebandegetau/Fiscal-shocks`, `kgeographer/cedop`, `inactinique/cliobrain`, `Florentia-Project/CittaFracta`, `DeepSpawn/ragusa-geneology`.
- pypi.org/project/zotero-mcp-local; pypi.org/project/zotero-fulltext-mcp; pypi.org/project/research-hub-pipeline; mcp.directory/blog/zotero-mcp-complete-guide-2026; glama.ai/mcp/servers/xiaofei03/cite-rag-mcp; dev.co/ai/mcp/claude-scholar; github.com/cliodeck/cliodeck-app/wiki — read 2026-10-22.
- bcf.princeton.edu (Goldsmith-Pinkham series); causalinf.substack.com/s/claude-code/archive; github.com/pedrohcgs/claude-code-my-workflow (via a slide deck citing it) — read 2026-10-22.
