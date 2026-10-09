---
title: Retrieval report workflow - reading the codebooks and the vault back as evidence
type: reference
tags: [provenance, coding-ontology, tooling]
project: HistorEE
source-session: comanda-commenda-retrieval-report-2026-10-09
database: [organizational_forms, loss_mitigation_forms]
created: 2026-10-09
status: seed
---

# Retrieval report workflow - reading the codebooks and the vault back as evidence

**What the exercise is.** An assistant is asked a comparative question and answers it only from what the project has already recorded: the live cells, the recodings, the rulings and coding notes in `HistorEE_codebooks`, and the claim notes in this vault. No new source is read. The output is a prose report written as a draft section of a paper. The exercise tests two things at once: whether the record can be found and read back correctly, and whether it is coherent enough to write from. Discrepancies it turns up are part of the result.

**First run, 2026-10-09.** "The Spanish comanda against the other commenda forms coded earlier." The report is in the Project as `claude/comanda-commenda-interim-report-2026-10-09.md`, read against `HistorEE_codebooks` at `c39a618` and this vault at `86b7190`. It produced the claim notes of this session, listed under "Links", and one record correction (comanda adjudication 7 omits `TS2` and `RB3` from the cells separating `comanda_ad_societatem` from `societas_maris`).

## Procedure

1. **Pin the state.** Clone or pull both repositories and record the commit hashes in the report's header. Say what is unreviewed and unadjudicated.
2. **Read the batch records before the data.** The coding NOTES, the rulings and the type rows in `records/` say what was decided, on what sources, and what was declined; the Project pages say what happened afterwards.
3. **Tabulate the cells.** Pull every compared form's values, confidence and articulation from both `data.csv` files into one table, then read the `notes` of every cell that differs. Values without their notes mislead.
4. **Read the recodings.** `recodings.csv` holds the unadjudicated readings (arm S, stage 4, stage 5) that can reverse a live value. The pilot's directed searches, for example the formulary counts behind `RB3`, often carry the strongest evidence in the record.
5. **Read the vault cluster.** Start from the thematic MOC, not search: the MOC hubs surface the relevant notes more reliably than `project_search`. Read the session's claim notes and the older notes they link.
6. **State the footing.** Before comparing, name the asymmetries of source layer, rater and non-independence.
7. **Sort every difference** into evidence, vocabulary or form ([[A difference between coded forms is a difference of evidence, vocabulary or form]]), and report only the third as a candidate finding.
8. **Write what must not be claimed.** A short section listing the inferences the record does not license.
9. **Check the record against itself.** Compare every value the NOTES or a Project page assert against `data.csv`; report mismatches, do not fix them.
10. **List what would move each finding**, by source and by cell.

## Rules

- Nothing is changed in either tree during the exercise. Corrections are reported to MS.
- **This note and any retrieval report spend the blind on every form they discuss.** Withhold slug `comanda-commenda-retrieval-report-2026-10-09` from any bundle that codes the commenda family.
- Cite cells as `form CHAR = value` and sources by author, year and page as the cells do; never cite the report itself as evidence for a value.

## Links

- [[Bilateral names two different loss rules in Genoa and Catalonia]]
- [[The commenda family fixes the allocation of loss and varies its proof]]
- [[Genoese notaries drafted the commenda as equity and Catalan notaries as credit]]
- [[The comanda ad societatem shares the isqa's allocation but not its construction]]
- [[Agent-borne capital loss clusters in local contracts]]
- [[Primary against secondary coding workflow - three arms, reveal, application]]
- [[Blind re-coding workflow - operator, coder, application]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]
