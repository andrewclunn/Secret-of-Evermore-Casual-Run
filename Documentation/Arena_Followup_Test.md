# Post-arena dialogue follow-up test

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.37_Arena_Followup_Test.sfc`, with matching `.asm` beside it. This cumulative build retains the Tiny introduction and arena recruitment corrections. Release artifacts are preserved.

Four Generic NPC openers now use Pompolonius's `$13` theme:

| Operand | Dialogue |
|---|---|
| `$D9E50B` | TEXT 2466, congratulations |
| `$D9E51F` | TEXT 2467, sword award |
| `$D9E5BC` | TEXT 2472/2473, “Hmm…” and west-side/Diamond Eyes explanation |
| `$D9E620` | TEXT 2477, statue's power and jewel quest |

The live merged TEXT 2469 now ends “Where are we?” with a native `$86` page break in place of its trailing space. Its original pause remains. The next display, TEXT 2470 “What are we doing here?”, starts a fresh page, followed by TEXT 2471 “How do we get back to Podunk?”. No text relocation or new allocation is needed.

The live merged TEXT 1045 at `$F465A5` lacked a space between “Not yet, Your Cleanliness.” and “I've offered…”. Its redundant second `$96` is replaced by `$20`, retaining its initial `$96`, both surrounding pauses, wording and allocation size. The older stored TEXT 1045 copy at `$F7209B` is not the active pointer target and is left unchanged.

Verification passed: four theme operands, all 12 display calls from congratulations through the Boy's movie quote, inherited speaker themes, exact fresh-page/spacing bytes, retained earlier fixes, all 3,002 primary text pointers, zero overlapping writes, and exact source reproduction. The diff from the recruitment test is limited to six functional bytes and checksum bytes; event lengths, animation, item award, branches and remaining text are unchanged.

SHA-256: `a914eac982c3f0c5934c4bd1428141aaf25715ddee7f375a8f72231404b90724`.
Checksum/complement: `$26CA / $D935`.

Reproduce with `Build/build_arena_followup_test.py` after building the recruitment test. Clean-base reconstruction is unverified because the clean ROM is unavailable locally. In-game confirmation remains pending: replay the post-Vigor award/quest conversation and the Carltron/Artificial Horace “Number Two” scene from before their windows open. Check Pompolonius's themes, the Boy's new page, and the visible space before “I've offered…”. This test is not promoted to a release.
