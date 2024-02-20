In Python, the `..` syntax typically represents a relative import. When you see `..` at the beginning of an import statement, 
it means that you're importing a module relative to the current package/module's parent directory.

Here's what each dot represents in a relative import:

- `.` represents the current directory or package.
- `..` represents the parent directory or package.
- `...` represents the grandparent directory or package, and so on.

So, in your example `from ..some.another import some`, it means you're trying to import the `some` module from the `another` package, 
which is located in the `some` package that is a sibling of the current package or module.

For example, if your current module is located in a package structure like this:

```
parent_package/
    current_package/
        current_module.py
    some/
        another/
            __init__.py
            some.py
```

And you're writing code in `current_module.py`, then `from ..some.another import some` would import 
the `some` module from the `another` package, which is located in the `some` package that is a sibling of the `current_package`.
