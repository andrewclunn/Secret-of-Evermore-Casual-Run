# Boy dialogue position test

Moves the shared Boy dialogue helper ($04) upward by one Y interval:
Y=$12 (18) becomes Y=$11 (17) at $F7E91A. X/style=$84, width=$1E,
height=$06, text and event behavior remain unchanged.

Based on the spear switch test, retaining the spear throw fix, Mud Pepper
loot cap of 99, and pyramid return passage.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Boy_Dialogue_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Boy_Dialogue_Test.asm`.
Rebuild: `Build/build_boy_dialogue_position_test.py <clean-USA-ROM>`.

Verified the complete before/after helper geometry. Differences from the
previous test ROM are restricted to the Y operand and checksum. Source
audit reports zero overlapping writes and validates 3,002 text pointers.

Open a new Boy dialogue window to see the change. A window already open in
a savestate retains its old position until reopened. Visual gameplay
verification remains pending. Published/default release remains v1.40.
