def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(12, 18))  # Expected output: 6
print(gcd(10, 25))  # Expected output: 5
print(gcd(101, 10))  # Expected output: 1