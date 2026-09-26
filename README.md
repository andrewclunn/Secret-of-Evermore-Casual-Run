# Secret of Evermore - Casual Run Patch - Version 1.17

## Patch Summary

**Secret of Evermore: Casual Run** is a cumulative improvement patch for the clean, unheadered U.S. release of *Secret of Evermore*. It incorporates FuSoYa's two-player work, selected balance and bug-fix work by Ninakoru, selected fixes by assassin17, an integrated version of the Conn/RedScorpion MSU-1 patch, and a large set of original Casual Run quality-of-life, progression, balance, dialogue, and control changes.

The goal is a faster, smoother playthrough with less grinding and fewer progression traps while preserving the feel of the original SNES game. Casual Run is not intended to be a hard-mode hack or a radical redesign. It favors useful quality-of-life improvements, clearer progression, modest balance changes, and optional depth without adding modern HUD elements or intrusive interfaces.

Version **1.17** completes the full story/world script review begun after the regional text-arena conversion. Every documented script arena has now been reviewed entry-by-entry, including NPC dialogue, signs, receipts, conditional variants, Dog-only text, major story scenes, and the active New Game Plus callbacks. The accepted pass corrects grammar, punctuation, terminology, consistency, and selected awkward wording while preserving established character voices, event logic, and the frozen gameplay/control feature set.

---

## Version 1.17 Release Notes

- Completes the full **25-arena** story/world script review.
- Standardizes recurring terminology such as **formula** versus **spell** where the game is specifically referring to alchemy formulas.
- Corrects punctuation, capitalization, spacing, typographical errors, item-name consistency, and a small number of awkward constructions throughout the game.
- Preserves established major-character voices and intentional joke/synchronization text rather than broadly rewriting the script.
- Retains all active normal/NG+ mirrored callbacks, including the residual-memory dialogue.
- Keeps the v1.16 regional raw-text arena architecture and all accepted gameplay/control behavior unchanged.

---

## New Controls and Ring Shortcuts

Casual Run's final control layout is designed around the fact that normal movement already defaults to running.

### Field Controls

- **A** - Action, interaction, attack, and confirm. This takes over the original B-button role.
- **B** - Walk while held and accelerate weapon charging. This takes over the original A-button walk/charge role.
- **Start** - Open the Boy's **Main Ring**.
- **X** - Open the Boy's **Item Ring** directly.
- **Y** - Open the Boy's **Alchemy Ring** directly.

### Ring Controls

- **A** - Confirm.
- **B** - Cancel / back.
- **Start** - Cancel / back, including closing the Ring.
- **Select** - Switch between the Boy and Dog Rings.

The shortcuts use the game's own remembered Ring-page state rather than simulating menu navigation, so Item and Alchemy open directly without visible intermediate transitions.

### Two-Player Behavior

- The A/B role swap applies to both controllers.
- Player 1 receives the Start/X/Y Ring shortcuts.
- Player 2 does **not** receive the new menu shortcuts.
- Player 2's Start button retains FuSoYa's original multiplayer enable/disable behavior.
- The existing two-player character-ownership and camera behavior is otherwise preserved.

---

## Movement and Weapon Charging

### Run Button Becomes Walk / Fast-Charge Button

- Movement defaults to running whenever running is available.
- Holding **B** makes the controlled character walk.
- Running no longer drains the attack gauge or forces a charge above 100% back down to 100%.
- The attack gauge continues charging normally while running, including above 100%.
- Holding **B** charges the attack gauge at four times the normal rate, both below and above 100%, including while stationary.
- Charging beyond 100% happens automatically unless the attack button is pressed.
- Charge sound effects above 100% are silenced to reduce repeated audio during normal play.
- The Bazooka continues charging in a loop rather than stopping permanently at 100% unless the attack button is held. This makes reloading more deliberate and keeps it from completely overshadowing the other weapons.

---

## Faster Character and Skill Growth

### Character Leveling

- Total cumulative experience required to reach level 99 is approximately half of the original amount.
- The Boy keeps his original level-1 Defense and gains one additional cumulative innate Defense point after every four level-ups.
- The Dog keeps its original level-1 Attack and gains one additional cumulative innate Attack point after every five level-ups.

### Weapon Experience

- Kills credited to either the Boy or Dog can grant weapon-family experience to the Boy's currently equipped weapon family.
- This preserves the inherited shared weapon-family progression while making Dog participation less punishing to the Boy's weapon growth.

### Dog Growth From Sniffing

- Successful ingredient finds give the Dog a small amount of character experience.
- Ingredient pickups found by sniffing also advance the Dog's attack-skill experience.
- This gives normal exploration and sniffing a meaningful long-term benefit without requiring dedicated Dog grinding.

---

## Fixed 50% Alchemy-Family Experience Sharing

The diminishing passive formula experience inherited from the balance patch has been replaced with a predictable family-sharing system.

Every second cast within a family awards one normal, current-level experience tick to every formula in that family.

- The formula actually cast still receives its normal direct experience.
- On every second family cast, the active formula also receives the passive tick.
- Over time, the active formula therefore receives about 150% of normal experience while related formulas receive about 50%.
- Passive experience can accumulate for formulas that have not yet been learned.
- Passive level-ups remain silent.
- All formulas retain the normal level-9 cap.
- The every-second-cast counter is shared by the family, so alternating related formulas still advances the same rhythm.
- Laser remains isolated in its own one-formula family.

| Family | Formulas |
|---|---|
| Enhancement | Atlas, Barrier, Defend, Energize, Force Field, Reflect, Speed |
| Elemental | Acid Rain, Fireball, Fire Power, Flash, Lightning Storm, Slow Burn |
| Restoration | Cure, Heal, Miracle Cure, One Up, Regrowth, Revive, Super Heal |
| Utility | Call Up, Escape, Levitate, Revealer, Stop |
| Offensive | Corrosion, Crush, Double Drain, Drain, Explosion, Hard Ball, Lance, Nitro, Sting |
| Laser | Laser |

---

## Healing, Consumables, and Ingredient Rewards

### Improved Healing Items

- **Petal:** heals 80 HP.
- **Nectar:** heals 200 HP.

### Consumable Cap Increased to 9

The practical carry cap is raised from 6 to 9 for ordinary consumables, including:

- Petals
- Nectar
- Honey
- Dog Biscuits
- Wings
- Essence
- Pixie Dust

Special Honey and Petal reward paths that bypass the normal loot handler are also updated so they respect the new cap.

### Better Ingredient Rewards

- Common ingredient sniff rewards give **2** ingredients instead of 1.
- Normal one-unit enemy ingredient drops give **2** instead of 1.

---

## Economy Changes

- Regular-enemy currency rewards are doubled.
- Boss rewards and scripted currency awards are unchanged.
- The hidden Crustacia desert-crossing Amulet of Annihilation price is reduced from **10,000 to 500 Jewels** for the first crossing.
- The Nobilia Atlas Amulet vendor charges a flat **100 Jewels** per amulet and continually restocks the supply.
- One redundant Nobilia rice vendor is replaced with a convenient bead vendor selling **5 beads for 75 Jewels**.

---

## Boss and Weapon Rebalancing

### Selected Boss HP Reductions

Five longer fights have their maximum HP reduced by 20%:

| Boss | New HP |
|---|---:|
| Salabog | 1,280 |
| Rimsala (Pyramid) | 1,600 |
| Aquagoth | 2,800 |
| Verminator | 3,600 |
| Mungola | 8,000 |

### End-Game Weapon Adjustment

- Laser Lance: base power reduced by 5.
- Neutron Blade: base power reduced by 5.
- Atom Smasher remains unchanged, leaving it as the strongest base weapon of the three.

---

## Charm Rebalancing

| Charm | Effect |
|---|---|
| Armor Polish | Adds 12.5% of equipped armor Defense. |
| Chocobo Egg | +45 maximum HP to both characters, capped at 999. |
| Insect Incense | Prevents insect/arachnid attack routines from hurting the party. |
| Jade Disk | Approximately +2-3 Hit for both characters, capped at 99. |
| Jaguar Ring | Enables the faster Casual Run movement behavior and its revised walk/charge control. |
| Magic Gourd | Ceramic-pot rewards become 50 Jewels instead of the ordinary 10. |
| Moxa Stick | Increases item and alchemy healing by 50%. |
| Oracle Bone | Unlocks additional dialogue and makes Stop available from an alchemist. |
| Ruby Heart | Reduces enemy Hit chance by 15 percentage points. |
| Silver Sheath | Adds 25% of the qualifying sword-family weapon's attack value. |
| Staff of Life | Reads Defense from five levels farther along the stat table. |
| Sun Stone | Reads Attack from five levels farther along the stat table. |
| Thug's Cloak | Adds 5 Evade to both characters, capped at 99. |
| Wizard's Coin | Approximately +10-12 Magic Defense for the Boy and +4-6 for the Dog. |

---

## Map, Navigation, and Progression Changes

### Prehistoria

- Adds the repeatable **New Game Plus** system described below.

### Crustacia

- Fixes the river-bridge bug introduced by the two-player patch.
- Reduces the hidden desert vendor's first-crossing amulet price to 500 Jewels.

### Nobilia

- Atlas Amulets cost 100 Jewels and restock indefinitely.
- A redundant rice vendor is replaced with the 5-beads-for-75-Jewels vendor.
- Fixes the replacement vendor's page/lock behavior so using it cannot trap the player.

### Gothica / Tinker's Area

- The NPC formerly used for the Bursitis exchange is repurposed as a bookshelf/navigation hint.
- Fixes progression when Mungola is defeated before the usual Verminator/Tinker sequence.
- Defeating Mungola through unusual backtracking now establishes a coherent post-imposter, pre-Windwalker state instead of leaving Ebon Keep/Tinker's Tower progression contradictory or softlocked.
- Queen's Key and related dungeon-repeatability state are cleaned up for replay/NG+ behavior.

### Ivory Tower

- Fixes the post-banquet dungeon spawn/progression issue.

### Omnitopia

- The vertical pipes begin opened for faster traversal.
- Certain horizontal-door sentry behavior is suppressed to avoid unnecessary progression friction.

---

## New Game Plus

New Game Plus is an intentionally opt-in feature accessed through **Jade**, an out-of-place older man in a hut in the prehistoric village.

Jade becomes available after the Mammoth Graveyard vipers have been defeated. His dialogue explicitly asks whether the player believes time travel is possible and whether they want to help with an experiment, so NG+ cannot be triggered accidentally.

Activating the experiment resets the game to a stable early-story replay state just after Fire Eyes has asked for help and the Dog has been named.

### Reset

- Story and boss-completion progression needed for another playthrough.
- Doors, switches, bridges, and related event triggers.
- Chests, gourds, and sniff spots.
- Act and map progression state.
- Exhibition Ticket.
- Diamond Eyes.
- Energy Core.
- Queen's Key and other reset-sensitive story inventory handled by the NG+ state cleanup.

### Retained / Changed

- Character levels, learned formulas, equipment progression, and other intended long-term growth are retained unless specifically reset by the NG+ script.
- Jaguar Ring is retained.
- Bazooka is removed.
- Bone Crusher becomes the equipped weapon.
- Early raptor/intro state is deliberately retained so the opening Dog-introduction sequence does not replay.
- The Carltron box-cleaning cameo marker is enabled and also serves as Casual Run's reliable NG+ dialogue marker.

After activation Jade says, **"It worked! Naris will be so proud!"** and later identifies Naris as his son.

### NG+ Dialogue Variations

Several scenes contain subtle alternate dialogue in NG+ suggesting residual memory of the previous cycle. These are selective callbacks rather than a full rewrite and include material involving Fire Eyes, Camellia, Tinker, the arena, Ruffleberg, and Horace.

---

## Dialogue and Movie-Reference Pass

Casual Run includes a targeted dialogue pass replacing selected fictional or placeholder movie references with real-film references while preserving the Boy's movie-obsessed characterization and leaving appropriate in-world titles alone.

References introduced or revised include material drawing on films such as *Mars Needs Women*, *Planet of the Vampires*, *The Poseidon Adventure*, *The Blob*, *Flash Gordon*, *Invasion of the Body Snatchers*, *Spartacus*, *Puppet Master*, *Destroy All Monsters*, *The Adventures of Buckaroo Banzai Across the 8th Dimension*, *The Brave Little Toaster*, and *The Thing*.

This pass also supports the NG+ residual-memory dialogue described above.

---

## Optional MSU-1 Support With Native Music Fallback

Casual Run integrates the Conn/RedScorpion MSU-1 v3 track numbering and loop policy into the expanded ROM without sacrificing the original soundtrack.

- With no MSU-1 hardware/files available, the game uses the original SPC soundtrack normally.
- If MSU-1 is available and the requested PCM track exists, the MSU track plays.
- If an expected PCM track is missing, Casual Run falls back to the native SPC soundtrack and keeps native music ownership for the remainder of that play session.
- This prevents a later MSU track from layering over already-running SPC music.
- A reset/power cycle makes MSU-1 eligible again.
- The old MSU patch's permanent SPC mute is **not** used.

Historical PCM packs use the basename `soe_msu`, for example:

- `soe_msu.sfc`
- `soe_msu.msu` (if the emulator/core expects a marker file)
- `soe_msu-0.pcm`
- `soe_msu-1.pcm`
- and so on.

The PCM music files themselves are not part of Casual Run.

---

## Presentation Changes

- Internal ROM title changed to **SoE Casual Run**.
- The title screen includes a **CASUAL RUN** tag.
- Jaguar Ring tutorial text is updated for the final B-button walk/charge control.

---

## Inherited Two-Player Support by FuSoYa

Casual Run retains FuSoYa's two-player foundation, with later control integration layered on top.

- Player 2 can join or withdraw using the retained multiplayer Start behavior.
- Either controller can control either character through the existing ownership system.
- A controller indicator shows character ownership.
- Existing single-player character switching and multiplayer camera behavior are preserved where not superseded by the Ring-specific controls described above.
- Casual Run applies its A/B control-role swap to both controllers while reserving Start/X/Y Ring shortcuts for Player 1.

---

## Inherited Bug Fixes by Ninakoru

- Corrects a sound-delay problem seen in many SNES emulators.
- Corrects stat-magic wear-off behavior, preventing stacked-stat exploits involving death, resurrection, and Pixie Dust.
- Prevents the extreme Atlas-related damage/stat exploit associated with saving while the effect is active.
- Miracle Cure also removes Confound/reversed-control status.

---

## Selected Balance-Patch Changes by Ninakoru

Casual Run retains selected parts of Ninakoru's balance work where they fit the project's faster, lower-friction design.

- Rebalances weapon charge multipliers and base damage, particularly overpowered level-three attacks.
- Rebalances weapon base damage so progression between weapons is more meaningful.
- Uses shared weapon-family experience: every fourth qualifying kill grants experience to related weapons in the equipped weapon's family, including weapons not yet acquired.
- Caps physical evasion at 64%, preventing extreme Speed-based evasion exploits.
- Rebalances the formula learning-rate table to reduce excessive grinding.
- Reduces Cryo-Blast's base damage from 800 to 600.
- Rebalances individual formulas, including reduced Heal and Crush strength and improved later offensive formulas.
- Adjusts Speed, Regrowth, Barrier, and other effect durations.
- Changes Barrier's Limestone requirement to an Atlas Amulet to limit repeated near-invulnerability.
- Rebalances the Boy's Attack, Dog's Defense, and both characters' Magic Defense development.
- Reduces helmet and bracelet Defense bonuses by roughly 30%.
- Reduces the toaster Dog's bonuses from +80 Attack/+250 Defense to +70/+180.
- Rebalances statistics of various enemies and bosses, with some values later overwritten by Casual Run changes.
- Corrects the space-station Aquagoth tentacles to use the intended stronger version.
- Adds Guardbots and strengthens upper-floor Neo Greebles in the space-station area.

Not every feature of the original balance patch is included. Changes that conflicted with Casual Run's design were deliberately omitted or reverted; for example, Casual Run does **not** keep the restriction that prevented alchemy casting below 100% weapon charge.

---

## Bug Fixes by assassin17

- **Silver Sheath fix:** the sword-damage bonus is applied only after the Silver Sheath has actually been obtained. The unmodified game effectively applies the bonus regardless of ownership.
- **Infinite Bazooka Ammo fix:** Particle Bomb and Cryo-Blast ammunition is properly consumed.
- **Bazooka leveling/interface fix:** the Bazooka begins at level one and its equipped-weapon/ammunition information is handled correctly.

---

## Known Remaining Limitation

- A rare Tiny/Pyramid progression problem is still noted. The NG+ system provides a practical escape/recovery path, but the underlying edge case is not claimed as fully repaired.
- Old save files already damaged by superseded experimental Tinker/Windwalker builds are not specifically repaired. Current v1.17 progression logic is designed to prevent that bad state from being created going forward.

---

## Applying the Patch

Apply `Casual_Run_Patch_v117.ips` to a **clean, unheadered U.S. ROM** using an IPS-compatible patcher.

### Required Base ROM

- Game: *Secret of Evermore (USA)*
- Header: none / unheadered
- Expected size: **3,145,728 bytes**
- SHA-256: `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`

### Expected Patched ROM

The patch expands the ROM to 4 MiB.

- Expected size: **4,194,304 bytes**
- v1.17 SHA-256: `ff1ffb57e4c5ba96f18ae912cbf327f49b51fd89e90467f2519ce7aa8a51c068`
- SNES checksum/complement: `4E33 / B1CC`

This is the accepted v1.17 release ROM produced by the authoritative source and release IPS.

---

## Version Highlights

| Version | Major Change |
|---|---|
| v0.09 | Two-player/balance foundation, default running, walk/fast-charge control, charge preservation while running. |
| v0.10 | Atlas Amulet vendor changed to 100 Jewels with unlimited restocking. |
| v0.11 | Double regular-enemy currency, consumable-cap work, Dog kills contribute to Boy weapon growth, boss HP reductions, first desert crossing 500. |
| v0.12 | Slightly faster Boy Defense and Dog Attack growth. |
| v0.14 | Stable 50% alchemy-family experience sharing. |
| v0.16 | Petal/Nectar improvements and doubled common ingredient rewards. |
| v0.17 | Sniffing advances Dog growth; above-100% charge audio silenced. |
| v0.18 | Charm-effect rebalance. |
| v0.19 | Character EXP curve reduced to about half through level 99. |
| v0.20-v0.21 | Jade/New Game Plus established in its current form. |
| v0.23-v0.25 | Nobilia bead vendor, navigation/progression fixes, end-game weapon adjustment, Mungola/Tinker safeguard. |
| v1.00 | Internal ROM title changed to SoE Casual Run. |
| v1.02 | Stable Mungola/Tinker/Windwalker progression-state fix. |
| v1.03 | Final CASUAL RUN title-screen treatment. |
| v1.04 | Real-film dialogue pass and NG+ residual-memory dialogue. |
| v1.05 | MSU-1 support with safe native-SPC fallback. |
| v1.06 | Final A/B controls and direct Start/X/Y Ring shortcuts. |
| v1.07 | Source flattened to one authoritative ASM file; no gameplay-byte changes from v1.06. |
| v1.08 | Status-aware ordinary-enemy drops; Drain / Double Drain rebalance. |
| v1.09 | Secondary-menu B-back/display cleanup; Dog Equipment replaces Control Prefs; Dog main Ring removed from normal access. |
| v1.10 | Tiny's-lair leave/re-entry softlock prevention. |
| v1.11-v1.14 | Major-character script passes for Fire Eyes/Elizabeth, Horace, Camellia/Queen Bluegarden, and Ruffleberg/Carltron. |
| v1.15 | Redundant Targeting command removed from the Boy Main Ring. |
| v1.16 | Live story text reorganized into documented regional raw-text arenas with reserved expansion space. |
| v1.17 | Full 25-arena story/world script review completed and promoted as the official release. |

---

## Credits and Source Lineage

Casual Run is cumulative work built on several earlier community projects and fixes:

- **FuSoYa** - two-player foundation.
- **Ninakoru** - balance-patch work and bug fixes selectively incorporated into Casual Run.
- **assassin17** - Silver Sheath, Bazooka-ammo, and Bazooka-level/interface fixes incorporated into the foundation.
- **Conn / RedScorpion** - original Secret of Evermore MSU-1 v3 implementation whose track numbering and loop policy were ported into Casual Run's fallback-safe MSU system.
- **Casual Run project** - cumulative QoL, control, economy, growth, New Game Plus, progression, dialogue, title-screen, MSU integration, and source-recovery/maintenance work described above.

---

## Design Note

Casual Run intentionally does **not** try to automate every useful action. Earlier development experimented with automatic healing and repeat-last-alchemy shortcuts, but these were dropped. Direct access to the Item and Alchemy Rings proved faster, more flexible, easier to understand, and more consistent with *Secret of Evermore*'s original interface.

The current control scheme is considered final.

--

## Technical References

For **Secret of Evermore–specific technical documentation**, these have been the most useful, roughly in order of how much they have contributed to the Casual Run project:

1. **Data Crystal / TCRF – Secret of Evermore ROM & RAM maps**
   Probably the single most useful general reference. The SoE pages document the ROM format, known ROM regions, WRAM locations, entity structures, charms/progression flags, enemy-stat layout, drop-chance byte, interrupt-related state, and a lot of other low-level information. We have repeatedly used it as the first reference point before verifying something directly against the ROM. ([Data Crystal][1])
   [Secret of Evermore on Data Crystal](https://datacrystal.tcrf.net/wiki/Secret_of_Evermore?utm_source=chatgpt.com)

2. **RAMsetta Stone for Secret of Evermore – CleanCodeX/XETH**
   Extremely valuable for **SRAM ↔ WRAM relationships and structured save/player data**. This was especially useful for HP, stats, inventory, alchemy levels, equipment, and other persistent state. It gave us a more structured view than the older flat RAM maps.
   [RAMsettaStone.SoE on GitHub](https://github.com/CleanCodeX/RAMsettaStone.SoE?utm_source=chatgpt.com)

3. **RustyBlazer – hellow554**
   The most useful source we found when we needed something closer to an actual **bank-by-bank SoE disassembly** rather than just address lists. Its labels and reconstructed routines were particularly valuable when tracing controller handling, Ring-menu logic, item/alchemy routines, and general engine flow. It is not always identical to the exact patched ROM we are working from, so we still verify bytes against our ROM, but it is excellent for establishing what native code is trying to do.
   [RustyBlazer on GitHub](https://github.com/hellow554/RustyBlazer?utm_source=chatgpt.com)

4. **Evermizer – black-sliver**
   Probably the strongest existing body of **modern SoE ROM-hacking source code**. Because Evermizer actually changes a huge range of game systems, its source and patch files expose useful ROM addresses, item/action IDs, alchemy structures, script locations, ring-menu data, progression requirements, and known engine quirks. We have used it both as documentation and as independent corroboration of things discovered in the ROM. ([GitHub][2])
   [Evermizer source](https://github.com/black-sliver/evermizer?utm_source=chatgpt.com)

5. **Awesome Secret of Evermore – maluramichael**
   Less a reverse-engineering project itself and more the best **index/archive of SoE technical work**. It points to and preserves tools, ROM hacks, RAM documentation, the Gameplay Balance Patch, FuSoYa's two-player patch, assassin17's fixes, SecretOfEverhack, SoETilesViewer, SRAM utilities, and other material that would otherwise be scattered or lost. It has been invaluable for discovering older work. ([GitHub][3])
   [Awesome Secret of Evermore](https://github.com/maluramichael/awesome-secret-of-evermore?utm_source=chatgpt.com)

6. **SecretOfEverhack – Gemini/Loboto3**
   Especially useful for the **text engine**. It contains the SoE translation toolchain, text extraction/reinsertion code, text pointer rebuilding, menu-text handling, and assembly intended to work around the game's dialogue compression. That made it one of the more useful references when our work moved beyond simple fixed-length string replacement and into relocated script/text banks. ([GitHub][4])
   [SecretOfEverhack on GitHub](https://github.com/Gemini-Loboto3/SecretOfEverhack?utm_source=chatgpt.com)

7. **FuSoYa's Secret of Evermore 2-Player Edition / FuSoYa's Niche**
   Crucial because Casual Run inherits FuSoYa's multiplayer implementation. The public documentation is not a full disassembly, but the patch itself and associated material establish the controller-ownership model and multiplayer behavior we have had to preserve. A large part of the controls work only made sense once we stopped assuming that the patched engine's Boy/Dog input paths were synonymous with controller 1/controller 2. FuSoYa's site still hosts the SoE 2 Player Edition section. ([FuSoYa's Niche][5])
   [FuSoYa's Niche](https://fusoya.eludevisibility.org/?utm_source=chatgpt.com)

8. **Ninakoru's Secret of Evermore Gameplay Balance Patch + assassin17's bug-fix work**
   These have been less like general-purpose documentation and more like **documented prior research into specific engine systems**. Ninakoru's work gave us known-good implementations and observations around combat formulas, weapon EXP, alchemy growth, stats, charms, enemies, equipment, and other balancing systems. assassin17's patches supplied proven fixes for Silver Sheath behavior, Bazooka ammunition, and Bazooka level/interface issues. The Awesome SoE archive has been especially useful for keeping this older material accessible. ([GitHub][3])

9. **Zeldix + RetroAchievements' SoE/MSU documentation**
   These became particularly important for the **MSU-1 port**. The Conn/RedScorpion implementation provided the original SoE-specific MSU code, track numbering, loop information, NMI/request handling, and manifests. RetroAchievements was also useful for verifying recognized vanilla, FuSoYa, and MSU ROM identities/hashes. ([RetroAchievements][6])
   [Zeldix](https://www.zeldix.net/?utm_source=chatgpt.com)

10. **GameFAQs / Secret of Evermore Wiki / older gameplay guides**
    These have been secondary rather than assembly references, but useful when we need to establish **intended gameplay behavior**: formulas, item effects, missables, progression order, obscure interactions, boss/stat information, or whether something we observe is actually vanilla behavior. They are best treated as leads to verify rather than authoritative ROM documentation.
