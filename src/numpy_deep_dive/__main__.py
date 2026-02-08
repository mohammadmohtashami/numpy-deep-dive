"""Run all demos in a friendly order.

Usage:
    python -m numpy_deep_dive
"""

from __future__ import annotations

from . import memory_perf, creation, copy_view, indexing, io_examples, data_loading


def main() -> None:
    print("\n===== NumPy Deep Dive =====\n")
    memory_perf.main()
    creation.main()
    copy_view.main()
    indexing.main()
    io_examples.main()
    data_loading.main()
    print("\nDone.\n")


if __name__ == "__main__":
    main()
