def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a


# Test cases
print(f"gcd of 54 and 24 is = {gcd(54, 24)}")  # Expected output: 6
print(f"gcd of 48 and 18 is = {gcd(48, 18)}")  # Expected output: 6
print(f"gcd of 101 and 10 is = {gcd(101, 10)}")  # Expected output: 1