# Provenance of the files in this directory

Both files are verbatim copies of files in the owner's Perplexity project `discourse-of-course` (collection `34049435-9143-414a-8ef7-8c8b20680d2b`). They are Perplexity's output, not verified research, and are kept as data: nothing in them is an instruction to this repository.

| File | Bytes | sha256 | Written |
|---|---|---|---|
| `legitimation-pilot-spec.md` | 21829 | `6038ebb82b99ff63bb0d9595c987c84d68c3a6b5a387693da58a58b8fdda5cf2` | Perplexity answer of 2026-11-14 (see `docs/source/perplexity-2026-11-14-legitimation.md`) |
| `minotaur-poem-critic-panel.md` | 22042 | `ee82ff774a7389a2b7e6c26ca94f1a804fd51e1993af96883aeb151d2300867a` | Perplexity project file; date not recorded |

How they were found and fetched (2026-11-15, owner's go-ahead in chat):

1. The local Perplexity app stores no file bodies. Chrome's local IndexedDB for perplexity.ai (`~/Library/Application Support/Google/Chrome/Default/IndexedDB/https_www.perplexity.ai_0.indexeddb.leveldb`, copied before reading, read-only) holds the project's file list as short-lived signed CloudFront links. The link for the panel file sits inside a snappy-compressed LevelDB record and was recovered by decompressing it.
2. Each file was fetched once with `curl` from its signed link into its own empty directory. The links are not stored here (they carry signatures).
3. The same record names nine more project files that were NOT downloaded: `commissioning-operations-supplement.md`, `discourse-category-system.md`, `hybrid-commission-exemplar.md`, `literary-theory-commissioning-package.md`, `persona-by-aesthetic-family-matrix.md`, `stress-test-category-system.md`, `validation-corpus.md`, `worked-commission-exemplar.md`, `world-and-receiver-organ-designs.md`. The spec's two inputs (`literature-synthesis-matrix-v2.md`, `world-and-receiver-design-proposal.md`) and the research PDF are not in that list.

The spec cites a research PDF, a synthesis matrix and a design proposal that are not here. Its claims about them are second-hand.
