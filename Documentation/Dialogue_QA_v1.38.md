# v1.38 Antiqua dialogue QA release

Promoted at user request on October 4, 2026. The release ROM is byte-identical to the cumulative `Secret_of_Evermore_Casual_Run_v1.37_Horace_Followup_Test.sfc`. Authoritative source: `Build/Secret_of_Evermore_Casual_Run_v1.38.asm`. Cumulative release patch: `Secret_of_Evermore_Casual_Run_v1.38.ips`. The default builder uses v1.38. Generated ROMs remain local and excluded from Git.

## Changes

- Tiny's introduction: restores `$D5C6B7` to `$0B`, the high byte of TEXT 993's display operand. An earlier theme edit had selected TEXT 1761, the fragment “to ”. His actual `$14` theme helper remains intact.
- Arena recruitment: nine openers now select Tiny or Pompolonius, including continuation pages, the Sacred Dog selection and waiting-room introduction. The Boy's replies and native save path retain their correct presentation.
- Post-arena conversation: four additional Pompolonius openers receive his theme. The Boy starts “What are we doing here?” on a fresh page. Artificial Horace's “Not yet, Your Cleanliness. I've offered…” receives the missing space while retaining its pauses.
- Horace introduction: TEXT 1573–1608 receive 35 acknowledged final pages. The Boy's name/Dog introduction stays continuous, with a space after the comma.
- Horace rescue and later help: ten openers covering sixteen texts receive Horace's theme, including the pit rescue, introductory question, magic explanation and Call Bead conversations. Four rescue speaker metadata entries are corrected. Seven later help entries receive acknowledged final pages, including the Call Bead explanation after “I'd like to help you directly as well.”

The release retains v1.37's Nobilia B/C pot removal and all preceding features. Dialogue copies use `$FA5500–$FA5E46` and `$FA5E50–$FA605D` in the existing Horace arena. Original text copies remain stored. Existing event lengths, state branches, animations, Call Bead awards/refill quantities, system receipt presentation, and save operations are preserved.

## Verification

- Clean USA base requirement: 3,145,728 bytes; SHA-256 `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`.
- Release ROM: 4,194,304 bytes; SHA-256 `f187a38f9c7c177e017dfad75f177b28f5eada6893e1924b5e1973993fe9fc45`.
- Checksum/complement: `$2D9A / $D265`.
- IPS SHA-256: `9717c83e62793f6ee1f5ceda717660277bb364be353c69188be6a52cf8cb7157`.
- Source audit validates all 3,002 primary text pointers, reports zero overlapping writes, and reproduces the accepted cumulative test exactly against the verified local baseline. Current layout reports are regenerated from v1.38.
- Focused checks validated true theme-helper operands, dialogue addresses, speaker transitions and continuation pages, explicit waits/spacing, strict per-test ROM change limits, and retained native award/branch bytes.
- The cumulative IPS preserves verified v1.37 patch writes and overlays the v1.38 differences. Applying it to the verified local v1.37 baseline reproduces the release exactly, including the four-MiB size.
- A clean-base rebuild/application was not performed because the clean ROM is unavailable locally. Baseline application and patch composition do not substitute for that check.

The user's promotion request authorizes this release; it does not establish exhaustive runtime coverage of every conditional branch. The full-game QA pass remains active, including repeat rescues, Boy/Dog interaction, Diamond Eyes state variants and Call Bead refill paths.

With a verified clean base, reproduce the standard build using:

```powershell
python Build/build.py BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.38.sfc --ips Secret_of_Evermore_Casual_Run_v1.38.ips
python Build/script_layout.py audit BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.38.asm --baseline-rom Build/Secret_of_Evermore_Casual_Run_v1.38.sfc --report-prefix Documentation/Script_Layout_Current
```
