# Evil Horace statue activation dialogue test

This cumulative test starts from the v1.41 Bronze Axe Test, retaining the Bronze Axe power increase and Boy axe-dialogue theme fix.

The earlier Evil Horace correction covered the west-bank Diamond Eyes handover. The city-square statue activation is a separate event. Its actual dialogue openers still called generic theme $03 even though text metadata already assigned Evil Horace theme $11. Three strings ended without an input wait.

Corrected lines:

- TEXT 1893: “Behold! The Diamond Eyes are mine!”
- TEXT 1894: “With their power, I shall command the entire Ancient World!”
- TEXT 1896: “Enough commentary! Let the menacing begin!”

The scene's two Evil Horace window openers at CPU $D7AFFA and $D7B1EF now call helper $11 (Artificial Horace). TEXT 1894 continues the first Evil Horace window without an intervening theme change. The Boy's TEXT 1895 retains helper $04 and its existing input wait.

Each of the three Evil Horace strings is copied with an $86 input wait before its $00 terminator. New strings occupy $FB295E-$FB29ED within the reserved HORACE_FINALE text arena. Only their primary text pointers are redirected. Original text allocations remain intact.

Validation:

- Source rebuild matches the previous test before edits.
- Zero overlapping source writes; 3,002 primary text pointers retained.
- ROM differences restricted to the two theme operands, three text pointers, copied text payloads, and checksum.
- Event animations, yields, branches, and battle setup remain byte-for-byte unchanged.
- Native event decoding confirms helper $11 at both Evil Horace openers and helper $04 before the Boy's reply.
- All three new strings end in $86 $00. Bronze Axe remains 33 and the Boy axe-reply fix remains present.

Gameplay validation remains pending. The decoder's existing empty-stack warning at $928005 also appears with earlier builds.

Output: `Build/Secret_of_Evermore_Casual_Run_v1.41_Evil_Horace_Statue_Test.sfc` and matching `.asm`.

SHA256: `52643eb2a50b845643593b8fbf0f4dc403906b419d2ab9e8a3b6e798cb66c4a5`.

Rebuild with `Build/build_evil_horace_statue_test.py`, passing the clean USA ROM path. Published v1.41 remains the release baseline.
