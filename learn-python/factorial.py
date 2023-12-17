"""
The name "factorial" originates from the Latin word "factorium," which means "a maker" or "something that does." 
In mathematics, it was introduced to describe the product of multiplying successive positive integers.

The notation for factorial uses an exclamation mark (!). For example, 

5! (read as "5 factorial") is the product of all positive integers from 1 to 5:

5!=5*4*3*2*1=120

When you say you have 120 ways to arrange 5 books, you are essentially referring to the fact that there are 120 different possible orders in 
which those 5 books can be arranged on a shelf. In a broader sense, each arrangement represents a distinct "fact" or statement about the order of the books.

So, saying 5! = 120 not only means you have 120 ways to arrange 5 books, but it also signifies that there are 120 unique statements or facts about the order 
in which these 5 components (in this case, books) can be arranged. The factorial operation captures the idea of counting all possible arrangements 
systematically, providing a concise way to express the multiplicative combinations of these components.
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(factorial(5))