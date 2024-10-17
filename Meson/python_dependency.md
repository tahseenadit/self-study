**Problem**

```
../my_file.c:1:10: fatal error: 'Python.h' file not found
#include <Python.h>
```

**Solution**

In meson.build file, you need to explicitely mention the dependency like:

```
project('my_file', 'c', 'cpp')

# Dependency for Python
python_dep = dependency('/Users/tahseen/optimizedsklearn/.venv/bin/python3', required: true)

# Add the correct python for the linker
linker_dep = declare_dependency(
    link_args : ['-L' + '/Library/Frameworks/Python.framework/Versions/3.11/lib', '-l' + 'python3.11'])


# Define the shared library
my_lib = shared_library('my_module',
                                'my_file.c',
                                dependencies: [python_dep, linker_dep])
```
