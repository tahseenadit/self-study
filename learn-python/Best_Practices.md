# Try Except Finally

Only catch specific exception if you want to handle them by yourself i.e if you want to do something when that specific exception occurs.\n
Otherwise, do not catch specific exception. Instead, just use general `except Exception as ex` to catch any exception.

For example, below we are catching specific exception to check if rawpy supports reading file and if not, we would like to raise a specific Error. Therefore, we caught that exception.

```
try:
    self._imgae = rawpy.imread(request.get_file())
except rawpy.NotSupportedError as ex:
    raise InitializationError(
        f"RawPy can not read {request.raw_uri}."
    ) from None
```

But do not do something like below:

```
try:
    nd_image = self._imgae.postprocess(**kwargs)
except (AttributeError, ImportError) as ex:
    print(ex)
except (rawpy.LibRawError, rawpy.LibRawFatalError, rawpy.LibRawNonFatalError) as ex:
    print(ex)
except Exception as ex:
    print(ex)
```
Because we are actually doing nothing by catching specific exception and just printing the message ex.

```
try:
    nd_image = self._imgae.postprocess(**kwargs)
except Exception as ex:
    raise ex
```

Instead, just use Exception in general as above and raise the exception instead of just printing the message. If your code snippet is part of a function and you raise exception, then may be some other function that called your function may catch it and handle it. If you just print it, then anyone calling your function won't be able to catch the exception because then you have handled it very poorly by just printing the exception message.

# Do not call low-level function of a library unless needed

If you see the imread function of rawpy library, it looks like below:

```
def imread(pathOrFile):
    """
    Convenience function that creates a :class:`rawpy.RawPy` instance, opens the given file,
    and returns the :class:`rawpy.RawPy` instance for further processing.
    
    :param str|file pathOrFile: path or file object of RAW image that will be read
    :rtype: :class:`rawpy.RawPy`
    """
    d = RawPy()
    if hasattr(pathOrFile, 'read'):
        d.open_buffer(pathOrFile)
    else:
        d.open_file(pathOrFile)
    return d
```

Instead of calling `rawpy.imread(image_path)`, you can do something like below:

```
try:
    file= rawpy._rawpy.RawPy.open_buffer(image_path)
except Exception as ex:
    raise ex
finally:
    file.close()
```
But, you should not use open_buffer because calling imread will just call open_buffer. If the author of rawpy decides to change or update open_buffer, then directly calling open_buffer may break in your code or it may not serve you the same purpose which is to read a raw image. But the author may still change or update open_buffer in such a way that the purpose of imread stays the same. So, users of rawpy do not need to change their code. If you are one of those users, then you will be safe. That is why, use imread instead of open_buffer specially when you see that imread evenrually calls open_buffer without doing any other special thing.\n
This practice applies to using other python libraries as well.

# When to Access Class Variables Directly vs. Introducing Intermediate Variables

What option below is a good practice in python and why ?

``` 
# Option 1:

var_a = Class_c.var_x
var_b = Class_c.var_x

# Option 2:

var_x = Class_c.var_x

var_a = var_x
var_b = var_x
```

That depends on whether Class_c.var_x is mutable (List, Dict) or immutable (Integer, String, Tuple). If mutable, then changing `var_a` or `var_b` or `Class_c.var_x` will change all of them since they have the same reference. But if immutable, then `var_a` and `var_b` and `Class_c.var_x` are separated and changing one won't affect the others.

**Key Points:**

- **Python passes references:** When you pass an object (like a list or dictionary) to a function, a reference (memory address) to the original object is passed, not a copy.
- **Mutability matters:** This reference passing only comes into play when dealing with **mutable objects** (objects that can be changed). Immutable objects (like integers, strings, and tuples) are always copied by value.

Keeping this in mind, here are the suggestions:

I'd recommend **Option 1:**

```python
var_a = Class_c.var_x
var_b = Class_c.var_x
```

Here's a breakdown of why it's the preferred approach:

**Clarity and Conciseness:**

- Directly accessing the class variable using `Class_c.var_x` explicitly states the source of the data. This makes the code easier to understand, especially for those unfamiliar with the class structure.

**Reduced Risk of Mutation:**

- If `Class_c.var_x` is immutable then independent assignments create separate references for `var_a` and `var_b`. Any modifications to one variable won't affect the other. This prevents unintended side effects and promotes data consistency.

**Consistency with Common Practices:**

- Accessing class variables directly through the class name aligns with well-established Python conventions. This promotes code readability and maintainability for developers familiar with these practices.

**Example:**

```python
class MyClass:
    class_var = "This is a class variable"

obj1 = MyClass()
obj2 = MyClass()

var_a = MyClass.class_var  # Access directly using class name
var_b = MyClass.class_var

print(var_a, var_b)  # Output: "This is a class variable" "This is a class variable"

# Modifications won't affect each other
var_a = "Modified value"
print(var_b)  # Output: "This is a class variable" (remains unchanged)
```

**Explanation of Option 2's Drawbacks:**

- **Redundancy:** Assigning `Class_c.var_x` to `var_x` creates an unnecessary intermediate variable. This adds an extra step without any benefit. Always think what is the **benifit** of adding an extra step.
- **Potential Confusion:** If `var_x` is later used for something else, it might lead to unintended consequences, especially when dealing with multiple variables referencing the same class variable.

In conclusion, directly accessing class variables through the class name (`Class_c.var_x`) is the recommended approach due to its clarity, reduced risk of mutation, and adherence to common Python practices.

**When the type is immutable:**

In the context of your example:

- **Option 1:** Both `var_a` and `var_b` directly reference the class variable `Class_c.var_x`. Since `var_x` is not involved, there's no issue of modifying one variable affecting the other.
- **Option 2:** Here's where the potential for confusion arises:
    1. `var_x = Class_c.var_x` creates a new variable `var_x` that initially holds a reference to the same object as `Class_c.var_x`.
    2. **However,** subsequent modifications to `var_x` **do not** affect `Class_c.var_x` because you're only changing the value at the memory location pointed to by `var_x`. You're not modifying the original object itself. ** Why would you use `var_x`if it has no other use ? ** 

**When the type is mutable:**

**Example:**

```python
class MyClass:
    class_var = [1, 2, 3]  # Mutable list

obj = MyClass()

var_x = obj.class_var  # Both var_x and class_var reference the same list object

# This modifies the original list object
var_x.append(4)

print(var_x)  # Output: [1, 2, 3, 4]
print(obj.class_var)  # Output: [1, 2, 3, 4] (Also modified)
```

**Explanation:**

- `var_x` is assigned a reference to the same list object as `obj.class_var`.
- Appending to `var_x` modifies the original list object in memory, affecting both `var_x` and `obj.class_var` since they point to the same location.

**Therefore, while Python technically passes references, it's crucial to consider the mutability of the object being passed.**

**Reinforcing Option 1's Preference:**

- **Clarity and Explicitness:** Directly accessing `Class_c.var_x` makes the intent clear and avoids the intermediate step of creating `var_x`.
- **Reduced Potential for Errors:** It eliminates the possibility of accidentally modifying `var_x` and unintentionally affecting `Class_c.var_x`.

**In essence, while Option 2 might seem to work due to reference passing, Option 1 remains the preferred approach for better code clarity, maintainability, and reduced risk of unintended consequences.**

 **Consider performance implications. While Python does optimize attribute lookups to a degree, there's still a slight overhead involved.**

**Here's a breakdown of how Python handles attribute lookups and caching:**

1. **Initial Lookup:**
   - When encountering `obj.class_var` for the first time, Python searches for `class_var` in the object's namespace.
   - This involves a dictionary lookup, which has a small but measurable cost.

2. **Caching:**
   - If `class_var` is found in the object's namespace, Python caches its value in the object's `__dict__` attribute (internal dictionary).
   - Subsequent accesses to `obj.class_var` within a relatively short timeframe often retrieve the value directly from the cache, avoiding a full lookup.

3. **Overhead:**
   - The cache isn't unlimited and can be cleared under certain circumstances, such as deleting `class_var` or modifying its value.
   - Nested attribute access (e.g., `obj.nested.attribute`) can involve multiple lookups, potentially increasing overhead.

**Considerations for Intermediate Variables:**

- **Potential Performance Gain:** Introducing an intermediate variable can eliminate the need for repeated attribute lookups within a loop or tight code block.
   - However, be mindful of the trade-offs with code readability and maintainability.

**When to Prioritize Caching:**

- **Frequent Accesses:** If you anticipate frequent accesses to `obj.class_var` within a small code section, the caching mechanism likely outweighs the overhead of a few initial lookups.
- **Nested Attributes:** The overhead becomes more noticeable with nested attribute chains, making caching more beneficial.

**Best Practices:**

- **Prioritize Clarity First:** Favor clear and maintainable code structure unless performance profiling identifies specific bottlenecks.
- **Profiling:** Use profiling tools to measure performance impact in critical code sections and make informed decisions.
- **Alternative Solutions:** Consider alternative approaches for performance-critical scenarios, such as:
    - Using properties for controlled attribute access
    - Employing caching libraries for explicit management

**Remember:** In most cases, the performance difference between direct access and intermediate variables is negligible. Focus on writing clear and readable code, optimizing only when necessary based on profiling results.

