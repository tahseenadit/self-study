from enum import Enum

class Logging(Enum):
    # Enum members
    Console = "console"
    Gcp = "gcp"

    # Non-enum attribute (unconventional)
    _non_enum_attribute = "This is not an enum member"

"""
### Understanding Enumerations in Python

An enumeration (or Enum) is a set of symbolic names (members) bound to unique, constant values. In Python, when you create an Enum class, 
like `Logging`, each member of this class becomes an instance of the class.

### The `Logging` Enum Class

In your `Logging` enum class, you have defined two members: `Console` and `Gcp`. Here's what happens:

1. **Each Member is an Instance:** `Logging.Console` and `Logging.Gcp` are both instances of the `Logging` enum class. This is a key feature of Python enums.

2. **Named and Valued:** Each member of the enum has a name (like 'Console') and a value (like 'console'). The name is what you use to refer to the 
enum member in the code, and the value can be any immutable data type (like strings, numbers, etc.).

### How a vairable i.e `log_type` Becomes an Instance of `Logging`

When you assign `Logging.Console` to `log_type`:

```python
log_type = Logging.Console
```

- `log_type` now holds an instance of the `Logging` class, specifically the `Console` member.

### What Does `Logging.Console` Return?

- `Logging.Console` returns the `Console` member of the `Logging` enum.
- It is an instance of the `Logging` enum class.
- It has a name ('Console') and a value ('console') as defined in your enum class.

### Enum Instances in Practice

Since `log_type` is an instance of the `Logging` enum, you can:

- Compare it with other members of the same enum (like `log_type == Logging.Gcp`).
- Use it in functions or methods, like `init_logger()`, to make decisions based on its value.
- Access its name and value using `log_type.name` and `log_type.value`.

This behavior makes enums in Python especially useful for creating sets of named items with unique, constant values, improving code readability and 
maintainability. Enums ensure that you use a predefined set of values, reducing errors like typos in string literals.

In Python, when you define a class using the Enum base class, each attribute you define in the class that doesn't start with an underscore (_) becomes 
an enum member, not a simple variable. These enum members are instances of the enum class. This behavior is specific to the Enum class in Python.

In an Enum class, every attribute that doesn't start with an underscore and isn't a special method (like __init__) becomes an enum member.

To define non-enum class attributes in an Enum class, you would typically start the attribute name with an underscore (_) to prevent it from being 
treated as an enum member. However, this is not common practice since the primary purpose of an Enum class is to define enum members.

If you need to have both simple variables and enum members, you might be better off using a regular class or structuring your code differently. 
Enums are specifically designed for creating a set of named constants, and mixing in other types of class attributes can make the code less clear.
"""
