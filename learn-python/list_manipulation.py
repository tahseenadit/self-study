class Example:
    def __init__(self):
        # Initialize an empty dictionary for _meta
        self._meta = {}

    def set_meta_value(self, key, metafield, value):
        # Use setdefault to ensure the key exists in _meta
        self._meta.setdefault(key, {})[metafield] = value

# Creating an instance of Example
example_instance = Example()

# Setting values using set_meta_value method
example_instance.set_meta_value("item1", "description", "This is item 1")
example_instance.set_meta_value("item2", "description", "This is item 2")
example_instance.set_meta_value("item2", "price", 20.0)

# Printing the modified _meta dictionary
print("Modified _meta dictionary:", example_instance._meta)
