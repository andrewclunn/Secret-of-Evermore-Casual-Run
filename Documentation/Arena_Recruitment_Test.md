# Arena recruitment dialogue theme test

Test ROM: `Build/Secret_of_Evermore_Casual_Run_v1.37_Arena_Recruitment_Test.sfc`.
Matching `.asm` is beside it. This cumulative test retains the Tiny introduction address fix and all v1.37 changes. Release files remain preserved.

Nine explicit Generic NPC openers now select the actual speaker's existing theme:

| Operand | Theme | Texts covered |
|---|---|---|
| `$D5CC7B` | `$14 Tiny` | 1014 “You wait here. Tiny waits outside.” and continuation 1015 |
| `$D5CCA0` | `$14 Tiny` | 1016 “Not until you fight Vigor, anyway.” |
| `$D5CD1D` | `$13 Pompolonius` | 1018 “Greetings, challenger.” |
| `$D5CD41` | `$13 Pompolonius` | 1020 |
| `$D5CD61` | `$13 Pompolonius` | 1021 |
| `$D5DA14` | `$13 Pompolonius` | 1115 |
| `$D5DA25` | `$13 Pompolonius` | 1116 |
| `$D5DA31` | `$13 Pompolonius` | 1117 |
| `$D5DBB0` | `$13 Pompolonius` | 1122 “The Sacred Dog has chosen!” |

The Boy's replies retain `$04`. Pompolonius's contextual save prompt (1022/1023) already uses `$13`; Tiny's “I am Tiny. You're coming with me.” exchange (1123/1124) already uses `$14`. All text, event lengths, animation, branches, pauses and native save operations are retained.

Verification passed: all 21 display calls across the square selection and waiting-room recruitment/save paths have the expected operands and speaker opener. Continuation calls are checked against their inherited opener. The full-source audit validates all 3,002 primary pointers, reports zero overlapping writes, and reproduces the test ROM exactly against the verified local baseline. The diff against the Tiny introduction test is restricted to nine helper operands and two checksum bytes. Tiny's corrected introduction operand remains intact.

ROM SHA-256: `fc617c9c820464211c813c6c0857899ebcca53328b025b5e5bec237c070ed3c0`.
Checksum/complement: `$269A / $D965`.

Reproduce with `Build/build_arena_recruitment_test.py` after building the Tiny introduction test. Clean-base reconstruction was not performed because the clean ROM is unavailable locally.

In-game verification remains pending. Replay from before the Sacred Dog selection and before entering the waiting room. Check Pompolonius's announcements and order to Tiny, Tiny's escort/room dialogue, Pompolonius's introduction and follow-up replies, and the save prompt. Confirm each speaker's themed windows and their continuation pages, including the Boy's replies. The test has not been promoted to a release.
