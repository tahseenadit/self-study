class ClassA:
    def __init__(self):
        pass

class ClassB:
    def __init__(self):
        self._instance = None

    def get_instance(self):
        self._instance = ClassA()
        instance = self._instance
        return instance 
    

obj1 = ClassB()
obj2 = obj1.get_instance()
print(obj1._instance)
print(obj2)
obj1._instance = None
print(obj1._instance)
print(obj2)

"""
So, changing the value of instance varible of obj1 does not change the value for obj2.
They are two separate references just pointing to the same memory address of the same class object.
so it is safe to return self._instance instead of instance (which will just create a memory overhead). Even if
someone changes self._instance for one instance, the returned value for other instances won't change. 

Key Points:

In Python, objects are passed by reference, meaning you pass references to the memory location where the object resides.
Changing the value of an instance variable modifies the object itself, not just the reference.
Understanding reference behavior is crucial for efficient memory management in Python.
"""

class ClassA:
    def __init__(self):
        pass

class ClassB:
    def __init__(self):
        self._instance = None

    def get_instance(self):
        self._instance = ClassA()
        instance = self._instance
        self.modify_instance()
        return instance
 
    def modify_instance(self):
        self._instance = None
 
obj1 = ClassB()
obj2 = obj1.get_instance()
print(obj1._instance)
print(obj2)

"""
In this case, you can use instance local variable if you want to return whatever self._instance is assigned before modification.
Even here, chaging self._instance does not change instance local variable. 
Remember, values are passed by reference, not by value. This means you pass references to the location in memory, 
not copies of the data itself.
"""