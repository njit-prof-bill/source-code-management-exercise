def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a == 0 and b == 0:
        print("both inputs are zero, undefined")
        return None
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))
print(gcd(-48, -18))
print(gcd(0, 0))
