# Casual Run v1.42

Promoted October 4, 2026 at the user's request. The release is byte-identical to `Secret_of_Evermore_Casual_Run_v1.41_Horace_Finale_Theme_Test.sfc`.

## Changes since v1.41

- Raises Bronze Axe base power from 32 to 33. Bronze Spear remains 32.
- Uses the Boy's theme for “I hit it with my axe!” when talking to the Drain alchemist.
- Corrects Evil Horace's actual speaker openers during the city-square Diamond Eyes statue scene and adds input waits to his three lines.
- Adds 16 missing final-page waits throughout the post-fight conversation, covering both met-Horace branches, Tiny, Madronius, and departure advice.
- Corrects 12 speaker openers throughout that exchange to use Horace, Tiny, or Boy themes as appropriate.

All earlier changes are retained. Complete dialogue windows wait for player input. The player-name sentence prefix remains continuous with its name/“son!” continuation; timed reward banners remain unwindowed.

## Release artifacts

- Source: `Build/Secret_of_Evermore_Casual_Run_v1.42.asm`.
- ROM: `Build/Secret_of_Evermore_Casual_Run_v1.42.sfc` (4,194,304 bytes).
- Cumulative patch: `Secret_of_Evermore_Casual_Run_v1.42.ips`.
- Base: clean unheadered USA ROM, 3,145,728 bytes; SHA256 `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`.
- ROM SHA256: `44ddfdc0dc6487a6d86c5e72588937ae2ee7b3208b42d16405129b746f2424bf`.
- IPS SHA256: `bd3e9108d3a3461df3d103189a3b8160dd951f5aa23f64205cd3a06479abe16b`.
- Checksum/complement: `$DF6B / $2094`.

The default builder, current layout reports, and README point to v1.42. Earlier releases remain available. Promotion is recorded in `Build/promote_v142.py`.

## Verification

Clean-USA source reconstruction and independent cumulative IPS application reproduce the accepted test ROM exactly. Source auditing reports zero overlapping writes and validates 3,002 primary text pointers. The default builder is also checked independently against the accepted ROM. Native decoding validates actual event helper operands; the complete post-fight windowed dialogue set was audited for input waits. Promotion changes no gameplay bytes relative to the accepted test.

User-requested promotion follows the test iterations. No additional live emulator replay was performed for the final theme corrections. The occasional temporary status-display glitch remains unresolved.

Detailed evidence: `Documentation/Axe_Dialogue_Theme_Test.md`, `Bronze_Axe_Power_Test.md`, `Evil_Horace_Statue_Test.md`, `Horace_Finale_Wait_Test.md`, and `Horace_Finale_Theme_Test.md`.
