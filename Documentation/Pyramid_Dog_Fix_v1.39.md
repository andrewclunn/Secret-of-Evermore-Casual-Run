# v1.39 Pyramid dog separation release

Promoted at user request on October 4, 2026 after the user confirmed that R2
worked. The release is byte-identical to the accepted
`Secret_of_Evermore_Casual_Run_v1.38_Dog_Separation_Test_R2.sfc`.

Authoritative source: `Build/Secret_of_Evermore_Casual_Run_v1.39.asm`.
Cumulative patch: `Secret_of_Evermore_Casual_Run_v1.39.ips`.
The default builder and current source-layout reports now use v1.39.
Generated ROMs remain local and excluded from Git.

## Change

On the first descent from the Pyramid upper floor, the lower-floor entry made
an unavailable dog available without requesting restoration of his saved room
position. Shared entry consequently placed him beside the Boy. Going upstairs
and descending again set the restoration flag and avoided the problem.

The four-byte hook at $9594A3 calls a fifteen-byte routine at $F7F150. If the dog
was unavailable, it sets the pending-position flag $22E5.2 before performing the
original $2261.0 clear. Native entry then restores $2381/$2383 through $92A422.
An already available dog does not receive a new restoration request. Completed
puzzles bypass the hook. The native puzzle, door logic, rescue and character
switching remain intact. The failed unrelated Ivor Tower hook is not included.

v1.39 retains every v1.38 feature. Only the hook, helper and checksum differ:
19 changed bytes. Detailed investigation and R2 checks are recorded in
`Documentation/Dog_Separation_Test.md`.

## Verification

- Verified clean USA base: 3,145,728 bytes; SHA-256
  `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`.
- Release ROM: 4,194,304 bytes; SHA-256
  `7d049d480da303a063f28f24457f372dce07e7be9277b39e5b45bde9de0b6da5`.
- Checksum/complement: `$311B / $CEE4`.
- IPS SHA-256: `7c6d5b769533b597a0fa15139e8179e73563193d9bee62aeb9f5a54b82e15416`.
- Default clean-base build reproduces the accepted test ROM exactly.
- Applying the cumulative IPS to the verified clean base reproduces the release
  exactly, including its four-MiB size.
- Source audit reproduces the release and validates all 3,002 primary text
  pointers. The hook/helper allocation has no overlapping writes.
- R2's emitted guard was checked across 65,536 flag-byte combinations and
  independently decoded. Runtime checks from both local pre-stair states cover
  the first descent, return trip, repeat descent and character switching.
- A synthetic completed-puzzle test produced byte-identical final WRAM for
  v1.38 and R2. The user confirmed the reported gameplay issue was fixed.

Full switch-opening/rescue and live two-player join/withdraw coverage remain
part of the ongoing full-game QA pass.

```powershell
python Build/build.py BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.39.sfc --ips Secret_of_Evermore_Casual_Run_v1.39.ips
python Build/script_layout.py audit BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.39.asm --baseline-rom Build/Secret_of_Evermore_Casual_Run_v1.39.sfc --report-prefix Documentation/Script_Layout_Current
```
