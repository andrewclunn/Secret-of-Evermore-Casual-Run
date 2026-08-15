# Casual Fun Patch

`Casual_Run_Patch_v011.ips` is a cumulative IPS patch for the unheadered U.S. release of *Secret of Evermore*. It includes the FuSoYa's two-player patch and Ninakoru's gameplay-balance work.

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

Apply `Casual_Run_Patch_v011.ips` to a clean, unheadered U.S. ROM using an IPS-compatible patcher.

- Expected base-ROM size: 3,145,728 bytes
- Expected base-ROM SHA-256: `17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db`
