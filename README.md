# Secret of Evermore - Casual Run Patch

This patch is a cumulative IPS patch for the unheadered U.S. release of *Secret of Evermore*. It includes the FuSoYa's two-player patch, builds on Ninakoru's gameplay-balance work, and includes several of assassin17's bugfixes, while also making various adjustments and additional control and logic edits. The end goal is to remove glitches, make gameplay faster, and reduce grinding, while leaving the core gameplay experience intact.

## Version 0.12

### Slightly faster character-stat growth

- The boy retains his original level-1 Defense and gains one additional cumulative innate Defense point after every four level-ups.
- The dog retains its original level-1 Attack and gains one additional cumulative innate Attack point after every five level-ups.

These are changes to the characters' innate level-growth tables. Equipment and temporary effects are applied separately.

| Innate stat | Level | v0.11 | v0.12 |
|---|---:|---:|---:|
| Boy Defense | 1 | 5 | 5 |
| Boy Defense | 30 | 34 | 41 |
| Boy Defense | 40 | 44 | 53 |
| Dog Attack | 1 | 17 | 17 |
| Dog Attack | 30 | 119 | 124 |
| Dog Attack | 40 | 154 | 161 |

### Temporary effects are not retained by saving

- Saving does not cure the current session. Active effects continue normally until they expire, are removed, or the save is reloaded.
- The save buffer receives the characters' unmodified base stats, empty temporary-status slots, zero temporary modifiers, and cleared status-outline state.
- Loading removes temporary positive and negative effects such as Atlas, Defend, Speed, Poison, Plague, Regrowth, and related statuses. The proper unmodified stats are restored first, preventing a discarded effect from becoming a permanent stat change.
- Older save files that still contain serialized temporary effects are normalized when loaded under v0.12.

The reordered save/load foundation is assassin17's `StaSav-U` fix. v0.12 adds explicit save-buffer and load-time cleanup around that reviewed fix.

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

## Version 0.11.1

- Corrects the consumable-cap implementation from v0.11. Field pickups and ordinary rewards allow Petals, Nectar, Honey, Dog Biscuits, Wings, Essence, and Pixie Dust to reach 9 before displaying the full-inventory message.
- Updates special Honey and Petal reward paths that bypass the ordinary loot handler.
- Restores eight glove and collar inventory checks that v0.11 changed accidentally. Their original limit remains 6.

## Version 0.11

- Doubles the table-based currency reward for regular enemies. Boss rewards and scripted currency awards are unchanged.
- Raises the inventory limit for Petals, Nectar, Honey, Dog Biscuits, Wings, Essence, and Pixie Dust from 6 to 9. Call Beads retain their normal 99 limit.
- Kills credited to either the boy or dog now grant weapon experience to the boy's currently equipped weapon family.
- Reduces the maximum HP of five longer bosses by 20%:

| Boss | New HP |
|---|---:|
| Salabog | 1,280 |
| Rimsala (Pyramid) | 1,600 |
| Aquagoth | 2,800 |
| Verminator | 3,600 |
| Mungola | 8,000 |

- Lowers the hidden Crustacia vendor's Amulet of Annihilation price from 10,000 to 500 Jewels.

## Version 0.10

- The Atlas Amulet vendor charges a flat 100 Jewels per amulet.
- The vendor continually restocks Atlas Amulets to 99, so the supply does not run out.

## Version 0.9

- Incorporates the other base patches.
- Fixes the Crustacia river-bridge bug.
- Makes the bridge fix work for both players on the two-player ROM base.
- Incorporates assassin17's Silver Sheath fix and Infinite Bazooka Ammo fix.

## Version 0.8

- Holding the former run button makes the character walk, so it functions as a walk button.
- Holding the walk button charges the attack gauge at four times the normal rate, both below and above 100%. This also works while stationary.
- Removes the repetitive 100%-charged sound.

## Version 0.7

- The attack gauge continues charging at its normal rate while running, including above 100%.
- Weapon charging beyond 100% happens automatically unless the attack button is pressed.

## Version 0.6

- Movement defaults to running whenever running is available.
- Running no longer drains the attack gauge or forces a charge above 100% back to 100%.

## Applying the patch

Apply `Casual_Run_Patch.ips` to a clean, unheadered U.S. ROM using an IPS-compatible patcher.

- Expected base-ROM size: 3,145,728 bytes
- Expected base-ROM SHA-256: `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`
