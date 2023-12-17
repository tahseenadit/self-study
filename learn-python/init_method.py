class example:
    def __init__(self):
        pass

"""
In Python, the __init__ method serves as the constructor for a class. It's a special method that is automatically called when a new instance of a class is created. Its primary purpose is to initialize the instance, setting up its initial state by assigning values to its properties or performing any other necessary setup.

Here are some key points about the __init__ method:

Initialization, Not Creation: The __init__ method initializes an already created instance of a class. The actual creation of the 
instance (memory allocation, etc.) is handled by the __new__ method, which is called before __init__.

Self Parameter: The first parameter of the __init__ method is self, which represents the instance of the class. Through self, you can access and 
modify the instance's attributes.

Arguments: You can pass additional arguments to __init__ to customize the initialization of the instance.

Automatically Invoked: You don't call __init__ directly. It's automatically invoked when you create a new instance of the class using the class 
name followed by parentheses.

"""