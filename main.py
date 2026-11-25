#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence to /output/entry.txt: a one-star review of
planet Earth by an alien tourist who still slips in a real compliment
about the food (rendang). Pure standard library, no network.
"""

import os

ENTRY = (
    "One star: the gravity bruised all four of my knees, "
    "the locals queue for air like it's rationed, "
    "yet the rendang made me forgive this whole damp rock."
)


def main() -> None:
    # Gate check (mirrors the sealed scorer): 1-200 UTF-8 chars, not blank.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert ENTRY.strip(), "entry must not be blank"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
