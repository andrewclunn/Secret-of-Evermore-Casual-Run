# Blimp dialogue test

Test ROM: `Build/Secret_of_Evermore_Casual_Run_v1.35_Blimp_Dialogue_Test.sfc`.
Matching source: `Build/Secret_of_Evermore_Casual_Run_v1.35_Blimp_Dialogue_Test.asm`.
The accepted v1.35 source and release IPS are unchanged.

## Corrections

- Image 1: TEXT 1858 now reads “What a relief! That beast…” with its original pause preserved. Its pointer returns to its existing 79-byte regional allocation at `$FB11DF`, with the former inline clear control replaced by a space. The shortened `$F46662` copy remains retained.
- Image 2: the Boy's “Well, if you like mud walls…” reply (TEXT 832) uses `$04 Boy`.
- Images 3–4: Blimp's hut introduction and gift-search lines (TEXT 831, 833–838) use `$06 Blimp` throughout. The Mud Pepper explanation already inherited that theme. Item receipt announcements retain System presentation.
- Image 5: dog greeting and repeat/rest dialogue use Blimp's theme. The contextual save question (TEXT 2407) starts with `$96 $87`, matching Cecil's existing fresh-question prefix, so it clears the preceding rest choices. The shared cave save question also receives this page reset.

No event instructions were inserted or relocated. All ten changed theme operands keep their original instruction lengths. Private hut/cave save scripts, branches, choice indices, healing, and native save operations are unchanged. TEXT 2407 grows from 86 to 87 bytes within its existing slot; the next allocation starts at `$F40280`.

## Verification

- Clean USA base SHA-256 verified by the builder.
- Five static regression checks pass (`Build/test_blimp_dialogue.py BASE_ROM`): relief spacing/pause, actual speaker callsites, repeat/rest theme continuity, fresh save choices/native contract, and a strict ROM-change allowlist.
- Source audit validates all 3,002 primary text pointers and reports no overlapping writes. Rebuilt source matches the delivered test ROM byte for byte.
- ROM size: 4,194,304 bytes.
- ROM SHA-256: `b132ad53271b7dcadb53ca4aa6daeaaaecba6c4017a0db761d0bdb97afe5248a`.

## In-game checks still needed

Replay from before the Blimp rescue/hut cutscene to exercise the newly corrected speaker transitions. Check the full gift-search sequence and both Mud Pepper explanation branches. Afterward, talk to Blimp with both the Boy and Dog, with and without a Mud Pepper. For the rest prompt, exercise both Sure and No thanks, followed by both save responses; confirm each question has its own clean page and remains in Blimp's theme. Also check the post-rest acknowledgement and cave save prompt.

Static checks do not establish emulator wrapping, window cleanup, or runtime theme appearance. This test has not been promoted to a release.
