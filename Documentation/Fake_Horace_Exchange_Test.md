# Evil Horace handover theme and response order

Based on the handover input-wait test, retaining Boy Y=18 and all prior fixes.

All Evil Horace openers in the Diamond Eyes handover use global helper $11,
Artificial Horace, rather than Generic NPC $03. This covers both introductory
branches, his offer, both "...At last" utterances, and the villainous reveal.

TEXT 1544 retains the complete Lone Starr quote but no longer contains the
polite handover line. That line becomes a separate acknowledged Boy text,
displayed immediately after the native exchange banner is dismissed, before
Evil Horace says "...At last." It occurs only in the original stranger branch.
The already-met-Horace branch retains its own existing Boy response.

The two identical "...At last" strings originally used TEXT 1547 and 1548.
Both existing utterances now display TEXT 1547. TEXT 1548 is safely reused for
the moved Boy line, with its theme metadata corrected to Boy. The new response
is allocated at $FA5480, and the small conditional post-exchange helper uses
$F7F340. Both allocations were blank and unowned in the previous build.

Native currency award, inventory transfer, reward banners, actor movements,
branch destinations and subsequent fight setup are preserved. Input waits
remain on the full quote, moved line and all other windowed conversation.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Fake_Horace_Exchange_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Fake_Horace_Exchange_Test.asm`.
Rebuild: `Build/build_fake_horace_exchange_test.py <clean-USA-ROM>`.
SHA-256: `d3125386d8935e41dee3674335933a0d5e6f719f8fcfa378813ef8d60294d7c2`.

Checks: restricted ROM differences, zero overlapping writes, 3,002 validated
text pointers, unchanged award/transfer bytes, and native decoding of the
conditional helper confirming Boy then Artificial Horace theme order and
return to the existing scene. Gameplay verification remains pending. Replay
from before the handover; a running text box in a savestate retains its old
pointer and theme. Published/default release remains v1.40.
