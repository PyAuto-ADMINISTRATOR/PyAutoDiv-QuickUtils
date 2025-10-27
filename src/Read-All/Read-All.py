#!/usr/bin/env python3
import pyperclip as clip
import os

def main():
    struct = []
    allowed = [
        "txt",
        "py",
        "pyw",
        "json",
        "c",
        "cpp",
        "sh",
        "cfg",
        "gd",
        "h"
    ]
    curr = os.path.abspath(__file__)
    dir_of_curr = os.path.dirname(curr)

    for dirpath, _, filenames in os.walk(os.getcwd()):
        print(f"Entering \"{dirpath}\"\n")
        for fname in filenames:
            tname = fname.split('.', 1)[-1].lower()
            if not tname in allowed:
                print(f"Skipped unallowed file \"{tname}\"")
                continue
            path = os.path.abspath(os.path.join(dirpath, fname))
            relpath = os.path.relpath(path, dir_of_curr)
            if path != curr:
                try:
                    with open(path, 'r', encoding="utf-8") as f:
                        a = f.read()
                    if a.strip() == "":
                        a = "[{empty}]"
                except Exception:
                    a = "[{unreadable}]"

                struct.append(f"{relpath}:\n{a}")
                print(f"Caught \"{relpath}\"")
            else:
                print("Skipped self")
        print(f"\nExiting \"{dirpath}\"\n")

    clip.copy("\n\n\n".join(struct))

main()
