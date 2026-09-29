---
title: Primary against secondary coding workflow - three arms, reveal, application
type: reference
tags: [verification, provenance, coding-ontology, tooling]
project: HistorEE
source-session: commenda-pilot-application
database: [organizational_forms, loss_mitigation_forms]
created: 2026-09-28
status: seed
---

# Primary against secondary coding workflow - three arms, reveal, application

**What this workflow tests.** It holds the rater fixed and varies the evidence. One model codes the same cells three times, in three chats: from the secondary works the live cells cite (arm S), from the transactional record those works compress (arm P, stage 4), and again from that record after the live and arm-S values are revealed (arm P, stage 5). The fixed-evidence re-code of [[Blind re-coding workflow - operator, coder, application]] measures the interpreter; this one measures what the secondary literature did to the documents, which is the question [[Hold the rater fixed and vary the evidence]] argues matters more. This note records the procedure as first run on 2026-09-28 (the commenda pilot: `commenda-secondary-2026-09-28` and `commenda-primary-2026-09-28`, 61 cells, `claude-opus-5-5` at `high`), with the repairs the run showed were needed. It states no cell value on purpose.

**Withhold this note by slug from any bundle that codes notarial acts.** Its "result" section reports which kinds of characteristic the acts could and could not address. That is the operator's observability prediction, scored; a coder who reads it is steered toward `.NR` before opening a source. Withhold `commenda-pilot-application` and `recode-methodology-discussion` together.

## The design

| arm        | reads                                                   | blind to                                  | `condition` | measures                                                |
|------------|---------------------------------------------------------|-------------------------------------------|-------------|---------------------------------------------------------|
| S          | exactly the works the live cells cite, and only if held | live values, arm P                        | `blind`     | the rater effect on the same literature (S against live) |
| P, stage 4 | the transactional record only, in the original language | live values, all secondary work, arm S    | `blind`     | the evidence effect, rater fixed (P4 against S)         |
| P, stage 5 | the same chat, after the reveal of live and arm-S cells | nothing                                   | `open`      | anchoring (P5 against P4) and severity (the directed search) |

**S and P must be separate chats.** A chat that has read the secondary account cannot then read the acts "primary-only". Stages 4 and 5 must be the same chat, because anchoring is the difference between one reader's two answers.

## The sequence

**0. Design, operator chat.** It spends the blind and never codes. The design document carries two operator-only sections: the operator's own exposure, and **the observability predictions**, which characteristics the source type can address at all. Both are withheld from every coder, because telling a coder which cells "cannot" be answered steers it.

**1. Bundles, operator chat.**

- **Minimal, not scrubbed.** Each bundle holds the doctrine files, both schemas, both characteristic vocabularies, a scope file (type code, name, tradition, period), the recodings templates, `cells-in-scope.csv` and its sources. **No `data.csv`, logbooks, CHANGELOG, views, `records/` or vault.** Where a family runs through the record from the census's first weeks, including less leaks less than scrubbing more. The cost is house practice from neighbouring rows; say so.
- **Redact by hand, and disclose what cannot be redacted**: a type code that implies a value, a type name that is definitional, the model's training knowledge, a skill's worked example. The coder lists every leak in its priors.
- **Prepare the primary corpus as evidence, not as an edition.** Cut the editors' introductions. Strip every editorial summary (Blancard's French *analyses*, for instance) and keep the original-language text. Treat the editors' headings (regesti) as a sampling aid, never as evidence. Segment the acts by the edition's numbering and validate the numbering against an independent edition of a subset.
- **Measure the edition's own selection and withhold its direction.** An editor who prints only some acts in full chooses which; the operator measures the bias from the editor's own summaries and keeps it for scoring. The coder is told that a selection exists, not which way it runs.
- **Pre-assign every id** for all three row sets in `cells-in-scope.csv` (blind ids for S and stage 4, open ids for stage 5).
- **Write a sha256 manifest** of each bundle into `records/`.
- **Channel check**: read the prompts, the READMEs and the loaded skills against the operator-only sections and delete every overlap.

**2. The hinge, per chat (MS).** The coder writes its priors, including an exposure section, and prints the file's sha256. MS copies the filled file into `records/`, checks the hash, commits, and replies "committed, hash matches". Only then does the coder open a source. **This repair of 2026-09-26 was tried on 2026-09-28 and held**: the application found both filled priors in the committed tree by reading `.git` objects.

**3. Arm S.** It codes from the cited works as held; a cited work that is not held yields `.NR`, never a reconstruction. It maps the works' non-independence (shared upstream, one author twice, a quotation that is another author's), freezes, and prints hashes.

**4. Arm P, stages 1–4.**

- **Type census**: classify every act by its drafting term, not by the editor's heading. Keep the undrafted acts that do the same work in a separate count; they decide the frame.
- **Sample**: strata are notary × drafting term. A stratum of 60 or fewer is taken whole; a larger one gets a systematic draw of 60 with a random start and a fixed, recorded seed. Sixty detects a state present in 5% of a stratum with probability 0.95; the target is minority states, not proportions.
- **Instance layer**: one row per act (parties with roles, capital, venture, every clause quoted verbatim and parsed), and one row per act per characteristic it speaks to. Quotes that carry a minority state are checked against the page image, because a text layer's OCR can invert a reading.
- **Aggregation**: the cell is the modal state among the acts that speak, pooled; a state held by at least 10% of the speaking acts in any one corpus is a named variant; **a frequency never becomes `P`**; `.NR` where no act speaks; ties go to the state with more distinct investors. Counts, shares and distinct investors go into every cell's `notes`, per corpus and pooled.
- **Freeze**, and print hashes.

**5. Reveal, operator.** Verify both freezes against the printed hashes and the manifests. Build the reveal file (per cell: the live value, confidence, articulation, `source_ref`, `source_read` and notes, and the same for arm S, with the stage-5 id), rebuild it to confirm that `data.csv` has not moved, commit it, and only then place it in the P bundle.

**6. Arm P, stages 5–6.** Per cell, **keep, dispute or revise**, with reasons. For every cell where stage 4 differs from live, search the whole corpus, not only the sample, for acts that would overturn the coder's own value. Stage-4 files stay frozen; stage-5 values are new rows with `condition=open`. The coder flags every revision the reveal prompted.

**7. Application, a fresh chat.** It neither codes nor adjudicates.

- Verify every hash, both manifests, the priors and reveal blobs in the committed tree, the join to `data.csv`, and zero drift between `data.csv` and the reveal file. Run the check suite green before writing.
- Fill `value_at_recoding` and `agreement` only; append in id order after a round-trip `cmp`; assert the old file is a byte prefix of the new one.
- Copy the record into `records/`: both coders' notes, the reveal notes, the frozen row files as `PROPOSED-RECODINGS-…`, and the instance layer.
- Score (next section), write the adjudication worksheet, the logbook entries, the CHANGELOG block, the commit message and three standing-table rows (both coding chats and itself), then run the checks again.

**8. Adjudication (MS).** Per cell: primary right, live stands, S right, definitional (a vocabulary question), split, or acquire first. Only a `replaced` ruling touches `data.csv`.

## Scoring

**Four comparisons, each answering one question.** S against live: the rater effect. P4 against S: the evidence effect. P4 against live: both. P5 against live: after the reveal.

**Four agreement classes, kept apart**: exact; confidence only; substantive (two coded values); missingness (a value against `.NR` or `.NA`, or `.NR` against `.NA`). Give them by row, by component and overall, and count the direction of the confidence differences over all cells.

**The four kinds of difference**, stage 4 against live and against S, cell by cell:

- **Compression error**: both coded, different values.
- **Compression loss**: a variant the primary arm names that the secondary coding's notes do not record as occurring. **This one is a judgment about what a note says, so list every call and its reason.**
- **Outrunning**: the primary arm returns `.NR` where the secondary coding has a value.
- **Primary gain**: the primary arm codes where the secondary coding is `.NR`.

A child cell set against a parent-derived `.NA` is none of the four; mark it dependent.

**Anchoring**: the share of stage-4 values revised at stage 5, the direction of each (to the live value, toward it, away, neither), and the stage-5 agreement recomputed without the revisions the coder flagged as reveal-prompted.

**Observability**: score the operator's withheld predictions against stage 4's `.NR` pattern, characteristic by characteristic, and check where the four kinds fall relative to them.

**Dependence**: for each disagreeing child, does its parent disagree too? `check_dependence.py` reads `data.csv` only, so import its applicability function and run it on each arm's grid.

## What the design cannot deliver

- **Corroboration, where primary and secondary share a base.** When the secondary dataset was built from the same cartularies, agreement between the arms corroborates nothing; disagreement measures the compression. [[Split provenance into priority and independence]].
- **A sample of parties.** A notarial clause measures the notary's formulary, so the effective n is the number of notaries, and two notaries thirty years apart cannot separate time from hand. [[The notarial security clause is boilerplate and cannot carry a typology]].
- **Proportions from a selective edition.** Where the editor printed the non-routine acts preferentially, the corpus is stronger for detecting minority states and weaker for their frequency.
- **An independent reader.** Every coder is a Claude model; errors correlate.
- **Proof that no source was opened before the priors.** The commits order the priors against the freeze, not against the first page read; that last step rests on the coder's account.
- **An independent stage 5.** The directed search is aimed by the reveal. A revision it finds can be right and still not count as blind.

## The first run, as counts only (2026-09-28)

- **Values agreeing, of 61**: S with live 52; stage 4 with S 40; stage 4 with live 40; stage 5 with live 43.
- **Against live**: 10 outrunning, 9 compression losses, 6 compression errors, 3 primary gains.
- **Anchoring**: 5 of 61 revised, all among the 21 cells where stage 4 differed from live, none away from it. Without the three the coder flagged as reveal-prompted, stage-5 agreement falls back to the stage-4 figure.
- **Observability**: 44 of 48 unconditional predictions held. **A notarial act binds its parties and addresses no one else**: it speaks to the contract's internal terms and is silent on outside creditors, juridical personhood, transfer of interests and the proof of a loss. Five of the ten outrunnings fell on characteristics the operator had predicted unaddressable, and two more on the proof of loss.
- **Confidence**: where the value matched and the confidence did not, every arm was lower than live on most cells (arm S on 19 of 20, stage 5 on 19 of 22).

## Repairs for the next run

- **Pre-register the rule for drafted omission.** The pilot's most consequential stage-5 move treated a clause the notary writes into his other instruments, but not into this one, as an observed absence. Whether that counts is a vocabulary question; decide it in the design, not in the reveal.
- **Fix the frame in the design.** Selecting by drafting term swept land partnerships into a sea-venture row and set several cells. Decide the frame, and record sea against land as a field, before sampling.
- **Make stage 5 write its instance changes to a file.** Stage-5 recounts rested on instance readings that exist only in the reveal notes, because the stage-4 instance files are frozen. A separate post-reveal instance-delta file keeps them auditable.
- **Specify `.NA` propagation into `source_class`** in the prompt and the template; one arm wrote a class on `.NA` rows.
- **Give the compression-loss rule to the coder**, or have arm S list the variants it records, so the application does not have to judge what a note says.
- **Test the foreign key, don't assume it.** A green `frictionless` run is evidence only after a negative control: alter one `record_id` in a scratch copy and watch it fail.
- **Grant the application chat its standing-table row in the licence**, as was done this time.

## Where the 2026-09-28 record lives

- **Codebooks:**
  - `records/NOTES-commenda-pilot-operator-2026-09-28.md` is the operator brief; the pilot design is `Claude outputs/PILOT-DESIGN-commenda-primary-secondary-2026-09-27.md`.
  - `records/PROMPT-commenda-{secondary,primary,pilot-apply}-2026-09-28.txt`, both `PRIORS-…`, both `MANIFEST-…` and `REVEAL-commenda-2026-09-28.csv`.
  - The coders' record: `NOTES-commenda-secondary-coding-…`, `NOTES-commenda-primary-coding-…`, `NOTES-commenda-primary-reveal-…`, the six `PROPOSED-RECODINGS-…` files, and `INSTANCES-`, `INSTANCE-CHARS-` and `TYPE-CENSUS-commenda-primary-2026-09-28.csv`.
  - Logbook 4 and logbook 5, 2026-09-28; the CHANGELOG block of the same date. The adjudication worksheet is open work in `proposed-of/`.
  - The coders' own logbook drafts and commit messages, and a hash-verified snapshot of each bundle without its PDF extracts (`records/BUNDLE-commenda-{secondary,primary}-2026-09-28/`, including the Amalric Latin extract arm P coded from). The bundles themselves were deleted; logbook 1, 2026-09-28, records the move.
- **Rows**: OF-R0065–R0190 and LM-R0001–R0057 in the two `recodings.csv` files, all `pending`.

## Links

- [[Blind re-coding workflow - operator, coder, application]]
- [[Hold the rater fixed and vary the evidence]]
- [[A prediction is evidence only if its priority is committed]]
- [[A blind is a property of the channel not of the dataset]]
- [[Split provenance into priority and independence]]
- [[The notarial security clause is boilerplate and cannot carry a typology]]
- [[Count degrees of freedom not cells]]
- [[MOC - Historiography and method]]
- [[MOC - HistorEE]]
