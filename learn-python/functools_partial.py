import functools

def foofunc(arg1, arg2):
    var1 = arg1
    var2 = arg2
    print(f"var1: {var1} var2: {var2}")

new_func = functools.partial(foofunc, "Hello", "world!")

new_func()