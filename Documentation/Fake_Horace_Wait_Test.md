# Boy Y=18 and Diamond Eyes handover input waits

Restores the Boy dialogue helper's Y value to 18. Adds acknowledged endings
to all thirteen windowed conversation texts in the Diamond Eyes handover:
1538-1544 and 1547-1552. Both the previously-met-Horace and stranger branches
are covered, including the complete Lone Starr quote, fake Horace's reveal,
the Boy's response, and the guards' closing line.

The original wording and existing page breaks remain intact. Texts are copied
to blank, unowned space at $FA6100-$FA6458 and their existing pointer entries
are redirected. Each ends in $86,$00 (acknowledged page ending, then end of
text). Existing acknowledged endings are not duplicated. Reward banners
1545/1546 keep their native timed presentation.

The entire scene event $D6C113-$D6C2B6 is unchanged, preserving the Diamond
Eyes transfer, payment, actor movement, battle setup, speaker routing and
branching. Both Halls spear fixes, Mud Pepper cap 99, and pyramid return path
are retained. No change to the temporary status-display glitch is claimed.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Fake_Horace_Wait_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Fake_Horace_Wait_Test.asm`.
Rebuild: `Build/build_fake_horace_wait_test.py <clean-USA-ROM>`.
SHA-256: `e2675156f1e6b0015d613984d498320c7c1c64f662483dd5c7cabbc04e873c16`.

Verified reconstruction of the preceding build, restricted ROM differences,
all thirteen acknowledged endings, unchanged event bytes, blank/unowned
allocation, zero source overlaps and 3,002 text pointers. Gameplay verification
is pending: the available post-scene snapshot did not replay the handover in
the attempted emulator check. Replay from before the handover to validate it;
an already-running dialogue in a savestate retains its existing text pointer.

This remains a cumulative test build. Published/default release remains v1.40.
