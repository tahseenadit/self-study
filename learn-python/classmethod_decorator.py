"""
@classmethod is a built-in Python decorator used to define a method within a class that operates on the class itself 
rather than on instances of the class. This means that the method has access to the class itself (through the cls parameter) 
and can be called directly on the class, rather than on an instance of the class.

"""

class MyClass:
    class_variable = "Class Variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable

    def instance_method(self):
        return self.instance_variable


# Accessing class method
print(MyClass.class_method())  # Output: Class Variable

# Creating instances
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

# Accessing instance methods
print(obj1.instance_method())  # Output: Instance 1
print(obj2.instance_method())  # Output: Instance 2

"""
In this example:

class_variable is a class variable defined within the MyClass class.
class_method is a class method defined using @classmethod. It takes cls as its first parameter, which refers to the class itself. 
Inside the method, cls.class_variable accesses the class variable.
instance_method is a regular instance method. It operates on instance variables and does not require @classmethod.
When we call MyClass.class_method(), it returns the value of the class variable class_variable. 
This method can be called directly on the class itself, without the need to create an instance of the class.

On the other hand, instance_method operates on instance variables and requires an instance of the class to be created. 
Hence, we need to create instances (obj1 and obj2) and then call instance_method() on these instances.

"""
