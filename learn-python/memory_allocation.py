class MyClass:
    a = 0
    def __init__(self):
        self.my_var = 1
    
obj1 = MyClass()
obj2 = MyClass()

"""
If you debug the above code snippet you will see how python interpreters allocates memory. 
At "compile" time, python just generates the bytecode that are instructions about how to 
interpret class and special functions and so on. But it does not interpret anything.

The python interpreter executes the line in the following order at runtime:

1. First, it comes to know that there is a class called MyClass. Because it already knows (bytecode instructions) how to interpret `class` keyword and what to do when the interpreter sees a `class`.
2. Then similarly it comes to know that there is a class variable `a` with value 0.
3. Then it knows that there is a special function `__init__` in the class.
4. Then it does not check what is inside __init__ . Thus python keeps a reference to MyClass in the memory. It know which memory address references __init__ and which references `a` variable.
5. It only checks inside __init__ when it reaches the line `obj1 = MyClass()`. The interpreter has bytecode instruction from compile time about what to do when an instance is created.
So, the interpreter now follows that instruction which is to look inside the __init__ method and create reference for instance variable my_var in the memory. Even though
my_var has not been used anywhere yet.
6. The interpreter again look inside the __init__ method and create another reference for instance variable my_var in the memory. This is for obj2. Even though
my_var has not been used anywhere yet.


By "repeated memory allocation," I meant the process of Python allocating memory for the same instance variable every time an object of the class is created, 
even if that variable isn't used.

You create a large number of objects. Each object creation incurs some overhead for memory allocation.
The unused variable is large. Allocating a lot of unused memory can strain your system's resources.
However, it's important to note that:

Modern Python interpreters are highly optimized, and the performance difference between different allocation strategies is often negligible for regular applications.
The advantages of Python's dynamic approach, such as flexibility and clarity, sometimes outweigh the potential memory overhead.
If memory efficiency is a critical concern, you can consider:

Avoiding unused variables: Don't define instance variables in the __init__ method if you don't need them in all instances.
Lazy initialization: Initialize variables only when they are actually needed, using methods or properties instead of the constructor.
Object pooling: Reuse existing objects instead of creating new ones repeatedly.

"""

class MyClass2:
    a = 0
    def __init__(self):
        self.my_var = 1
    
MyClass2.a = 2

"""
1. First, it comes to know that there is a class called MyClass. Because it already knows (bytecode instructions) how to interpret `class` keyword and what to do when the interpreter sees a `class`.
2. Then similarly it comes to know that there is a class variable `a` with value 0.
3. Then it knows that there is a special function `__init__` in the class.
4. Then it does not check what is inside __init__ . Thus python keeps a reference to MyClass in the memory. It know which memory address references __init__ and which references `a` variable.
5. The interpreter just goes to the reference of `a` and assigns the value 2.
"""