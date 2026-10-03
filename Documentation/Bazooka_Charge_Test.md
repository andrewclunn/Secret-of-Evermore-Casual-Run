# Bazooka charge test — issue #2

The Bazooka charge test was promoted to **v1.35** at user request. The release
source/ROM are `Build/Secret_of_Evermore_Casual_Run_v1.35.asm` and
`Build/Secret_of_Evermore_Casual_Run_v1.35.sfc`; the release IPS is
`Secret_of_Evermore_Casual_Run_v1.35.ips`. The release ROM is byte-identical to
the original test below. The default build now uses v1.35. Prior v1.34 and test
artifacts are preserved. Promotion authorization does not itself record a
completed in-game test; the gameplay checklist remains applicable.

Release verification: the default build reproduces the exact test ROM; all five
charging regressions and five layout regressions pass; the source audit validates
all 3,002 primary text pointers with no overlapping writes. Applying the v1.35 IPS
to the hash-verified clean base reproduces the release ROM byte for byte, including
the four-MiB expansion. IPS SHA-256:
`a2461ad72201017d1de8a1ede27b2982d6c7c400ab1d0fc561dd37f627a576cd`.

## Test handoff

- ROM: `Build/Secret_of_Evermore_Casual_Run_v1.34_Bazooka_Charge_Test.sfc`
- Source: `Build/Secret_of_Evermore_Casual_Run_v1.34_Bazooka_Charge_Test.asm`
- ROM size: 4,194,304 bytes.
- SHA-256: `90ba5f6262382de13a8437368a0c6218e84b6088ab536767d3c362e3386ea6da`.
- Issue: https://github.com/andrewclunn/Secret-of-Evermore-Casual-Run/issues/2

## Intended behavior

With the Bazooka equipped, ordinary recharge reaches 100% and stays there without
holding attack. B retains the inherited faster recharge below 100%, but cannot
push the Bazooka above 100%. Negative cooldown values are preserved. Old positive
overcharge is normalized to 100%, and the melee-style charging flag is cleared
on the Bazooka-specific input path. The normal firing and ammunition routines
are not patched.

The automatic guard uses the Boy actor and equipped weapon index, rather than a
physical controller number. The Dog and non-Bazooka weapons follow the existing
controller/charge routines. Weapon index `$001A` is corroborated by the native
Bazooka exclusion at `$CF:973E` and the native Bazooka equipment branch.

## Exact scope

- `$CF:CC77-$CF:CC7E`: automatic-charge hook. Ordinary below-100% regeneration
  immediately before this hook is unchanged.
- `$F0:0B00-$F0:0B05`: Boy fast-charge hook. Non-Bazooka paths replay the displaced
  input test and resume at `$F0:0B06`.
- `$F5:0900-$F5:0925` and `$F5:0940-$F5:09A0`: new helpers in the control-code
  expansion bank. Accepted v1.34 writes neither range and its built bytes there
  are zero; the native clean ROM ends before this bank. No existing allocations
  are reclaimed or relocated.
- SNES checksum/complement are recalculated. No other ROM bytes change.

## Automated verification

`Build/test_bazooka_charge.py` executes actual baseline/test ROM instructions in
a limited 16-bit CPU harness. Five checks pass:

1. Existing automatic/elevated-maximum fast-charge paths can exceed 100%; the
   test build holds 100% through 600 update pairs per tested ownership state.
2. Fast-charge input combinations, active/idle states, elevated charge maxima,
   and stale positive overcharge stay capped and preserve the caller return.
3. Negative cooldown values remain unchanged.
4. Non-Bazooka weapon indices and Dog paths match baseline RAM/register/flag
   results across the tested charge, input, and ownership combinations.
5. Every changed ROM byte belongs to the two hooks, two helpers, or checksum.

The source audit rebuilds this exact ROM, rejects overlapping source writes,
and validates all 3,002 primary text pointers. These checks do not validate
projectile creation, animations, ammunition, or a complete in-game charge cycle.

## Gameplay acceptance — still required

Use the test ROM explicitly; disable cheats. Record emulator/version and build.

1. Start a new game and reach the opening Bazooka fight. Release both A and B
   after recharging; watch the gauge for at least ten seconds. It must stay at
   100% while stationary and moving. Tap A: a projectile must appear and damage
   a target. Complete the opening without holding attack to stabilize charge.
2. After each shot, confirm the gauge refills and settles at 100% again. Repeat
   several shots while stationary, moving, and holding B during recharge.
3. Test late-game Bazooka ammunition types: shells, Particle Bomb, and Cryo-Blast.
   Verify damage, expected ammunition consumption, and reload readiness. Confirm
   out-of-ammo behavior and switching away/back do not freeze or resume looping.
4. Repeat with the Boy controlled by Player 2 and with an AI-controlled Boy.
   Confirm P2 join/withdraw and character switching still work.
5. Check representative sword, axe, spear, and Dog charging above 100%, including
   B fast charge. Confirm their charged attacks remain available.
6. If available, test Energize and a normal saved-game reload with the Bazooka.
   Confirm 100% readiness rather than a new overcharge loop.

Promotion is complete at user request; direct gameplay results are not recorded here. Pyramid issues
#1 and #3 remain separate follow-up work.

## Rebuild and audit

Use the bundled Python runtime or another Python 3 runtime; substitute the exact
clean, unheadered USA base ROM for `BASE_ROM`:

```powershell
python Build/build.py BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.34_Bazooka_Charge_Test.sfc --source Build/Secret_of_Evermore_Casual_Run_v1.34_Bazooka_Charge_Test.asm
python Build/test_bazooka_charge.py
python Build/script_layout.py audit BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.34_Bazooka_Charge_Test.asm --baseline-rom Build/Secret_of_Evermore_Casual_Run_v1.34_Bazooka_Charge_Test.sfc --report-prefix TEST_REPORT_PREFIX
```
