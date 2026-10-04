# Northeast Halls spear switch and Boy Y=16

This cumulative test includes all recent changes, moves Boy helper $04 Y from
17 to 16, and restores the northeast Halls spear branch at $D79E66 from 4 to
15. The previous spear correction repaired the main room ($D7940A), but the
reported screenshot was the northeast room, which has an independent event.
Both jumps had been mistaken for dialogue-theme arguments.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Spear_Switch_R2_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Spear_Switch_R2_Test.asm`.
Rebuild: `Build/build_spear_switch_r2_test.py <clean-USA-ROM>`.
SHA-256: `0465fca523f4b95162a2190364caa4867887d07f2e929bb7b6907d5813bd41ee`.

Verification:

- Relative to the Boy-dialogue test, only $D79E66, $F7E91A, and checksum change.
- Restored branch displacement matches clean USA ROM and targets $D79E77.
- Zero overlapping source writes and 3,002 valid text pointers.
- Native emulator comparison using the player's October 4 .000 snapshot:
  Bronze Spear is actually equipped ($235F=$14, $2360=$04), map=$2D.
  Approach the northeast switch from x=232,y=560 by walking south ten frames.
  Skip only the first-visit camera pan using its existing seen flag.
  Previous build leaves bridge flag $2834.3 clear; R2 sets it after the native
  throw sequence and completes the bridge animation. No weapon or script
  instruction pointer is injected. Both runs use the same initial snapshot.
- Results/screenshots retained in `Build/Halls_Spear/`; runtime probe is
  `Build/verify_spear_switch_r2.py`.

Open a new Boy dialogue window to apply Y=16. Published/default release is
still v1.40; this is a cumulative test build.
