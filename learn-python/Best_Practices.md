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

# Do not call low-level function call

If you see the imread function of rawpy library, it looks like below:

```
def imread(pathOrFile):
    """
    Convenience function that creates a :class:`rawpy.RawPy` instance, opens the given file,
    and returns the :class:`rawpy.RawPy` instance for further processing.
    
    :param str|file pathOrFile: path or file object of RAW image that will be read
    :rtype: :class:`rawpy.RawPy`
    """
    d = RawPy()
    if hasattr(pathOrFile, 'read'):
        d.open_buffer(pathOrFile)
    else:
        d.open_file(pathOrFile)
    return d
```

Instead of calling `rawpy.imread(image_path)`, you can do something like below:

```
try:
    file= rawpy._rawpy.RawPy.open_buffer(image_path)
except Exception as ex:
    raise ex
finally:
    file.close()
```
But, you should not use open_buffer because calling imread will just call open_buffer. If the author of rawpy decides to change or update open_buffer, then directly calling open_buffer may break in your code or it may not serve you the same purpose which is to read a raw image. But the author may still change or update open_buffer in such a way that the purpose of imread stays the same. So, users of rawpy do not need to change their code. If you are one of those users, then you will be safe. That is why, use imread instead of open_buffer specially when you see that imread evenrually calls open_buffer without doing any other special thing.\n
This practice applies to using other python libraries as well.