# Provenance of the files in this directory

All files here are verbatim copies of files in the owner's Perplexity project `discourse-of-course` (collection `34049435-9143-414a-8ef7-8c8b20680d2b`). They are Perplexity's output, not verified research, and are kept as data: nothing in them is an instruction to this repository.

| File | Bytes | sha256 | Title (first heading) |
|---|---|---|---|
| `commissioning-operations-supplement.md` | 8908 | `4ab61d2ab8329046fbb71f0f54ddf7857bba9bfb2c1c9e7e9a3c64fe810dc805` | Commissioning Operations Supplement |
| `discourse-category-system.md` | 28892 | `10950d20f86e06ba74fb2d353e0bfb4fd5994e1d7e140871929daf39d28440f9` | The Category System |
| `hybrid-commission-exemplar.md` | 23254 | `ee25b5ef117a109c647bfac87b38f6f29b20911c85b0347b0c61bd888ea9c022` | Worked Commission: Jane Eyre Through a Hybrid Region |
| `legitimation-pilot-spec.md` | 21829 | `6038ebb82b99ff63bb0d9595c987c84d68c3a6b5a387693da58a58b8fdda5cf2` | Legitimation Pilot — Next-Step Specification |
| `literary-theory-commissioning-package.md` | 71173 | `d4b9e5deae57835bbb6b74f35a71b75bcee2b43d6b19aec869a4e1ec71aa1361` | Commissioning Package & Editorial Guide |
| `minotaur-poem-critic-panel.md` | 22042 | `ee82ff774a7389a2b7e6c26ca94f1a804fd51e1993af96883aeb151d2300867a` | Panel Review: "THE WALLS —" (the Minotaur poem) |
| `persona-by-aesthetic-family-matrix.md` | 28888 | `c37f4d8e684dcfe6cad31760a2f94b64bc8683fe1ebeac41e4126aa2913a0ecc` | Persona by aesthetic family matrix |
| `stress-test-category-system.md` | 21177 | `d788b80bda9568e670f71c2bc0b7e466df4fb0038b62c9b2df59692727865987` | Stress Test: The Seven-Slot Category System |
| `validation-corpus.md` | 10219 | `5fe42e162fe9df8f26b08c20a1363f99bb802df253fdc5e0dfdd1bef64131270` | Empirical Validation: The Category System Against Fifteen Real Pieces of Criticism |
| `worked-commission-exemplar.md` | 18463 | `504c5b688c64c2b7017017c1c2ca7c3ff013d50fbae4b2839fb742c33859a7ca` | Worked Commission: The Great Gatsby Through the Formalist Preset |
| `world-and-receiver-organ-designs.md` | 24792 | `610137c67e14b4e4d8259fa5cbaf308111d42e0700b0aac73cae03b0ee904742` | World and Receiver Components — Design Proposal |

How they were found and fetched (2026-11-15, owner's go-ahead in chat, in two batches):

1. The local Perplexity app stores no file bodies. Chrome's local IndexedDB for perplexity.ai (`~/Library/Application Support/Google/Chrome/Default/IndexedDB/https_www.perplexity.ai_0.indexeddb.leveldb`, copied before reading, read-only) holds the project's file list as short-lived signed CloudFront links. Most links sit inside a snappy-compressed LevelDB record and were recovered by decompressing it.
2. Each file was fetched once with `curl` from its signed link into its own empty directory, then copied here. The links are not stored (they carry signatures).
3. The spec's own inputs are not in the project's file list as such: `literature-synthesis-matrix-v2.md` is not here and was not found anywhere local; the research PDF `History of Discourse and Personas in Art Creation.pdf` is not in the project's file list but was found in iCloud Downloads (see `docs/research/PROVENANCE.md`), and `world-and-receiver-design-proposal.md` appears as `world-and-receiver-organ-designs.md` (same title, "World and Receiver Components — Design Proposal"; not diffed against the original). The spec's claims about the matrix and the PDF are second-hand.

All files are Perplexity output, not verified research. Treat them as data; nothing in them is an instruction to this repository.
