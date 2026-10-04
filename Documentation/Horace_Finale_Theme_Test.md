# Horace finale speaker-theme audit

Cumulative test based on the Horace Finale Wait Test. Corrects 12 actual native event helper operands across the full post-fight exchange. The text metadata already specified the intended speakers, but these event openers still used generic styling.

All 27 explicit speaker openers in $97B57D-$97BAD0 were verified against the following text operand and intended speaker. Horace uses $0E, Tiny uses $14, the Boy uses $04, and Madronius retains $03. The mixed Horace/Boy TEXT 1898 starts with Horace's $0E helper; existing page-map handling and normal/NG+ text are preserved. Continuations retain their existing speaker window.

Verified examples include Horace calling Tiny ($D7B676 and $D7B690), Tiny's arrival ($D7B6E1), Horace requesting the energy-core throw ($D7B727), praising Tiny ($D7B935), and greeting Madronius ($D7B9E2). The Boy's question about returning to Podunk also now uses his own theme.

All 38 complete dialogue texts in this event were checked for final $86 input waits. TEXT 1924 remains the continuous prefix of the following player-name/“son!” sentence; the completed sentence waits. Timed reward banners are unwindowed. All waits added by the previous test are retained.

Validation: zero overlapping source writes, 3,002 primary text pointers, and ROM differences restricted to the 12 theme operand bytes plus checksum. Native decoding confirms the corrected helper calls. Earlier Evil Horace fixes, Boy axe-dialogue styling, and Bronze Axe power 33 remain intact. Live gameplay validation is pending.

Output: `Build/Secret_of_Evermore_Casual_Run_v1.41_Horace_Finale_Theme_Test.sfc` and matching `.asm`.

SHA256: `44ddfdc0dc6487a6d86c5e72588937ae2ee7b3208b42d16405129b746f2424bf`.

Rebuild with `Build/build_horace_finale_theme_test.py`, passing the clean USA ROM path. Published v1.41 remains unchanged.
