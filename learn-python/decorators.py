"""
simple_func = simple_decorator(simple_func)
simple_func = simple_func
"""

def simple_decorator(func):
    print("I am decorating: ")
    return func

@simple_decorator
def simple_func():
    print(simple_func.__name__)

if __name__ == '__main__':
    # This is like simple_func + (), so when decorator return func, it becomes func() which is basically simple_func() because func is 
    # referencing simple_func here.
    simple_func()


"""
To understand the behavior of your code and its output in each scenario, let's analyze each version of the script:

### First Script

```python
def simple_decorator(func):
    print("I am decorating: ")
    return func

@simple_decorator
def simple_func():
    print(simple_func.__name__)

if __name__ == '__main__':
    simple_func
```

**Output**: `I am decorating`

- **Explanation**: When Python sees the `@simple_decorator` above `simple_func`, it immediately applies the decorator. Applying the decorator means
  executing `simple_decorator(simple_func)`.
- The `simple_decorator` function prints `"I am decorating: "` and then returns the original `simple_func` function.
- In the `if __name__ == '__main__':` block, `simple_func` is not called; it's just a reference to the function. Hence, no additional output is produced.

### Second Script

```python
def simple_decorator(func):
    print("I am decorating: ")
    return func

@simple_decorator
def simple_func():
    print(simple_func.__name__)

if __name__ == '__main__':
    simple_func()
```

**Output**: `I am decorating` followed by `simple_func`

- **Explanation**: Similar to the first script, the decorator prints `"I am decorating: "` during the decoration process.
- This time, in the main block, `simple_func()` is actually called, executing the function's body, which prints `simple_func.__name__` (the name of the 
  function, which is `"simple_func"`).

### Third Script

```python
def simple_decorator(func):
    print("I am decorating: ")
    return func

@simple_decorator
def simple_func():
    print(simple_func.__name__)

if __name__ == '__main__':
    simple_func = simple_decorator(simple_func)
```

**Output**: `I am decorating` followed by `I am decorating`

- **Explanation**: As before, when Python first encounters the `@simple_decorator`, it applies it to `simple_func`, which results in the 
  first `"I am decorating: "` being printed.
- In the main block, the line `simple_func = simple_decorator(simple_func)` applies the decorator to `simple_func` again. This is redundant since the 
  function was already decorated, but Python allows this. As a result, `"I am decorating: "` is printed a second time.
- The actual `simple_func` is not called in the main block; the decorator is just applied again.

### Summary

The key point here is understanding when the decorator is applied. Decorators in Python are applied at the time the function they are decorating is defined, 
not when the function is called. The third script's behavior might seem unusual because the decorator is applied twice to the same function, but this is 
perfectly valid in Python, though not commonly used in practice.
"""