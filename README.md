# Secret of Evermore - Casual Run Patch - Version 0.18

## Current Bugs to Fix

## Patch Summary

This patch is a cumulative IPS patch for the unheadered U.S. release of *Secret of Evermore*. It includes the FuSoYa's two-player patch, builds on Ninakoru's gameplay-balance work, and includes several of assassin17's bugfixes, while also making various adjustments and additional control and logic edits. The end goal is to remove glitches, make gameplay faster, and reduce grinding, while leaving the core gameplay experience intact.

To that end the main new changes are turning the run button into a walk / charge-speed-up button, making running not interrupt waepon charging, increased currency and ingredient drops, changes to attack skill and alchemy experience growth, an experimental new game plus feature, and several other balancing and bug fix changes. A more complete change list is below.

## New Features

### Run Button Becomes Walk Button

- Movement defaults to running whenever running is available.
- Holding the former run button makes the character walk, so it functions as a walk button.
- Running no longer drains the attack gauge or forces a charge above 100% back to 100%.

### Improved Weapon Charging

- The attack gauge continues charging at its normal rate while running, including above 100%.
- Removes all attack meter charging sound effects.
- Weapon charging beyond 100% happens automatically unless the attack button is pressed.
- Holding the walk button charges the attack gauge at four times the normal rate, both below and above 100%. This also works while stationary.

### Improved Healing Items

- Petals and Nectars are now not so useless.

### Better Sniff Rewards

- More ingredients found when following your dog's nose.
- The dog gains a small amount of experience when you find ingredients on the ground.
- Picking up ingredients on the ground is also now how the dog gains attack level experience.

### Slightly faster character-stat growth

- The boy retains his original level-1 Defense and gains one additional cumulative innate Defense point after every four level-ups.
- The dog retains its original level-1 Attack and gains one additional cumulative innate Attack point after every five level-ups.

### Fixed 50% alchemy-family experience sharing

The diminishing passive formula experience inherited from the balance patch has been replaced. Every second cast within a family awards one normal, current-level experience tick to every formula in that family.

- The formula actually cast still receives its normal direct experience.
- On every second family cast, the active formula also receives the passive tick. Over time, that gives the active formula 150% of normal experience while its family members receive 50%.
- Passive experience includes formulas that have not been learned yet.
- Passive level-ups remain silent and all formulas retain the normal level-9 cap.
- The cast counter is shared by the family, so alternating between two related formulas still advances the same every-second-cast rhythm.
- Laser remains isolated in its own one-formula family.

| Family | Formulas |
|---|---|
| Enhancement | Atlas, Barrier, Defend, Energize, Force Field, Reflect, Speed |
| Elemental | Acid Rain, Fireball, Fire Power, Flash, Lightning Storm, Slow Burn |
| Restoration | Cure, Heal, Miracle Cure, One Up, Regrowth, Revive, Super Heal |
| Utility | Call Up, Escape, Levitate, Revealer, Stop |
| Offensive | Corrosion, Crush, Double Drain, Drain, Explosion, Hard Ball, Lance, Nitro, Sting |
| Laser | Laser |

### Consumable-cap Set to 9

- Field pickups and ordinary rewards allow Petals, Nectar, Honey, Dog Biscuits, Wings, Essence, and Pixie Dust to reach 9.
- Updates special Honey and Petal reward paths that bypass the ordinary loot handler.

### Double Currency Rewards

- Doubles the table-based currency reward for regular enemies.
- Boss rewards and scripted currency awards are unchanged.
- Normal one-unit enemy ingredient drops give two instead of one.

### Dog Kills Count for Boy's Weapon Experience

- Kills credited to either the boy or dog now grant weapon experience to the boy's currently equipped weapon family.

### Boss HP Rebalancing

- Reduces the maximum HP of five longer bosses by 20%:

| Boss | New HP |
|---|---:|
| Salabog | 1,280 |
| Rimsala (Pyramid) | 1,600 |
| Aquagoth | 2,800 |
| Verminator | 3,600 |
| Mungola | 8,000 |

### Cheaper Initial Amulet of Annihilation

- Lowers the hidden Crustacia vendor's Amulet of Annihilation price from 10,000 to 500 Jewels.

### Endless Atlas Amulet

- The Atlas Amulet vendor charges a flat 100 Jewels per amulet.
- The vendor continually restocks Atlas Amulets to 99, so the supply does not run out.

### Crustacia River-Bridge Bug Fixed

- Fixes the Crustacia river-bridge bug introduced by the two-player patch.

### Charm Rebalancing

| Charm         | Effect                                                               |
|---|---:|
| Armor Polish   | Adds 12.5% of equipped armor Defense                                |
| Chocobo Egg    | +45 maximum HP to both characters, capped at 999.                   |
| Insect Incense | Prevents insect/arachnid attack routines from hurting the party.    |
| Jade Disk      | Approximately +2–3 Hit for both characters, capped at 99.           |
| Jaguar Ring    | Enables auto-run                                                    |
| Magic Gourd    | Ceramic-pot rewards become 50 Jewels instead of the ordinary 10.    |
| Moxa Stick     | Increases item and alchemy healing by 50%                           |
| Oracle Bone    | Unlocks additional dialogue and Stop is available from an alchemist.|
| Ruby Heart     | Reduces enemy Hit chance by 15 percentage points                    |
| Silver Sheath  | Adds 25% of the qualifying sword-family weapon’s attack value.      |
| Staff of Life  | Reads Defense from five levels farther along the stat table.        |
| Sun Stone      | Reads Attack from five levels farther along the stat table.         |
| Thug’s Cloak   | Adds 5 Evade to both characters, capped at 99                       |
| Wizard’s Coin  | Approximately +10–12 Magic Defense for the boy and +4–6 for the dog |

### New Game Plus

NOTE - The New Game Plus has intentionally been removed due to causing bugs, and will be readded in a later revision. It is preserved as the feature functionality is intended to be re-added in a later version.

The device is deliberately repeatable and does not create an automatic save.

#### What New Game Plus retains

- Boy and dog names, levels, experience, and permanent character growth
- Owned weapons, the equipped weapon, and weapon levels/experience
- Learned alchemy formulas and their levels/experience
- Equipment, charms, rare items, ingredients, consumables, and ammunition
- Currencies and ordinary trade goods

Temporary positive and negative statuses are cleared, both characters are healed, both party members are made available, and the dog returns to its Act 1 wolf form.

#### What New Game Plus resets

The first pass broadly resets the normal progression windows used by:

- Boss and story completion
- Doors, switches, bridges, and other event triggers
- Chests, gourds, and sniff spots
- Major story keys and the Exhibition Ticket
- Act and map progression state

It then deliberately restores the state immediately after the raptor recovery so that the opening tutorial is not replayed and the next objective is Bugmuck.

## Inherited Changes

### Full Two-Player Support by FuSoYa

- Either controller can join or withdraw using Start.
- Either player can control either character.
- A controller indicator shows character ownership.
- Select switches characters in single-player or changes camera focus in multiplayer.

### Bug Fixes by Ninakoru

- Corrects a sound-delay problem seen in many SNES emulators.
- Corrects stat-magic wear-off behavior, preventing stacked-stat exploits involving death, resurrection, and Pixie Dust.
- Prevents the extreme Atlas-related damage/stat exploit associated with saving while the effect is active.
- Miracle Cure also removes Confound/reversed-control status.

### Balance Patch Updates by Ninakoru

- Rebalances weapon charge multipliers and base damage, particularly overpowered level-three attacks.
- Rebalances weapon base damage so weapon progression is more meaningful across the game.
- Introduces shared weapon-family experience: every fourth qualifying kill grants experience to other weapons in the equipped weapon’s family, including weapons not yet acquired.
- Caps physical evasion at 64%, preventing extreme Speed-based evasion exploits.
- Rebalances the formula learning-rate table to reduce excessive grinding.
- Reduces Cryo-Blast’s base damage from 800 to 600.
- Rebalances individual formulas, including reduced Heal and Crush strength and improved later offensive formulas.
- Adjusts Speed, Regrowth, Barrier, and other effect durations.
- Changes Barrier’s Limestone requirement to an Atlas Amulet to limit repeated near-invulnerability.
- Rebalances the boy’s Attack, dog’s Defense, and both of their Magic Defense development.
- Reduces helmet and bracelet Defense bonuses by roughly 30%.
- Reduces the toaster dog’s bonuses from +80 Attack/+250 Defense to +70/+180.
- Rebalances the statistics of various enemies and bosses.
- Corrects the space-station Aquagoth tentacles to use the intended stronger version.
- Adds Guardbots and strengthens the upper-floor Neo Greebles in the space-station area.
- NOTE Several features of this balance patch were seen as not compatible with the vision of the Casual Run patch, and so were specifically not included / removed. They are not mentioned here precisely because they were not included (an example being the limitation on casting alchemy when below 100% weapon charge.)

### Bug Fixes by assassin17

- Silver Sheath fix: the sword-damage bonus is applied only after the Silver Sheath has actually been obtained. The unmodified game effectively applies it whether owned or not.
- Infinite Bazooka Ammo fix: Particle Bomb and Cryo-Blast ammunition is properly consumed.
- Bazooka leveling/interface fix: the Bazooka begins at level one and its equipped-weapon and ammunition information is handled correctly.

## Applying the patch

Apply `Casual_Run_Patch.ips` to a clean, unheadered U.S. ROM using an IPS-compatible patcher.

- Expected base-ROM size: 3,145,728 bytes
- Expected base-ROM SHA-256: `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`
