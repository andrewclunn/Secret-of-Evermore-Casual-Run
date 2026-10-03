# Script consolidation checkpoint

The authoritative current source is `Build/Secret_of_Evermore_Casual_Run_v1.35.asm`.
The v1.35 Bazooka charge fix was promoted from the isolated test at user request.
Its ROM is byte-identical to that test, with SHA-256
`90ba5f6262382de13a8437368a0c6218e84b6088ab536767d3c362e3386ea6da`.
Current release: `Secret_of_Evermore_Casual_Run_v1.35.ips`. The current layout maps
include the new charge helpers. [Bazooka validation notes](Bazooka_Charge_Test.md)
record the change and test coverage.

The historical v1.34 consolidation checkpoint and its identity follow.
The consolidated checkpoint was promoted to v1.34 and reproduces the user-accepted
Strong Heart R4 build exactly, including the Sandpits southern-ledge Skelesnail removal.
The v1.33 release source, release IPS, and prior development sources/ROMs are preserved.
The release patch is `Secret_of_Evermore_Casual_Run_v1.34.ips` at the repository root.

Historical v1.34 ROM identity:

- Size: 4,194,304 bytes.
- SHA-256: `f7df247e844b2fd4e70361daf800e8cd50a0074c17e002ea65dcbc27617c2f45`.
- Checksum / complement: `$2A33` / `$D5CC`.
- v1.34 IPS SHA-256: `a9a103292380fbe777d68479a9352ed1aef69816c5cd7441600112b324a7159b`.

Release verification applied the generated IPS to the hash-verified clean base ROM,
including its four-MiB expansion record, and compared every byte with both the v1.34
build and accepted R4 ROM. All three outputs match. The v1.34 source audit also
verified all 3,002 primary text pointers and zero overlapping source writes.

## What changed

Successive source revisions wrote 5,336 bytes more than once. Consolidation resolves
the final writer of every address and emits exactly one active definition per address,
in CPU-address order. This includes partial overlaps and repeated writes of the same
value. Current patched primary pointers have individual `TextPointer_####` labels;
their current payload targets have `LiveText_####` labels. The ten NG+ mirror targets
have `NGPlusText_####` labels.

Original allocation labels and comments identify provenance. Older version names in
those labels do not select an older implementation. Detailed architecture/history
remains in the preserved R4 source; the consolidated source contains active definitions
and current metadata. Metadata for repurposed contextual-save text IDs now describes
their current speakers. Metadata changes do not alter ROM bytes.

Every previously source-written address remains source-written. Historical payloads,
inactive systems, graphics, and other non-text data are retained at their existing
addresses. No data has been repacked or reclaimed. Normal-save and emulator-state
behavior is unchanged because the complete ROM is identical.

## Current layout map

- `Script_Layout_Current.md`: expansion-bank ownership and the 25 inherited regional reserves.
- `Script_Layout_Current_text.csv`: all 3,002 primary pointers, decoded destinations,
  source ownership, speaker metadata, and NG+ mirror destinations where applicable.
- `Script_Layout_Current.json`: the same pointer inventory plus every final source-owned
  range, physical reservation counts, and text IDs stored outside their metadata arena.

These files are generated snapshots. The ASM definitions and embedded `TEXTMETA` /
`TEXTARENA` records are the current inputs; edit those and regenerate the map.

The primary table includes unused IDs and shared entries. A current pointer is not proof
of runtime reachability. Likewise, source-owned bytes are not necessarily active data,
and source-unwritten or zero-filled bytes are not proven free. Native references,
alternate entry points, parameterized global calls, and other indirect references still
need auditing before an allocation is reclaimed.

## Building and checking

Run these from the repository root with the available Python runtime. Substitute the
path to the verified clean, unheadered USA ROM for `BASE_ROM`.

```powershell
python Build/build.py BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.35.sfc --ips Secret_of_Evermore_Casual_Run_v1.35.ips
python Build/script_layout.py audit BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.35.asm --baseline-rom Build/Secret_of_Evermore_Casual_Run_v1.35.sfc --report-prefix Documentation/Script_Layout_Current
python Build/test_script_layout.py
```

The build script defaults to the authoritative v1.35 source. Explicit `--source`
still builds any preserved release/test source. Audit rejects overlapping writes and
invalid packed text pointers, and requires exact ROM equality when `--baseline-rom` is
supplied. Omit that comparison only when checking an intentional future behavior change.
Audit also validates the packed-pointer round trip for every primary entry.

`consolidate` mode is for an explicitly chosen historical/overlay source. Routine edits
belong in the v1.35 file; rerunning consolidation from R4 would discard later edits.
The original pre-promotion consolidation command is retained for provenance:

```powershell
python Build/script_layout.py consolidate BASE_ROM Build/Secret_of_Evermore_Casual_Run_v1.33_Strong_Heart_Save_Test_R4.asm --output Build/Secret_of_Evermore_Casual_Run_v1.33_Consolidated.asm --baseline-rom Build/Secret_of_Evermore_Casual_Run_v1.33_Strong_Heart_Save_Test_R4.sfc --report-prefix Documentation/Script_Layout_Current
```

## Follow-up boundary

This checkpoint prepares a selective relocation audit. It does not claim a complete
event graph, a safe unused-text-ID list, or a decoded text-length inventory. Before
repacking text, establish payload/control-token boundaries, shared/suffix references,
and inbound references; preserve paired NG+ offsets and bank-selector behavior.
Before moving events, establish instruction lengths, branch targets, continuations,
and alternate entry points. Text addresses are limited to each bank's lower half;
the Strong Heart R2 mistake is covered by a pointer-encoding regression check.

For the current storage-only consolidation, complete ROM equality is the decisive
behavior-preservation check. Future pointer/event changes require targeted in-game QA.
