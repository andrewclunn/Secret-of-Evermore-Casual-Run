# Secret of Evermore: Casual Run

**Version 2.4**

Casual Run makes *Secret of Evermore* faster to play and easier to enjoy, with more direct controls, less grinding, better rewards, revised dialogue, optional multiplayer, and New Game Plus. It keeps the original game's story, exploration, puzzles, and SNES presentation while smoothing out many of its frustrations.

This document describes what changes **compared with the original game**.

For the changes introduced in **2.1**, **2.2**, **2.3** and **2.4**, see the [changelog](CHANGELOG.md).

[Download the v2.4 IPS patch](Secret_of_Evermore_Casual_Run_v2.4.ips) | [ASM source](Build/Secret_of_Evermore_Casual_Run_v2.4.asm)

## Controls and menus

You run by default after acquiring the Jaguar Ring early on. Hold **B** when you want to walk or charge your weapon faster. Attacking, talking, and confirming selections use **A**, while **B** consistently cancels or backs out of menus.

Dedicated shortcuts let you open the Boy's rings directly:

| Button | Action |
|---|---|
| **A** | Attack, interact, and confirm |
| **B** | Walk and charge faster while held; cancel in menus |
| **Start** | Open the Boy's Main Ring; also close an open Ring |
| **X** | Open the Boy's Item Ring |
| **Y** | Open the Boy's Alchemy Ring |
| **Select** | Switch characters in single-player; switch camera focus in two-player play |

The Main Ring is simpler: Dog Equipment replaces Control Preferences, and the redundant Targeting command and Window Edit are removed from normal access. You can manage the Dog's equipment without opening a separate Dog Main Ring.

With the **Oracle Bone**, press **L** to cycle the Dog between **Prehistoric -> Sacred Dog -> Poodle -> Prehistoric**. Holding L transforms once; Toaster Dog ignores L. **R** commands sniff. Player 1 controls transformations in single-player, whether controlling the Boy or Dog. When player 2 controls the Dog, only player 2 can transform it. Native story and map form changes still apply. Successful L transformations now have a brief brightening effect.

The Oracle Bone description explains L transformations and R sniffing; the Magic Gourd description explains controller 3's Start button.

Charge sounds are silenced.

## Two-player co-op

A second player can control the other character. Press **Start on controller 2** to join or withdraw, allowing the AI to take over when needed. Both controllers use A to attack and confirm, and B to cancel; the direct Ring shortcuts belong to player 1.

Either player can switch the camera focus with Select. The character with camera focus handles area exits and certain events, while the other can move beyond the visible screen.

The inherited controller-2 join checks are corrected in 2.2. Player 2 can control the Dog alongside the optional third player.

## Optional third-player reflection

**The Magic Gourd enables a third human player.** Connect a **Multitap to physical controller port 2** in your emulator or on supported hardware. Logical controller 1 controls the Boy, controller 2 can join as the Dog, and controller 3 controls the reflection. The reflection has no AI.

| Controller 3 button | Action |
|---|---|
| **Start** | Form the reflection, or dismiss it if already formed |
| **D-pad** | Move |
| **A** | Attack |
| **B**, held | Walk and charge faster |

Formation requires the Magic Gourd, both the Boy and Dog present and alive, an equipped weapon, and an area where attacks are available. Menus, dialogue and scripted events can prevent formation. The reflection disappears when the ordinary party separates or becomes unarmed, and during some events, including enemy-drop pickups. The original party controls camera focus and progression.

The reflection is a blue copy of the Boy, using his jeans colors across its skin, hair, clothes and outlines. Each formation captures the Boy's **current HP, equipped weapon and combat stats**. Subsequent equipment/stat changes to the Boy do not change that reflection. It has its own position and charge, and its life can only decrease. Its HP and charge meter are deliberately hidden.

The reflection cannot open menus, talk to NPCs or interact with containers. It is excluded from single and multiple spell target selection. Normal weapon-hit kills credit the weapon captured when the reflection formed.

After voluntary dismissal or an event despawn, wait **two seconds of gameplay** before pressing Start again. If killed, it must wait **one minute of gameplay**. Pauses and blocked gameplay can extend those waits. Reforming takes a fresh snapshot of the Boy. A one-pixel blue outline follows the Boy's portrait silhouette when the reflection is absent and ready to form. The outline disappears while formed, during cooldowns, or when formation is blocked.

**Snes9x save states:** loading a state can restore stale Multitap routing even if Joypad 3 is enabled and mapped. After loading, select ordinary joypads in the Input menu, then select **Multi Player 5 / Multitap** again before pressing controller 3's Start.

The third-player feature has limited full-campaign coverage. Full immunity to enemy/area spells and status effects, all charged/projectile weapon EXP paths, crowded palettes and every cutscene interaction still need further validation. Its palette can fall back to the Boy's colors when no unused palette is available. The reflection can also obstruct narrow paths; dismiss it to clear the way. [Technical notes and test coverage](Build/ShadowPrototype/README.md) and [2.4 validation notes](Build/GrowthPrototype/README.md) record the current limits.

## Less grinding

Character growth and training are more forgiving:

- The total experience needed to reach level 99 is approximately halved.
- The Boy gains innate Defense slightly faster, and the Dog gains innate Attack slightly faster.
- Weapon experience is shared within sword, axe, and spear families. Kills credited to either character can contribute to the Boy's shared weapon progress.
- Successful sniffing gives the Dog character experience and attack-skill progress.
- Common sniff rewards and ordinary one-unit enemy ingredient drops give **two ingredients** instead of one.

Sniff bonuses depend on the Dog's form when the pickup is collected:

| Dog form | Character EXP | Attack-skill points |
|---|---:|---:|
| Prehistoric | 10 | 4 |
| Sacred Dog | 100 | 2 |
| Poodle | 1,000 | 1 |
| Podunk / Toaster | 50 | 4 |

These bonuses are awarded once per successful ingredient pickup; they do not change the ingredients or their quantity. Growth belongs to the Dog across all forms. Character EXP stops at level 99 and attack skill at level 3. One full attack-skill level takes 256 points, so Prehistoric needs 64 pickups, Sacred Dog 128, and Poodle 256 from an empty progress bar. A large character EXP award immediately processes all earned level-ups.

Related alchemy formulas also share experience. Every second cast within a family gives the other formulas in that family a normal experience tick for their current level, so you can develop a useful set of spells without training each one separately.

## Healing, shopping, and loot

Healing items go further: **Petals restore 80 HP** and **Nectar restores 200 HP**. The practical carrying limit for ordinary consumables is **nine**.

Regular enemies award double currency. Enemy remains on 71 combat maps offer rewards suited to their region:

| Reward | Share of reward outcomes |
|---|---:|
| Regional currency | 7/13 |
| Two regional ingredients | 4/13 |
| One regional trade good | 2/13 |

These rewards replace the routine healing-item prizes on those maps, making battles more useful for buying supplies, casting alchemy, and trading. Negative status effects improve the chance of receiving remains. The fractions above describe their contents when remains appear.

Several purchases and passages are more convenient:

- The first hidden desert-crossing Amulet of Annihilation costs **500 Jewels**, down from 10,000.
- Nobilia's Atlas Amulet vendor charges **100 Jewels** and restocks indefinitely.
- A bead vendor sells **five beads for 75 Jewels** in place of a redundant rice vendor.
- Two pots are removed to open the passage between Nobilia's vendor stalls.
- Mud Pepper loot can be collected up to a carrying limit of **99**.
- Defeating the final/third Dark Forest copy awards the **Magic Gourd** if you do not already own it. The original Nobilia trade remains available, so players who acquire it earlier can summon the reflection earlier.

## Combat and equipment

Combat receives selected balance changes to make more weapons, spells, and charms useful throughout a casual playthrough.

- Five lengthy boss fights have reduced maximum HP.
- Weapon power is adjusted across the game. The Laser Lance and Neutron Blade receive small end-game reductions, while the Atom Smasher remains the strongest base weapon.
- Drain and Double Drain combine modest damage with useful healing.
- Barrier, Atlas, and Crush receive balance adjustments.
- Enemy stats, armor, evasion, and character growth are adjusted alongside those changes.
- Several charms have stronger or corrected effects.
- Silver Sheath ownership and Bazooka ammunition, level, and equipment-display bugs are fixed.
- The **Crusader Sword** is now awarded after **Footknight's chessboard defeat**, following the checkmate dialogue, instead of after the Dark Forest copies. Already-owned rewards do not repeat their acquisition notification; an already-owned sword leaves your current equipment alone.

## Dialogue and presentation

The script is revised throughout the game, with corrections to grammar, punctuation, terminology, and inconsistent wording. Character voices remain recognizable, and selected movie references are replaced with real-film references that suit the Boy's movie obsession.

Dialogue windows help distinguish who's speaking. The Boy, robots, narration, and recurring characters have their own presentation, using different window positions, patterns, borders, and text sounds. Characters such as Fire Eyes, Strong Heart, Horace, Tinker, Queen Camellia, and Professor Ruffleberg keep their identities through conversations and dialog.

Page breaks, timing, and window transitions are cleaned up. Important passages wait long enough to be read, repeated or empty windows are removed, and conversations advance more naturally.

Version 2.1 added a dedicated **borderless Boy dialogue style for the opening Podunk and initial laboratory scenes**, with a blank background, lower-screen placement and his existing text voice. Later ordinary Boy dialogue retains its usual framed presentation; Carltron and the Professor retain their own styles.

Saving feels like part of the conversation: Strong Heart records your travels in his alchemy notes, Blimp writes on mud pepper leaves, the Professor offers to make a backup, and machines acknowledge a completed backup. Other named characters have their own save wording and farewells.

## Exploration and progression

Navigation and progression fixes reduce the chances of getting stuck when revisiting areas or taking an unusual route.

- The Crustacia bridge and Ivor Tower's post-banquet progression are repaired.
- Queen's Key handling and dungeon revisit behavior are corrected.
- Tinker's workshop progresses properly after major story events.
- Tiny's lair can be left and re-entered without the associated softlock.
- The Pyramid has clearer gate symbols, a reopened return passage, and corrected Dog separation behavior.
- Three lit floor tiles connect the lower corridor to the upper path in Dog Maze III.
- Both automatic spear throws in the Halls work as intended.
- Omnitopia traversal is smoother, with opened vertical pipes, reduced sentry friction, and vent/hatch interaction while holding B to walk.

Windwalker flight starts with the minimap **on** when you take flight and can still be toggled normally.

## Optional New Game Plus

**This section describes an optional replay feature and contains minor progression spoilers.**

Jade, an unusual older man in a Prehistoria village hut, offers a time-travel experiment after you defeat the Mammoth Graveyard vipers. The choice is explicit, so you can continue your ordinary playthrough without starting a new cycle.

Accepting returns you to an early-game state after the Fire Eyes introduction while retaining much of your long-term growth. Story events, bosses, switches, chests, gourds, and sniff spots reset for the new cycle.

The Jaguar Ring is retained, the Bazooka is removed, and the Bone Crusher becomes your equipped weapon. Weapon carryover is limited to the **Bone Crusher, Neutron Blade, Atom Smasher, and Laser Lance**. Replay-specific inventory handling also protects your carried weapons during the fall toward Gothica.

Some characters have alternate dialogue that hints at memories of the previous cycle. After defeating the vipers again, Jade can restore the ordinary timeline through another reset, or you can keep playing in New Game Plus. The experiment is repeatable.

## Installing

1. Start with a **clean, unheadered U.S. ROM of Secret of Evermore**.
2. Apply [Secret_of_Evermore_Casual_Run_v2.4.ips](Secret_of_Evermore_Casual_Run_v2.4.ips) using an IPS patcher.
3. Open the patched ROM in your SNES emulator.

Existing 2.1-2.3 battery saves can be used. If your emulator matches saves by ROM filename, copy the battery save to match the new ROM's name. Players who already own the Magic Gourd can use the reflection immediately in eligible areas. The new Dark Forest reward is granted when that encounter is completed; it is not retroactively added to a save where the encounter is already finished.

The patch contains the complete set of changes. Apply it to the original ROM, rather than over another version of Casual Run or a different hack.

### Building from source (optional)

The [ASM source](Build/Secret_of_Evermore_Casual_Run_v2.4.asm) includes technical comments for anyone interested in how the changes work.

The single ASM file combines the patch and native documentation in ascending ROM address order, from bank `$C0` through `$FF`. Bank headings summarize function and byte coverage; routine, data-table, map-record and event-entry notes appear at their corresponding addresses beside the relevant patch blocks. A short opening guide covers address conventions, runtime RAM and source references. Native bytes inherited from the clean ROM are documented without emitting duplicate data, and undecoded areas remain labelled explicitly. No separate native ASM or documentation include is required to build.

Change summaries explain the verified behavior of the main helpers. Commented symbolic instructions restore names and control flow from the matching release sources, while native before/after byte notes and printable text previews make data edits easier to inspect. Those symbolic lines are explanatory comments; the `org`/`db` statements remain the authoritative emitted bytes. Unattributed byte edits are not assigned speculative purposes.

The ASM is self-contained and needs no documentation generator to build. Its output has been checked against the approved v2.4 ROM and IPS using both the existing builder and Asar. An explicit final zero byte ensures direct assemblers also emit the full 4 MiB image. This is an address-organized patch and reference, not a complete native disassembly.

With Python installed, you can build from your clean ROM:

```powershell
python Build/build.py "PATH_TO_CLEAN_ROM" Build/Secret_of_Evermore_Casual_Run_v2.4.sfc
```

The required base is 3,145,728 bytes, with SHA-256 `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`. The resulting 4 MiB ROM has SHA-256 `620b6cde35ac77966f6ee1988561be38e4b848ae33dd9fed7612c0d8e6dda1c9`.

## Roadmap

The features above are available in **2.4**. The following additions remain planned; the larger content and audio expansion targets **3.0**.

### Status Key

- **Complete** — available in the current release.
- **In testing** — implemented, with validation still underway.
- **In progress** — under development.
- **Planned** — intended for a future release.

| Future feature | Status |
|---|---|
| Completion-based unlocks for New Game Plus and earlier three-player access | Planned |
| Return to Omnitopia by flying to it in the Windwalker | Planned |
| Optional quest to obtain the Atom Smasher | Planned |
| Repeatable end-game Colosseum challenges with rewards | Planned |
| New music for expanded content | Planned |
| Optional MSU-1 soundtrack support and higher-quality audio | Planned |
| Additional Windwalker landmarks and navigation improvements | Planned |

## Credits and thanks

Casual Run builds on the work of the Secret of Evermore hacking community.

- **FuSoYa** — the two-player foundation.
- **Silentfan86** - [second-hero add-on](https://github.com/Silentfan86/SoE-A-second-hero-instead-of-the-dog) research informing the reflection's weapon/animation handling and inherited multiplayer signature fixes; the reflection adds a separate actor while preserving the Dog.
- **Ninakoru** — balance work, bug fixes, and research into combat, growth, equipment, alchemy, charms, and enemies.
- **assassin17** — Silver Sheath and Bazooka fixes.
- **black-sliver / Evermizer** — Tiny's-lair softlock prevention, tools, and technical research.
- **Conn / RedScorpion** — MSU-1 work and soundtrack research supporting the planned audio expansion.

Thanks also to **Data Crystal / TCRF contributors**, **CleanCodeX / XETH** for the RAMsetta Stone, **Gemini / Loboto3** for SecretOfEverhack, **millanzarreta** for SoERomInfo, **John David Ratliff** for SRAM documentation, and **maluramichael** for Awesome Secret of Evermore. The **Zeldix**, **RetroAchievements**, **GameFAQs**, and **Secret of Evermore Wiki** communities and older guide authors have also provided valuable tools, documentation, and gameplay references.

The Casual Run project brings these foundations together with its own controls, progression and economy changes, New Game Plus, script revisions, dialogue presentation, and exploration fixes.
