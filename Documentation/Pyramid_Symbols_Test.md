# Pyramid door symbols — visual test

Accepted by the user and included in v1.40 on October 4, 2026, together with
the axe-wall repair. See `Documentation/Pyramid_Release_v1.40.md`.

Based on the accepted v1.39 release. This test copies each original 32×32 gold
switch symbol to the floor directly in front of the gate that switch opens.
The added symbols are passive artwork. No event, trigger, collision, switch,
door state, dog separation, character switching, or reunion logic is changed.

Test ROM: `Build/Secret_of_Evermore_Casual_Run_v1.39_Pyramid_Symbols_Test.sfc`.
Full source: `Build/Secret_of_Evermore_Casual_Run_v1.39_Pyramid_Symbols_Test.asm`.
The accepted release and default builder remain v1.39 until gameplay acceptance.

## Pairings

Coordinates here are 16-pixel cells relative to the map graphics origin.
Native trigger coordinates include the map's (6,13) origin offset.

| Symbol | Original cells (top left) | Gate marker cells (top left) | Door object | Native switch event |
|---|---|---|---|---|
| Eye | (64,36) | (24,39) | 0 | $958EBA |
| Scarab | (64,47) | (36,57) | 1 | $958F54 |
| Ankh | (77,36) | (54,57) | 2 | $958F07 |
| Barred symbol | (77,47) | (112,67) | 3 | $958FA1 |

The native events establish these pairings through their calls to door object
state routines. Only map $55 is changed. Each marker copies the source's two
graphics planes and retains every bit of the destination cell's attributes.

## Build and validation

- Verified clean USA ROM build reproduces v1.39 before applying the change.
- New ROM SHA-256:
  `8e4a97bcaba5df9e4e9aac2b082c3eaa140bf33e0753dff538c1bce2fb1bd3d3`.
- Sixteen visual cells changed; all 8,760 map-cell attribute words remain equal.
- Original table records, palettes, animation data, dynamic objects, initial
  object states, trigger lists, and trailing map data are preserved.
- Map data copied to blank, unowned $F01000–$F0FBE0, outside text reserves.
  Native mode-0 streams decode to the exact intended grid and graphics table.
- Full source rebuild, zero overlapping source writes, 3,002 validated text
  pointers, and restricted ROM differences pass. Differences are confined to
  the map pointer, new map allocation, and checksum.
- Headless Snes9x loads the new map through the native stair transition. All
  four markers were visually inspected in emulator captures. The dog remains
  separated at his saved position after descent. Test character teleports were
  applied only to the emulator's memory to inspect distant gates, not the ROM.
- Complete switch-opening/rescue sequence awaits the user's ongoing playthrough.

Rebuild with `Build/Pyramid_Symbols/build_symbols.py <clean-USA-ROM>` using
Python with Pillow. Or use `Build/build.py <clean-USA-ROM> <output-ROM>` with
`--source Build/Secret_of_Evermore_Casual_Run_v1.39_Pyramid_Symbols_Test.asm`.

Load the test ROM, then leave and re-enter the lower Pyramid floor. An existing
savestate on that floor retains its old decoded tiles until the map reloads.

Preview: `Build/Pyramid_Symbols/door_markers_preview.png`.
Detailed cell verification: `Build/Pyramid_Symbols/verification.json`.
