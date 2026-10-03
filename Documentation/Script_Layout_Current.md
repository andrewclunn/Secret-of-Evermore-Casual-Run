# Current script layout

Built ROM SHA-256: `90ba5f6262382de13a8437368a0c6218e84b6088ab536767d3c362e3386ea6da`.

This map records all 3,002 primary text pointers and every final source-owned range. It does not certify unused text IDs, dead payloads, or free space. Indirect references and native event entry points require separate audits.

| Expansion bank | Owned lower half | Owned upper half | Primary text pointers | NG+ mirrors |
|---|---:|---:|---:|---:|
| $F0 | 2,383 | 0 | 0 | 0 |
| $F1 | 18,415 | 605 | 1 | 0 |
| $F2 | 1,905 | 0 | 10 | 0 |
| $F3 | 2,302 | 0 | 0 | 10 |
| $F4 | 19,345 | 0 | 302 | 0 |
| $F5 | 20,884 | 12 | 218 | 0 |
| $F6 | 19,039 | 2,519 | 278 | 0 |
| $F7 | 22,046 | 6,412 | 254 | 0 |
| $F8 | 13,890 | 0 | 184 | 0 |
| $F9 | 25,784 | 135 | 307 | 0 |
| $FA | 17,172 | 555 | 240 | 0 |
| $FB | 12,749 | 149 | 381 | 0 |
| $FC | 0 | 170 | 0 | 0 |
| $FD | 0 | 136 | 0 | 0 |
| $FE | 16,538 | 164 | 243 | 0 |
| $FF | 10,952 | 0 | 164 | 0 |

Owned counts describe writes in the source, including retained historical payloads and non-text systems. They are not live text sizes or safe allocation budgets.

## Declared regional reserves

These are the inherited regional storage reservations. Counts reflect present physical writes, including later exceptions such as Strong Heart text in the Nobilia market reserve. Unwritten capacity still requires ownership and inbound-reference checks before allocation.

| Reserve | CPU range | Source-owned bytes | Unwritten bytes | Primary targets |
|---|---|---:|---:|---:|
| PROLOGUE_1965 | $F80000-$F807FF | 262 | 1,786 | 6 |
| PODUNK_OPENING | $F80800-$F80FFF | 751 | 1,297 | 14 |
| PODUNK_ENDING | $F81000-$F817FF | 620 | 1,428 | 14 |
| PREHISTORIA_WILDS | $F81800-$F83FFF | 7,253 | 2,987 | 90 |
| PREHISTORIA_VILLAGE_FIRE_EYES | $F90000-$F96FFF | 25,784 | 2,888 | 307 |
| ANTIQUA_CRUSTACIA_APPROACH | $F84000-$F857FF | 5,004 | 1,140 | 60 |
| NOBILIA_MARKET | $F40400-$F463FF | 17,259 | 7,317 | 269 |
| NOBILIA_CITY_SQUARE | $FA0100-$FA38FF | 9,985 | 4,351 | 133 |
| HORACE_WEST_BANK | $FA3900-$FA64FF | 7,022 | 4,242 | 107 |
| NOBILIA_CITY_PALACE | $F70100-$F760FF | 16,095 | 8,481 | 217 |
| NOBILIA_COLOSSEUM | $F76100-$F768FF | 914 | 1,134 | 21 |
| ANTIQUA_DESERT_TRAVEL | $FB0100-$FB10FF | 2,335 | 1,761 | 204 |
| ANTIQUA_HALL_PYRAMID | $FB1100-$FB20FF | 2,430 | 1,666 | 41 |
| HORACE_FINALE | $FB2100-$FB30FF | 2,139 | 1,957 | 44 |
| GOTHICA_ARRIVAL_DUNGEON_SEWER | $FB3100-$FB54FF | 5,689 | 3,527 | 92 |
| GOTHICA_TOWNS_EBON_IVOR | $F51400-$F57FFF | 20,043 | 7,605 | 218 |
| CAMELLIA_EBON_KEEP | $F61400-$F623FF | 3,666 | 430 | 61 |
| TINKER_GOMI_ROCKET | $F62400-$F64BFF | 8,617 | 1,623 | 125 |
| DARK_FOREST | $F64C00-$F65BFF | 3,091 | 1,005 | 31 |
| GOTHICA_CHESSBOARD_CORE | $F65C00-$F65FFF | 21 | 1,003 | 1 |
| IVOR_INTERIOR_PUPPET_MUNGOLA | $F66000-$F66FFF | 2,586 | 1,510 | 60 |
| IVOR_TOWN_FESTIVAL_MARKET | $FE0000-$FE27FF | 7,677 | 2,563 | 110 |
| IVOR_EXHIBITION_APPROACH | $FE4300-$FE5EFF | 5,107 | 2,061 | 90 |
| IVOR_CASTLE_BANQUET | $FE5F00-$FE6EFF | 3,367 | 729 | 43 |
| OMNITOPIA_PROFESSOR_CARLTRON | $FF0000-$FF2FFF | 10,952 | 1,336 | 164 |
