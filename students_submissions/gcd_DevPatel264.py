def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(120, 35))  # Expected output: 5 
print(gcd(81, 27))   # Expected output: 27 
print(gcd(56, 98))   # Expected output: 14

