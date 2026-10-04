#!/usr/bin/env python3
"""
Build Secret of Evermore: Casual Run from the authoritative ASM source.

BUILD / TEST OUTPUT CONVENTION
------------------------------
- Every generated ROM filename must begin with ``Secret_of_Evermore_Casual_Run``.
- Normal development/test handoffs should include only the generated ROM and the
  ASM source used to build it.
- Do not bundle PCM files, manifests, .msu marker files, or other MSU-1 assets with
  routine builds unless a complete test package is explicitly requested.
- PCM/audio assets remain external to the ASM source and should never be embedded
  into it; keeping them separate avoids unnecessary source/build growth.

The current development source uses one flattened definition in the recovered org/db subset. Hand-assembled 65816 helper
bytes are documented in the ASM beside each instruction. This keeps the build
dependency-free while preserving deterministic source control.
"""
from pathlib import Path
import argparse, hashlib, re, sys

BASE_SHA256 = "17c864a76d498feb6479eee8e7d6807b951c66225033228622bb66754baab1db"
BASE_SIZE = 3145728
EXPANDED_SIZE = 4194304
V103_SHA256 = "edf3640f98849916a31f8b9fdc1e126e66dd80b84a9e0ec50bcacc2880fcf899"
V104_SHA256 = "478886637c565d2ea657f4f5570bacce207ffc593ecd0fa487c80364a14b6ca0"
V105_SHA256 = "1cfd9d69ac50ab9ae5ca14bfb3b7f3310d004b83db0d13512d4292bf67a64d4a"

ORG_RE = re.compile(r"^\s*org\s+\$([0-9A-Fa-f]{6})\s*$")
DB_RE = re.compile(r"^\s*db\s+(.+?)\s*$")
BYTE_RE = re.compile(r"\$([0-9A-Fa-f]{2})")

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def cpu_to_pc(addr: int) -> int:
    if not 0xC00000 <= addr <= 0xFFFFFF:
        raise ValueError(f"Expected HiROM CPU address $C00000-$FFFFFF, got ${addr:06X}")
    return addr - 0xC00000

def apply_source(rom: bytearray, source_text: str) -> None:
    pc = None
    for lineno, raw in enumerate(source_text.splitlines(), 1):
        line = raw.split(";", 1)[0].strip()
        if not line or line.endswith(":") or line in {"arch 65816", "hirom"}:
            continue
        m = ORG_RE.match(line)
        if m:
            pc = cpu_to_pc(int(m.group(1), 16))
            continue
        m = DB_RE.match(line)
        if m:
            if pc is None:
                raise ValueError(f"line {lineno}: db appears before org")
            vals = [int(x, 16) for x in BYTE_RE.findall(m.group(1))]
            if not vals:
                raise ValueError(f"line {lineno}: malformed db: {raw}")
            end = pc + len(vals)
            if end > len(rom):
                raise ValueError(f"line {lineno}: write past expanded ROM end")
            rom[pc:end] = bytes(vals)
            pc = end
            continue
        raise ValueError(f"line {lineno}: unsupported source syntax: {raw}")

def make_ips(base: bytes, target: bytes) -> bytes:
    # Standard IPS; writes only bytes that differ. Expansion to 4 MiB is naturally
    # represented by records beyond the original EOF.
    if len(target) > 0x1000000:
        raise ValueError("IPS 24-bit offsets cannot represent this target size")
    padded = base + b"\x00" * max(0, len(target) - len(base))
    out = bytearray(b"PATCH")
    i = 0
    while i < len(target):
        if padded[i] == target[i]:
            i += 1
            continue
        start = i
        while i < len(target) and padded[i] != target[i] and i - start < 0xFFFF:
            i += 1
        payload = target[start:i]
        out += start.to_bytes(3, "big")
        out += len(payload).to_bytes(2, "big")
        out += payload
    out += b"EOF"
    # IPS supports an optional three-byte truncate/expand size after EOF. Always
    # emit it when the target size differs from the clean base so applying the
    # release patch reproduces the exact tested ROM, including zero-filled tail.
    if len(target) != len(base):
        out += len(target).to_bytes(3, "big")
    return bytes(out)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("base_rom", help="clean, unheadered U.S. Secret of Evermore ROM")
    ap.add_argument("output_rom", help="output ROM path")
    ap.add_argument("--source", default=str(Path(__file__).resolve().parent / "Secret_of_Evermore_Casual_Run_v1.38.asm"))
    ap.add_argument("--ips", help="optional IPS output path")
    ap.add_argument("--baseline-v103", action="store_true",
                    help="require output to match the recovered v1.03 baseline hash")
    args = ap.parse_args()

    base = Path(args.base_rom).read_bytes()
    if len(base) != BASE_SIZE:
        raise SystemExit(f"Wrong base size: {len(base)} bytes; expected {BASE_SIZE}")
    got = sha256(base)
    if got != BASE_SHA256:
        raise SystemExit(f"Wrong base SHA-256:\n  got      {got}\n  expected {BASE_SHA256}")

    rom = bytearray(base)
    rom.extend(b"\x00" * (EXPANDED_SIZE - len(rom)))
    source_text = Path(args.source).read_text(encoding="utf-8")
    apply_source(rom, source_text)

    # Recalculate the standard HiROM checksum/complement so the ROM emitted for
    # emulator testing is the exact artifact later used to derive the release IPS.
    rom[0xFFDC:0xFFE0] = bytes((0xFF, 0xFF, 0x00, 0x00))
    checksum = sum(rom) & 0xFFFF
    complement = checksum ^ 0xFFFF
    rom[0xFFDC:0xFFDE] = complement.to_bytes(2, "little")
    rom[0xFFDE:0xFFE0] = checksum.to_bytes(2, "little")

    output = bytes(rom)
    out_hash = sha256(output)
    if args.baseline_v103 and out_hash != V103_SHA256:
        raise SystemExit(
            "Source does not reproduce the v1.03 baseline.\n"
            f"  got      {out_hash}\n"
            f"  expected {V103_SHA256}"
        )

    Path(args.output_rom).write_bytes(output)
    if args.ips:
        Path(args.ips).write_bytes(make_ips(base, output))

    print(f"Built: {args.output_rom}")
    print(f"SHA-256: {out_hash}")
    if args.ips:
        print(f"IPS: {args.ips}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
