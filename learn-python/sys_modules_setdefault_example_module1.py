# sys_modules_setdefault_example_module1.py

import sys

def func_not_main(mod):
    if mod.__file__ == "/Users/mdana/My Work Files/learn-python/advanced/sys_modules_setdefault_example_module2.py":
        print("Someone has executed \"python sys_modules_setdefault_example_module2.py\"")

if '__name__' == '__main__':
    print("Someone has executed \"python sys_modules_setdefault_example_module1.py\"!")
