# gcd_richardsmith.py


def gcd(a: int, b: int) -> int:
    # Incorrect implementation: returns the smaller number instead of GCD
    return min(a, b)


# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
