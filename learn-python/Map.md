### Object Structure in Memory (Python Example)
In Python's C API, every object starts with a header containing:

**Reference count**: How many references point to this object.\
**Type pointer**: Points to a PyTypeObject, which contains information about the object's type.


The Python map() function returns an iterator, which allows for lazy evaluation—meaning it computes values only when needed, rather than upfront. It doesn't generate all the results at once; instead, it generates the next result on demand, when you explicitly iterate over it (e.g., in a for loop, or by using next()). This behavior enables the efficient handling of large datasets, without requiring the whole dataset to be loaded into memory at once.
The rationale should be the same as to why we use generators instead of list comprehensions. Why map still exists at all when generator expressions also exist, is that it can take multiple iterator arguments that are all looped over and passed into the function:

```map(min, [1,2,3,4], [0,10,0,10])```

### How `map()` Works:
The `map()` function internally:
1. Holds a reference to the function `func` and the iterable.
2. Uses an internal state to track where it is in the iteration.
3. When you request the next element (using `next()` or iterating over it), it applies `func` to the next element of the iterable, and returns the result.

This is what makes it **lazy**—the computation happens only when requested, allowing it to work efficiently with large or infinite iterables without needing to store all the results in memory.

### Vectorization (as done by libraries like NumPy)
**Vectorization** refers to the process of applying operations over entire arrays (vectors) at once, often leveraging CPU-level optimizations like SIMD (Single Instruction, Multiple Data). For this, you need the entire data at once in memory. This is commonly used in numerical computing libraries like **NumPy**.

In NumPy, operations are applied element-wise over large data structures (like arrays) in a way that is often **highly optimized and parallelized**. For example:
```
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = a + b  # Vectorized addition
```
Here, the addition happens all at once for the entire array, leveraging CPU optimizations, without explicit iteration.

### Does `map()` Use Vectorization?
No, `map()` does not perform any vectorization or parallel processing under the hood. Instead, it applies a function to each element of the iterable **one at a time** in a serial, step-by-step manner. This is fundamentally different from vectorized operations, which are applied across multiple elements simultaneously.

### Comparison: `map()` vs. Vectorization

| Feature                  | `map()`                                   | Vectorization (e.g., NumPy)          |
|--------------------------|-------------------------------------------|--------------------------------------|
| **Computation**           | Lazy, applies the function one at a time | Operates over entire arrays at once |
| **Memory Usage**          | Efficient, uses little memory since results are produced one by one | Requires memory for entire array in memory |
| **Performance**           | Suitable for non-numeric or functional programming tasks, but generally slower | Optimized for numerical operations, often faster |
| **Parallelism**           | No inherent parallelism                   | Leverages CPU-level parallelism     |
| **Typical Use Cases**     | Iterating over any iterable (e.g., list, tuple, etc.) | Fast computations on large arrays  |

### Can `map()` Be Combined with Vectorization?
While `map()` itself doesn't vectorize operations, you can combine it with libraries like NumPy for better performance when working with large numeric data. For example, you could apply a `map()` to an iterable that contains NumPy arrays or vectorized operations.

However, in practice, if you are working with large datasets and numerical computations, you're better off using **NumPy** or other specialized libraries directly, as they are designed for vectorized operations and can provide significant performance benefits.
