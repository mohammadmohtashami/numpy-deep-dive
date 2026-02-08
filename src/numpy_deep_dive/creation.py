"""
Array creation + shape/dtype + order flags.

Covers original topics:
- shape, dtype, ndim
- np.empty / empty_like
- np.eye / identity
- zeros/ones/full + *_like
- arange + reshape
- contiguous vs transpose flags
- asmatrix (legacy-ish) vs matrix

Run:
    python -m numpy_deep_dive.creation
"""

from __future__ import annotations

import numpy as np


def demo_shape_dtype() -> None:
    print("== shape / dtype ==")
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([[1, 2, 3, 4], [4, 3, 2, 2]])
    print("arr1.shape:", arr1.shape, "dtype:", arr1.dtype, "ndim:", arr1.ndim)
    print("arr2.shape:", arr2.shape, "dtype:", arr2.dtype, "ndim:", arr2.ndim)
    print()


def demo_empty_eye_zeros_ones_full() -> None:
    print("== empty / eye / zeros / ones / full ==")
    arr_empty = np.empty(5)
    arr_empty2 = np.empty((1, 2), dtype=int)
    print("empty(5):", arr_empty)
    print("empty((1,2), int):", arr_empty2)

    base = np.array([[1, 2], [3, 4]])
    print("empty_like(base):\n", np.empty_like(base))

    print("eye(3):\n", np.eye(3))
    print("eye(2, k=1):\n", np.eye(2, k=1))
    print("identity(3):\n", np.identity(3, dtype=int))
    print("ones((2,1)):\n", np.ones((2, 1)))
    print("zeros((2,2)):\n", np.zeros((2, 2)))
    print("zeros_like(base):\n", np.zeros_like(base))
    print("full((3,3), 2):\n", np.full((3, 3), fill_value=2))
    print()


def demo_arange_reshape_contiguous() -> None:
    print("== arange + reshape + contiguous flags ==")
    a = np.arange(6).reshape((2, 3))
    print("a:\n", a)

    x = np.ascontiguousarray(a)
    print("x.flags (C contiguous expected):", x.flags["C_CONTIGUOUS"], "F:", x.flags["F_CONTIGUOUS"])

    z = x.T
    print("z = x.T flags (often F contiguous):", z.flags["C_CONTIGUOUS"], "F:", z.flags["F_CONTIGUOUS"])
    print()


def demo_matrix_vs_asmatrix() -> None:
    print("== matrix vs asmatrix ==")
    x = np.arange(4).reshape((2, 2))
    y = np.asmatrix(x)  # typically a view-like wrapper (copy=False)
    m = np.matrix(x)    # matrix(...) often copies by default
    print("x type:", type(x))
    print("asmatrix(x) type:", type(y))
    print("matrix(x) type:", type(m))
    print()


def main() -> None:
    print("----- creation.py -----")
    demo_shape_dtype()
    demo_empty_eye_zeros_ones_full()
    demo_arange_reshape_contiguous()
    demo_matrix_vs_asmatrix()


if __name__ == "__main__":
    main()
