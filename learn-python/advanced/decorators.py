"""
simple_func = simple_decorator(simple_func)
simple_func = simple_func
"""


def simple_decorator(func):
    print("I am decorating: ")
    return func

@simple_decorator
def simple_func():
    print(simple_func.__name__)

if __name__ == '__main__':
    simple_func()