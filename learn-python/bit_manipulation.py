# The following function finds the number of '1' in the binary representation of an integer n
def hamming_weight(n: int) -> int:
    totalBits = len(bin(n)[2:])
    check = 1 << (totalBits - 1)
    result = 0

    for i in range(totalBits):
        if n & check == check:
            result += 1
        n = n << 1
    
    return result

if __name__ == '__main__':
    n = 11
    print(hamming_weight(n))


"""
Now, let's execute the code with n = 11:

bin(n): This part converts the integer n into its binary representation, which is a string. 
For example, if n = 11, bin(n) would result in the string '0b1011'. The prefix '0b' indicates that the string represents a binary number.

bin(n)[2:]: This part slices the binary string to remove the first two characters, which are '0b'. So, '0b1011' becomes '1011'.

len(...): This calculates the length of the string obtained in the previous step. In this case, len('1011') will be 4.

totalBits = 4: The binary representation of n is 1011, which has 4 bits.

check = 8: Since totalBits is 4, we set the check variable to 1 << 3, which is 1000 in binary, or 8 in decimal.

result = 0: We initialize result to store the count of '1' bits.

Now, let's step through the loop with the binary representation 1011:

Iteration 1:

n & check is 1011 & 1000, which equals 1000. Since it's equal to check, it means the leftmost bit is '1'. So, result becomes 1.
We shift n one position to the left, and it becomes 0110.

Iteration 2:

n & check is 0110 & 1000, which equals 0000. The leftmost bit is '0', so result remains 1.
n becomes 1100.

Iteration 3:

n & check is 1100 & 1000, which equals 1000. The leftmost bit is '1', so result becomes 2.
n becomes 1000.

Iteration 4:

n & check is 1000 & 1000, which equals 1000. The leftmost bit is '1', so result becomes 3.
n becomes 0000.
The loop has checked all bits in the binary representation of 11, and the function returns 3, 
which is the count of '1' bits in the binary representation of 11.

Time Complexity
__________________

The time complexity of this function, hamming_weight(n), is O(log n), which means the time it takes to run the function grows slowly 
as the input number n gets larger.

Here's a simple explanation:

The function starts by converting the input number n into its binary representation, which requires processing each bit in n. 
The number of bits to represent n in binary (logarithmically proportional to n) determines how many iterations are needed to perform this conversion. 
This step has a time complexity of O(log n).

The number of bits needed to represent a positive integer n in binary is proportional to the logarithm (specifically, the base-2 logarithm) of n. 
This means that as n increases, the number of bits required to represent it also increases, but not linearly. 
Instead, it increases in a logarithmic fashion.

To break it down with an example:

Let's say we want to represent the numbers from 1 to 16 in binary:

1 in binary is 1 (1 bit)
2 in binary is 10 (2 bits)
3 in binary is 11 (2 bits)
4 in binary is 100 (3 bits)
5 in binary is 101 (3 bits)
6 in binary is 110 (3 bits)
7 in binary is 111 (3 bits)
8 in binary is 1000 (4 bits)
9 in binary is 1001 (4 bits)
10 in binary is 1010 (4 bits)
11 in binary is 1011 (4 bits)
12 in binary is 1100 (4 bits)
13 in binary is 1101 (4 bits)
14 in binary is 1110 (4 bits)
15 in binary is 1111 (4 bits)
16 in binary is 10000 (5 bits)
As you can see, the number of bits needed to represent these numbers increases, but not at a linear rate. It follows a logarithmic pattern. 
The largest number (16) requires one more bit than the previous largest number (8), and this pattern continues as the numbers get larger.

This logarithmic relationship means that when we say the number of bits is "logarithmically proportional to n," we mean that the number of bits 
required grows slowly compared to the increase in n. The base-2 logarithm is commonly used because we are working in a binary system. In terms of 
algorithm complexity analysis, this property is significant, as it indicates how certain operations scale with input size.

After obtaining the binary representation, the function loops through each bit (0 or 1) in the binary representation. 
In the worst case, where all bits in the binary representation are 1, the loop iterates through all bits. 
The number of iterations in this step is directly related to the length of the binary representation, which is also O(log n).

The overall time complexity is determined by the two steps combined. 
Since both steps have a time complexity of O(log n), the total time complexity of the function is O(log n). 
This means that as the input number n becomes larger, the time it takes for the function to run increases at a slower rate, 
which is a desirable characteristic for efficient algorithms.

Space Complexity
_________________

The space complexity of the hamming_weight(n) function is O(1), which means it uses a constant amount of memory space regardless of the input number n.

Here's why:

The function primarily uses a few integer variables (totalBits, check, and result) to perform its operations. 
These variables consume a fixed amount of memory, and their memory usage does not depend on the size of the input number n.

The binary representation of n is not explicitly stored in memory as a separate data structure. 
Instead, it is calculated on the fly without allocating additional memory for it. 
This means that the space used for the binary representation does not grow with the size of n.
In a hypothetical scenario where the function stores the entire binary representation in memory:

binary_repr = "1011"  # Hypothetical storage of binary representation
However, in the actual function, the binary representation is not stored in this manner. 
Instead, it is calculated step by step during the execution of the loop without explicitly creating and storing the binary string. 
The function checks each bit one at a time using bitwise operations and doesn't need to keep the full binary string in memory

Overall, the function's memory usage is constant and does not increase with larger input values. As a result, the space complexity of the function is O(1).

"""