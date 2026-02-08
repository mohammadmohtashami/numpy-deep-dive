# NumPy Deep Dive

A **clean, GitHub-ready** refactor of my original one-file NumPy learning script.
Goals:

- Small, runnable demos (topic-based modules)
- Correct, reproducible mini-benchmarks (not one-off timings)
- Coverage of *everything* from the original script (nothing dropped)

> Results will vary across machines (CPU, NumPy build, BLAS, OS).

## Project structure

```
numpy-deep-dive/
  src/numpy_deep_dive/
    __init__.py
    __main__.py
    memory_perf.py
    creation.py
    copy_view.py
    indexing.py
    io_examples.py
    data_loading.py
  NOTES.md
  requirements.txt
  pyproject.toml
  .gitignore
```

## Install & run

```bash
python -m venv .venv
# Linux/Mac:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

pip install -r requirements.txt

# Run everything:
python -m numpy_deep_dive

# Or run a single module:
python -m numpy_deep_dive.memory_perf
python -m numpy_deep_dive.creation
python -m numpy_deep_dive.copy_view
python -m numpy_deep_dive.indexing
python -m numpy_deep_dive.io_examples
python -m numpy_deep_dive.data_loading
```

## Benchmarking notes

- Uses `time.perf_counter()` and multiple repeats.
- Moves setup outside the timed section when possible.
- Educational benchmarks only.

## Source

Refactored from the original `list_array.py` study script.

## License

MIT
