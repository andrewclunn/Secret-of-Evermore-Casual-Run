"""Consolidate org/db source and audit final text pointers without relocating bytes.

Generated maps describe source ownership and primary-table references, not proof
that an unreferenced range is free. Native/event/indirect references still matter.
"""
from array import array
import argparse
import csv
import io
import json
from pathlib import Path
import re

import build

TEXT_TABLE = 0x11D000
TEXT_COUNT = 3002
META_RE = re.compile(r"^;@TEXTMETA (.+)$")
LABEL_RE = re.compile(r"^([A-Za-z_][A-Za-z_0-9]*):$")
ARENA_RE = re.compile(r"^;\s+([A-Z][A-Z_0-9]+)\s+\$([A-F0-9]{2}:?[A-F0-9]{4})-\$([A-F0-9]{2}:?[A-F0-9]{4})\s*$", re.M)


def arena_reserves(source):
    embedded = [json.loads(line.removeprefix(";@TEXTARENA "))
                for line in source.splitlines() if line.startswith(";@TEXTARENA ")]
    if embedded:
        return embedded
    directory = source.split("; REGIONAL ARENAS\n", 1)[-1].split("; MIRRORED NG+ CALLBACK ARENAS", 1)[0]
    return [{"name": match[1], "pc_start": int(match[2].replace(":", ""), 16)-0xC00000,
             "pc_end_exclusive": int(match[3].replace(":", ""), 16)-0xC00000+1}
            for match in ARENA_RE.finditer(directory)]


def decode_text_pointer(raw):
    return (raw & 0x007FFF) | ((raw & 0x7F8000) << 1)


def encode_text_pointer(pc, compressed=False):
    if not 0 <= pc < build.EXPANDED_SIZE or pc & 0x8000:
        raise ValueError("Text pointers require the lower half of a ROM bank")
    return (pc & 0x7FFF) | ((pc & 0x7F0000) >> 1) | (0x800000 if compressed else 0)


def finalize_checksum(rom):
    rom[0xFFDC:0xFFE0] = bytes.fromhex("FF FF 00 00")
    checksum = sum(rom) & 0xFFFF
    rom[0xFFDC:0xFFDE] = (checksum ^ 0xFFFF).to_bytes(2, "little")
    rom[0xFFDE:0xFFE0] = checksum.to_bytes(2, "little")
    return checksum


def parse_source(source, base):
    rom = bytearray(base + bytes(build.EXPANDED_SIZE - len(base)))
    owners = array("I", [0]) * build.EXPANDED_SIZE
    groups = [{"label": "Clean_ROM", "line": 0, "notes": []}]
    group = 0
    pc = None
    pending = []
    metadata = {}
    writes = overwritten = changed_overwrites = 0
    group_has_data = False
    for lineno, raw in enumerate(source.splitlines(), 1):
        meta = META_RE.match(raw)
        if meta:
            row = json.loads(meta[1])
            metadata[row["id"]] = row
            continue
        code, _, inline = raw.partition(";")
        line = code.strip()
        if not line:
            if raw.lstrip().startswith(";"):
                pending.append(raw)
            else:
                pending = []
            continue
        if line in {"arch 65816", "hirom"}:
            continue
        org = build.ORG_RE.match(line)
        label = LABEL_RE.match(line)
        if org or label:
            if org:
                pc = build.cpu_to_pc(int(org[1], 16))
                name = f"Allocation_{pc + 0xC00000:06X}"
            else:
                name = label[1]
            notes = pending[:]
            if label and not group_has_data:
                notes = groups[group]["notes"] + notes
            groups.append({"label": name, "line": lineno, "notes": notes})
            group = len(groups) - 1
            group_has_data = False
            pending = []
            continue
        db = build.DB_RE.match(line)
        if not db or pc is None:
            raise ValueError(f"Unsupported source at line {lineno}: {raw}")
        data = bytes(int(v, 16) for v in build.BYTE_RE.findall(db[1]))
        if not data or pc + len(data) > len(rom):
            raise ValueError(f"Invalid write at line {lineno}")
        for offset, value in enumerate(data):
            target = pc + offset
            if owners[target]:
                overwritten += 1
                changed_overwrites += rom[target] != value
            owners[target] = group
            rom[target] = value
        if inline.strip() and inline.strip() not in groups[group]["notes"]:
            groups[group]["notes"].append("; " + inline.strip())
        writes += len(data)
        group_has_data = True
        pc += len(data)
        pending = []
    return rom, owners, groups, metadata, {
        "source_write_bytes": writes,
        "overwritten_write_bytes": overwritten,
        "overwrites_changing_value": changed_overwrites,
        "unique_source_owned_bytes": sum(bool(owner) for owner in owners),
    }


def source_ranges(owners, groups):
    ranges = []
    start = 0
    while start < len(owners):
        if not owners[start]:
            start += 1
            continue
        owner = owners[start]
        end = start + 1
        while end < len(owners) and owners[end] == owner:
            end += 1
        ranges.append({"pc_start": start, "pc_end_exclusive": end,
                       "cpu_start": f"${start + 0xC00000:06X}",
                       "cpu_end_inclusive": f"${end - 1 + 0xC00000:06X}",
                       "bytes": end - start, "origin": groups[owner]["label"],
                       "origin_line": groups[owner]["line"]})
        start = end
    return ranges


def text_rows(rom, owners, groups, metadata):
    rows = []
    for text_id in range(TEXT_COUNT):
        entry = TEXT_TABLE + text_id * 3
        raw = int.from_bytes(rom[entry:entry+3], "little")
        pc = decode_text_pointer(raw)
        if pc >= len(rom) or encode_text_pointer(pc, bool(raw & 0x800000)) != raw:
            raise ValueError(f"Invalid pointer for TEXT {text_id}: {raw:06X}")
        meta = metadata.get(text_id, {})
        rows.append({"id": text_id, "pointer_cpu": f"${entry + 0xC00000:06X}",
                     "packed_pointer": f"${raw:06X}",
                     "mode": "compressed" if raw & 0x800000 else "raw",
                     "target_pc": pc, "target_cpu": f"${pc + 0xC00000:06X}",
                     "target_source_owned": bool(owners[pc]),
                     "target_origin": groups[owners[pc]]["label"],
                     "ngplus_target_cpu": f"${pc + 0xC10000:06X}" if pc >> 16 == 0x32 and not raw & 0x800000 else "",
                     "arena": meta.get("arena", "NATIVE_SHARED"),
                     "speaker": meta.get("source", "unclassified"),
                     "theme": meta.get("theme", "caller/native")})
    return rows


def current_metadata(metadata):
    # Reused text IDs retain older story metadata in the historical source.
    # Correct their present caller-specific meanings, without touching ROM bytes.
    overrides = {
        2406: ("Cecil", "$16 Cecil", "GOTHICA_TOWNS_EBON_IVOR"),
        2407: ("Blimp", "$06 Blimp", "CONTEXTUAL_SAVE"),
        2408: ("Professor Ruffleberg", "$0C Professor", "OMNITOPIA_PROFESSOR_CARLTRON"),
        2410: ("Omnitopia save terminal", "$05 Robot", "OMNITOPIA_PROFESSOR_CARLTRON"),
        2411: ("Omnitopia save terminal", "$05 Robot", "OMNITOPIA_PROFESSOR_CARLTRON"),
        2414: ("Junkyard save terminal", "$05 Robot", "OMNITOPIA_PROFESSOR_CARLTRON"),
        2415: ("Strong Heart", "$07 Strong Heart", "PREHISTORIA_WILDS"),
        2416: ("Strong Heart", "$07 Strong Heart", "PREHISTORIA_WILDS"),
        2417: ("Strong Heart", "$07 Strong Heart", "PREHISTORIA_WILDS"),
    }
    result = {k: dict(v) for k, v in metadata.items()}
    for text_id, (speaker, theme, arena) in overrides.items():
        result[text_id] = {"id": text_id, "hex": f"{text_id:04X}", "arena": arena,
                           "source": speaker, "assignment": "fixed", "theme": theme,
                           "helper": theme.split()[0]}
    return result


def consolidated_source(rom, owners, groups, metadata, arenas, input_name, checksum, digest):
    rows = text_rows(rom, owners, groups, metadata)
    targets = {}
    ngplus_targets = {}
    for row in rows:
        targets.setdefault(row["target_pc"], []).append(row["id"])
        if row["ngplus_target_cpu"]:
            ngplus_targets.setdefault(row["target_pc"] + 0x10000, []).append(row["id"])
    # Every patched primary pointer receives a named three-byte definition.
    boundaries = set(targets) | set(ngplus_targets)
    pointer_starts = {}
    for row in rows:
        pc = TEXT_TABLE + row["id"]*3
        if all(owners[pc:pc+3]):
            pointer_starts[pc] = row
            boundaries.update((pc, pc+3))
    output = [
        "; Secret of Evermore: Casual Run -- consolidated development source",
        "; This is the editable current development definition; accepted release v1.33 is retained.",
        f"; Byte-identical baseline: {input_name}",
        f"; Expected built SHA-256: {digest}",
        f"; Expected checksum/complement: ${checksum:04X} / ${checksum ^ 0xFFFF:04X}",
        "; Includes accepted Strong Heart R4 flow and the existing Sandpits spawn test.",
        "; No bytes relocated, removed, or reclaimed. No event/text behavior changed.",
        "; Each address is written exactly once. Bytes are grouped in CPU-address order.",
        "; Origin comments are provenance; version names in labels do not select behavior.",
        "; Detailed historical design/withdrawal notes remain in the preserved baseline source.",
        "; Metadata below describes primary TEXT ownership, not an event reachability proof.",
        "; Generated layout files are advisory: unreferenced or zero bytes are NOT declared free.",
        "; Text pointer decode: pc=(raw & $007FFF)|((raw & $7F8000)<<1).",
        "; Raw text allocations must stay within a bank's lower $0000-$7FFF half.",
        "; Preserve matched F2/F3 NG+ offsets and the native F4 bank selector.",
        "; Shared native save helpers $4E/$4F and global IDs remain native-owned.",
        "; Edit this source directly; validate with script_layout.py audit before handoff.",
        "arch 65816", "hirom", "",
    ]
    emitted_names = set()
    pc = 0
    while pc < len(rom):
        if not owners[pc]:
            pc += 1
            continue
        start = pc
        owner = owners[pc]
        pc += 1
        while pc < len(rom) and owners[pc] == owner and pc not in boundaries:
            pc += 1
        origin = groups[owner]
        name = origin["label"]
        if start in pointer_starts:
            row = pointer_starts[start]
            name = f"TextPointer_{row['id']:04d}"
            note = f"; TEXT {row['id']:04d} -> {row['target_cpu']} ({row['mode']}); {row['speaker']}"
            output.append(note)
        elif start in targets:
            ids = targets[start]
            name = "LiveText_" + "_".join(f"{i:04d}" for i in ids)
            output.append("; Primary TEXT targets: " + ", ".join(str(i) for i in ids))
            output.extend(origin["notes"])
        elif start in ngplus_targets:
            name = "NGPlusText_" + "_".join(f"{i:04d}" for i in ngplus_targets[start])
            output.append("; Mirrored NG+ TEXT targets: " + ", ".join(str(i) for i in ngplus_targets[start]))
            output.extend(origin["notes"])
        else:
            output.extend(note for note in origin["notes"] if not note.startswith(";@TEXTMETA"))
        if name in emitted_names:
            name += f"_At_{start + 0xC00000:06X}"
        emitted_names.add(name)
        output += [f"; Origin: {origin['label']}, baseline line {origin['line']}.",
                   f"org ${start + 0xC00000:06X}", name + ":"]
        for offset in range(start, pc, 16):
            output.append("    db " + ", ".join(f"${b:02X}" for b in rom[offset:min(pc, offset+16)]))
        output.append("")
    output.append("; Canonical current per-TEXT metadata (one row per ID).")
    output.extend(";@TEXTMETA " + json.dumps(metadata[key], ensure_ascii=False, separators=(",", ":"))
                  for key in sorted(metadata))
    output.append("; Regional reserves carried forward; ownership counts are regenerated in the layout report.")
    output.extend(";@TEXTARENA " + json.dumps(arena, separators=(",", ":")) for arena in arenas)
    return "\n".join(output) + "\n"


def report(rom, owners, groups, metadata, arenas, stats, digest, baseline_digest=None):
    rows = text_rows(rom, owners, groups, metadata)
    ranges = source_ranges(owners, groups)
    banks = []
    target_counts = {}
    ngplus_counts = {}
    for row in rows:
        bank = row["target_pc"] >> 16
        target_counts[bank] = target_counts.get(bank, 0) + 1
        if row["ngplus_target_cpu"]:
            ngplus_counts[bank+1] = ngplus_counts.get(bank+1, 0) + 1
    for bank in range(0x30, 0x40):
        start = bank << 16
        banks.append({"cpu_bank": f"${bank + 0xC0:02X}",
                      "source_owned_lower_half": sum(bool(v) for v in owners[start:start+0x8000]),
                      "source_owned_upper_half": sum(bool(v) for v in owners[start+0x8000:start+0x10000]),
                      "primary_text_pointer_count": target_counts.get(bank, 0),
                      "mirrored_ngplus_target_count": ngplus_counts.get(bank, 0)})
    reserve_rows = []
    for arena in arenas:
        start, end = arena["pc_start"], arena["pc_end_exclusive"]
        if start < 0 or end > len(rom) or start >= end:
            raise ValueError("Invalid declared arena reserve")
        claimed = sum(bool(v) for v in owners[start:end])
        reserve_rows.append({**arena, "bytes": end-start, "source_owned_bytes": claimed,
                             "source_unwritten_bytes_not_certified_free": end-start-claimed,
                             "primary_targets_stored_here": sum(start <= row["target_pc"] < end for row in rows),
                             "foreign_arena_primary_ids": [row["id"] for row in rows if start <= row["target_pc"] < end and row["arena"] != arena["name"]]})
    return {"sha256": digest, "comparison_baseline_sha256": baseline_digest,
            "byte_identical_to_baseline": digest == baseline_digest if baseline_digest else None,
            "scope": "Primary text table and final source writes; not complete event/indirect reachability",
            "free_space_policy": "No source-unwritten, zero, or unreferenced range is certified free",
            "statistics": stats, "banks": banks, "arena_reserves": reserve_rows,
            "source_ranges": ranges, "text_pointers": rows}


def write_reports(layout, prefix):
    Path(str(prefix) + ".json").write_text(json.dumps(layout, indent=2) + "\n", encoding="utf-8")
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=layout["text_pointers"][0].keys())
    writer.writeheader()
    writer.writerows(layout["text_pointers"])
    Path(str(prefix) + "_text.csv").write_text(stream.getvalue(), encoding="utf-8")
    lines = ["# Current script layout", "", f"Built ROM SHA-256: `{layout['sha256']}`.", "",
             "This map records all 3,002 primary text pointers and every final source-owned range. "
             "It does not certify unused text IDs, dead payloads, or free space. "
             "Indirect references and native event entry points require separate audits.", "",
             "| Expansion bank | Owned lower half | Owned upper half | Primary text pointers | NG+ mirrors |",
             "|---|---:|---:|---:|---:|"]
    for bank in layout["banks"]:
        lines.append(f"| {bank['cpu_bank']} | {bank['source_owned_lower_half']:,} | "
                     f"{bank['source_owned_upper_half']:,} | {bank['primary_text_pointer_count']} | {bank['mirrored_ngplus_target_count']} |")
    lines += ["", "Owned counts describe writes in the source, including retained historical payloads "
              "and non-text systems. They are not live text sizes or safe allocation budgets.", ""]
    lines += ["## Declared regional reserves", "",
              "These are the inherited regional storage reservations. Counts reflect present physical writes, "
              "including later exceptions such as Strong Heart text in the Nobilia market reserve. "
              "Unwritten capacity still requires ownership and inbound-reference checks before allocation.", "",
              "| Reserve | CPU range | Source-owned bytes | Unwritten bytes | Primary targets |",
              "|---|---|---:|---:|---:|"]
    for arena in layout["arena_reserves"]:
        lines.append(f"| {arena['name']} | ${arena['pc_start']+0xC00000:06X}-${arena['pc_end_exclusive']-1+0xC00000:06X} "
                     f"| {arena['source_owned_bytes']:,} | {arena['source_unwritten_bytes_not_certified_free']:,} "
                     f"| {arena['primary_targets_stored_here']} |")
    lines.append("")
    Path(str(prefix) + ".md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("consolidate", "audit"))
    parser.add_argument("base_rom", type=Path)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, help="Consolidated ASM destination")
    parser.add_argument("--baseline-rom", type=Path, help="Require exact built-ROM equality")
    parser.add_argument("--report-prefix", type=Path, required=True)
    args = parser.parse_args()
    base = args.base_rom.read_bytes()
    if len(base) != build.BASE_SIZE or build.sha256(base) != build.BASE_SHA256:
        raise ValueError("Expected clean unheadered USA base ROM")
    source = args.source.read_text(encoding="utf-8")
    arenas = arena_reserves(source)
    rom, owners, groups, metadata, stats = parse_source(source, base)
    checksum = finalize_checksum(rom)
    digest = build.sha256(rom)
    baseline_digest = None
    if args.baseline_rom:
        baseline = args.baseline_rom.read_bytes()
        baseline_digest = build.sha256(baseline)
        if bytes(rom) != baseline:
            raise ValueError("Built ROM does not match supplied baseline")
    if args.mode == "consolidate":
        if not args.output:
            parser.error("consolidate requires --output")
        metadata = current_metadata(metadata)
        output = consolidated_source(rom, owners, groups, metadata, arenas, args.source.name, checksum, digest)
        rebuilt, new_owners, new_groups, new_meta, new_stats = parse_source(output, base)
        finalize_checksum(rebuilt)
        if rebuilt != rom or new_stats["overwritten_write_bytes"]:
            raise ValueError("Consolidation changed bytes or retained overlapping writes")
        if any(bool(a) != bool(b) for a, b in zip(owners, new_owners)):
            raise ValueError("Consolidation changed allocation coverage")
        args.output.write_text(output, encoding="utf-8")
        print("Consolidated:", args.output)
        print("Removed overwritten writes:", stats["overwritten_write_bytes"])
        rom, owners, groups, metadata, stats = rebuilt, new_owners, new_groups, new_meta, new_stats
    elif stats["overwritten_write_bytes"]:
        raise ValueError("Audit requires one active write per address")
    layout = report(rom, owners, groups, metadata, arenas, stats, digest, baseline_digest)
    write_reports(layout, args.report_prefix)
    print("Verified SHA-256:", digest)
    print("Primary text pointers validated:", len(layout["text_pointers"]))
    print("Final source ranges:", len(layout["source_ranges"]))


if __name__ == "__main__":
    main()
