# Mud Pepper loot cap test

Based on v1.40 with the pyramid return-passage update included. Mud Pepper
loot now uses the normal ingredient maximum of 99 instead of the original
special maximum of one. Two-ingredient drops retain their existing quantity.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Mud_Pepper_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Mud_Pepper_Test.asm`.
Rebuild: `Build/build_mud_pepper_test.py <clean-USA-ROM>`.
SHA-256: `18c18bb7abac6a1e648b74546412e1a9a715e6280406800a643c3d1eb613a9d8`.

The native item dispatch at $D2AA2F remains intact. Its Mud Pepper branch now
calls a 34-byte helper at $F7F300, then resumes at $D2AB86. The helper preserves
the original inventory update and loot-success flag bytes exactly. Only the
maximum in the comparison changes: inventory plus extra quantity must be less
than 99 before awarding one plus extra quantity.

Verification:

- Clean-ROM reconstruction exactly matches the preceding pyramid return test.
- Helper allocation is blank and unowned in that build.
- No overlapping source writes; all 3,002 text pointers validate.
- Differences from the preceding test are restricted to the seven-byte dispatch,
  helper allocation, and checksum.
- Native script decoding confirms the cap comparison, award expression,
  success flag, return, and continuation target.
- Boundary evaluation: a two-pepper drop takes 0 to 2, 50 to 52, and 97 to 99;
  inventories of 98 and 99 reject it without changing the inventory. A single
  pepper takes 98 to 99.
- Live enemy-drop gameplay remains to be checked. The available saved-game
  snapshots did not trigger the temporary event harness used for emulator QA.

This is a test build. The published release and default builder remain v1.40.
