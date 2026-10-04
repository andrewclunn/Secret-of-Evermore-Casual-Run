# Pyramid return passage test

Based on v1.40. Removes only the rightmost of the two red square blocks in
the southeast lower-floor corridor, opening a permanent route beside the
remaining block. Both the artwork and collision are replaced with floor.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Pyramid_Return_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Pyramid_Return_Test.asm`.
Rebuild: `Build/build_pyramid_return_test.py <clean-USA-ROM>`.
SHA-256: `e7a8402086e4faf183e1a0e12fff0f396b4ef5c53e6e42509393a1faca280ccf`.

The four map $55 cells (105,65), (106,65), (105,66), (106,66) now use ordinary
floor records from the same columns in row 67. The map's existing raw grid
allocation is edited in place. The left block, stone bridges, gates, floor
symbols, axe-wall repairs, rescue sequence and all other events remain intact.

## Verification

- Verified clean-USA reconstruction of v1.40 before editing.
- Exactly four grid cells changed. The complete graphics/attribute table is
  unchanged; native decoding reproduces the intended grid exactly.
- Source audit reports zero overlapping writes and 3,002 valid text pointers.
- ROM differences are restricted to the four grid pointers and checksum.
- The ordinary source builder reproduces the test ROM exactly.
- Emulator comparison on two fresh native map loads: v1.40 blocks northward
  movement at y=1075; the test crosses the removed block's former position to
  y=921 and returns south to y=1096. Both direction checks pass on both loads.
- The rendered map confirms that the left block remains and the right-hand
  space is ordinary floor. Detailed edits and runtime results are retained in
  `Build/Pyramid_Return/`.

Leave and re-enter the lower Pyramid floor after loading this ROM. A savestate
already on that floor retains the previous decoded tiles until a fresh map load.
This remains a test build; the current release and default builder are v1.40.
