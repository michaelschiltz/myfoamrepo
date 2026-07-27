# Licensing

This repository carries two licences, split by what a file *is*, mirroring the arrangement in the sibling repository [`HistorEE_codebooks`](https://github.com/michaelschiltz/HistorEE_codebooks).

## The split

**Prose — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).**
All note content is licensed under the Creative Commons Attribution 4.0 International licence. This covers the atomic notes and hubs (`notes/`, `mocs/`), the controlled vocabulary (`tags.md`), the glossary (`glossary.md`), and the prose of `readme.md`. You may share and adapt this material, including commercially, provided you give appropriate credit (see *Attribution* below).

**Code — [MIT](./LICENSE).**
All executable material is licensed under the MIT licence: everything in `scripts/`, the git hooks in `.githooks/`, and the GitHub Actions workflows in `.github/`.

Bundled third-party material keeps its own licence: the Foam documentation under `_foam-docs/` and the template scaffolding (`_layouts/`, `assets/`) are the work of the Foam project and are governed by [Foam's own MIT licence](https://github.com/foambubble/foam/blob/main/LICENSE), not by this repository's terms.

## Per-file override

The split above is the default. **A single note may override it in its own YAML frontmatter** with a `license:` field, e.g.:

```yaml
license: CC-BY-NC-4.0
```

This exists for one reason in particular: some notes quote or closely paraphrase **archive-restricted or third-party copyrighted material** (primary sources under repository permissions, in-copyright secondary literature). Where a note reproduces such material, the quoted portion is *not* mine to relicense, and the note carries a narrower `license:` (or an explicit note in its body) accordingly. When in doubt, treat quoted matter inside a note as reserved to its original rights-holder and the surrounding analysis as CC BY 4.0.

## Attribution

For the prose, cite as:

> Michael Schiltz, *Clearing and Settling the Realm* working vault (HistorEE), CC BY 4.0, https://github.com/michaelschiltz/myfoamrepo

A machine-readable citation, including the released version and date, is in [`CITATION.cff`](./CITATION.cff) — GitHub renders it as the "Cite this repository" button.

## Note

This is a working research vault, not a finished publication. Notes carry explicit `status:` (`stub` / `seed` / `developed`) and preserve `verify` flags where a citation is unconfirmed. Cite accordingly: the presence of a claim here is a record of the argument's development, not a warranty of its final form.
