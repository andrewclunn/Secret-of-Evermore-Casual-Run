"""Cumulative v1.36 dialogue QA regressions. Run with the verified clean USA ROM as argument.

These checks verify ROM data and event routing; emulator presentation is separate.
"""
from pathlib import Path
import sys
import unittest

import build
import script_layout


ROOT = Path(__file__).resolve().parent
BASE = Path(sys.argv.pop(1)).read_bytes()
assert len(BASE) == build.BASE_SIZE and build.sha256(BASE) == build.BASE_SHA256


def assemble(name):
    rom = bytearray(BASE + bytes(build.EXPANDED_SIZE - len(BASE)))
    build.apply_source(rom, (ROOT / name).read_text(encoding="utf-8"))
    return rom


OLD = assemble("Secret_of_Evermore_Casual_Run_v1.35.asm")
NEW = assemble("Secret_of_Evermore_Casual_Run_v1.36.asm")


def text(rom, text_id):
    entry = script_layout.TEXT_TABLE + text_id * 3
    raw = int.from_bytes(rom[entry:entry + 3], "little")
    assert not raw & 0x800000
    pc = script_layout.decode_text_pointer(raw)
    # Only the checked plain-ASCII/known-control payloads use this reader.
    return pc, bytes(rom[pc:rom.index(0, pc) + 1])


class DialogueQATests(unittest.TestCase):
    def test_relief_keeps_pause_and_sentence_space(self):
        pc, payload = text(NEW, 1858)
        self.assertEqual(pc, 0x3B11DF)
        self.assertIn(b"What a relief!\x80\x79\x80 That beast", payload)
        self.assertEqual(payload.count(0x86), 1)
        self.assertEqual(len(payload), 79)

    def test_hut_speakers_at_actual_text_calls(self):
        # Opener address, expected identity, first following text ID.
        routes = [(0xD4DD25, 6, 831), (0xD4DD3B, 4, 832),
                  (0xD4DD5E, 6, 833), (0xD4DD74, 6, 834),
                  (0xD4DD8A, 6, 835), (0xD4DDA0, 6, 836),
                  (0xD4DDB6, 6, 837), (0xD4DDC2, 6, 838),
                  (0xD4DE4E, 6, 843)]
        for cpu, helper, tid in routes:
            with self.subTest(text_id=tid):
                pc = cpu - 0xC00000
                self.assertEqual(NEW[pc:pc + 3], bytes([0xA3, helper, 0x51]))
                self.assertEqual(int.from_bytes(NEW[pc + 3:pc + 5], "little"), tid * 3)

    def test_repeat_rest_and_save_theme_continuity(self):
        # TEXT 844/846 share the repeat opener; both original save callers
        # still enter the private hut routine. Post-rest TEXT 847 opens $06.
        self.assertEqual(NEW[0x14DE56:0x14DE58], b"\xA3\x06")
        self.assertEqual(NEW[0x14DE08:0x14DE0A], b"\xA3\x06")
        self.assertEqual(NEW[0x14DE73:0x14DE79], b"\xA3\x06\x29\x00\x12\x32")
        self.assertEqual(NEW[0x14DE20:0x14DE24], b"\x29\x00\x12\x32")
        self.assertIn(b"\xA3\x06\x51\xED\x09", NEW[0x369200:0x3692C4])
        self.assertEqual(NEW[0x369200:0x3692C4], OLD[0x369200:0x3692C4])

    def test_save_choices_start_fresh_and_retain_native_contract(self):
        pc, payload = text(NEW, 2407)
        old_pc, old_payload = text(OLD, 2407)
        self.assertEqual(pc, old_pc)
        self.assertEqual(payload, old_payload[:1] + b"\x87" + old_payload[1:])
        self.assertEqual(payload[:2], text(NEW, 2230)[1][:2])
        self.assertEqual(payload.count(0x8B), 2)
        self.assertIn(b"\x8BSure.\x0A\x8BNo, that's okay.", payload)
        self.assertEqual(text(NEW, 846), text(OLD, 846))
        self.assertEqual(text(NEW, 847), text(OLD, 847))
        self.assertEqual(NEW[0x369300:0x36931B], OLD[0x369300:0x36931B])

    def test_only_intended_rom_ranges_change(self):
        operands = {0x14DD26, 0x14DD3C, 0x14DD5F, 0x14DD75, 0x14DD8B,
                    0x14DDA1, 0x14DDB7, 0x14DDC3, 0x14DE4F, 0x14DE57}
        entry = script_layout.TEXT_TABLE + 1858 * 3
        allowed = operands | set(range(entry, entry + 3)) | {0x3B11DF + 18}
        allowed |= set(range(0x340200, 0x340257))
        allowed |= {0x1480C3, 0x14810B, 0x148171, 0x148183, 0x14818D}
        allowed |= set(range(0x382632, 0x38263F))
        allowed |= {0x14B4ED, 0x14B527, 0x14B840, 0x14B890}
        allowed |= {0x15D07F, 0x15D0C8, 0x15D289, 0x15D2AA}
        allowed |= {0x37E90F, 0x37E911}
        changed = {pc for pc, (before, after) in enumerate(zip(OLD, NEW)) if before != after}
        self.assertTrue(operands <= changed)
        self.assertFalse(changed - allowed, f"Unexpected changes: {changed - allowed}")

    def test_volcano_alchemist_save_and_boy_reply(self):
        for pc in [0x1480C3, 0x14810B, 0x148171, 0x148183, 0x14818D]:
            self.assertEqual(NEW[pc-1:pc+1], b"\xA3\x03")
        for pc in [0x1480C8, 0x148110, 0x148176, 0x148192]:
            self.assertEqual(NEW[pc:pc+2], b"\xA3\x4E")
            self.assertEqual(NEW[pc-6:pc-4], b"\xA3\x03")
        self.assertEqual(text(NEW, 511)[1], b"\x96Huh?\x86\x00")
        self.assertEqual(NEW[0x148060:0x148062], b"\xA3\x04")

    def test_fire_eyes_entire_exchange(self):
        routes = [(573,0x14B4EC,0x10,0x14B4EE),(574,0x14B4FF,4,0x14B501),
                  (575,0x14B526,0x0D,0x14B52C),(576,0x14B539,0x10,0x14B53B),
                  (577,0x14B54B,0x0D,0x14B54D),(578,0x14B55F,0x10,0x14B561),
                  (579,0x14B573,0x0D,0x14B575),(580,0x14B581,0x10,0x14B583),
                  (581,0x14B58F,0x10,0x14B591),(582,0x14B5B5,0x10,0x14B5B7),
                  (583,0x14B5F7,0x10,0x14B5F9),(584,0x14B815,0x0D,0x14B817),
                  (585,0x14B83F,0x10,0x14B841),(586,0x14B88F,0x10,0x14B891)]
        for tid, pc, helper, call in routes:
            with self.subTest(text_id=tid):
                self.assertEqual(NEW[pc:pc+2], bytes([0xA3, helper]))
                self.assertEqual(NEW[pc+2:call], bytes([0x4D])*(call-pc-2))
                self.assertEqual(NEW[call:call+3], bytes([0x51])+(tid*3).to_bytes(2,"little"))

    def test_artificial_horace_scene_and_continuations(self):
        routes = [(0x15D072,0x13,1037),(0x15D07E,0x11,1038),
                  (0x15D0A0,0x13,1040),(0x15D0C7,0x11,1042),
                  (0x15D1A8,0x13,1043),(0x15D27C,0x0B,1044),
                  (0x15D288,0x11,1045),(0x15D29D,0x0B,1046),
                  (0x15D2A9,0x11,1047),(0x15D2BA,0x0B,1049)]
        for pc, helper, tid in routes:
            with self.subTest(text_id=tid):
                self.assertEqual(NEW[pc:pc+9], bytes([0xA3,helper])+bytes([0x4D])*4+
                                 bytes([0x51])+(tid*3).to_bytes(2,"little"))
        for pc, tid, start in [(0x15D08E,1039,0x15D087),
                               (0x15D0B1,1041,0x15D0A9),(0x15D2B4,1048,0x15D2B2)]:
            self.assertEqual(NEW[pc:pc+3], bytes([0x51])+(tid*3).to_bytes(2,"little"))
            self.assertNotIn(0xA3, NEW[start:pc])

    def test_generic_npc_expands_symmetrically(self):
        self.assertEqual(NEW[0x129914:0x129917], bytes.fromhex("0a e9 32"))
        self.assertEqual(NEW[0x37E90A:0x37E914], bytes.fromhex("54 01 55 44 00 03 02 1a 08 00"))
        self.assertEqual(2*OLD[0x37E90F]+OLD[0x37E911],
                         2*NEW[0x37E90F]+NEW[0x37E911])

    def test_release_patch_exact_reproduction(self):
        patch = (ROOT.parent / "Secret_of_Evermore_Casual_Run_v1.36.ips").read_bytes()
        self.assertEqual(patch[:5], b"PATCH")
        result = bytearray(BASE)
        cursor = 5
        while patch[cursor:cursor+3] != b"EOF":
            pc = int.from_bytes(patch[cursor:cursor+3], "big")
            size = int.from_bytes(patch[cursor+3:cursor+5], "big")
            cursor += 5
            if size:
                payload = patch[cursor:cursor+size]
                cursor += size
            else:
                count = int.from_bytes(patch[cursor:cursor+2], "big")
                payload = patch[cursor+2:cursor+3] * count
                cursor += 3
            if pc+len(payload) > len(result):
                result.extend(bytes(pc+len(payload)-len(result)))
            result[pc:pc+len(payload)] = payload
        cursor += 3
        if len(patch)-cursor == 3:
            size = int.from_bytes(patch[cursor:cursor+3], "big")
            result = (result + bytes(max(0,size-len(result))))[:size]
        expected = bytearray(NEW)
        expected[0xFFDC:0xFFE0] = bytes.fromhex("ff ff 00 00")
        checksum = sum(expected) & 0xFFFF
        expected[0xFFDC:0xFFDE] = (checksum ^ 0xFFFF).to_bytes(2,"little")
        expected[0xFFDE:0xFFE0] = checksum.to_bytes(2,"little")
        self.assertEqual(result, expected)
        self.assertEqual(build.sha256(result),
                         "a6ced1e7309222863ef61e02cb0a2887d7004b295ebce632fee70d8dcd1ea4d5")


if __name__ == "__main__":
    unittest.main()
