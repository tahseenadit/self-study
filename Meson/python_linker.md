If you encounter "undefined symbols" when building, make sure you link against the correct version of the Python library that matches your environment (x86_64). This typically involves ensuring the correct -L and -l flags are set during linking.

Problem:

```
[2/3] Linking target libmy_predict_module.dylib
FAILED: libmy_predict_module.dylib 
cc  -o libmy_predict_module.dylib libmy_predict_module.dylib.p/my_predict.c.o -Wl,-dead_strip_dylibs -Wl,-headerpad_max_install_names -shared -install_name @rpath/libmy_predict_module.dylib
Undefined symbols for architecture x86_64:
  "_PyArg_ParseTuple", referenced from:
      _my_predict in my_predict.c.o
  "_PyCapsule_GetPointer", referenced from:
      __import_array in my_predict.c.o
  "_PyCapsule_Type", referenced from:
      __import_array in my_predict.c.o
  "_PyErr_Clear", referenced from:
      __import_array in my_predict.c.o
  "_PyErr_ExceptionMatches", referenced from:
      __import_array in my_predict.c.o
  "_PyErr_Format", referenced from:
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
  "_PyErr_Print", referenced from:
      _PyInit_my_predict_module in my_predict.c.o
  "_PyErr_SetString", referenced from:
      _PyInit_my_predict_module in my_predict.c.o
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
  "_PyExc_ImportError", referenced from:
      _PyInit_my_predict_module in my_predict.c.o
  "_PyExc_ModuleNotFoundError", referenced from:
      __import_array in my_predict.c.o
  "_PyExc_RuntimeError", referenced from:
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
  "_PyImport_ImportModule", referenced from:
      __import_array in my_predict.c.o
      __import_array in my_predict.c.o
  "_PyModule_Create2", referenced from:
      _PyInit_my_predict_module in my_predict.c.o
  "_PyObject_GetAttrString", referenced from:
      __import_array in my_predict.c.o
      _my_predict in my_predict.c.o
      _my_predict in my_predict.c.o
      _my_predict in my_predict.c.o
      _my_predict in my_predict.c.o
      _my_predict in my_predict.c.o
  "__Py_Dealloc", referenced from:
      _Py_DECREF in my_predict.c.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.
```

**Solution**

In meson.build file, include the following dependency:
```
# Add the correct python for the linker
linker_dep = declare_dependency(
    link_args : ['-L' + '/Library/Frameworks/Python.framework/Versions/3.11/lib', '-l' + 'python3.11'])


# include the dependency in the the shared library like below
my_lib = shared_library('my_module',
                                'my_file.c',
                                dependencies: [linker_dep])
```

Ensure that '/Library/Frameworks/Python.framework/Versions/3.11/lib' is not a symlink. If it is a symlink, then you may need to mention the path to actual installation that the symbolic python is pointing to. You can get that path using `ls -l $(which python3.11)`.
