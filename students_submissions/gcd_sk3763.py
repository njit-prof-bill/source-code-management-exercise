def gcd(a: int, b: int) -> int | None:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursively).
    Handles negative inputs and edge cases.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None

    a, b = abs(a), abs(b)

    if a == 0 and b == 0:
        print("Error: GCD is undefined for both numbers being zero.")
        return None

    if a == 0:
        return b
    return gcd(b % a, a)


# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1