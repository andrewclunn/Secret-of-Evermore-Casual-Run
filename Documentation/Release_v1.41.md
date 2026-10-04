# Casual Run v1.41

Promoted October 4, 2026 at the user's request. The release is byte-identical
to `Secret_of_Evermore_Casual_Run_v1.40_Fake_Horace_Exit_Test.sfc`.

## Changes since v1.40

- Removes the rightmost red block in the lower Pyramid corridor, including
  collision, allowing the player to return through that passage.
- Raises the Mud Pepper loot maximum from one to 99, allowing the existing
  two-ingredient drop quantity to work.
- Repairs dialogue edits that damaged the automatic spear-throw branches in
  both the main Halls room and the northeast room.
- Keeps the Boy's dialogue window at Y=18 after the positioning trials.
- Adds input waits throughout the fake Horace Diamond Eyes handover.
- Uses Artificial Horace's theme throughout that exchange and reveal.
- Moves "Well, here are your Diamond Eyes, good sir" immediately after the
  exchange in the never-met-Horace branch.
- Gives the never-met-Horace branch the requested closing response:
  "Another happy client, who I'm sure isn't about to betray us."
  followed by a page break and "Come on [dog's current name], let's go to
  that fine drinking establishment at a leisurely pace."
- Retains the familiar-Horace closing response only in the met-Horace branch.

All v1.40 features and earlier fixes are retained.

## Release artifacts

- Source: `Build/Secret_of_Evermore_Casual_Run_v1.41.asm`.
- ROM: `Build/Secret_of_Evermore_Casual_Run_v1.41.sfc` (4,194,304 bytes).
- Cumulative patch: `Secret_of_Evermore_Casual_Run_v1.41.ips`.
- Base: clean unheadered USA ROM (3,145,728 bytes), SHA-256
  `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`.
- ROM SHA-256:
  `1102b85b9e46c883d36b126aab0b407f035e86c94d73859016dfb8c533357fb2`.
- IPS SHA-256:
  `6497654fa84489a6fd377397bb07183188940b3faf0a9f8fa5c887244ea60248`.
- Checksum/complement: `$757D / $8A82`.

The default builder and README now point to v1.41. Earlier versions remain
available. Reproduce promotion with `Build/promote_v141.py <clean-USA-ROM>`
before changing the default builder beyond this version.

## Verification and coverage

Clean-USA source reconstruction and independent cumulative IPS application
both exactly reproduce the accepted test ROM. Source auditing reports zero
overlapping writes and validates all 3,002 primary text pointers. The extra
branch-specific response pointer at $D1FFD9 is separately validated against
its raw string at $FA605E. Current audit reports are in
`Documentation/Script_Layout_Current.json` and `.md`.

Native emulator comparisons verified the Pyramid return passage and the
northeast Halls automatic spear throw. Dialogue and loot follow-ups were
checked through source/ROM comparisons, native event decoding, pointer and
payload validation, and user gameplay feedback during the test iterations.
The final branch-specific closing response was accepted for release without
an additional emulator replay. No fix for the occasional temporary status
display glitch is claimed; moving the Boy window did not resolve it.

Detailed development evidence remains in `Documentation/Pyramid_Return_Test.md`,
`Mud_Pepper_Test.md`, `Spear_Switch_R2_Test.md`, `Fake_Horace_Wait_Test.md`,
`Fake_Horace_Exchange_Test.md`, and `Fake_Horace_Exit_Test.md`.
