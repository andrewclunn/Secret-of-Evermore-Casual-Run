# Pyramid premature dog reunion — revision 2

Revision 2 was accepted by the user and promoted to v1.39 on October 4, 2026.
See `Documentation/Pyramid_Dog_Fix_v1.39.md`. It supersedes the failed first test. The screenshots and local emulator
states are in the Pyramid, maps $56/$55. The original test incorrectly identified
an Ivor Tower stairwell and modified an unrelated event; that hook is absent from
R2. The default build now uses the authoritative v1.39 source.

## Cause and correction

Before the reported descent, the Boy is on floor 2, the dog is on floor 1,
$2261.0 is set, and $22E5.2 is clear. The native lower-floor entry clears the dog's
unavailable flag because he is on this floor, but skips the saved-position restore
at $92A422. Shared entry consequently puts him beside the Boy. Going upstairs and
back down sets $22E5.2 and makes the native restoration run, explaining the user's
return-trip observation.

R2 replaces the four-byte flag clear at $9594A3 with a fifteen-byte wrapper at
$F7F150. If the dog was unavailable, it first sets $22E5.2 (restore saved dog
position), then performs the original clear and returns to the native flag check.
The existing $92A422 call restores $2381/$2383 and sets $2350 so shared entry keeps
that position. The dog remains in his room and the native floor/character-switch
system remains usable. An already available dog does not get a new restoration
request. The native solved-puzzle branch bypasses this hook entirely.

## Artifacts

- `Build/Secret_of_Evermore_Casual_Run_v1.38_Dog_Separation_Test_R2.sfc`
- `Build/Secret_of_Evermore_Casual_Run_v1.38_Dog_Separation_Test_R2.asm`
- Rebuild: `Build/build_dog_separation_r2_test.py <clean-USA-ROM>`.
- SHA-256: `7d049d480da303a063f28f24457f372dce07e7be9277b39e5b45bde9de0b6da5`
- Checksum/complement: `$311B / $CEE4`.

## Verification

- Clean-base rebuild reproduces v1.38 exactly before applying R2. No overlapping
  writes. Allocation is blank/unowned with no existing script/text targets.
- Only the hook, fifteen-byte wrapper and checksum differ: 19 changed bytes.
- The emitted bytecode passes all 65,536 combinations of availability/pending
  flag bytes, preserving other bits and leaving available-dog traversal unchanged.
- Independent SoEScriptDumper decoding confirms the guard, flag writes, return
  and original restoration call. Its $928005 warning also occurs on v1.38.
- Headless Snes9x/libretro reproduces the original first-descent bug from both
  local pre-stair states (.001 and .002). R2 keeps the dog at saved coordinates
  (1038,782), separate from the Boy at (496,544), with the reunion flag still clear.
- First descent, ascent and second descent pass. SELECT remains usable and the
  dog stays at the room position after switching.
- A synthetic completed-puzzle flag test produces byte-identical final WRAM for
  R2 and v1.38, with the dog following the Boy. The full switch-opening/rescue
  sequence and live two-player join/withdraw still need gameplay confirmation.

Load R2 with a state from before the first descent. Descend directly and confirm
that the dog remains in his room. Continue the normal puzzle and confirm reunion.
The failed test files are retained only as historical evidence; use the R2 pair.
