# Boy axe-reply theme

Based on v1.41. TEXT 0564, "I hit it with my axe!", now uses the Boy's shared
theme ($04) instead of Generic NPC ($03). The event helper operand at $D4A6D7
changes from $03 to $04. Its speaker metadata is corrected to Boy.

The preceding alchemist question and following "So you did!" response retain
the alchemist's theme. No wording, timing, rewards, or event branching changes.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.41_Axe_Dialogue_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.41_Axe_Dialogue_Test.asm`.
Rebuild: `Build/build_axe_dialogue_theme_test.py <clean-USA-ROM>`.

Verified exact opener/display operands for both speakers, a ROM diff restricted
to one theme byte and checksum, zero source overlaps, and 3,002 text pointers.
Gameplay verification is pending. Replay the conversation from before the
Boy's response. Published/default release remains v1.41.
