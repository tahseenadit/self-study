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

# Python Class Overhead

There can be some overhead associated with creating Python classes. This overhead includes memory consumption for storing the class attributes, methods, and other related metadata. Additionally, there might be a slight performance overhead when accessing attributes or methods due to the dynamic nature of Python's attribute lookup mechanism. However, in most cases, the overhead is minimal and not a significant concern for most applications.

Here are some reasons why creating Python classes may incur overhead:

1. **Memory Consumption**: Each class definition in Python consumes memory to store its attributes, methods, and other related metadata. This memory overhead can add up, especially in applications with many classes or instances.

2. **Dynamic Nature of Python**: Python is a dynamically typed language, which means that attribute lookup is performed at runtime. This dynamic attribute lookup mechanism may introduce a slight performance overhead compared to statically typed languages where attribute lookup can be resolved at compile time.

3. **Object Instantiation**: Creating instances of classes in Python involves some overhead, such as memory allocation for the instance itself and initializing attributes. While this overhead is generally low, it can become significant if many instances are created frequently.

4. **Method Resolution**: Python employs method resolution order (MRO) to determine the order in which methods are called in the presence of inheritance. This process involves traversing the class hierarchy and can incur some overhead, particularly in complex inheritance structures.

5. **Attribute Access**: Python provides mechanisms such as properties, descriptors, and dunder methods (__getattr__, __setattr__, etc.) for controlling attribute access. While these features offer flexibility and convenience, they may introduce additional overhead compared to simple attribute access.

Overall, while there is some overhead associated with creating Python classes, it is usually minimal and rarely a significant concern for most applications. The benefits of using classes, such as code organization, encapsulation, and code reuse, typically outweigh the associated overhead.

The memory consumption associated with class definition in Python primarily occurs at runtime, not compile time. This means that when your Python program is running, memory is allocated to store the attributes, methods, and other metadata associated with each class.

Here's an example to illustrate this:

```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def my_method(self):
        return self.x

# Creating an instance of MyClass
obj = MyClass(10)
```

In this example, the `MyClass` definition is processed at runtime when the Python interpreter encounters it during program execution. Memory is allocated to store information about the class, including its methods (`__init__` and `my_method`), attributes (such as `x`), and other metadata.

The memory consumption increases as you create more instances of the class or define additional classes in your program. For example:

```python
# Creating multiple instances of MyClass
obj1 = MyClass(20)
obj2 = MyClass(30)
```

Each instance of `MyClass` consumes memory to store its own attributes, methods, and a reference to the class definition.

Compile time in Python generally involves parsing and compiling the source code into bytecode, which does not directly involve storing class definitions in memory. Instead, the bytecode includes instructions for the interpreter to dynamically create classes and instances as needed during runtime execution. Therefore, the memory consumption associated with class definitions occurs at runtime.

In statically typed languages like C++ or Java, the compiler knows the type of each variable and can resolve attribute lookups at compile time. This means that accessing attributes of objects in these languages is generally faster because the compiler can directly generate instructions to access the memory locations of the attributes.

In contrast, Python is dynamically typed, which means that the type of a variable is determined at runtime. As a result, attribute lookup in Python involves a process of searching through the object's attributes at runtime to find the requested attribute. This dynamic attribute lookup mechanism can introduce a slight performance overhead compared to statically typed languages.

Here's an example to illustrate this difference:

```python
# Python example
class MyClass:
    def __init__(self):
        self.x = 10

obj = MyClass()
print(obj.x)
```

In this Python code, when `obj.x` is accessed, Python performs a lookup at runtime to find the attribute `x` associated with the object `obj`.

```java
// Java example
public class MyClass {
    public int x = 10;
}

public class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        System.out.println(obj.x);
    }
}
```

In this Java code, when `obj.x` is accessed, the compiler knows the type of `obj` (MyClass) and can directly generate instructions to access the memory location of the attribute `x`.

While the difference in performance between dynamic attribute lookup in Python and static attribute lookup in statically typed languages may be negligible for many applications, it can become more significant in performance-critical scenarios or when dealing with large amounts of data. However, Python's dynamic nature offers flexibility and ease of development, which often outweighs the slight performance overhead introduced by dynamic attribute lookup.

While Python classes do introduce some overhead compared to simple functions, it's crucial to consider the context and trade-offs:

**Overhead in Python Classes:**

- **Memory Management:** Classes require additional memory for storing the class definition itself (including methods and attributes) and each object instance created from the class.
- **Attribute Lookup:** Accessing object attributes involves a lookup process within the object's dictionary, which has a small overhead compared to directly calling a function.

**However, these overheads are often minimal in most practical scenarios.** Python is optimized for attribute lookups, and the benefits of using classes often outweigh the slight overhead:

**Benefits of Classes:**

- **Encapsulation:** Classes bundle data (attributes) and behavior (methods) together, promoting data protection and code organization.
- **Code Reusability:** Classes allow you to create multiple objects with the same attributes and methods, reducing code duplication.
- **Inheritance:** Classes enable the creation of hierarchical relationships, allowing subclasses to inherit attributes and methods from parent classes, promoting code maintainability.

**In specific case:**

- **Simple Functions vs. Class:** If your friend's script only contained a few simple, unrelated functions, converting them to a class might be unnecessary. The overhead of creating and using the class might outweigh the benefits.

**Here's a breakdown of when a class might be appropriate:**

- **Shared Data and Behavior:** If the functions operate on similar data or share common functionality, a class can encapsulate this shared logic and data, improving code organization.
- **Object-Oriented Design:** If your script deals with real-world entities with attributes and behaviors, using classes aligns well with object-oriented programming principles.

**Recommendations:**

- **Focus on Readability and Maintainability:** If the original code using simple functions was clear and easy to understand, there might not be a compelling reason to rewrite it as a class.
- **Consider the Trade-offs:** Evaluate the complexity of the script and the potential benefits of using a class for data encapsulation, code reusability, and maintainability.
- **Profiling:** If performance becomes a concern, use profiling tools to measure the actual overhead of the class structure. This can help you make data-driven decisions.

**In essence, while Python classes introduce a slight overhead, their benefits in terms of code organization, maintainability, and reusability often outweigh this overhead in most practical scenarios. Focus on using classes when they provide a clear advantage in terms of code structure and design.**

# Check python version in setup.py

You can check it using the sys module like below:

```python

import sys

if sys.version_info < (3, 8):
    print("Error: Solution does not support this version of Python.")
    print("Please upgrade to Python 3.8 or higher.")
    sys.exit(1)
```

# Check if a specific module version is not met

You can check if user's environment has the required version of a module like below in setup.py file:

```python

try:
    from setuptools import find_namespace_packages
except ImportError:
    # the user has a downlevel version of setuptools.
    print("Error: dbt requires setuptools v40.1.0 or higher.")
    print('Please upgrade setuptools with "pip install --upgrade setuptools" ' "and try again")
    sys.exit(1)
```

# Long Description in setup.py

Do not write long description directly in setup.py file's setup function. Instead, write the description in readme.md file. Then get the description from the readme file like below:

```python

import os

this_directory = os.path.abspath(os.path.dirname(__file__)) # __file__ is the current file which is setup.py
with open(os.path.join(this_directory, "README.md")) as f: # We assume that README.md is in the same directory as setup.py
    lont_description = f.read()
```

Then pass long_description to the parameter of setup function in setup.py file like below:

```python

...

setup(
    ...
    long_description=long_description,
    ...
)
```