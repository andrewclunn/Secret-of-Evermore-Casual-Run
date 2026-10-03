# v1.36 dialogue QA release

Promoted at user request after the cumulative QA pass. The release is byte-identical to `Secret_of_Evermore_Casual_Run_v1.35_Dialogue_Window_Test.sfc`. The authoritative source is `Build/Secret_of_Evermore_Casual_Run_v1.36.asm`; the release patch is `Secret_of_Evermore_Casual_Run_v1.36.ips`. The default builder now uses v1.36. Earlier accepted v1.35 artifacts remain preserved. Generated ROMs are local build outputs and are excluded from Git.

## Changes

- Blimp: restored the space in “What a relief! That beast…” while preserving its pause; corrected the hut introduction, gift-search, dog greeting, and repeat/rest themes; assigned the Boy's mud-walls reply to his own theme; made the contextual save question start fresh after the rest choices. The shared cave question receives that page reset too.
- Volcano alchemist: five save/return helper operands now use Generic NPC instead of Strong Heart. The Boy's introductory “Pardon me?” is now “Huh?” in his existing theme.
- Fire Eyes volcano exchange: corrected the artificial twin's greeting and both closing remarks, and assigned “You called?” to Fire Eyes / Elizabeth. TEXT 575's speaker metadata now matches the actual speaker.
- Artificial Horace's Nobilia scene: four openers covering six lines now use his theme, including the opening “Indeed, Pompolonius!” and inherited continuation lines. Pompolonius and Carltron retain their themes.
- Default Generic NPC windows: X decreases from 4 to 3 and width increases from 24 to 26, expanding one column on each side while retaining the horizontal center. Vertical position, height, and styling are unchanged. Horizontal movement uses X in the event format.

The Crustacia amulet seller was confirmed working by checking the pots on the right side of the room. No vendor appearance fix is included.

Existing event lengths, branches, healing, save operations, and cutscene choreography are retained. TEXT 1858 reuses its existing 79-byte regional allocation at `$FB11DF`; its former shortened copy remains stored. TEXT 2407 grows from 86 to 87 bytes within its existing slot. The shorter TEXT 511 keeps its allocation and pointer, with zero padding after the terminator. There is no new WRAM or event relocation.

## Release verification

- Clean unheadered USA base: 3,145,728 bytes; SHA-256 `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`.
- Release ROM: 4,194,304 bytes; SHA-256 `a6ced1e7309222863ef61e02cb0a2887d7004b295ebce632fee70d8dcd1ea4d5`.
- Checksum/complement: `$57D8 / $A827`.
- Ten regression tests pass: Blimp spacing/pause and speaker routing; repeat/rest/save continuity and choice contract; a strict cumulative ROM-change allowlist; volcano save/reply checks; all 14 Fire Eyes exchange calls; all 13 Nobilia scene calls and continuation windows; centered NPC expansion; and exact IPS reproduction.
- The source audit validates all 3,002 primary text pointers, reports zero overlapping writes, and reproduces the release ROM exactly. Current layout reports were regenerated from v1.36.
- CSV report export now preserves the CSV writer’s line endings on Windows instead of introducing a second carriage return.
- IPS SHA-256: `254314260283c0b0a5e86cf2e3d4d300628decc482ac44cbe88845ac54b3aaf6`.
- Applying the release IPS to the verified clean base reproduces the release ROM byte for byte, including its four-MiB expansion. The promoted ROM also matches the accepted cumulative test byte for byte.

Reproduce these checks from the repository root:

```powershell
python Build/build.py BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.36.sfc --ips Secret_of_Evermore_Casual_Run_v1.36.ips
python Build/test_dialogue_qa.py BASE_ROM
python Build/script_layout.py audit BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.36.asm --baseline-rom Build/Secret_of_Evermore_Casual_Run_v1.36.sfc --report-prefix Documentation/Script_Layout_Current
```

The user's acceptance authorizes release promotion; it does not record exhaustive in-game testing of every optional rest/save branch or scene transition. The ongoing full-game QA pass remains active. Existing Bazooka gameplay coverage and unrelated outstanding issues remain tracked in `Bazooka_Charge_Test.md`.
