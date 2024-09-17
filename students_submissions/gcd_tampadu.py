def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    """
    
    if a == 0:
        return b
    return gcd(b % a, a)