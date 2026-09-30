# MSU-1 Experiment - Findings and 3.0 Reimplementation Notes

This document records the Casual Run MSU-1 work that was active from v1.05 through v1.29 and
was withdrawn from the production 2.0 line in v1.30.

MSU-1 itself is **not abandoned**. It is deliberately moved to the 3.0 roadmap so it can be
reimplemented from a clean native-audio baseline rather than carrying forward an interception
path that full-game QA proved unsafe.

## Production decision

v1.30 uses Secret of Evermore's native SPC music path end to end. Casual Run no longer hooks the
native music-change routine, accesses MSU-1 registers, ships an active loop-policy table, or
requires external PCM files.

The older v1.05/v1.18 implementation should be treated as historical research only. Do not
re-enable its hooks in the 2.0 source.

## What the earlier MSU work accomplished

The experiment was useful and solved several real problems before the later regression was found.

### v1.05

Casual Run ported the Conn/RedScorpion Secret of Evermore MSU-1 approach into its expansion-ROM
layout and retained the established numeric track mapping and loop policy.

The first Casual Run backend had two important limitations:

- a successful MSU request could skip native SPC song initialization, which disturbed native
  sound-effect state;
- one missing PCM could latch the session back to native music instead of allowing later MSU
  tracks to recover.

### v1.18

The backend was rewritten around per-request fallback:

- native SPC song data was always initialized;
- a valid PCM could mute only native music and then start the external track;
- a missing PCM fell back for that request only;
- later MSU tracks could still play;
- loop/one-shot policy was resolved before native SPC processing.

Targeted regression testing passed the intended sequence:

1. available one-shot PCM;
2. missing PCM with native fallback;
3. later available looping PCM.

That testing established that the backend could handle the obvious MSU/native handoff cases. It
did **not** prove that the hook preserved every native music-request semantic throughout the game.

## Full-game regression that invalidated the v1.18 production path

Later full-game QA exposed deterministic music changes in places that normally **do not start a
new song at all**. They should simply inherit whatever music is already playing.

Two reproducible examples were particularly useful:

- an affected Horace scene began playing the short, rapidly looping cue heard during the opening
  ship descent immediately before the crash;
- entering the Nobilia Windwalker/takeoff room began playing music associated with the space
  station.

These were valid, recognizable pieces of game audio, but the important bug was not which songs
were selected. The important bug was that **a new song was being started in a context that should
not have changed music**.

Reloading a save did not reset or cure the behavior. This was not treated as a transient
post-flight or save-state audio-state problem.

## Isolation tests

| Test | Change | Result | Conclusion |
| --- | --- | --- | --- |
| Music expansion foundation | Existing song-pointer table relocated for future IDs | Wrong-song behavior observed in full-game QA | The bug became visible on the expanded audio development line, but this alone did not identify the cause. |
| Audio QA1 - hybrid table | IDs 0-70 read directly from the original `$81:9903` table; only future IDs used the expansion table | **Failed** - unintended song changes remained | Relocating existing song pointers was **not** the direct cause. |
| Audio QA2 - native music routine | Restored the native music-change routine while the Audio QA1 hybrid pointer-table diagnostic remained in place; MSU helpers became unreachable | **Passed** - problem disappeared | The active v1.18 MSU interception path is the confirmed regression source; the existing-song pointer relocation was not required for the failure. |
| v1.30 production rollback | Removes all active Casual Run MSU hooks/helpers/tables and leaves native audio in control | Promoted from the QA2 result | Stable 2.0 baseline; MSU deferred to 3.0. |

## What is proven

1. **The wrong-song bug is not fixed by returning existing song IDs to the original pointer table.**
   Audio QA1 did exactly that and the problem remained.

2. **Restoring the native music-change routine fixes the observed problem even while the hybrid pointer-table diagnostic remains.**
   Audio QA2 removed the interception from active playback and the affected scenes behaved
   correctly again. This is especially useful because it separates the playback-control bug from
   the pointer-table experiment.

3. **The v1.18 interception path therefore changes native behavior in at least some no-change
   contexts.**

4. **The old targeted MSU regression suite was incomplete.**
   It tested available/missing/available playback transitions but did not test rooms and
   cutscenes whose correct behavior is to preserve the currently playing music.

## What is not proven

The exact lower-level mechanism is still open. The current evidence does **not** justify claiming
that the root cause is any one of the following without new trace data:

- a particular song ID or pointer-table offset;
- a bad PCM loop-policy value;
- corrupted native SPC sequence data;
- a save-file problem;
- one specific sentinel/control value;
- one specific event script;
- one particular MSU register transaction.

The v1.18 hook was intentionally placed after the native zero/same-song guards, yet full-game
behavior still differed from native. That means our model of the routine's complete semantic
contract was incomplete. The next implementation should be based on tracing that contract rather
than on another local patch around the two known scenes.

## Engineering lessons

### "No music change" is a first-class behavior

A music backend cannot be validated only by checking that requested songs play correctly. It must
also prove that transitions which intentionally inherit current music remain true no-ops.

### Let native code decide whether a change happens

The preferred 3.0 direction is to preserve the native decision path as long as possible. Rather
than replacing control flow early and attempting to reconstruct native semantics, external audio
should mirror a **confirmed native music change** after the game has decided that a change really
is required.

This is a design direction, not yet a proven hook location.

### Separate music expansion from MSU interception

Adding new native song IDs and replacing native playback with MSU are separate engineering
problems. They should be developed and validated independently in 3.0 so a failure in one does
not obscure the other.

### Full-game QA is required for infrastructure hooks

The v1.18 backend passed focused tests and still caused failures in unrelated late-game rooms.
Any future global audio hook needs broad scene-transition coverage before promotion.

## 3.0 reimplementation plan

A future MSU-1 implementation should start from the **v1.30 native-audio ROM/source**, not from
v1.18 code.

Recommended sequence:

1. Trace the native music-change routine in an emulator across representative scenes and record
   request value, current-song state, callsite, whether native actually changes music, and the
   final song selected.
2. Include deliberate no-change transitions such as the Horace and Nobilia examples before
   writing any new MSU hook.
3. Identify a hook point where the native engine has already established that a real music
   change will occur.
4. Build an MSU mirror around that confirmed change while allowing native SPC initialization to
   remain authoritative for sound effects.
5. Reintroduce per-request missing-PCM fallback without creating a session latch.
6. Reintroduce one-shot/loop policy only after the no-change semantics are proven.
7. Add native music-ID expansion as a separate step, with existing IDs left on their proven
   native path until the new-ID mechanism is independently accepted.
8. Run a full-game audio regression before promotion.

### Required 3.0 regression matrix

At minimum, test:

- no MSU hardware / no `.msu` file;
- MSU hardware present with a complete PCM set;
- partial PCM set with repeated native <-> MSU transitions;
- available one-shot -> missing -> available looping;
- consecutive same-song requests;
- zero/no-change requests;
- room transitions that inherit current music;
- short cinematic cues and fanfares;
- save/load while native music is active;
- save/load while MSU music is active;
- sound effects during MSU-owned playback;
- Nobilia takeoff room;
- the affected Horace scene;
- Windwalker takeoff/landing and Omnitopia transitions;
- full-game end-to-end playback coverage.

## Historical track map preserved for 3.0

The old Casual Run MSU implementation used numeric runtime filenames of the form
`Secret_of_Evermore_Casual_Run-<track>.pcm`. The following mapping is preserved as historical
3.0 input; it is **not active in v1.30**.

| ID | Canonical title | Historical mode | Legacy descriptive stem |
| ---: | --- | --- | --- |
| 01 | Main Title | once | `Main_Title` |
| 02 | Battle with Thraxx | loop | `Battle_with_Thraxx` |
| 03 | In the Arena | loop | `In_the_Arena` |
| 04 | Escape from Evermore | loop | `Escape_from_Evermore` |
| 05 | Return to Podunk | once | `Return_to_Podunk` |
| 06 | Village on the Plateau | loop | `Village_on_the_Plateau` |
| 07 | Within the Volcano | loop | `Within_the_Volcano` |
| 08 | Swamplands | loop | `Swamplands` |
| 09 | Southern Jungle | loop | `Southern_Jungle` |
| 10 | Bugmuck Tar Pits | loop | `Bugmuck_Tar_Pits` |
| 11 | Desert of Doom | loop | `Desert_of_Doom` |
| 12 | Queen Bluegarden | loop | `Queen_Bluegarden` |
| 13 | High in the Sky | loop | `High_in_the_Sky` |
| 14 | Control Room | loop | `Control_Room` |
| 15 | Hall of Collosia | loop | `Hall_of_Collosia` |
| 16 | Horace Highwater | loop | `Horace_Highwater` |
| 17 | Major Enemy | loop | `Major_Enemy` |
| 18 | Merchant in the Cave | loop | `Merchant_in_the_Cave` |
| 19 | Elephant Graveyard | loop | `Elephant_Graveyard` |
| 20 | Pirates of Crustacia | loop | `Pirates_of_Crustacia` |
| 21 | Lively Nobilia Marketplace | loop | `Lively_Nobilia_Marketplace` |
| 22 | Menu | loop | `Menu` |
| 23 | Machinery | loop | `Machinery` |
| 24 | Game Over | once | `Game_Over` |
| 25 | Raptor Attack! | loop | `Raptor_Attack` |
| 26 | Victory Fanfare | once | `Victory_Fanfare` |
| 27 | Good Night | once | `Good_Night` |
| 28 | The Seashore | loop | `The_Seashore` |
| 29 | Many Years Ago... | once | `Many_Years_Ago` |
| 30 | The Professor's Room | loop | `The_Professors_Room` |
| 31 | Quiet Plaza | loop | `Quiet_Plaza` |
| 32 | Omnitopia Surface | loop | `Omnitopia_Surface` |
| 33 | Storekeepers | loop | `Storekeepers` |
| 34 | Great Pyramid | loop | `Great_Pyramid` |
| 35 | Underground Path | loop | `Underground_Path` |
| 36 | Hidden River | loop | `Hidden_River` |
| 37 | Staff Roll | once | `Staff_Roll` |
| 38 | A Boy and His Dog | once | `A_Boy_and_His_Dog` |
| 39 | Engine Rumble | loop | `Engine_Rumble` |
| 40 | Explosion | loop | `Explosion` |
| 41 | Applause | loop | `Applause` |
| 42 | Palace Fountains | loop | `Palace_Fountains` |
| 43 | Fire Eyes | loop | `Fire_Eyes` |
| 44 | Puppet Show | loop | `Puppet_Show` |
| 45 | Minor Minion | loop | `Minor_Minion` |
| 46 | Distant Wind | loop | `Distant_Wind` |
| 47 | Death of a Minotaur | loop | `Death_of_a_Minotaur` |
| 48 | Fields of Gothica | loop | `Fields_of_Gothica` |
| 49 | City of Ebony | loop | `City_of_Ebony` |
| 50 | Over the Waterfall | loop | `Over_the_Waterfall` |
| 51 | Darkness of the Temple | loop | `Darkness_of_the_Temple` |
| 52 | Dark Forest | loop | `Dark_Forest` |
| 53 | City of Ivory | loop | `City_of_Ivory` |
| 54 | Omnitopia Hallways | loop | `Omnitopia_Hallways` |
| 55 | Quicksand Fields | loop | `Quicksand_Fields` |
| 56 | Tinker Tinderbox | loop | `Tinker_Tinderbox` |
| 57 | Deserted Castle | loop | `Deserted_Castle` |
| 58 | Dank Dungeon | loop | `Dank_Dungeon` |
| 59 | Regal Castle | loop | `Regal_Castle` |
| 60 | Freak Show!!! | loop | `Freak_Show` |
| 61 | Item Fanfare | once | `Item_Fanfare` |
| 62 | Northern Jungle | loop | `Northern_Jungle` |
| 63 | Lonely Halls | loop | `Lonely_Halls` |
| 64 | Dark Greenhouse | loop | `Dark_Greenhouse` |
| 65 | Vigor the Indestructible! | once | `Vigor_the_Indestructible` |
| 66 | Racing Pigs! | loop | `Racing_Pigs` |
| 67 | Collapse of Ivor Tower | once | `Collapse_of_Ivor_Tower` |
| 68 | Volcano Pipes | loop | `Volcano_Pipes` |
| 69 | Final Battle ~ Carltron | loop | `Final_Battle_Carltron` |
| 70 | Intruder Alarm | loop | `Intruder_Alarm` |

## Current status

**2.0 production audio:** native Secret of Evermore SPC soundtrack only.

**v1.05/v1.18 MSU implementation:** withdrawn and removed from active source.

**Temporary native-song expansion/hybrid lookup work:** also removed from the v1.30 production line and deferred to 3.0 so it can be developed independently.

**MSU-1 feature:** planned for 3.0 as a clean reimplementation.

**Higher-quality PCM soundtrack:** planned for 3.0 after the replacement backend is stable.

**New music / additional native song IDs:** planned for 3.0 and should be engineered separately
from the MSU interception layer.

---

v1.30 ROM SHA-256: `c47b4871d7519e9b2a630f356c054b329a62280d152380167d34f1a34d13ccb7`  
v1.30 SNES checksum/complement: `$6B43 / $94BC`
