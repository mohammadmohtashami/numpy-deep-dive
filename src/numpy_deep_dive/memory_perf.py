"""
Memory + performance comparisons: Python lists vs NumPy arrays.

Covers topics from the original study script:
- list memory estimation (container + elements)
- NumPy array memory: object overhead vs data buffer (nbytes)
- mini benchmark: list comprehension vs vectorized NumPy

Run:
    python -m numpy_deep_dive.memory_perf
"""

from __future__ import annotations

from dataclasses import dataclass
from sys import getsizeof
from time import perf_counter
from typing import Callable

import numpy as np


@dataclass(frozen=True)
class TimingResult:
    name: str
    seconds: float


def deep_getsizeof_list(values: list[int]) -> int:
    \"\"\"Estimate size of a list of ints: list container + each int object.\"\"\"
    total = getsizeof(values)
    for v in values:
        total += getsizeof(v)
    return total


def numpy_memory_report(arr: np.ndarray) -> dict[str, int]:
    \"\"\"Report NumPy memory metrics (object overhead + data buffer).\"\"\"
    return {
        "getsizeof(arr)_object_overhead_bytes": int(getsizeof(arr)),
        "arr.nbytes_data_buffer_bytes": int(arr.nbytes),
        "dtype_itemsize_bytes": int(arr.dtype.itemsize),
        "size_num_elements": int(arr.size),
    }


def time_best_of(fn: Callable[[], None], repeats: int = 7) -> float:
    \"\"\"Best-of timing over repeats (min) to reduce noise.\"\"\"
    best = float("inf")
    for _ in range(repeats):
        t0 = perf_counter()
        fn()
        dt = perf_counter() - t0
        if dt < best:
            best = dt
    return best


def benchmark_addition(n: int = 1_000_000) -> list[TimingResult]:
    \"\"\"Compare list comprehension addition vs vectorized NumPy addition.\"\"\"
    # Prepare outside timing
    lst1 = list(range(n))
    lst2 = list(range(n))
    arr1 = np.arange(n)
    arr2 = np.arange(n)

    def list_add() -> None:
        _ = [a + b for a, b in zip(lst1, lst2)]

    def numpy_add() -> None:
        _ = arr1 + arr2

    return [
        TimingResult("list_comprehension_zip", time_best_of(list_add)),
        TimingResult("numpy_vectorized", time_best_of(numpy_add)),
    ]


def demo_memory_small() -> None:
    print("== Memory (small example) ==")
    my_list = [1, 2, 3]
    arr = np.array([1, 2, 3], dtype=np.int64)

    print("python_list_estimated_bytes:", deep_getsizeof_list(my_list))
    rep = numpy_memory_report(arr)
    for k, v in rep.items():
        print(f"{k}: {v}")
    print()


def demo_speed() -> None:
    print("== Speed (mini benchmark) ==")
    results = benchmark_addition()
    for r in results:
        print(f"{r.name}: {r.seconds:.6f} s")

    list_t = next(r.seconds for r in results if r.name == "list_comprehension_zip")
    np_t = next(r.seconds for r in results if r.name == "numpy_vectorized")
    if np_t > 0:
        print(f"speedup (list / numpy): {list_t / np_t:.2f}x")
    print()


def main() -> None:
    print("----- memory_perf.py -----")
    demo_memory_small()
    demo_speed()


if __name__ == "__main__":
    main()
