# Horace rescue and later dialogue test

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.37_Horace_Followup_Test.sfc`, with matching `.asm` beside it. This cumulative test retains all prior Tiny, arena, spacing and Horace introduction fixes. Release artifacts remain preserved.

Ten Generic NPC openers now use `$0E Horace Highwater`:

| Operand | Texts covered |
|---|---|
| `$D6D707` | 1565, repeat fall rescue warning |
| `$D6D73D` | 1568, rescue reply “That's a good idea.” |
| `$D6D74B` | 1569, “Are you OK? You took quite a spill…” |
| `$D6D795` | 1571, “Who are you, friend? Where are you from?” |
| `$D6D9E2` | 1598–1601, magic and Diamond Eyes state branches |
| `$D6DA93` | 1609, Dog reminder |
| `$D6DAA6` | 1610/1611, direct help and first Call Bead gift |
| `$D6DADD` | 1613/1614, one-eye reminder and refill |
| `$D6DAFD` | 1616/1617, repeat help and refill |
| `$D6DB34` | 1619, Sacred Dog resemblance greeting |

The four rescue texts' speaker metadata is corrected from Generic Antiqua NPC to Horace. Their text payloads already have acknowledged endings and are unchanged.

Seven later dialogue entries (1610, 1611, 1613, 1614, 1616, 1617, 1619) now have a native `$86` input wait before their final terminator. This includes the “If you're in trouble, use a Call Bead. I'll come to you.” page after “I'd like to help you directly as well.” Existing internal pages, pauses and wording remain intact.

The new copies occupy `$FA5E50–$FA605D`, 526 bytes in the existing HORACE_WEST_BANK arena, immediately after the earlier introduction copies. Source ownership, zero-filled baseline contents and primary text pointers were checked before allocation. Original copies remain stored. Only ten helper operands, seven primary pointers, new text copies and checksum bytes change. Boy and system receipt themes, native Call Bead quantities, stock tests, branches, animations and other event bytes remain unchanged.

Verification passed: ten true A3 helper operands covering sixteen dialogue texts, seven acknowledged final pages, exact preservation of earlier fixes and native award/branch bytes, all 3,002 primary text pointers, zero overlapping writes, restricted ROM diff and exact source reproduction.

ROM SHA-256: `f187a38f9c7c177e017dfad75f177b28f5eada6893e1924b5e1973993fe9fc45`.
Checksum/complement: `$2D9A / $D265`.

Reproduce with `Build/build_horace_followup_test.py` after building the Horace introduction test. Clean-base reconstruction remains unverified because the clean ROM is unavailable locally.

In-game confirmation remains pending: replay the first fall rescue and a repeat rescue, check the later magic explanation, talk to Horace with both Boy and Dog, and exercise the Call Bead gift/repeat/refill paths with zero and one Diamond Eye. Each Horace window should use his theme; each help page should remain until input. This test is not promoted to a release.
