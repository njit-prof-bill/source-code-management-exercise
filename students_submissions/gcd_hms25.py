 def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive, no loops).
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Both inputs must be integers.")
        return None
    if a == 0 and b == 0:
        print("GCD is undefined for both inputs being zero.")
        return None
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)

# Test cases
print(gcd(54, 24))      # Expected: 6
print(gcd(48, 18))      # Expected: 6
print(gcd(101, 10))     # Expected: 1
print(gcd(-54, 24))     # Expected: 6
print(gcd(0, 0))        # Expected: None
print(gcd("a", 5))      # Expected: None

