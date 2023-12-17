# sys_modules_setdefault_example_module2.py

import sys
import subprocess
import sys_modules_setdefault_example_module1

def func_main():
    print("hello!")

# You can give any name to the key. So this is like aliasing the main module.
mod = sys.modules.setdefault("tahseen", sys.modules["__main__"])

# This won't print the statement inside the if '__name__' == '__main__' condition in module 1
subprocess.run(["python", "sys_modules_setdefault_example_module1.py"])


import tahseen

# Now you can call func_main using the alias
tahseen.func_main()

# Now you can pass the main module to module 1
sys_modules_setdefault_example_module1.func_not_main(mod)

# The main module is still module 2 since you executed "python ys_modules_setdefault_example_module2.py"
print(sys.modules["__main__"])

