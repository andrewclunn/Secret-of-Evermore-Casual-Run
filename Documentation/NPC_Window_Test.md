# Default NPC window expansion test

The cumulative test ROM/source are `Build/Secret_of_Evermore_Casual_Run_v1.35_Dialogue_Window_Test.sfc` and the matching `.asm`. All preceding dialogue fixes are retained; accepted v1.35 release artifacts remain unchanged.

Generic NPC helper `$03`, reached through its existing global pointer at `$D29914`, still opens its window at `$F7E90A`. Its horizontal X operand at `$F7E90F` changes from 4 to 3, and width at `$F7E911` changes from 24 to 26. This expands one column on each side while preserving the horizontal center. Y remains 2, height remains 8, and styling is unchanged. Horizontal movement is encoded as X in this event format, resolving the request's reference to reducing Y to move left.

Static verification confirms the helper pointer and full geometry, preserved horizontal center, and exactly two changed ROM data bytes compared with the preceding cumulative test before checksum recalculation. Other theme helpers, all text, and prior corrections remain intact. The source audit validates all 3,002 primary pointers with no overlapping writes and reproduces the delivered ROM exactly.

ROM SHA-256: `a6ced1e7309222863ef61e02cb0a2887d7004b295ebce632fee70d8dcd1ea4d5`.

In-game verification is pending. Check ordinary NPC dialogue, longer choice prompts, and transitions between Generic NPC and named-character windows. Open a new dialogue window to exercise the updated shared geometry; an already-open window in a savestate retains its current dimensions.
