# Artificial Horace Nobilia scene theme test

The cumulative test is `Build/Secret_of_Evermore_Casual_Run_v1.35_Dialogue_QA_Test.sfc`, with matching `.asm` beside it. It retains all preceding Blimp, volcano alchemist, and Fire Eyes/twin corrections. Accepted v1.35 release artifacts remain unchanged.

Four explicit Generic NPC openers now select `$11 Artificial Horace`:

| Operand | Texts covered |
|---|---|
| `$D5D07F` | 1038 “Indeed, Pompolonius!” and continuation 1039 |
| `$D5D0C8` | 1042 |
| `$D5D289` | 1045 |
| `$D5D2AA` | 1047 and continuation 1048 |

Verification checked all 13 text calls in the exchange, including the inherited continuation windows. Pompolonius retains `$13`, Carltron retains `$0B`, and all six artificial Horace texts now use `$11`. A strict ROM comparison against the preceding cumulative test confirms only these four operands differ before checksum recalculation. Text payloads, pointers, event lengths, branches, cutscene timing, and all earlier fixes are retained.

The source audit validates all 3,002 primary pointers, reports no overlapping writes, and reproduces the delivered ROM exactly. SHA-256: `65b28687d4b893694c2c9c01475c15de276672e049e426e8b1e339557e75ed36`.

In-game verification remains pending. Replay the scene from before the first dialogue window opens, checking the twin's opening and later replies, his continuation pages, and transitions to Pompolonius and Carltron.
