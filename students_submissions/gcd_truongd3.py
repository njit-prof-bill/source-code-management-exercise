def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a

print(gcd(1, 2)) # 1
print(gcd(4, 2)) # 2
print(gcd(15, 23)) # 1
print(gcd(150, 250)) # 50