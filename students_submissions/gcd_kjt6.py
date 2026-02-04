def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: a and b must be integers.")
        return None

    if a == 0 and b == 0:
        print("Error: GCD is undefined for both numbers being zero.")
        return None
    
    a = abs(a)
    b = abs(b)

    # Base case
    if b == 0:
        return a

    # Recursion
    return gcd(b, a % b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(7, 13))   # Expected: 1 (both prime)
print(gcd(-24, 36)) # Expected: 12 (negative number)
print(gcd(0, 5))  # Expected: 5
print(gcd(0, 0))  # Expected: Error + None
print(gcd(10, "5"))  # Expected: Error + None