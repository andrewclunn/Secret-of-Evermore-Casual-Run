# Secret of Evermore: Casual Run

**Current development baseline:** v1.28  
**Next major milestone:** 2.0  
**Longer-term expansion:** 3.0

## What Casual Run Is

**Secret of Evermore: Casual Run** is a cumulative improvement patch for the clean, unheadered U.S. release of *Secret of Evermore*.

The goal is a faster, smoother, less frustrating playthrough while preserving the feel and presentation language of the original SNES game. Casual Run is not intended to be a hard-mode hack or a remake. It favors quality-of-life improvements, clearer progression, modest rebalance, optional depth, bug fixes, and better presentation without turning the game into a modern HUD-heavy redesign.

Casual Run builds on earlier community work, including FuSoYa's two-player patch, selected balance and bug-fix work by Ninakoru, fixes by assassin17, the Conn/RedScorpion MSU-1 work, and later community research and fixes credited below.

This README is the **player-facing feature summary, roadmap, and credits document**. The authoritative ASM source is the technical source of truth for exact ROM changes, build identity, hooks, memory usage, validation requirements, historical experiments, and implementation details.

---

## Roadmap at a Glance

The headings **1.0**, **2.0**, and **3.0** are major public-release generations rather than a literal mapping to every internal development version. **1.0** represents the foundation that was already released publicly. **2.0** is the current major revision: several of its headline systems are already implemented in the v1.28 development baseline, while final QA and the Omnitopia flight-return feature remain unfinished. **3.0** is the planned future content expansion.

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
| **2.0** | Windwalker flight overhaul | **Complete** | DSP-1 perspective rendering, calmer turning response, repaired native world-map graphics, and an always-visible flight minimap. |
| **2.0** | MSU-1 support with native fallback | **Complete** | Optional external soundtrack support while preserving native sound effects and falling back cleanly to the original soundtrack when a PCM is missing. |
| **2.0** | Dialogue presentation and character theming | **Complete** | Reworked dialogue presentation, semantic character/theme identities, cleaner window behavior, and character/category-specific visual treatment. |
| **2.0** | Script and dialogue revision | **Complete** | Full regional story/world script review, movie-reference cleanup, terminology and consistency corrections, and selected NG+ dialogue variants. |
| **2.0** | Full-game QA, script, theme, and friction pass | **In progress** | Play the game end to end and make surgical corrections to bugs, awkward presentation, dialogue/theme coverage, unclear progression, and unnecessary friction discovered in normal play. |
| **2.0** | Return to Omnitopia through Windwalker flight | **Planned** | Replace the menu-style return to the space station with an actual action/destination taken during Windwalker flight. |
| **3.0** | Higher-quality MSU-1 PCM soundtrack | **Planned** | Regenerate or replace the existing external soundtrack PCMs at substantially higher quality while preserving the working MSU/native fallback behavior. |
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

The reset returns the story to a stable early-game replay state while retaining much of the player's long-term growth. Story progression, bosses, switches, chests, gourds, sniff spots, and other replay-sensitive state are reset as needed. The Jaguar Ring is retained, the Bazooka is removed, and the Bone Crusher becomes the equipped weapon.

Selected characters also receive subtle alternate dialogue in NG+, suggesting residual memory of the previous cycle without rewriting the entire story around the mechanic.

---

# 2.0 — Current Major Revision

2.0 is a substantial second-generation release rather than a small polish update. Several of its headline features are already implemented in the current v1.28 development baseline; the remaining work is to finish the full-game QA/polish pass and make returning to Omnitopia an action performed in Windwalker flight.

The four completed feature families below are therefore **2.0 features**, even though they were developed and tested incrementally in internal v1.x builds.

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
- Semantic presentation identities distinguish narration/system text, generic NPCs, the Boy, robots, comedic characters, alchemists, merchants, guards/authority figures, inventors, adventurers, major story characters, artificial counterparts, supernatural guides, and other recurring categories.
- Themes can use different combinations of window placement, pattern, and border treatment without abandoning the visual language of the original game.

The underlying theme system is considered established. The remaining full-game QA pass is intended to catch missed or misapplied callsites rather than redesign the architecture.

## Optional MSU-1 Soundtrack Support — **Complete**

Casual Run supports an external MSU-1 soundtrack while retaining the original SNES music as a reliable fallback.

- With no MSU-1 support, the native soundtrack behaves normally.
- If a requested PCM is present, the external track can replace the native music for that request.
- Native song data still initializes so sound effects continue to work correctly.
- If a PCM is missing, that request falls back to native music.
- A missing PCM does **not** disable later MSU tracks, so partial soundtrack packs are supported.

The current soundtrack uses the established 1–70 track numbering. PCM files are optional and are not part of the core ROM patch.

## Windwalker Flight Overhaul — **Complete**

The 2.0 flight overhaul substantially upgrades the Windwalker world-map presentation.

- The world map now uses a DSP-1-assisted perspective rather than the original flatter presentation.
- Turning response is reduced to a calmer half-rate heading integration while preserving the native acceleration behavior.
- The original world-map/minimap object graphics were repaired after an older patch allocation was found to overlap them.
- The native lower-left minimap, facing indicator, landing markers, position math, and layout are retained.
- The minimap remains visible during Windwalker flight.

Experimental altitude-speed changes, alternate flight-control mappings, and prototype field-of-view wedges are **not** part of the current baseline.

## Full-Game QA, Script, Theme, and Friction Pass — **In progress**

The game will be played from beginning to end with the current feature set active.

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

The intended result is for Omnitopia to feel like a real place the player returns to through Windwalker navigation. The exact approach/trigger presentation will be determined through implementation and testing, but the design goal is straightforward: **fly back to the station instead of selecting it from a menu**.

This is the only planned new headline gameplay feature for 2.0.

---

# 3.0 — New Content and Soundtrack Expansion

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

Add new tracks where the new 3.0 content benefits from distinct music. New music is being held for the content expansion rather than added to 2.0 in isolation so that the soundtrack additions have clear in-game purposes.

## Higher-Quality MSU-1 PCM Set — **Planned**

Produce a substantially higher-quality version of the external MSU-1 soundtrack. Existing track identity and fallback compatibility should be preserved wherever appropriate, while the audio assets themselves receive a quality upgrade.

This work naturally pairs with the new 3.0 music so the expanded soundtrack can be treated as one coherent package.

## Expanded Windwalker Navigation and Presentation — **Planned**

Revisit additional flight-space ideas after the 2.0 Omnitopia-return feature establishes the basic destination interaction.

Possible work in this bucket includes clearer landmarks and approach cues, additional minimap/navigation presentation, and other flight-world polish that supports the new content. Specific visual experiments are not considered locked merely because they were prototyped earlier; each one still has to justify itself in actual play.

---

## Retired Experiments / Not Current Roadmap Scope

Casual Run has tried a number of ideas that did not survive testing. Unless deliberately reopened in the future, these should not be treated as planned features.

- Automatic healing shortcuts.
- Repeat-last-alchemy shortcuts.
- Synthetic auto-target/menu-navigation experiments replaced by the direct Ring shortcuts.
- Faster Windwalker ascent/descent experiments.
- Alternate Windwalker control remapping experiments.
- Prototype flight FOV indicators that were not accepted into the current baseline.
- Modern boss-HP or numeric-combat overlays and other HUD-heavy presentation changes that conflict with the project's SNES-style design.

A failed prototype may still teach us something, but it is not part of the roadmap simply because code for it once existed.

---

## Applying Casual Run

Casual Run is intended for a **clean, unheadered U.S. ROM of _Secret of Evermore_**.

Use the release patch associated with the version you want to play and apply it to that clean base ROM with an appropriate patcher.

For exact base-ROM hashes, patched-ROM hashes, checksums, source build instructions, expansion-space ownership, and other technical validation information, consult the authoritative ASM source included with the project.

---

# Credits and Thanks

Casual Run is cumulative work. Some features directly incorporate earlier patches; others were made possible by documentation, reverse engineering, archives, tools, and independent research from the wider *Secret of Evermore* community.

## Work Incorporated Into Casual Run

- **FuSoYa** — original *Secret of Evermore* two-player foundation that Casual Run retains and builds around.
- **Ninakoru** — gameplay balance work and bug fixes selectively incorporated into the Casual Run foundation, including extensive prior research into combat, growth, equipment, formulas, charms, enemies, and related systems.
- **assassin17** — Silver Sheath fix, Bazooka ammunition fix, and Bazooka level/interface fixes incorporated into the project.
- **Conn / RedScorpion** — original *Secret of Evermore* MSU-1 implementation and the track numbering, loop policy, and music-mute approach that remain the basis for Casual Run's optional soundtrack support.
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

The Casual Run project adds the cumulative original work described in this README: control integration, quality-of-life changes, progression and economy tuning, New Game Plus, dialogue and presentation revisions, theme architecture, progression repairs, MSU integration/repair, source recovery and documentation, Windwalker presentation work, and the ongoing 2.0/3.0 roadmap.

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
