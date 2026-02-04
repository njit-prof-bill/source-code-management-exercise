def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers
    """
    if b == 0:
        return -1*a if a < 0 else a
    else:
        return gcd(b, a % b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(-48, 18))  # Expected output: 6
print(gcd(-25, -5))  # Expected output: 5
print(gcd(-25, -5))  # Expected output: 5
print(gcd(5, 7))  # Expected output: 1

