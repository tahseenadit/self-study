The noexcept and nogil keywords in Cython serve specific purposes related to exception handling and the Global Interpreter Lock (GIL) in Python. Here's a breakdown of why they are not included in the C header file (criterion.h):
Explanation of noexcept and nogil

---

### **What is `noexcept` in C++?**
1. In C++, functions can throw exceptions when something goes wrong (like dividing by zero or running out of memory). Exceptions are a way to handle errors gracefully.
   - Example: If a function tries to open a file that doesn’t exist, it might throw an exception.

2. The `noexcept` keyword tells the compiler, **"This function will not throw exceptions."** 
   - This is like a promise you make when writing the code. If the function does throw an exception despite this promise, the program will likely crash.

3. Why is this useful?
   - If the compiler knows a function won’t throw exceptions, it can make the program run faster by skipping certain checks related to exception handling.
   - It also helps you write safer and clearer code because you know which functions might cause unexpected errors.

4. In **C**, there’s no such thing as exceptions or exception handling.
   - In C, errors are handled in simpler ways, like returning an error code from a function.
   - Since functions in C don't throw exceptions, you don’t need something like `noexcept`. All functions are assumed to not throw exceptions by default.

---

### **What is `nogil` in Cython?**
1. Python has something called the **Global Interpreter Lock (GIL)**.
   - The GIL is a mechanism in Python that makes sure only one thread can execute Python code at a time, even on a computer with multiple CPUs. This can limit the performance of multi-threaded programs.

2. **Cython** is a tool that lets you write Python-like code that gets converted into fast C code.
   - When writing Cython code, you can use the `nogil` keyword to tell the program, **"This part of the code does not need the GIL."**

3. Why is this useful?
   - If your function is doing something that doesn’t involve Python objects (like working with raw numbers or files), releasing the GIL allows other threads to run Python code in parallel, improving performance in multi-threaded applications.

4. In **C**, there’s no concept of the GIL.
   - The GIL is a feature of the Python interpreter, not C. C doesn’t have anything like it because it doesn’t need to manage Python objects or threads.
   - So, if you’re writing C code, you don’t need to worry about `nogil`.

---

### **Simple Comparisons**

| Feature          | C++ with `noexcept`                | Cython with `nogil`             | C                                |
|-------------------|------------------------------------|----------------------------------|----------------------------------|
| Purpose           | Guarantees a function won’t throw exceptions. | Lets code run without holding the GIL. | Doesn’t have exceptions or GIL. |
| Used for          | Optimization and error safety.    | Multi-threaded performance.     | Basic error handling (e.g., error codes). |
| Needed in C?      | No, because C doesn’t have exceptions. | No, because C doesn’t have the GIL. | N/A.                            |

---

## Conclusion
Since noexcept and nogil are specific to Cython and its interaction with Python, they are not relevant in a pure C context. Therefore, when translating the Cython code to C, you can omit these keywords. The function declarations in the C header file are sufficient for defining the interface without needing to specify exception handling or GIL-related concerns.
If you need to document that certain functions are thread-safe or do not throw exceptions, you can do so in comments, but it is not necessary in the function signatures themselves.
