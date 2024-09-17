def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    while b:
        a, b = b , a % b

    return a


assert gcd(15, 5) == 5
assert gcd(36, 60) == 12
assert gcd(5, 10) == 5
