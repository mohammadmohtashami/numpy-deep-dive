"""
Constructors + genfromtxt + conversions to list.

Covers original topics:
- frombuffer (bytes -> array of bytes)
- fromfunction (function over indices)
- fromiter (iterator -> array)
- fromstring (string -> array)
- genfromtxt (StringIO example + important parameters)
- tolist vs list(array) type differences

Run:
    python -m numpy_deep_dive.data_loading
"""

from __future__ import annotations

import io

import numpy as np


def demo_frombuffer() -> None:
    print("== frombuffer ==")
    b = b"mohammad"
    a = np.frombuffer(b, dtype="S1", count=-1)
    print(a)
    print()


def demo_fromfunction() -> None:
    print("== fromfunction ==")
    x = np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
    y = np.fromfunction(lambda i, j: i + j, (2, 2), dtype=int)
    print("i==j:\n", x)
    print("i+j:\n", y)
    print()


def demo_fromiter() -> None:
    print("== fromiter ==")
    gen = (x**x for x in range(5))
    arr = np.fromiter(gen, dtype=float, count=3)
    print(arr)
    print()


def demo_fromstring() -> None:
    print("== fromstring ==")
    txt = "1,2,3,4,5"
    print(np.fromstring(txt, count=3, sep=","))
    print()


def demo_genfromtxt_stringio() -> None:
    print("== genfromtxt with StringIO ==")
    data = "1,2,3\\n4,5,6"
    f = io.StringIO(data)
    x = np.genfromtxt(f, delimiter=",")
    print(x)
    print()

    print("Important genfromtxt params (notes):")
    print("- delimiter=',' | skip_header | skip_footer | usecols | names=True")
    print("- missing_values={'A':'N/A', ...} + filling_values={'A':0, ...}")
    print("- converters={col_index: func} for bad formats (e.g. '4.3%')")
    print()


def demo_tolist_vs_list() -> None:
    print("== tolist() vs list(arr) ==")
    x = np.uint32([1, 2, 3])
    x_list = x.tolist()
    print("type(x_list[0]) =", type(x_list[0]))
    print("type(list(x)[0]) =", type(list(x)[0]))

    arr = np.array([[1, 2], [3, 2]])
    print("list(arr) ->", list(arr))
    print("arr.tolist() ->", arr.tolist())
    print()


def main() -> None:
    print("----- data_loading.py -----")
    demo_frombuffer()
    demo_fromfunction()
    demo_fromiter()
    demo_fromstring()
    demo_genfromtxt_stringio()
    demo_tolist_vs_list()


if __name__ == "__main__":
    main()
