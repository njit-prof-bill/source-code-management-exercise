def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(54, 24))  # Expected output: 6
                    # a = 24, b = 6
                    # a = 6, b = 0
print(gcd(48, 18))  # Expected output: 6
                    # a = 48, b = 18
                    # a = 18, b = 12
                    # a = 12, b = 6
                    # a = 6, b = 0
print(gcd(101, 10)) # Expected output: 1

# Test cases
