# Tiny introduction dialogue test

Test ROM: `Build/Secret_of_Evermore_Casual_Run_v1.37_Tiny_Dialogue_Test.sfc`.
Matching source: `Build/Secret_of_Evermore_Casual_Run_v1.37_Tiny_Dialogue_Test.asm`.

The screenshot's “to Nobody lifts my rock but me!” comes from a misidentified theme operand at CPU `$D5C6B7`. The actual instructions are `A3 14` (Tiny's theme), then `51 A3 0B` (display TEXT 993). The earlier edit changed the high byte of that text operand to `$14`, selecting TEXT 1761 instead. That entry points to the fragment `to ` at `$FB0737`. The subsequent `51 A6 0B` correctly displays TEXT 994, appending “Nobody lifts my rock but me!” after the fragment.

The test restores only `$D5C6B7` from `$14` to `$0B`, plus the ROM checksum. Tiny's actual theme helper remains `$14`. Both dialogue payloads, text pointers, pauses, and event lengths are unchanged. The v1.37 release artifacts remain preserved; this test is not promoted.

Verification passed: correct theme and TEXT 993/994 event operands, exact payloads, all 3,002 primary text pointers, zero overlapping source writes, exact source reproduction against the local verified baseline, and a strict diff limited to one event byte and two checksum bytes.

ROM SHA-256: `24b47b44e01d090ced097b917ce7d2b27fc538d6fe2b2fe789f9cbc3ec899319`.
Checksum/complement: `$2608 / $D9F7`.

A clean base ROM is unavailable locally, so clean-base reconstruction was not performed. In-game confirmation remains pending: replay Tiny's first conversation from before the introduction and confirm “I am Tiny the Barbarian. I am the strongest creature alive.” appears before the rock line, with no stray “to ” and with Tiny's theme intact. Prefer an in-game save from before the conversation; a mid-dialogue emulator state can retain old text state.

Reproduce the local build and verification with `Build/build_tiny_dialogue_test.py`.
