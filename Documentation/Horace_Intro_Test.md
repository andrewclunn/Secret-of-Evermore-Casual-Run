# Horace introduction input-wait test

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.37_Horace_Intro_Test.sfc`, with matching `.asm` beside it. This cumulative test retains the Tiny, arena recruitment, post-arena themes, Boy pagination and Number Two spacing fixes. Release artifacts remain preserved.

Horace's first west-bank conversation (TEXT 1573–1608) had raw entries ending directly in `$00`. The event script immediately continued to close or replace those windows, leaving no final input wait. The new copies add native `$86` acknowledged page endings to 35 of the 36 entries, covering greetings, introductions, the Podunk explanation, all Diamond Eyes state branches, quest instructions and the Boy's departure.

TEXT 1579 (“Wow! You're right! I'm <Boy>,”) remains continuous with TEXT 1580 (“and this is my dog, <Dog>.”). A space is added after the comma; the input wait comes after the complete introduction. Existing internal page controls, wording, name tokens, and speaker themes are retained.

The 36 entries are copied into `$FA5500–$FA5E46`, 2,375 bytes within the existing HORACE_WEST_BANK arena. The original entries remain intact. The range was checked against source ownership, zero-filled baseline contents and every primary text pointer before use. Only the 36 primary pointers, new copies and checksum bytes change. Event instructions, branches, animations, timing commands, shared helpers and later repeat/formula dialogue are unchanged.

Verification passed: 35 acknowledged endings, continuous Boy/Dog introduction, all 36 display operands, exact original event-script preservation, all 3,002 primary pointers, zero overlapping source writes, restricted diff and exact source reproduction against the verified local baseline.

ROM SHA-256: `4691bb53bebe66785ed6f5903ff71dd033380f48a66cecacabf5502ad18be12d`.
Checksum/complement: `$7599 / $8A66`.

Reproduce with `Build/build_horace_intro_test.py` after building the arena follow-up test. A clean-base rebuild is unverified because the clean ROM is unavailable locally.

In-game confirmation remains pending. Load from before the first Horace conversation, release the advance button when a page appears, and confirm each page remains visible until input. Check the Boy/Dog introduction as one continuous exchange, Horace's longer explanation and the final departure. Diamond Eyes branches should also wait for input when encountered. This test has not been promoted to a release.
