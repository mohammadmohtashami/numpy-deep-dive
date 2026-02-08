"""
Copy vs view & related constructors.

Covers original topics:
- np.array(copy=...), dtype changes force a copy
- matrix subclass sharing memory and subok=True behavior
- np.asarray (copy=False default)
- np.asanyarray (subok=True + copy=False behavior)
- np.copy (shallow copy of ndarray data buffer)

Run:
    python -m numpy_deep_dive.copy_view
"""

from __future__ import annotations

import numpy as np


def demo_np_array_copy_behavior() -> None:
    print("== np.array copy behavior ==")
    arr = np.array([1, 2, 3])

    arr2 = np.array(arr)  # copy by default
    print("arr is arr2:", arr is arr2)

    arr3 = np.array(arr, copy=False)  # view when possible
    print("arr is arr3:", arr is arr3)

    arr4 = np.array(arr, copy=False, dtype=np.float32)  # dtype change forces a copy
    print("arr4:", arr4, "arr4 is arr:", arr4 is arr)
    print()


def demo_matrix_subclass_and_subok() -> None:
    print("== matrix subclass, memory sharing, subok ==")
    mat = np.matrix([1, 2, 3])
    arr = np.array(mat, copy=False)  # ndarray view on matrix data when possible

    print("type(mat):", type(mat), "type(arr):", type(arr))
    print("np.may_share_memory(mat, arr):", np.may_share_memory(mat, arr))

    # Changing arr can affect mat if they share memory:
    arr[0, 2] = 10
    print("mat after arr edit:", mat)
    print("arr:", arr)

    arr_sub = np.array(mat, copy=False, subok=True)
    print("subok=True keeps subclass? type(arr_sub):", type(arr_sub))
    print()


def demo_asarray_asanyarray() -> None:
    print("== asarray / asanyarray ==")
    arr = np.array([1, 2, 3])
    arr6 = np.asarray(arr)
    print("arr is np.asarray(arr):", arr is arr6)

    mat = np.matrix([1, 2, 3])
    arr7 = np.asanyarray(mat)  # keeps subclass if possible
    print("np.asanyarray(mat) is mat:", arr7 is mat, "type:", type(arr7))
    print()


def demo_np_copy() -> None:
    print("== np.copy (ndarray data copy) ==")
    x = np.array([[1, 2], [3, 4]])
    y = np.copy(x)
    x[1, 1] = 1
    print("x:\n", x)
    print("y (unchanged):\n", y)
    print()


def main() -> None:
    print("----- copy_view.py -----")
    demo_np_array_copy_behavior()
    demo_matrix_subclass_and_subok()
    demo_asarray_asanyarray()
    demo_np_copy()


if __name__ == "__main__":
    main()
