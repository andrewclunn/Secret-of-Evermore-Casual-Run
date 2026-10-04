# Market exploration experiment 01

Based on the verified v1.36 release. This is a separate experiment, not a promoted release. The production ASM and ROM are unchanged.

ROM: `Build/Market_Experiment/Secret_of_Evermore_Casual_Run_v1.36_Market_Experiment_01.sfc`

Matching full ASM: `Build/Market_Experiment/Secret_of_Evermore_Casual_Run_v1.36_Market_Experiment_01.asm`

## Four tests

The comparison image labels the affected pots. Coordinates below are zero-based 16-pixel map cells.

| Label | Location | Intended appearance | Intended movement |
|---|---|---|---|
| A | Requested pot immediately right of the Boy in the screenshot, beside the lower birdcage; x=26, y=60–61 | Pot replaced by pavement | Boy and Dog can pass through |
| B | Upper of the two pots just right of the green-shirted merchant's stall; x=31, y=55–56 | Pot replaced by pavement | Original collision remains; an invisible obstruction is expected |
| C | Lower of those two pots; x=31, y=57–58 | Pot remains visible | Floor attributes replace its original attributes; passing through is expected |
| D | Pot just left of the same merchant's stall; x=25, y=54–55 | Pot replaced by pavement | Boy and Dog can pass through |

B and C deliberately separate graphics from collision. They are diagnostic controls, not proposed final gameplay changes. Floor attributes include other map flags, so watch for changes in character layering or interaction behavior as well as movement.

![Original and experimental map crop](../Build/Market_Experiment/market_comparison.png)

## Testing

1. Use a copy of your regular battery save with the experimental ROM. The different ROM filename may require copying/renaming the save so your emulator recognizes it.
2. Enter the market from another room. If you load a save state already inside the market, leave and re-enter before judging the changes: the state can contain the original decoded map in memory.
3. Check A, B, C and D with the Boy, then with the Dog. Try crossing each spot from multiple directions, including the diagonal gaps near the stall and cage.
4. Talk to the merchant and nearby vendors; check the surrounding baskets and cage for unintended changes. Leave and re-enter once more to check persistence. If the market scene changes later in the story, check the spots then too.

Useful feedback: which labels disappeared, which locations you could cross, whether the Dog followed, and any invisible walls, graphical seams, layering changes, altered interactions, freezes or room-entry failures. A screenshot is useful for anything unexpected.

## Implementation and verification

### User runtime results — October 3, 2026

The user tested the experimental ROM and supplied an in-game screenshot:

- A and D appear completely removed. Passage through both locations was not explicitly reported.
- B appears removed but still blocks access, matching the graphics-only control.
- C remains visible but can be walked through, matching the collision-only control.

These observations confirm that the relocated market loads and that the appearance and movement changes for B/C behave independently as intended. Full removal should use the combined floor replacement applied to A/D. Dog traversal, merchant interactions, repeat entry and later story variants remain unreported. No production changes or release promotion were made from this feedback.

The market is map $0A. Its native record begins at ROM offset $1FAAEB. Its decoded grid contains 48 × 76 cells (7,296 bytes). Each grid pointer selects an eight-byte runtime record containing the two background-layer tile words and tile attributes. The original compressed attribute/graphics table contains 1,807 records.

The experiment copies the room into previously zero-filled, source-unowned $FC0000–$FC4F62, outside every declared text arena, and repoints only map $0A at CPU address $DFFE0F. The copied record replaces the compressed grid and tile table with the game's supported raw compression mode 0. B and C use four appended records, preserving every original table entry and index. A and D reuse existing floor records. Eight grid cells change in total. The room header, palette list, graphics list, dynamic tile definitions, event lists, and remaining room data are copied unchanged. Native CPU code is not hooked or changed.

The earlier withdrawn experiment instead modified the screen-drawing routine and used a fixed replacement pointer for x=31, y=55–58. It did not target the pot requested here. This experiment does not restore that hook.

Completed checks:

- Verified the input ROM against the accepted v1.36 SHA-256.
- Decoded original grid, graphics list and tile table with a bounded interpreter of the game's decompression routines; every grid pointer falls within the original table.
- Reconstructed the original map visually and matched the screenshot location.
- Verified both relocated raw streams through the same native decompression interpreter, with exact output equality.
- Rebuilt the experimental ROM from the full ASM using the provided v1.36 ROM as the initial image; checked source ownership without overlaps and validated all 3,002 primary text pointers.
- Checked that ROM differences are confined to the new room allocation, the market pointer and checksum; all eight intended cells and original table records were checked.
- Rendered the experimental map and confirmed that A, B and D disappear while C remains visible. The render is a static reconstruction, not an emulator screenshot, and excludes moving actors.

The user's emulator test confirms room entry and the intended B/C appearance/collision behavior; the remaining gameplay checks are listed above. The new allocation's ownership and text targets were checked; unknown indirect engine dependencies remain an experimental risk. A clean base ROM is not in this workspace, so a clean-ROM rebuild was not performed. The full ASM can be used with the normal build script and the clean U.S. base ROM.

ROM size: 4,194,304 bytes. Checksum/complement: `$2A6B / $D594`.

Experimental SHA-256: `2ba8cec7ba2939b53a2e4cd64b60173fda64002891d2a497cf6c5a1e1062e3ab`

Research references: [black-sliver's native room-table decoder](https://github.com/black-sliver/SoEScriptDumper), [background graphics compression notes](https://github.com/black-sliver/soe-tools/blob/master/background-tile-compression.txt), and [darkmoon2321's map-format research](https://gamefaqs.gamespot.com/boards/588645-secret-of-evermore/73461986?page=9). The ROM decoding and experiment generation were performed locally against this project's baseline.
