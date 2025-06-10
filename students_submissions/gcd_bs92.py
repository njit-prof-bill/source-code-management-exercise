def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if (not (type(a) is int)) or (not (type(b) is int)):
        print("gcd: both arguments must be of type int")
        return None
    # Use absolute values for a and b
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    # Base case: remainder is zero
    if not b:
        return a
    return gcd(b, a % b)
