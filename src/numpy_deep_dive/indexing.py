"""
Indexing: slices (views), boolean masks, fancy indexing.

Covers original topics:
- slicing returns views (editing slice edits the original)
- boolean mask returns copy
- fancy indexing examples (rows reorder, element selection)
- axis meaning in 2D (rows axis=0, cols axis=1)

Run:
    python -m numpy_deep_dive.indexing
"""

from __future__ import annotations

import numpy as np


def demo_slice_is_view() -> None:
    print("== slicing returns view ==")
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = x[2:6]
    y[0] = 10
    print("x:", x)
    print("y:", y)
    print()


def demo_2d_indexing_axis() -> None:
    print("== 2D indexing + axis notes ==")
    arr = np.arange(12).reshape(3, 4)
    val = arr[2, 3]
    print("arr:\n", arr)
    print("arr[2,3] =", val)
    # Examples (views):
    print("arr[:2, 1:]:\n", arr[:2, 1:])
    print("arr[1, :2] shape:", arr[1, :2].shape, "arr[1:2, :2] shape:", arr[1:2, :2].shape)
    print()


def demo_boolean_mask_copy() -> None:
    print("== boolean mask returns copy ==")
    names = np.array(["ali", "mohammad", "ali", "hassan"])
    data = np.random.randn(4, 4)

    mask = names == "ali"
    picked = data[mask]
    print("mask:", mask)
    print("picked rows:\n", picked)

    # Prove it's a copy:
    if picked.size:
        picked[0, 0] = 999
    print("data[mask] after editing picked (data unchanged):\n", data[mask])
    print()


def demo_fancy_indexing() -> None:
    print("== fancy indexing ==")
    x = np.empty((4, 3))
    for i in range(4):
        x[i] = i
    print("x:\n", x)

    y = x[[1, 3, 2]]  # reorder rows
    print("x[[1,3,2]]:\n", y)

    z = x[[1, 2, 3], [2, 2, 0]]  # pick specific elements -> 1D
    print("x[[1,2,3],[2,2,0]]:", z)

    # 2D selection: first choose rows, then reorder columns
    a = x[[1, 2, 3]][:, [2, 0, 1]]
    print("x[[1,2,3]][:,[2,0,1]]:\n", a)
    print()


def main() -> None:
    print("----- indexing.py -----")
    demo_slice_is_view()
    demo_2d_indexing_axis()
    demo_boolean_mask_copy()
    demo_fancy_indexing()


if __name__ == "__main__":
    main()
