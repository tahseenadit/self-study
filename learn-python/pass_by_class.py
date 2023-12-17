def some_func(cls):
    # Example function body that prints a message
    print(f"I received the {cls.__name__} class.")

class dummy:
    # Example class body
    pass

# Call some_func with the dummy class
some_func(dummy)

"""
Understanding the Call some_func(dummy)
In this call, dummy is not an instance of the class but the class itself. If some_func is intended to work with an instance of a class, 
you would normally create an instance of dummy and pass that instance to some_func. For example:

instance_of_dummy = dummy()
some_func(instance_of_dummy)

If, however, some_func is designed to work with the class itself (perhaps doing something with class-level attributes or methods), 
then calling some_func(dummy) directly with the class is appropriate.
"""