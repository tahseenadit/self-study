import math

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def sin_function(x, terms=10):
    """
    There are 2π radians in a full circle. (So 2π radians should equal 360°.

    When working with angles, it's often useful to ensure they are within a specific range to simplify calculations and comparisons. 
    By using the modulo operator %, you obtain the remainder after division. So, x % (2 * math.pi) calculates the remainder when x is divided by 2π.

    The result of x % (2 * math.pi) will be an angle within the range [0, 2π]. This operation "wraps" the angle around, ensuring that even if x was 
    larger than 2π (or negative), it brings it back into the valid range of a single period of the sine function.

    For example, if x is 5π, then x % (2 * math.pi) would be 5π mod(2π)=π, bringing it within the range of [0, 2π].
    """
    x = x % (2 * math.pi)  # Ensure x is within one period (0 to 2*pi)
    result = 0

    """
    Taylor's idea of using alternating signs and factorials in the Taylor series is deeply connected to the behavior of functions 
    and their derivatives. Let's break it down in simpler terms: Alternating Signs (- and +): The alternating signs in the Taylor series 
    (-1 raised to the power of n) are there to capture the oscillating nature of certain functions. For functions like sine and cosine, 
    the sign of the derivatives changes regularly. 
 
        - **Odd and Even Terms:** When \(n\) is odd, \((-1)^n\) is -1, making the terms negative. When \(n\) is even, \((-1)^n\) is 1, 
        making the terms positive.

        - **Mimicking Oscillations:** By alternating signs, the Taylor series tries to mimic the oscillations inherent in functions like sine and cosine. 
        This alternating pattern helps create a series that, when summed up, approximates the function.

    **Factorials for Scaling:** The factorials in the denominator (\(n!\)) serve a crucial role in scaling the terms appropriately.

        - **Damping Effect:** As \(n\) increases, the factorial in the denominator grows rapidly. This creates a damping effect, 
        making each successive term smaller in magnitude.

        - **Balancing Growth:** The growth of the factorial balances the growth of the \(x^n\) term in the numerator. 
        This prevents individual terms from becoming too large and helps ensure that the series converges to the actual function.

        - **Smooth Transition:** Factorials contribute to the smooth transition between terms, allowing the series to converge more effectively.

    So, in summary, Taylor used alternating signs to capture the oscillatory behavior of functions and factorials to appropriately scale the terms, 
    ensuring that the series provides an accurate approximation of the function over a range of \(x\). The combination of alternating signs and 
    factorials helps create a series that converges to the function it represents.
    
    The use of factorials in the Taylor series is deeply tied to the properties of functions and their derivatives. 
    While it's true that there could be alternative ways to balance the growth of terms, the factorial is particularly effective for several 
    reasons. The Taylor series is derived from Taylor's theorem, which involves the derivatives of a function at a specific point. 
    The factorial naturally emerges when expressing the higher-order derivatives of a function.
    """
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        result += term
    return result


if __name__ == '__main__':
    pass