Key differences between static and const:

**static is a class member modifier:**
- Belongs to the class itself, not instances
- Can be modified
- Shared across all instances
- Used like: ClassName.propertyName

**const is a variable declaration:**
- Cannot be reassigned after initialization
- Block-scoped
- Used for immutable values
- Used like: const myVar = value
