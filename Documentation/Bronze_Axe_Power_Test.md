# Bronze Axe power test

This cumulative v1.41 test includes the Boy theme correction for “I hit it with my axe!” and raises Bronze Axe base power from 32 to 33. Bronze Spear remains 32.

Outputs: `Build/Secret_of_Evermore_Casual_Run_v1.41_Bronze_Axe_Test.asm` and `.sfc`.

The native weapon table starts at ROM offset 0x438E6 and uses 36-byte records. Each record starts with a little-endian 16-bit power followed by a name pointer. The Bronze Axe name pointer resolves to “Bronze Axe” at 0x46118; its power is at 0x4399A (CPU $C4399A). Bronze Spear power is at 0x43A2A and its name resolves to 0x46149. This identifies the target from the ROM itself.

Validation: the rebuilt ROM differs from the Axe Dialogue Test only at the Bronze Axe power byte ($20 to $21) and the header checksum. The entire Bronze Spear record is unchanged. Source parsing reports zero overlapping writes and retains 3,002 primary text pointers. Gameplay testing remains pending.

ROM SHA256: `f521511d32a248aa0beb7e890b07e8dc8c17308f574f2653e751bc2b4e0d309b`.

Reproduce with `Build/build_bronze_axe_power_test.py`, passing the clean USA ROM path as its first argument. Published v1.41 remains the release baseline.
