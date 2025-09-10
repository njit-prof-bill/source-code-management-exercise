def gcd(a: int, b: int) -> int:
    # Calculating GCD using the Euclidean algorithm.
    # Returns None for invalid inputs.
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: must be integers.")
        return None
    if a == 0 and b == 0:
        print("Error: GCD is undefined.")
        return None
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

# Test cases
print(gcd(54, 24))    # Expected: 6
print(gcd(48, 18))    # Expected: 6
print(gcd(101, 10))   # Expected: 1
print(gcd(-48, 18))   # Expected: 6
print(gcd(0, 0))      # Expected: Error
print(gcd(0, 5))      # Expected: 5
