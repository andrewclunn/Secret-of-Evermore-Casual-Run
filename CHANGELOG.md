# Changelog

## 2.4

- Successful sniffed-ingredient pickups now award Dog growth according to form:
  Prehistoric 10 character EXP / 4 attack-skill points; Sacred Dog 100 / 2;
  Poodle 1,000 / 1. Podunk and Toaster retain 50 / 4.
- Ingredient identities, quantities and capacity checks are unchanged. Progress
  remains shared between forms. Native attack-skill notifications and the level-3
  cap are retained; large EXP awards process all earned character levels.
- A one-pixel blue silhouette outline around the Boy's portrait indicates that
  the reflection is absent and ready to summon. Active reflections, cooldowns
  and unavailable formation suppress it.
- Oracle Bone transformations briefly brighten the Dog's palette. Existing
  combat stats, HP and form-specific movement speeds are retained.
- Magic Gourd description: "Player 3: press START to summon or dismiss a shadow copy."
- Oracle Bone description: "Press L to change your dog's form. R makes him sniff."
- Promoted the user-approved 2.4 test without changing ROM bytes. Reward, cap,
  full ingredient pickup, control, visual and reflection regression checks pass;
  both descriptions were visually verified in the native rare-item menu.

## 2.3

- With the Oracle Bone, press L to cycle Prehistoric Dog → Sacred Dog → Poodle
  → Prehistoric Dog. Holding L changes form once. Toaster Dog ignores L.
- Player 1 controls this in single-player, whether controlling the Boy or Dog.
  When player 2 controls the Dog, only player 2 can transform it.
- R retains native sniff behavior in single-player and co-op. L no longer
  commands sniff, including before acquiring the Oracle Bone.
- Uses native form graphics, portraits, palettes and stat recalculation;
  transformations preserve current HP and level. Native scripted form changes
  retain priority.
- Headless tests cover the unlock, cycle, held-button behavior, toaster,
  controller ownership, sniffing and transformations alongside the reflection.
  The existing reflection regression suite also passes on this build.
- Promoted the user-tested Dog Forms build without changing ROM bytes; updated
  the default build, player guide and release artifacts to 2.3.

## 2.2

### Third-player reflection

- The Magic Gourd enables an optional third human-controlled player alongside
  the Boy and Dog. Use a Multitap in physical controller port 2 and press Start
  on logical controller 3 to form or dismiss the reflection.
- The reflection uses the Boy's existing jeans blues across its whole body,
  including skin, hair and outlines. It has no AI, menus or NPC interaction.
- Each formation captures the Boy's current HP, equipped weapon and combat
  record. Later changes to the Boy do not update that reflection. Its HP can
  decrease but cannot be restored; HP and charge meters are hidden.
- Controller 3 uses the D-pad to move, A to attack and B to walk/charge faster.
  Its position, HP and charge are independent of the original party.
- Formation requires both ordinary party members to be present and alive, an
  equipped weapon, an area permitting attacks, and available normal gameplay.
- Dismissal and event/room despawns use a two-second cooldown; death uses one
  minute. The timers advance during gameplay. Press Start again to reform.
- The clone is excluded from single and multiple spell target selection,
  avoiding the targeting freeze encountered during testing.
- Corrected three inherited ROM-title checks that prevented controller 2 from
  joining Casual Run. Player 2 can control the Dog while the clone is active.

### Reward changes

- Defeating the final/third Dark Forest copy grants the Magic Gourd if missing.
  The original Nobilia trade remains available, allowing an earlier unlock.
- The Crusader Sword moves from the Dark Forest copies to Footknight's
  chessboard victory scene, after the existing checkmate dialogue.
- Already-owned rewards skip their grant and acquisition notification. An
  already-owned Crusader Sword also leaves current equipment alone.

### Release and documentation

- Updated the cumulative player guide, installation links, build default,
  save-state/Multitap instructions, credits and outstanding work.
- Reused the approved PoC 04 ROM bytes for this release. Its source, ROM and
  full IPS-from-clean build are verified to reproduce the same output.
- The optional three-player feature still has limited campaign coverage. Full
  enemy/area-spell and status immunity, all weapon EXP paths, palette pressure
  and every boss/cutscene interaction remain areas for further testing. See
  [technical notes](Build/ShadowPrototype/README.md) for the precise coverage.

## 2.1

- Added a dedicated borderless Boy dialogue style for the opening Podunk and
  initial laboratory scenes. The new style uses a blank background with no
  frame, lower-screen placement and the Boy's existing text voice.
- Routed those opening Boy passages through the new style while keeping later
  ordinary Boy dialogue, Carltron and Professor presentation unchanged.
- Preserved the style's borderless container setting when constructing the
  text window. The normal bordered Boy style still handles later dialogue,
  including the subsequent "Now what?" passage.

## 2.0

The cumulative baseline introduced the revised story/world dialogue and speaker
presentation, contextual save conversations, regional enemy-drop economy,
expanded quality-of-life and progression fixes, native-audio baseline, two-player
integration, controls/menu changes and optional New Game Plus described in the
[player guide](README.md).
