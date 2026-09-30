# DSP-1 Windwalker Experiment — Lessons Learned

This document records the DSP-1 flight experiment that began in Casual Run v1.27,
continued through v1.28, and was withdrawn for the v1.29 production baseline.

The purpose is not to argue that DSP-1 is unusable in Secret of Evermore. The experiment
proved that DSP-1 can generate a convincing live Mode-7 perspective for the Windwalker.
It also proved that our particular attempt to replace Evermore's live Windwalker raster
generator introduced deterministic corruption outside the flight scene. Because the exact
low-level cause was not isolated with enough confidence to ship safely, v1.29 returns live
flight to the native renderer.

## Final production decision

v1.29 uses:

- the original Secret of Evermore Windwalker Mode-7 raster generator;
- the original left/right Windwalker steering rate;
- vanilla cartridge type `$02`, so DSP-1 is not required;
- the repaired v1.28 native world-map OBJ/minimap graphics relocated to `$F6:8000-$F6:87FF`;
- the native minimap visibility state at `$7E:0B1D`;
- a one-time Windwalker setup initializer that sets `$0B1D = 1`, making the minimap visible
  by default while preserving the game's normal toggle afterward.

The live DSP-1 renderer and half-rate yaw helpers remain in the flat source only as
historical/inactive material. They are not reached by active v1.29 hooks.

## What the DSP-1 experiment successfully demonstrated

The experiment was valuable even though it was withdrawn.

1. **DSP-1 can generate the desired perspective.**  
   DSP-1 Parameter/Raster operations were successfully used to generate per-scanline Mode-7
   matrices and feed Evermore's existing HDMA table layout. In-flight presentation worked and
   provided the more dramatic horizon/perspective that motivated the experiment.

2. **Evermore's existing world-map pipeline can accept externally generated matrix data.**  
   The visual experiment did not require replacing the whole world-map renderer. The custom
   routine wrote the same matrix workspace the native renderer uses.

3. **The native minimap is independent enough to preserve.**  
   The separate minimap graphics problem was traced to an older ROM-space overlap, not to the
   DSP camera itself. Relocating the clean native `$0800`-byte world-map OBJ block solved the
   minimap marker graphics and survives the DSP rollback.

4. **The planned space-station approach does not require live DSP-1 flight.**  
   The important design goal is a visible station that appears ahead of the Windwalker and
   grows as the player approaches. That can be built on the stable native renderer with
   projected/OBJ-based landmark graphics and discrete distance scaling. DSP-1 remains an
   optional research path for a future self-contained cinematic or isolated rendering mode.

## The failure that forced the rollback

After flying with the DSP renderer and returning to ordinary gameplay, Ring/menu graphics
became severely corrupted. Text, icons, bars, and other menu elements were visibly scrambled.
The clean base game did not reproduce the issue.

The corruption was deterministic enough to make live DSP flight unsuitable for release.

The audio/music issue noticed during the same QA session was later shown to be independent of
flight and should be investigated separately as a music-table/MSU problem. It should not be
used as evidence for or against the DSP renderer.

## QA isolation history

The following tests were performed against the v1.28 flight work.

| Test | Change | Result | What it established |
| --- | --- | --- | --- |
| QA1 | Restored the three native minimap visibility reads instead of forcing them ON | Failed | The locked-on minimap checks were not the source of the post-flight menu corruption. |
| QA2 | Removed use of `$7E:32F6-$32F7` as DSP temporary scratch | Failed | Those undocumented scratch writes were not sufficient to explain the corruption. |
| QA3 | Restored the complete native raster generator, leaving the experimental half-rate yaw and DSP cartridge declaration | Failed | Removing DSP raster execution alone was not sufficient while the yaw modification remained. |
| QA4 | Restored both native raster generation and native yaw; DSP cartridge type remained declared | **Passed** | The DSP cartridge declaration by itself was not enough to cause the corruption. Returning both active flight modifications to native produced clean menus. |
| QA5 | Kept DSP raster but replaced half-velocity yaw arithmetic with alternate-frame native-sized yaw steps | Failed | A safer reduced-yaw implementation did not cure the system while DSP raster execution remained active. |
| QA6 | Restored fully native yaw while keeping the DSP raster | Failed | **DSP raster execution independently reproduces the corruption.** Reduced steering is not required for the failure. |
| QA7 | Ran the native raster first and then overlaid DSP matrices | Failed; flight sheared and slowed | Doing both raster calculations in one frame is not viable and does not repair the post-flight state. |
| QA8 | Cleared `$7F:D000-$7F:D6FF` before opening the Boy Ring | Failed | Merely leaving stale DSP matrix data in the flight workspace is not the root cause. |
| QA9 | Altered the Op `$0A` stream shutdown/drain behavior | Failed | The corruption was not fixed by that DSP stream-handling experiment. Later emulator-source review showed the earlier theory about the eight `$80` writes was not a reliable root-cause explanation. |
| QA10 | First caller-sensitive setup/live dispatcher | Crashed | The diagnostic dispatcher itself was unsafe because it assumed processor width on entry; this result was discarded as a test of the DSP hypothesis. |
| QA10b | Safe caller-sensitive gate: native setup, DSP only in live flight | Crashed when switching to the DSP view | The live DSP path depends on state established during the earlier takeoff/setup processing; DSP could not simply be deferred until after setup. |
| QA11 | Kept DSP flight but generated one final native raster at altitude zero before landing | Failed | Restoring native matrix contents on the last grounded flight frame is not sufficient. |
| QA12 | Full DSP rollback + native yaw + repaired minimap graphics + default-ON/native-toggle minimap | **Passed** | This is the stable production baseline promoted to v1.29. |

## Conclusions supported by the tests

### 1. The production bug is tied to executing the custom DSP raster path

QA6 is the clearest isolation result: native steering plus the DSP raster still corrupts the
menus. QA4, where both raster and steering were native, remains clean.

This is stronger evidence than the earlier suspicion that the reduced steering algorithm alone
was responsible.

### 2. The DSP cartridge declaration itself is not the problem

QA4 still declared the DSP cartridge type and remained stable as long as the active flight
renderer and yaw path were native.

### 3. The minimap repair is safe to keep

The repaired native minimap graphics and their relocated ROM source remain active in QA12/v1.29
without reproducing the failure.

The better visibility policy is to initialize the native minimap state ON once, not to replace
its state reads with unconditional constants. This preserves the player's ability to toggle it.

### 4. Simple cleanup after flight is not enough

Clearing the matrix workspace did not help. Regenerating a native ground-level raster before
landing did not help. The failure therefore cannot be described merely as "DSP values remain in
the Mode-7 buffer."

### 5. The exact low-level mechanism remains unproven

The test series narrowed the failure to the active DSP raster integration, but it did **not**
prove whether the final cause is:

- an unrecognized native side effect bypassed by the replacement routine;
- timing/transition pressure caused by the synchronous DSP workload;
- a coprocessor protocol/state interaction not captured by the diagnostics;
- another CPU/PPU/HDMA state dependency;
- or some interaction between those factors.

Do not document any one of those as the established root cause without new evidence.

## Engineering lessons

### Preserve native side effects unless every one is understood

A routine that appears to "just calculate matrices" may also participate in timing, direct-page
state, HDMA setup, transition sequencing, or other contracts not obvious from its output
buffers. Replacing a native routine because its visible product is understood is riskier than
wrapping or augmenting it.

### A visually correct frame is not proof of a safe renderer

The DSP flight looked good while it was running. The regression appeared later in unrelated UI.
For renderer work, validation must include:

- takeoff;
- sustained flight;
- ascent/descent;
- turning;
- landing;
- immediate Ring/menu use;
- dialogue/windows after landing;
- scene transitions and save/reload behavior.

### Prefer state initialization over forced state bypasses

For the minimap, setting `$0B1D = 1` once at Windwalker initialization is cleaner than replacing
every visibility check with a constant. It preserves native behavior and makes future code easier
to reason about.

### Keep experiments isolated and reversible

The flat-source model made it possible to back out the DSP renderer while retaining the separate
minimap repair. Future experimental renderers should be introduced behind a small, explicit
entry/exit boundary and should not become entangled with unrelated world-map fixes.

### Runtime QA outranks an elegant theory

Several plausible explanations were disproven:

- forced minimap rendering;
- temporary WRAM scratch;
- stale Mode-7 buffers;
- final raster contents at landing;
- reduced-yaw arithmetic alone;
- one proposed DSP stream cleanup.

The project should retain those negative results. They prevent us from re-running the same
experiments later and mistaking an attractive explanation for a demonstrated cause.

## Guidance if DSP-1 is revisited

Do not reconnect the v1.27 hooks directly.

A future DSP investigation should start from v1.29 and use one of these safer boundaries:

1. **Self-contained cinematic/approach mode.**  
   Enter a dedicated DSP-driven scene, perform the station approach, then execute a complete
   map/scene reload before ordinary gameplay resumes. This gives the DSP renderer a hard
   lifecycle boundary instead of requiring it to coexist transparently with the normal
   Windwalker engine.

2. **Offline/precomputed perspective assets.**  
   Use DSP-1 or external tooling during development to derive tables/visuals, but ship fixed
   data driven by the native runtime.

3. **Native-renderer landmark projection.**  
   Keep native Mode-7 terrain and implement the station as projected OBJ graphics. Use heading,
   player/world position, and distance to select horizontal placement and a discrete sprite size.
   This is the preferred 2.0 direction because it preserves the stable renderer.

4. **Emulator-assisted state tracing before another live replacement.**  
   If live DSP rendering is attempted again, capture native-vs-DSP state across the entire
   `$C0:D934` call and the subsequent landing transition: CPU flags/registers, direct page,
   HDMA state, PPU registers, relevant WRAM, stack state, and frame timing. Do not resume
   trial-and-error patching until a concrete state difference is identified.

## Current status

**DSP-1 live Windwalker rendering: withdrawn from production.**

**Native Windwalker renderer: restored in v1.29.**

**Repaired minimap graphics: retained.**

**Minimap behavior: ON by default, then natively toggleable.**

**Space-station approach: still planned, with native-renderer landmark projection as the
preferred implementation path.**

---

v1.29 ROM SHA-256: `32fa349736831a45b200fcb2241dfc0819a0a3a22366cc5fca95e7c6b90ad43e`  
v1.29 SNES checksum/complement: `$C7ED / $3812`
