"""
### What is `yield`?

The `yield` statement is used in Python to create a generator. A generator is a special type of iterator that lazily generates values on 
the fly without storing them in memory. When a function contains a `yield` statement, it automatically becomes a generator function.

### How `yield` Works

When a generator function is called, it doesn't execute its code. Instead, it returns a generator object. When this object is iterated 
over (for example, using a `for` loop), the function executes up to the first `yield` statement and sends that value back to the caller. 
The function then pauses its execution, retaining its state, and waits until the next value is requested. This process continues until the 
function runs out of values to yield, at which point it raises a `StopIteration` exception to signal the end of iteration.

### Memory Optimization with `yield`

The key advantage of using `yield` is memory efficiency. Traditional functions that return lists or other collections must prepare the entire collection 
in memory before returning it. In contrast, a generator creates values one at a time, which means that it can handle much larger datasets without consuming 
a large amount of memory.

### Example with Explanation

Let's consider a simple example to demonstrate how `yield` works and its memory benefits:
"""

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for number in countdown(5):
    print(number)

"""
**How this works:**

1. **Creating the Generator**: When we call `countdown(5)`, it returns a generator object. The function's code hasn't run yet.

2. **Iterating Over the Generator**: The `for` loop starts iterating over the generator. On the first iteration, `countdown` runs until it 
hits `yield n`, yielding `5`. The function then pauses.

3. **Resuming Execution**: On the next iteration, the function resumes where it left off (right after the `yield`), decrements `n` to `4`, and 
hits the `yield` again, pausing after yielding `4`. This process repeats until `n` becomes `0`.

4. **Memory Efficiency**: At no point does the `countdown` function store a list of numbers from 5 to 1 in memory. Instead, it generates each number 
on the fly, one at a time, as the loop requests them. This is much more memory-efficient than generating and storing the entire list, especially for 
large datasets.

**Expected Output:**
```
5
4
3
2
1
```

In the context of your audio data processing, using a generator with `yield` allows you to process each audio file one at a time, rather than loading 
and processing all audio files at once, which can be very memory-intensive. This way, you efficiently use memory and avoid overwhelming your system, 
especially when working with large datasets.
"""