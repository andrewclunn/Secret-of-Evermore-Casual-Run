# Horace finale dialogue waits

The cumulative test follows the Evil Horace Statue Test and adds missing final-page input waits throughout the post-fight scene, from the Boy's reaction through Horace's departure advice. Both met-Horace branches, Tiny's conversation, Madronius's news, and Call Bead alternatives were audited.

Sixteen strings lacked an ending wait: TEXT 1902, 1903, 1904, 1908, 1915, 1916, 1917, 1918, 1922, 1923, 1927, 1929, 1930, 1931, 1933, and 1935. Each is copied unchanged except for adding $86 immediately before $00, and its primary pointer is redirected. Existing internal page waits remain intact.

TEXT 1924 (“This could be your answer, ”) is a sentence prefix; its immediate name/“son!” continuations 1925 and 1926 already wait. It remains continuous. Reward banners 1932 and 1934 remain timed.

Validation uses all opcode $51 dialogue references from the native post-fight event ($97B57D-$97BAD0). Every complete dialogue string in that range now ends with an input wait. The native event bytes, including all speaker helpers, branches, movement, rewards, and animations, are unchanged. ROM differences are restricted to the 16 pointers, 877 bytes of copied strings ($FB29EE-$FB2D5A), and checksum. Source parsing reports zero overlapping writes and 3,002 primary pointers.

Output: `Build/Secret_of_Evermore_Casual_Run_v1.41_Horace_Finale_Wait_Test.sfc` and matching `.asm`. Earlier test fixes are retained. Published v1.41 remains the release baseline.

SHA256: `d10c43ebdc5ca27d3b4ede1a79b2acd505b8afb74b8fb48ed044d41b42c9c5a9`.

Rebuild: run `Build/build_horace_finale_wait_test.py` with the clean USA ROM path. The builder reads the statue test's native event decode at `Build/Fake_Horace/statue_decoded.txt` to verify coverage. In-game validation remains pending.
