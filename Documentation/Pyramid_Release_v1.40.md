# v1.40 Pyramid polish release

Promoted October 4, 2026 at the user's request after gameplay acceptance.
The release is byte-identical to the accepted
`Secret_of_Evermore_Casual_Run_v1.39_Pyramid_Axe_Test.sfc`.

Authoritative source: `Build/Secret_of_Evermore_Casual_Run_v1.40.asm`.
Cumulative patch: `Secret_of_Evermore_Casual_Run_v1.40.ips`.
The default builder and current source-layout reports use v1.40.

## Changes

- The four gold switch symbols also appear directly before their corresponding
  Pyramid gates. The added markers are passive graphics; every destination
  attribute/collision word and the original switch logic are preserved.
- Six Bronze Axe wall events identify the entity that triggered the event as
  the Boy explicitly, replacing the ambiguous native character predicate that
  incorrectly rejected him. The axe requirement, wall states, sounds,
  animation operations, and rescue/reunion sequence are retained.
- All earlier features remain, including v1.39's first-descent dog separation
  repair and v1.38's Antiqua dialogue corrections.

Detailed investigation and test evidence remain in
`Documentation/Pyramid_Symbols_Test.md` and `Documentation/Pyramid_Axe_Test.md`.
Those test sources/ROMs remain historical artifacts; use v1.40 for development.

## Verification

- Verified clean USA base: 3,145,728 bytes; SHA-256
  `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`.
- Release ROM: 4,194,304 bytes; SHA-256
  `dfeec1c24ef79cbc4111ba1007ffbd62a6314c0f28c6caa9ab567f633e515f9e`.
- Checksum/complement: `$0861 / $F79E`.
- IPS SHA-256:
  `98df7ee8ea923c817da5103519587ec8308d56a51c9984eba1bd67336e880895`.
- The clean-base release build reproduces the accepted test ROM exactly.
- Applying the cumulative IPS to the clean base independently reproduces the
  release, including its four-MiB size. Apply it to the clean ROM directly.
- Full source audit: zero overlapping writes and 3,002 validated text pointers.
- Prior tests verify sixteen changed visual cells and all 8,760 unchanged
  collision/attribute words, exact native decompression, and all four markers
  rendered in the emulator.
- Prior emulator tests reproduce the reported axe failure and verify all five
  lower walls with the Boy/Bronze Axe, Boy/wrong weapon, and Dog/axe ID: fifteen
  passing checks, including the native rescue sequence.
- The user accepted both the marker update and axe-wall repair. Independent
  upper-floor gameplay and live two-player coverage remain part of ongoing QA;
  upper-event bytecode, branches, and call destinations are independently checked.

Rebuild with the default `Build/build.py` and the verified clean USA ROM.
Generated ROMs remain local and excluded from Git.
