# Secret of Evermore: Casual Run

**Current development baseline:** v1.38\
**Next major milestone:** 2.0  
**Longer-term expansion:** 3.0

**Current release:** [v1.38 IPS patch](Secret_of_Evermore_Casual_Run_v1.38.ips), with the authoritative source in [Build/Secret_of_Evermore_Casual_Run_v1.38.asm](Build/Secret_of_Evermore_Casual_Run_v1.38.asm). This version fixes Tiny's introduction, missing Tiny/Pompolonius/Horace dialogue themes, post-arena pagination and spacing, and Horace's dialogue input waits. It retains the v1.37 vendor-passage removal and all earlier features. The build script defaults to v1.38; [dialogue release verification notes](Documentation/Dialogue_QA_v1.38.md) record validation and gameplay coverage limits.

## What Casual Run Is

**Secret of Evermore: Casual Run** is a cumulative improvement patch for the clean, unheadered U.S. release of *Secret of Evermore*.

The goal is a faster, smoother, less frustrating playthrough while preserving the feel and presentation language of the original SNES game. Casual Run is not intended to be a hard-mode hack or a remake. It favors quality-of-life improvements, clearer progression, modest rebalance, optional depth, bug fixes, and better presentation without turning the game into a modern HUD-heavy redesign.

Casual Run builds on earlier community work, including FuSoYa's two-player patch, selected balance and bug-fix work by Ninakoru, fixes by assassin17, and later community research and fixes credited below. Conn/RedScorpion's MSU-1 work remains an important historical reference for the planned 3.0 audio reimplementation, but MSU-1 is not active in the v1.36/2.0 production line.

This README is the **player-facing feature summary, roadmap, and credits document**. The authoritative ASM source is the technical source of truth for exact ROM changes, build identity, hooks, memory usage, validation requirements, historical experiments, and implementation details.

---

## Roadmap at a Glance

The headings **1.0**, **2.0**, and **3.0** are major public-release generations rather than a literal mapping to every internal development version. **1.0** represents the foundation that was already released publicly. **2.0** is the current major revision: its script, presentation, stable Windwalker/minimap behavior, native-audio baseline, enemy-prize economy, focused character theming, and contextual save-dialogue work are implemented through v1.36, while final QA and the Omnitopia flight-return feature remain unfinished. **3.0** is the planned future content and audio expansion.

### Status Key

- **Complete** — implemented and accepted into the current development baseline for that release generation.
- **In testing** — implemented and undergoing runtime validation before acceptance.
- **In progress** — active work is underway but the feature is not ready for release acceptance.
- **Planned** — accepted roadmap scope, but implementation is still future work.

| Release bucket | Feature | Status | Summary |
|---|---|---|---|
| **1.0** | Core controls and Ring-menu overhaul | **Complete** | Default running, walk/fast-charge behavior, A/B role cleanup, direct Main/Item/Alchemy Ring shortcuts, and consistent menu controls. |
| **1.0** | Two-player integration | **Complete** | FuSoYa's multiplayer foundation retained and integrated with Casual Run controls without breaking Player 2's join/withdraw behavior. |
| **1.0** | Faster progression and reduced grinding | **Complete** | Faster character growth, shared weapon-family progress, Dog growth from sniffing, improved ingredient rewards, and reworked alchemy-family experience sharing. |
| **1.0** | Economy, healing, item, charm, weapon, and combat rebalance | **Complete** | Gentler economy and progression tuning, selected boss/weapon adjustments, useful charm improvements, and targeted alchemy balance. |
| **1.0** | Progression and softlock fixes | **Complete** | Numerous navigation, state, dungeon-repeatability, Mungola/Tinker, Tiny's-lair, Ivory Tower, and related progression safeguards. |
| **1.0** | New Game Plus | **Complete** | Optional repeatable replay system through Jade with retained progression and selective residual-memory dialogue. |
| **2.0** | Windwalker flight stabilization | **Complete** | Native perspective and steering restored after the DSP-1 experiment; repaired world-map graphics retained; minimap defaults ON but remains toggleable. |
| **2.0** | Native audio stability baseline | **Complete** | Experimental MSU-1 interception removed after full-game QA found unintended song changes; 2.0 uses the original SPC music path. |
| **2.0** | Dialogue presentation and focused character theming | **Complete** | Reworked dialogue presentation, cleaner window behavior, and focused semantic identities for narration, robots, the Boy, and recurring named characters rather than broad occupation/class themes. |
| **2.0** | Script and dialogue revision | **Complete** | Full regional story/world script review, movie-reference cleanup, terminology and consistency corrections, selected NG+ dialogue variants, and later QA-driven character/presentation fixes. |
| **2.0** | Enemy-prize economy redesign | **Complete** | Ordinary enemy remains on 71 combat-map profiles now favor regional cash, ingredients, and trade goods instead of routine healing-item prizes. |
| **2.0** | Contextual save conversations | **Complete** | Strong Heart, Tinker, Pompolonius, Cecil, Blimp, Professor Ruffleberg, and Omnitopia/Junkyard machines use caller-specific save dialogue while the native save operation remains intact. |
| **2.0** | Full-game QA, script, theme, and friction pass | **In progress** | Continue the end-to-end playthrough and make surgical corrections to bugs, awkward presentation, dialogue/theme coverage, unclear progression, and unnecessary friction discovered in normal play. |
| **2.0** | Return to Omnitopia through Windwalker flight | **Planned** | Replace the menu-style return to the space station with an actual action/destination taken during Windwalker flight. |
| **3.0** | MSU-1 support reimplementation | **Planned** | Rebuild external soundtrack support from the v1.30 native-audio baseline, preserving no-change room semantics and validating the new backend across the full game. |
| **3.0** | Higher-quality MSU-1 PCM soundtrack | **Planned** | Produce a substantially higher-quality external soundtrack after the replacement MSU backend is stable. |
| **3.0** | New music | **Planned** | Expand the soundtrack with new music where the new 3.0 content benefits from its own musical identity. |
| **3.0** | Atom Smasher side quest | **Planned** | Turn acquisition of the strongest end-game weapon into a meaningful optional quest rather than leaving its current acquisition as-is. |
| **3.0** | End-game Colosseum arena | **Planned** | Add repeatable postgame/end-game combat content built around fame, challenges, rewards, and useful loot. |
| **3.0** | Expanded Windwalker navigation/presentation | **Planned** | Revisit additional flight-space landmarks, approach cues, minimap/navigation ideas, and presentation refinements where they support the expanded content. |

---

# 1.0 — Original Public Foundation

The 1.0 bucket represents the core Casual Run foundation that was already released publicly before the current 2.0 development cycle. These systems established the project's faster, lower-friction approach to controls, progression, balance, replayability, and bug fixing.

## Faster, More Direct Controls

Normal movement defaults to running. The former run button instead becomes a deliberate walk/fast-charge control, allowing the player to move quickly by default without giving up weapon charging.

### Field controls

- **A** — action, interaction, attack, and confirm.
- **B** — walk while held and accelerate weapon charging.
- **Start** — open the Boy's Main Ring.
- **X** — open the Boy's Item Ring directly.
- **Y** — open the Boy's Alchemy Ring directly.
- **Select** — switch the controlled character in the field.

### Ring and management controls

- **A** confirms selections.
- **B** consistently backs out or cancels.
- **Start** can also close the Ring.
- Direct Ring shortcuts use the game's actual remembered Ring state rather than visibly simulating menu navigation.
- The redundant Targeting command and normal access to Window Edit were removed from the Boy's Main Ring.
- Dog Equipment replaces the old Control Preferences slot, while the Dog's separate main Ring is removed from normal access.

### Two-player behavior

Casual Run retains FuSoYa's two-player foundation. The A/B role swap applies to both controllers, while Player 1 receives the new Start/X/Y Ring shortcuts. Player 2's existing Start-button join/withdraw behavior is deliberately preserved.

The Bazooka now recharges to **100% and stays ready without holding attack**. Holding B still accelerates recharge below 100%. Melee and Dog charging retain their existing behavior. See the [Bazooka validation notes](Documentation/Bazooka_Charge_Test.md) for verification and remaining gameplay coverage.

## Less Grinding, Better Growth

Casual Run reduces the amount of repetitive training needed to enjoy the game's systems.

- Total character experience needed to reach level 99 is approximately halved.
- The Boy receives slightly faster innate Defense growth.
- The Dog receives slightly faster innate Attack growth.
- Kills credited to either character can contribute to the Boy's weapon-family growth where the inherited shared-family system applies.
- Successful sniffing gives the Dog character and attack-skill progress.
- Common ingredient sniff rewards and ordinary one-unit enemy ingredient drops give two ingredients instead of one.
- Charge sound effects above 100% are silenced to make ordinary play less noisy.

### Alchemy-family experience

Related formulas share experience at a predictable 50% rate. Every second cast within a family awards a normal current-level experience tick to the other formulas in that family, reducing the need to grind every spell independently while still rewarding actual use.

## Healing, Inventory, Economy, and Rewards

- Petals heal **80 HP**.
- Nectar heals **200 HP**.
- The practical cap for ordinary consumables is raised to **9**.
- Regular enemies award double currency.
- The first hidden desert-crossing Amulet of Annihilation costs **500 Jewels** instead of 10,000.
- The Nobilia Atlas Amulet vendor charges **100 Jewels** and restocks indefinitely.
- Two pots beside the Nobilia vendor stalls are removed to open the passage between vendors.
- A redundant Nobilia rice vendor is replaced with a bead vendor selling **5 beads for 75 Jewels**.
- Ordinary drop behavior is more rewarding when enemies are affected by negative status conditions.

## Combat, Alchemy, Weapons, and Charms

Casual Run uses targeted rather than wholesale rebalance. The intent is to reduce obvious outliers and make more of the game's existing options worth using.

- Five longer boss fights have reduced maximum HP.
- Laser Lance and Neutron Blade receive small end-game power reductions while Atom Smasher remains the strongest base weapon.
- Drain and Double Drain are normalized around a modest offensive strength and useful healing role.
- Barrier, Atlas, and Crush receive mild later balance trims.
- Selected inherited weapon, formula, enemy, armor, stat-growth, and evasion adjustments are retained where they fit Casual Run's lower-friction design.
- Multiple charms receive stronger or corrected effects so collecting them matters more.
- Silver Sheath ownership behavior and Bazooka ammunition/level/interface bugs are repaired.

## Progression and Softlock Repairs

A major Casual Run priority is preventing unusual routing, backtracking, or replay from leaving the game in contradictory states.

Examples include:

- Crustacia bridge repair.
- Ivory Tower post-banquet progression repair.
- Queen's Key cleanup and dungeon-repeatability safeguards.
- Mungola completion establishing a coherent post-imposter, pre-Windwalker Tinker state.
- Tiny's-lair leave/re-entry softlock prevention.
- Removal or suppression of several unnecessary progression blockers and repeated traversal obstacles.
- Faster Omnitopia traversal through opened vertical pipes and reduced sentry friction.

## New Game Plus

Casual Run includes an optional, repeatable New Game Plus system accessed through **Jade**, an intentionally out-of-place older man in a Prehistoria village hut.

Jade becomes available after the Mammoth Graveyard vipers are defeated and explicitly asks whether the player wants to participate in a time-travel experiment, so the reset cannot be triggered accidentally.

The reset returns the story to a stable early-game replay state while retaining much of the player's long-term growth. Story progression, bosses, switches, chests, gourds, sniff spots, and other replay-sensitive state are reset as needed. The Jaguar Ring is retained, the Bazooka is removed, and the Bone Crusher becomes the equipped weapon. As of v1.32, weapon carryover is deliberately limited to **Bone Crusher, Neutron Blade, Atom Smasher, and Laser Lance**, preventing unrelated weapon inventory state from leaking into the new cycle.

Selected characters also receive subtle alternate dialogue in NG+, suggesting residual memory of the previous cycle without rewriting the entire story around the mechanic.

---

# 2.0 — Current Major Revision

2.0 is a substantial second-generation release rather than a small polish update. Its major script, presentation, stable Windwalker/minimap, native-audio, enemy-prize economy, focused-theme, and contextual save-dialogue work are implemented in the current v1.36 development baseline; the remaining work is to finish the full-game QA/polish pass and make returning to Omnitopia an action performed in Windwalker flight.

These completed feature families are therefore **2.0 features**, even though they were developed and tested incrementally in internal v1.x builds.

### Changes accepted since v1.30

- **v1.31 — Enemy-prize economy:** 71 explicit combat-map profiles were redesigned so ordinary remains resolve to **7/13 regional cash, 4/13 regional ingredients ×2, and 2/13 regional trade goods ×1**. Routine direct healing-item prizes were removed from those profiles; the existing status-aware remains chance was not changed.
- **v1.32 — Focused themes and full-game QA corrections:** the broad occupation/class theme experiment was replaced with focused named-character identities; Narration/System was standardized to centered five-line presentation; repeated Omnitopia shuttle prompts were corrected to System; missed Camellia and late Professor Ruffleberg callsites were fixed; a repeated Robot text sequence was collapsed to one page; NG+ weapon carryover was restricted to four intended late-game weapons; and Tinker gained a Yes-only post-save acknowledgement without changing the native/shared save implementation.
- **v1.33 — Contextual save dialogue and character polish:** Sting's unrelated duplicate “See you later!” became “Stay safe out there.”; Pompolonius gained a themed Colosseum last-words save prompt; Cecil's Ebon Keep theme continuity, question pagination, and save dialogue were corrected; Blimp's hut/cave saves use his mud-pepper-leaf wording; Professor Ruffleberg's saves use a backup joke; and Omnitopia/Junkyard machine saves use machine-native backup language.
- **v1.35 — Strong Heart save dialogue, Sandpits polish, and source consolidation:** Strong Heart keeps his theme through all save paths, offers to record your travels in his alchemy notes, and ends with “There we are. Just keep a look out for giant beetles!”; both final responses wait for dismissal. The southern raised-ledge Skelesnail in the Sandpits was removed. The source was consolidated into one active definition per address, with text-pointer and allocation audits; consolidation and release promotion preserve the exact accepted R4 ROM bytes.

- **v1.37 — Nobilia vendor passage:** completely removes the two pots labeled B/C during the map experiment, including their collision. The other experiment pots retain their original behavior. Final combined removal and vendor access await emulator confirmation.
- **v1.38 — Antiqua dialogue QA:** restores Tiny's introduction and missing Tiny, Pompolonius and Horace themes; fixes post-arena pagination and spacing; adds input waits to Horace's introduction and later help pages.
- **v1.36 — Dialogue QA and NPC window polish:** corrected Blimp’s spacing, hut speaker themes, and rest/save question separation; the volcano alchemist’s save theme and the Boy’s “Huh?” reply; Fire Eyes/twin theme continuity; and Horace’s twin’s Nobilia scene themes. Default NPC windows move one column left and widen by two columns. The Crustacia amulet vendor was confirmed working through its existing pots trigger and received no appearance change.

## Script and Dialogue Revision — **Complete**

The original script has received both targeted character passes and a full regional story/world review.

Changes include:

- Grammar, punctuation, terminology, speaker attribution, and consistency fixes.
- Selected dialogue revisions that preserve established character voices.
- Replacement of selected fictional or placeholder movie references with real-film references that better support the Boy's movie-obsessed characterization.
- Selective NG+ residual-memory dialogue.

## Dialogue Presentation and Character Theming — **Complete**

The way dialogue is presented has also been overhauled rather than merely rewritten.

- Ordinary dialogue uses cleaner pacing and window lifecycle behavior.
- Redundant or awkward page breaks and unnecessary presentation delays are removed where appropriate.
- Semantic presentation identities distinguish narration/system text, generic NPCs, the Boy, robots, and recurring named characters. The v1.32 QA pass intentionally **removed the earlier broad occupation/class assignments** for generic merchants, guards, alchemists, inventors, comedic characters, and adventurers; those reusable roles now fall back to Generic NPC unless the speaker has a dedicated identity.
- Dedicated supporting-character themes currently cover **Blimp, Strong Heart, Gomi, Lance, Tinker Tinderbox, Carltron, Fire Eyes, Horace, Queen Camellia, Pompolonius, Tiny, the Gothica King, Cecil, and the Eerie Guide/supernatural presentation**, in addition to the Boy, Robot, Narration/System, and Generic NPC baselines.
- Themes can use different combinations of window placement, pattern, border treatment, and sound without abandoning the visual language of the original game.
- v1.32 also standardized centered Narration/System to five-line geometry and corrected missed Camellia, Professor Ruffleberg, Robot, and Omnitopia shuttle presentation cases found during full-game QA.

The underlying theme system is considered established. The remaining full-game QA pass is intended to catch missed or misapplied callsites rather than redesign the architecture.

## Enemy-Prize Economy — **Complete**

v1.31 replaces the repetitive ordinary-enemy healing-item prize mix on **71 explicit combat-map profiles** with more regionally useful rewards.

- **7/13** outcomes award regional cash.
- **4/13** outcomes award two of a regional ingredient.
- **2/13** outcomes award one regional trade good.
- Routine direct healing-item prizes are removed from those profiles.
- The v1.08 status-aware remains chance still determines whether remains appear at all; v1.31 changes the contents, not the chance system.
- Maps outside the audited 71-profile set retain their existing remains setup.

The result is a prize economy that feeds the game's money, alchemy, and trading systems more often instead of repeatedly handing out consumable healing items the player may already be carrying.

## Contextual Save Conversations — **Complete**

v1.32-v1.36 make save prompts feel like part of the scene rather than exposing one generic utility dialogue everywhere. The underlying native save operation remains unchanged; the difference is who asks and how they phrase it.

- **Tinker** keeps his native save route but now gives his “lab assis-good friend” acknowledgement only after the player actually chooses to save.
- **Strong Heart** keeps his theme on first and repeat visits, asks “Shall I record your travels in my alchemy notes?”, and follows saving with “There we are. Just keep a look out for giant beetles!” His save and decline farewells wait for a button press.
- **Pompolonius** uses his own presentation and a Colosseum-specific “last words” prompt.
- **Cecil** stays in his own theme through the Ebon Keep exchange, his three-question introduction advances cleanly from each answer to the next page, and his save prompt is character-specific.
- **Blimp** asks whether he should write the journey down on his mud pepper leaves at both of his save locations.
- **Professor Ruffleberg** phrases his save offer as making a backup, with “I like to live dangerously.” as the refusal.
- **Omnitopia and Junkyard machines** use machine-native backup wording rather than the generic human “record your progress / See you later!” exchange; the ordinary terminal acknowledges a successful save with **“Backup complete.”**
- The humorous **Ivor banquet/arrest** save sequence remains intact and serves as the model for scene-specific one-off save jokes.
- The Sting alchemist's unrelated duplicate “See you later!” was changed to **“Stay safe out there.”** so it no longer looks like part of the save system when auditing dialogue.

Ordinary unnamed save NPCs can still use the shared generic save conversation. The goal is not to replace the save engine, but to keep distinctive characters and machines from suddenly sounding interchangeable.

## Native Audio Stability Baseline — **Complete**

2.0 now deliberately uses Secret of Evermore's original SPC music path.

Earlier Casual Run builds included an MSU-1 backend that passed focused one-shot/loop/fallback tests, but the full-game QA pass uncovered unintended song changes in scenes and rooms that normally preserve the music already playing. Restoring the native music-change routine fixed the problem, while restoring the original song-pointer table alone did not.

For the v1.30 native-audio baseline, retained unchanged through v1.36 and the eventual 2.0 release:

- Native SPC music playback remains in control end to end.
- No Casual Run MSU-1 hook is active.
- External PCM files are not required or used.
- The old v1.05/v1.18 implementation is retired rather than patched around individual bad rooms.
- MSU-1 is moved to 3.0 for a clean reimplementation from the native-audio baseline.

The full experiment history, isolation tests, historical 1-70 track mapping, and 3.0 requirements are preserved in **`README_MSU1_EXPERIMENT.md`**.

## Windwalker Flight Stabilization — **Complete**

The world-map work keeps the useful navigation repair while returning the renderer and steering to the game's proven native behavior.

- The original Windwalker Mode-7 perspective is restored.
- Native left/right steering response is restored.
- The original world-map/minimap object graphics were repaired after an older patch allocation was found to overlap them.
- The native lower-left minimap, facing indicator, landing markers, position math, and layout are retained.
- The minimap starts **ON** when Windwalker flight begins, but the game's normal toggle remains functional.

A DSP-1 perspective renderer and reduced-yaw experiment looked promising in flight but caused deterministic post-flight Ring/menu graphics corruption. Those implementations were withdrawn rather than carried into 2.0. The detailed test history is preserved in **`README_DSP1_EXPERIMENT.md`**.

Experimental altitude-speed changes and alternate flight-control mappings are also not part of the current baseline.

## Full-Game QA, Script, Theme, and Friction Pass — **In progress**

The game will be played from beginning to end with the current feature set active.

This pass has already produced the accepted v1.31 enemy-prize redesign, the v1.32 focused-theme/NG+/Tinker corrections, the v1.33 contextual-save/Cecil/Pompolonius/Sting fixes, and the v1.35 Strong Heart/Sandpits corrections described above. The v1.36 dialogue and NPC-window fixes continue that pass. It remains active for the rest of the 2.0 playthrough.

This pass can make surgical corrections when normal play exposes:

- Bugs or regressions.
- Missed or incorrect dialogue-theme assignments.
- Script wording, speaker, punctuation, or presentation problems.
- Awkward window lifecycle or pacing.
- Unclear progression or navigation.
- Unnecessary menu trips, repeated presentation, or other friction that conflicts with Casual Run's design goals.
- Balance issues that become obvious only in the context of a complete casual playthrough.

The goal is **coverage and polish**, not another architectural rewrite.

## Return to Omnitopia Through Windwalker Flight — **Planned**

Returning to the space station should become an action taken in the flight world rather than a menu-style destination choice.

The intended result is for Omnitopia to feel like a real place the player returns to through Windwalker navigation. The 2.0 implementation should build on the stable native Mode-7 renderer, using a visible station landmark/approach cue rather than depending on the withdrawn live DSP-1 renderer. The design goal is straightforward: **fly back to the station instead of selecting it from a menu**.

This is the only planned new headline gameplay feature for 2.0.

---

# 3.0 — New Content and Audio Expansion

Where 2.0 finishes the existing game, 3.0 is intended to expand it. The features below belong together because the new quests, combat content, flight-space presentation, and music can be designed as one cohesive addition rather than separate late patches.

## Atom Smasher Side Quest — **Planned**

Create a new optional quest around obtaining the Atom Smasher. The weapon can remain the strongest of the late-game trio, but acquiring it should become a memorable piece of end-game content rather than leaving its current acquisition path unchanged.

## End-Game Colosseum Arena — **Planned**

Expand the Colosseum into repeatable end-game/postgame combat content with a fame-and-reward structure.

The exact challenge ladder, reward economy, opponent structure, and relationship to New Game Plus remain design work, but the intended pillars are:

- Repeatable combat challenges.
- Fame or equivalent progression.
- Useful loot and rewards.
- A reason to engage with the game's combat systems after the normal story progression has opened up.

## New Music — **Planned**

Add new tracks where the new 3.0 content benefits from distinct music. New music is being held for the content expansion rather than added to 2.0 in isolation so that the soundtrack additions have clear in-game purposes. Native song-ID expansion should be engineered and validated separately from the MSU interception layer so the two systems can be debugged independently.

## MSU-1 Support Reimplementation — **Planned**

Reintroduce optional external soundtrack support from the stable native-audio baseline established in v1.30 and retained through v1.36, rather than reviving the v1.18 interception path.

The replacement backend must treat **"do not change music"** as a first-class behavior, not merely map requested song IDs correctly. Development should begin by tracing native music-change semantics across representative rooms and cutscenes, then choose a hook point where the game has already determined that a real music change is required.

Acceptance will require full-game regression coverage in addition to the familiar one-shot, looping, missing-PCM, partial-pack, and native-SFX tests. The Horace and Nobilia no-change cases that exposed the old bug become permanent regression tests.

See **`README_MSU1_EXPERIMENT.md`** for the preserved findings and requirements.

## Higher-Quality MSU-1 PCM Set — **Planned**

Produce a substantially higher-quality version of the external MSU-1 soundtrack **after** the replacement 3.0 backend is stable. The historical 1-70 track identity can be used as a starting point, while the audio assets themselves receive a quality upgrade.

This work naturally pairs with the new 3.0 music so the expanded soundtrack can be treated as one coherent package.

## Expanded Windwalker Navigation and Presentation — **Planned**

Revisit additional flight-space ideas after the 2.0 Omnitopia-return feature establishes the basic destination interaction.

Possible work in this bucket includes clearer landmarks and approach cues, additional minimap/navigation presentation, and other flight-world polish that supports the new content. Specific visual experiments are not considered locked merely because they were prototyped earlier; each one still has to justify itself in actual play.

---

## Retired Implementations and Experiments

Casual Run has tried a number of ideas that did not survive testing. Unless deliberately reopened in the future, these should not be treated as planned features.

- Automatic healing shortcuts.
- Repeat-last-alchemy shortcuts.
- Synthetic auto-target/menu-navigation experiments replaced by the direct Ring shortcuts.
- Faster Windwalker ascent/descent experiments.
- Alternate Windwalker control remapping experiments.
- Prototype flight FOV indicators that were not accepted into the current baseline.
- The v1.27/v1.28 live DSP-1 Windwalker renderer and half-rate yaw implementation; findings are preserved in `README_DSP1_EXPERIMENT.md`.
- The v1.05/v1.18 Casual Run MSU-1 implementation; MSU-1 itself remains planned for a fresh 3.0 implementation documented in `README_MSU1_EXPERIMENT.md`.
- Modern boss-HP or numeric-combat overlays and other HUD-heavy presentation changes that conflict with the project's SNES-style design.

A failed prototype may still teach us something, but it is not part of the roadmap simply because code for it once existed.

---

## Applying Casual Run

Casual Run is intended for a **clean, unheadered U.S. ROM of _Secret of Evermore_**.

Apply [Secret_of_Evermore_Casual_Run_v1.38.ips](Secret_of_Evermore_Casual_Run_v1.38.ips) to that clean base ROM with an appropriate patcher. Earlier versioned patches remain available for their corresponding releases.

For exact base-ROM hashes, patched-ROM hashes, checksums, source build instructions, expansion-space ownership, and other technical validation information, consult the authoritative ASM source included with the project.

Required clean base: 3,145,728 bytes; SHA-256 `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`.

Current v1.38 ROM: 4,194,304 bytes; SHA-256 `f187a38f9c7c177e017dfad75f177b28f5eada6893e1924b5e1973993fe9fc45`; checksum/complement `$2D9A / $D265`. The cumulative IPS was composed from the verified v1.37 release patch and the v1.38 changes. Patch composition and application to the local baseline were checked; a clean-ROM rebuild/application remains unverified because the clean base is unavailable in this workspace.

---

# Credits and Thanks

Casual Run is cumulative work. Some features directly incorporate earlier patches; others were made possible by documentation, reverse engineering, archives, tools, and independent research from the wider *Secret of Evermore* community.

## Work Incorporated Into Casual Run

- **FuSoYa** — original *Secret of Evermore* two-player foundation that Casual Run retains and builds around.
- **Ninakoru** — gameplay balance work and bug fixes selectively incorporated into the Casual Run foundation, including extensive prior research into combat, growth, equipment, formulas, charms, enemies, and related systems.
- **assassin17** — Silver Sheath fix, Bazooka ammunition fix, and Bazooka level/interface fixes incorporated into the project.
- **Conn / RedScorpion** — original *Secret of Evermore* MSU-1 implementation and historical track numbering/loop-policy research that informed Casual Run's experiments and will remain an important reference for the planned 3.0 reimplementation.
- **black-sliver / Evermizer** — Tiny's-lair leave/re-entry softlock prevention incorporated into Casual Run, along with a large body of modern *Secret of Evermore* hacking work that has served as valuable reference material.

## Research, Tools, Documentation, and Community Resources

Special thanks to the people and projects whose work made the later source recovery, text work, reverse engineering, validation, and feature development practical:

- **Data Crystal / TCRF contributors** — ROM/RAM maps and long-running technical documentation for *Secret of Evermore*.
- **CleanCodeX / XETH — RAMsetta Stone for Secret of Evermore** — structured SRAM/WRAM and persistent-state documentation.
- **hellow554 — RustyBlazer** — disassembly and labeled engine research useful for tracing native game behavior.
- **Gemini / Loboto3 — SecretOfEverhack** — text-engine and translation tooling/research, especially useful once Casual Run moved into relocated script work.
- **maluramichael — Awesome Secret of Evermore** — invaluable archive/index of patches, tools, technical work, and older community resources.
- **Zeldix community** — MSU-1 information, preservation, and discussion.
- **RetroAchievements community** — useful ROM-identity and compatibility reference material.
- **GameFAQs, Secret of Evermore Wiki contributors, and older guide authors** — gameplay documentation and leads for obscure intended behavior that could then be verified against the game.

## Casual Run Project Work

The Casual Run project adds the cumulative original work described in this README: control integration, quality-of-life changes, progression and economy tuning, New Game Plus, dialogue and presentation revisions, theme architecture, progression repairs, source recovery and documentation, Windwalker/minimap work, audio experimentation and rollback documentation, and the ongoing 2.0/3.0 roadmap.

---

## Project Philosophy

When deciding whether something belongs in Casual Run, the guiding questions are simple:

- Does it make a normal playthrough smoother without flattening the game into automation?
- Does it reduce grinding, softlocks, missable traps, or unnecessary friction?
- Does it preserve optional depth for players who want to engage more deeply?
- Does it still look and feel like something that belongs in a SNES game?
- If the original game is confusing or inconsistent, can it be fixed cleanly rather than merely preserved?
- Can the change be tested and maintained without making the rest of the project fragile?

The roadmap can change when testing proves an idea does not work. The current accepted ROM and authoritative ASM decide what Casual Run actually is; this README describes the player-facing result and where the project intends to go next.
