"""
I/O examples: npy/npz + notes for savetxt/fromregex.

Covers original topics:
- np.save / np.load (.npy)
- np.savez / np.savez_compressed (.npz)
- np.savetxt basics (not executed by default)
- np.fromregex pattern sketch

Run:
    python -m numpy_deep_dive.io_examples
"""

from __future__ import annotations

import os
import tempfile

import numpy as np


def demo_save_load_npy() -> None:
    print("== np.save / np.load (.npy) ==")
    arr = np.arange(6).reshape(2, 3)
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "my_array.npy")
        np.save(path, arr)
        loaded = np.load(path, allow_pickle=False)
        print("saved arr:\n", arr)
        print("loaded:\n", loaded)
    print()


def demo_savez_npz() -> None:
    print("== np.savez / np.savez_compressed (.npz) ==")
    arr = np.array([i + j for i in range(2) for j in range(2)])
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "bundle.npz")
        np.savez(path, x=arr)  # named array in container
        loaded = np.load(path, allow_pickle=False)
        print("files:", loaded.files)
        print("loaded['x']:", loaded["x"])

        path2 = os.path.join(d, "bundle_compressed.npz")
        np.savez_compressed(path2, x=arr)
        loaded2 = np.load(path2, allow_pickle=False)
        print("compressed files:", loaded2.files)
        print("loaded2['x']:", loaded2["x"])
    print()


def notes_savetxt_fromregex() -> None:
    print("== notes: savetxt / fromregex (not executed) ==")
    print("- np.savetxt('file.txt', arr, fmt='%.2f', delimiter=' ')  # works for 1D/2D arrays")
    print("- regexp example: r'(\\d+)\\s(...)'")
    print("- np.fromregex('file.txt', regexp, dtype=[('num', np.int64), ('key','S3')])")
    print()


def main() -> None:
    print("----- io_examples.py -----")
    demo_save_load_npy()
    demo_savez_npz()
    notes_savetxt_fromregex()


if __name__ == "__main__":
    main()
