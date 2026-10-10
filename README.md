# Secret of Evermore: Casual Run

**Version 2.0**

Casual Run makes *Secret of Evermore* faster to play and easier to enjoy, with more direct controls, less grinding, better rewards, revised dialogue, and optional two-player play and New Game Plus. It keeps the original game's story, exploration, puzzles, and SNES presentation while smoothing out many of its frustrations.

This document describes what changes **compared with the original game**.

[Download the v2.0 IPS patch](Secret_of_Evermore_Casual_Run_v2.0.ips) · [ASM source](Build/Secret_of_Evermore_Casual_Run_v2.0.asm)

## Controls and menus

You run by default (after aquiring a particular item early on). Hold **B** when you want to walk or charge your weapon faster. Attacking, talking, and confirming selections use **A**, while **B** consistently cancels or backs out of menus.

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

Charge sounds are silenced.

## Two-player co-op

A second player can control the other character. Press **Start on controller 2** to join or withdraw, allowing the AI to take over when needed. Both controllers use A to attack and confirm, and B to cancel; the direct Ring shortcuts belong to player 1.

Either player can switch the camera focus with Select. The character with camera focus handles area exits and certain events, while the other can move beyond the visible screen.

## Less grinding

Character growth and training are more forgiving:

- The total experience needed to reach level 99 is approximately halved.
- The Boy gains innate Defense slightly faster, and the Dog gains innate Attack slightly faster.
- Weapon experience is shared within sword, axe, and spear families. Kills credited to either character can contribute to the Boy's shared weapon progress.
- Successful sniffing gives the Dog character experience and attack-skill progress.
- Common sniff rewards and ordinary one-unit enemy ingredient drops give **two ingredients** instead of one.

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

## Combat and equipment

Combat receives selected balance changes to make more weapons, spells, and charms useful throughout a casual playthrough.

- Five lengthy boss fights have reduced maximum HP.
- Weapon power is adjusted across the game. The Laser Lance and Neutron Blade receive small end-game reductions, while the Atom Smasher remains the strongest base weapon.
- Drain and Double Drain combine modest damage with useful healing.
- Barrier, Atlas, and Crush receive balance adjustments.
- Enemy stats, armor, evasion, and character growth are adjusted alongside those changes.
- Several charms have stronger or corrected effects.
- Silver Sheath ownership and Bazooka ammunition, level, and equipment-display bugs are fixed.

## Dialogue and presentation

The script is revised throughout the game, with corrections to grammar, punctuation, terminology, and inconsistent wording. Character voices remain recognizable, and selected movie references are replaced with real-film references that suit the Boy's movie obsession.

Dialogue windows help distinguish who's speaking. The Boy, robots, narration, and recurring characters have their own presentation, using different window positions, patterns, borders, and text sounds. Characters such as Fire Eyes, Strong Heart, Horace, Tinker, Queen Camellia, and Professor Ruffleberg keep their identities through conversations and dialog.

Page breaks, timing, and window transitions are cleaned up. Important passages wait long enough to be read, repeated or empty windows are removed, and conversations advance more naturally.

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
2. Apply [Secret_of_Evermore_Casual_Run_v2.0.ips](Secret_of_Evermore_Casual_Run_v2.0.ips) using an IPS patcher.
3. Open the patched ROM in your SNES emulator.

The patch contains the complete set of changes. Apply it to the original ROM, rather than over another version of Casual Run or a different hack.

### Building from source (optional)

The [ASM source](Build/Secret_of_Evermore_Casual_Run_v2.0.asm) includes technical comments for anyone interested in how the changes work. With Python installed, you can build from your clean ROM:

```powershell
python Build/build.py "PATH_TO_CLEAN_ROM" Build/Secret_of_Evermore_Casual_Run_v2.0.sfc
```

The required base is 3,145,728 bytes, with SHA-256 `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`. The resulting 4 MiB ROM has SHA-256 `718614572208aec79b28e2287a09369bd3c9b64d3b1e87a17be26b56ecbef0e6`.

## Roadmap

The features above are available in **2.0**. The following additions are planned for **3.0**.

### Status Key

- **Complete** — available in the current release.
- **In testing** — implemented, with validation still underway.
- **In progress** — under development.
- **Planned** — intended for a future release.

| Future feature | Status |
|---|---|
| Return to Omnitopia by flying to it in the Windwalker | Planned |
| Optional quest to obtain the Atom Smasher | Planned |
| Repeatable end-game Colosseum challenges with rewards | Planned |
| New music for expanded content | Planned |
| Optional MSU-1 soundtrack support and higher-quality audio | Planned |
| Additional Windwalker landmarks and navigation improvements | Planned |

## Credits and thanks

Casual Run builds on the work of the Secret of Evermore hacking community.

- **FuSoYa** — the two-player foundation.
- **Ninakoru** — balance work, bug fixes, and research into combat, growth, equipment, alchemy, charms, and enemies.
- **assassin17** — Silver Sheath and Bazooka fixes.
- **black-sliver / Evermizer** — Tiny's-lair softlock prevention, tools, and technical research.
- **Conn / RedScorpion** — MSU-1 work and soundtrack research supporting the planned audio expansion.

Thanks also to **Data Crystal / TCRF contributors**, **CleanCodeX / XETH** for the RAMsetta Stone, **Gemini / Loboto3** for SecretOfEverhack, **millanzarreta** for SoERomInfo, **John David Ratliff** for SRAM documentation, and **maluramichael** for Awesome Secret of Evermore. The **Zeldix**, **RetroAchievements**, **GameFAQs**, and **Secret of Evermore Wiki** communities and older guide authors have also provided valuable tools, documentation, and gameplay references.

The Casual Run project brings these foundations together with its own controls, progression and economy changes, New Game Plus, script revisions, dialogue presentation, and exploration fixes.
