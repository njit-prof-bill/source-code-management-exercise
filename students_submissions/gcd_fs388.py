def gcd(a: int, b: int) -> int:
    # Handle negative numbers
    a = abs(a)
    b = abs(b)
    # Base case
    if b == 0:
        return a
    # Recursive case
    return gcd(b, a % b)
# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(-54, 24))  # Expected output: 6 