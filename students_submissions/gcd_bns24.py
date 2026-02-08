def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if a == 0 and b == 0:
        print("Error: Undefined.")
        return None

    if b == 0:
        return abs(a) #gcd is never negative
    return gcd(b, a%b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(0, 0))  # Expected output: "Error: Undefined."
print(gcd(-36, 6)) # Expected output: 6
print(gcd(-36, -6)) # Expected output: 6
print(gcd(7, 11)) # Expected output: 1
