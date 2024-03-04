# Try Except Finally

Only catch specific exception if you want to handle them by yourself i.e if you want to do something when that specific exception occurs.\n
Otherwise, do not catch specific exception. Instead, just use general `except Exception as ex` to catch any exception.

For example, below we are catching specific exception to check if rawpy supports reading file and if not, we would like to raise a specific Error. Therefore, we caught that exception.

```
try:
    self._imgae = rawpy.imread(request.get_file())
except rawpy.NotSupportedError as ex:
    raise InitializationError(
        f"RawPy can not read {request.raw_uri}."
    ) from None
```

But do not do something like below:

```
try:
    nd_image = self._imgae.postprocess(**kwargs)
except (AttributeError, ImportError) as ex:
    print(ex)
except (rawpy.LibRawError, rawpy.LibRawFatalError, rawpy.LibRawNonFatalError) as ex:
    print(ex)
except Exception as ex:
    print(ex)
```
Because we are actually doing nothing by catching specific exception and just printing the message ex.

```
try:
    nd_image = self._imgae.postprocess(**kwargs)
except Exception as ex:
    raise ex
```

Instead, just use Exception in general as above and raise the exception instead of just printing the message. If your code snippet is part of a function and you raise exception, then may be some other function that called your function may catch it and handle it. If you just print it, then anyone calling your function won't be able to catch the exception because then you have handled it very poorly by just printing the exception message.