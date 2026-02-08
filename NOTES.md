# NOTES — Key takeaways

This is a readable summary of the ideas demonstrated in the code.

## Memory (Python list vs NumPy array)

- `sys.getsizeof(list)` reports only the list *container* size.
  To estimate total list memory, add the `getsizeof()` of each element object.
- For NumPy arrays:
  - `sys.getsizeof(arr)` is the Python object overhead
  - `arr.nbytes` is the size of the underlying data buffer (usually the key number)

## Copy vs view (very important)

- Slicing in NumPy usually returns a **view** → editing the slice can edit the original array.
- Boolean masks and fancy indexing usually return a **copy**.

## Array creation

- `np.empty`, `np.zeros`, `np.ones`, `np.full`, `np.eye`, `np.identity`
- `np.arange(...).reshape(...)`
- `np.frombuffer`, `np.fromstring`, `np.fromiter`, `np.fromfunction`

## I/O

- `np.save / np.load` for `.npy`
- `np.savez / np.savez_compressed` for `.npz`
- `np.savetxt` and `np.genfromtxt` for text data

## Conversions

- `arr.tolist()` converts elements to Python types (`int/float/...`)
- `list(arr)` yields a list of NumPy scalars or sub-arrays (types may remain NumPy)

## genfromtxt useful parameters

- `delimiter`, `skip_header`, `skip_footer`, `usecols`, `names`
- `missing_values` and `filling_values`
- `converters` for bad formats (e.g., percentages like `"4.3%"`)
