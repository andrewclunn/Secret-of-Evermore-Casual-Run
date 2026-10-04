# Fire Eyes volcano exchange theme test

The cumulative test is `Build/Secret_of_Evermore_Casual_Run_v1.35_Prehistoria_Dialogue_Test.sfc`, with the matching `.asm` beside it. It includes the preceding Blimp and volcano-alchemist corrections. Accepted v1.35 release artifacts remain unchanged.

Four Generic NPC helper operands were corrected:

| Text | Speaker | Operand address | Theme |
|---|---|---|---|
| 573 “Hello, Kiddo!” | Artificial Fire Eyes | `$D4B4ED` | `$10` |
| 575 “You called?” | Fire Eyes / Elizabeth | `$D4B527` | `$0D` |
| 585 “Let's see how she fares…” | Artificial Fire Eyes | `$D4B840` | `$10` |
| 586 “So long, Sis!” | Artificial Fire Eyes | `$D4B890` | `$10` |

TEXT 575's metadata incorrectly described the artificial twin. It now identifies Fire Eyes / Elizabeth, matching the scene's speaker and `$0D` theme. Other theme assignments in this exchange already select the intended speakers.

Static verification checked every framed opener and following text call for TEXT 573–586, including the Boy's response, Fire Eyes' interjections, and the artificial twin's speeches before and after the fight. All 14 calls select the correct theme. A strict comparison against the preceding cumulative build confirms exactly four ROM data bytes change before checksum recalculation. Dialogue text, pointers, event lengths, branches, combat choreography, and all preceding fixes are retained.

The source audit validates all 3,002 primary text pointers, with no overlapping writes, and reproduces the delivered ROM exactly. SHA-256: `baace9dcbfda14fcb763598ffbd4659b03e037d2a40c1ded6a4fa5eab05751f8`.

In-game verification remains pending. Replay from before the artificial twin's greeting; check the Boy's reply, Fire Eyes' offscreen “You called?”, the full exchange, and both post-fight closing remarks. Static routing checks do not establish the rendered theme appearance.
