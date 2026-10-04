# Pyramid axe-wall test

Accepted by the user and promoted to v1.40 on October 4, 2026. See
`Documentation/Pyramid_Release_v1.40.md`; use the v1.40 source and release patch.

Includes the accepted v1.39 Pyramid door-symbol map test and dog separation fix.
This is a test build; the release and default builder remain v1.39.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.39_Pyramid_Axe_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.39_Pyramid_Axe_Test.asm`.
SHA-256: `dfeec1c24ef79cbc4111ba1007ffbd62a6314c0f28c6caa9ab567f633e515f9e`.

## Cause and fix

The user's latest savestate reproduces the problem at the lower western wall.
The Boy is the active character ($0F42=$4E89), and $235F contains the Bronze
Axe ID $0C. Nevertheless, the native `$08 $D7` character predicate skips the
wall-opening body. Replacing only that predicate with false makes the wall
open, isolating the failed condition. The event bytes themselves match the
clean ROM; the preceding visual update did not change them.

Six wall events now compare the entity attached to the triggering script
against the Boy explicitly. Non-Boy actors skip the original body. The exact
Bronze Axe check, wall states, sounds, animation operations and dog rescue
sequence remain. The events are copied to $F7F160–$F7F22B and their native
short-script pointers are repointed. The upper event's relative call becomes
an absolute call to the same native routine, with its weapon-failure branch
adjusted to skip the expanded call. No shared character predicate is changed.

| Wall event | Native event | Replacement |
|---|---|---|
| Lower western wall | $958AC5 | $F7F160 |
| Lower northern wall | $958AE2 | $F7F180 |
| Lower eastern wall | $958B45 | $F7F1A0 |
| Lower hidden wall | $958AFF | $F7F1C0 |
| Dog rescue wall | $958B17 | $F7F1DB |
| Upper hidden wall | $95984B | $F7F20C |

## Verification

- Clean-USA base validation and exact reconstruction of the accepted symbol
  build before patching. Final full-source rebuild reproduces the test ROM.
- Zero source overlaps; helper allocation is blank/unowned and outside text
  reserves; all 3,002 text pointers validate.
- ROM differences relative to the symbol build are restricted to six script
  pointers, the new event allocation, and the checksum.
- Independent SoEScriptDumper decoding confirms explicit script-actor guards,
  Bronze Axe checks, native object calls and correctly aligned branches.
- The user's actual lower western wall opens from the unchanged savestate
  using the test ROM. It fails with the preceding symbol ROM.
- Headless Snes9x tests all five lower walls with Boy + Bronze Axe, Boy + wrong
  weapon, and Dog + Bronze Axe ID: all fifteen checks pass. Test-only character
  teleports/weapon changes are made in emulator RAM, not in the ROM or saves.
- The rescue test opens the wall, sets the native reunion flag and restores
  availability through the retained event body.
- Upper-floor gameplay remains unverified: attempts with an older pre-axe
  snapshot did not invoke the target wall event. Its relocated bytecode and
  call/branch destinations are checked. Live two-player coverage also remains
  part of the ongoing QA playthrough.

Rebuild: `Build/build_pyramid_axe_test.py <clean-USA-ROM>`.
Use the same Pyramid savestate to retry the axe doorway. The accepted map
symbols are already included; no additional patch layering is needed.

Historical reports describe the same symptom with the two-player patch:
[Huge Grand Pyramid Glitch](https://gamefaqs.gamespot.com/boards/588645-secret-of-evermore/53086050).
That report supports the symptom history; the diagnosis above comes from the
local ROM and savestate tests.
