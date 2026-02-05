def gcd(a: int, b: int) -> int:
    # Type checking
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both arguments must be integers.")
        return None

    # Handle the undefined case gcd(0, 0)
    if a == 0 and b == 0:
        print("Error: GCD is undefined for a = 0 and b = 0.")
        return None

    # Work with absolute values to handle negatives
    a, b = abs(a), abs(b)

    # Base case: gcd(a, 0) = a
    if b == 0:
        return a

    # Recursive Euclidean Algorithm
    return gcd(b, a % b)

print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))
