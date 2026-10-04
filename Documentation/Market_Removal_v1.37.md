# v1.37 — Nobilia vendor passage

The user selected complete removal of the two pots labeled B and C in market experiment 01 to open access beside the vendors. v1.37 replaces both pots' graphics and tile attributes with ordinary pavement. The pots labeled A and D retain their original v1.36 graphics and attributes.

## Deliverables

- ROM: `Build/Secret_of_Evermore_Casual_Run_v1.37.sfc`
- Full authoritative source: `Build/Secret_of_Evermore_Casual_Run_v1.37.asm`
- Cumulative clean-USA-base patch: `Secret_of_Evermore_Casual_Run_v1.37.ips`
- Machine-readable edits and validation: `Documentation/Market_Removal_v1.37_manifest.json`

This version retains the accepted v1.36 dialogue fixes and all previous features. The standard build script now defaults to v1.37. Experiment 01 remains available separately.

## Change and validation

Four cells change: map $0A, x=31, y=55–58, covering B and C. B's two cells reuse the floor record at (31,54); C's two cells reuse the floor record at (31,59). Both donor records have ordinary open-floor attributes. All other grid pointers, including A and D, match v1.36 exactly. All 1,807 original tile-table entries remain identical; this release needs no diagnostic records appended to the table.

The market room uses the same relocation and native raw-decompression approach tested in experiment 01. The room resides at $FC0000–$FC4F4A (20,299 bytes), with its map pointer at $DFFE0F. Original event lists, palette/graphics lists, dynamic tile definitions, and room tail data are copied unchanged. No native CPU instructions or additional WRAM are changed.

Checks passed: accepted v1.36 input hash; source allocation and text-reserve checks; native raw-decompression output equality; full-source rebuild from the provided v1.36 image; no source overlaps; validation of all 3,002 primary text pointers; exactly four grid-pointer changes; preservation of all original tile-table records; ROM differences limited to the room allocation, market pointer and checksum; cumulative IPS composition and application equality. Current source-layout reports were regenerated.

The cumulative IPS preserves every original v1.36 patch write and overrides the bytes changed by v1.37. It is intended for the clean, unheadered USA ROM, not for applying over another version. The baseline patch's writes were checked against the verified local v1.36 ROM. The resulting patch was applied to that image and reproduced the new ROM exactly. A clean-ROM build/application was not performed because no clean base ROM is available in this workspace.

The reconstructed map confirms both B/C pots are absent and A/D remain. The user previously confirmed the relocated market loads, graphics-only B still blocks, and collision-only C can be traversed. **Final combined B/C removal, vendor access, Dog movement, and later story variants still need emulator confirmation.**

## Gameplay check

Load the v1.37 ROM with a copied battery save. If starting from a save state inside the market, leave and re-enter to reload the edited map. Walk both characters through the former B/C locations from several directions and talk to the vendors from that side. Check for invisible collision, floor seams, layering problems, or changed vendor interactions. A and D should be back in their original positions.

ROM size: 4,194,304 bytes. Checksum/complement: `$2611 / $D9EE`.

ROM SHA-256: `1b9f0a927c6f1c8d12caeb61ea2cc56a7c40e1bdf352bb636f57ea57727db14a`

IPS SHA-256: `e442169ba255d0c80b25b9f73a5db19f29a46ed2e555791c95d773297650af83`
