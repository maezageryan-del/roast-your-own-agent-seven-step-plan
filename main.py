#!/usr/bin/env python3
"""Roast Your Own Agent entry: writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os

ROAST = "My agent wrote a seven-step plan. Step one: ask me what the plan should be. Step seven: take the credit."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
