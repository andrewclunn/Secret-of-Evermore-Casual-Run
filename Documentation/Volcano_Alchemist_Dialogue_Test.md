# Volcano alchemist dialogue test

This cumulative test includes the preceding Blimp corrections.

- ROM: `Build/Secret_of_Evermore_Casual_Run_v1.35_Blimp_Volcano_Dialogue_Test.sfc`
- Source: `Build/Secret_of_Evermore_Casual_Run_v1.35_Blimp_Volcano_Dialogue_Test.asm`
- SHA-256: `49ced685b77b712c828489f931a18ed74599c0c41aeff58063e77bf95bdcc3c7`

The volcano alchemist's ordinary speech was already Generic NPC. Five explicit helper operands still selected `$07 Strong Heart`: `$D480C3`, `$D4810B`, `$D48171`, `$D48183`, and `$D4818D`. These now select `$03 Generic NPC`, covering all four native save-conversation calls and the post-save return path. Shared native save scripts and Strong Heart's actual dialogue are unchanged.

The Boy's introductory response, TEXT 511 at `$F82632`, is now “Huh?” instead of “Pardon me?”. It retains his `$04 Boy` caller, the authored final page boundary, its original pointer, and its 13-byte allocation, with zero padding after the new terminator.

Static verification passed for the four save callers, post-save theme, reply text and Boy routing, and a strict byte-difference check against the Blimp test. Only the five theme operands and TEXT 511's existing allocation differ before checksum recalculation; all Blimp changes are retained. The source audit validates all 3,002 primary pointers with no overlapping writes and exactly reproduces the supplied ROM.

In-game verification is pending: replay the introduction, then exercise saving and declining across the introduction/repeat branches, with and without a Mud Pepper. Confirm the offer and post-save return use Generic NPC and the Boy says “Huh?” in his own theme. Accepted v1.35 release artifacts remain unchanged.
