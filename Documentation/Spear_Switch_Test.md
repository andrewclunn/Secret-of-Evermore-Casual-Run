# Halls spear switch test

Fixes the automatic spear throw at the main Halls of Collosia pit switch.
Includes the previous Mud Pepper cap and pyramid return-passage changes.

An earlier dialogue-theme edit mistook $D7940A for a speaker argument. It is
actually the low byte of the conditional branch displacement at $D79403.
Changing 13 to 4 routed an equipped spear to the hint text rather than the
throw sequence. This build restores the original displacement of 13.

ROM: `Build/Secret_of_Evermore_Casual_Run_v1.40_Spear_Switch_Test.sfc`.
Source: `Build/Secret_of_Evermore_Casual_Run_v1.40_Spear_Switch_Test.asm`.
Rebuild: `Build/build_spear_switch_test.py <clean-USA-ROM>`.
SHA-256: `7836c46b083bb366d7ff6113a693a3fe4e609ee5210478b1069e0db26e89a4b2`.

Checks passed:

- Only $D7940A and the ROM checksum differ from the Mud Pepper test.
- The restored byte matches the clean USA ROM.
- Native decoding confirms spear family 4 branches to $D79419, proceeds
  through the existing weapon check, and calls the throw at $D79443.
- No overlapping source writes; 3,002 text pointers validate.

Gameplay testing remains pending. With the Bronze Spear equipped, dismiss
the dialogue and step away from and back onto the trigger in front of the pit.
No weapon-skill training is required for this scripted throw. This remains
a test build; the published/default release is v1.40.
