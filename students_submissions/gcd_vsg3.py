def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive).
    
    Returns:
        int: The GCD of a and b.
        None: If inputs are invalid.
    """
    # Check if inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Inputs must be integers.")
        return None

    # Handle zero cases
    if a == 0 and b == 0:
        print("Error: GCD is undefined for a = 0 and b = 0.")
        return None

    # Convert negative numbers to positive
    a, b = abs(a), abs(b)

    # Base case
    if b == 0:
        return a
    return gcd(b, a % b)

# Basic test cases
print(gcd(54, 24))      # Expected: 6
print(gcd(48, 18))      # Expected: 6
print(gcd(101, 10))     # Expected: 1
print(gcd(-48, 18))     # Expected: 6
print(gcd(0, 5))        # Expected: 5
print(gcd(0, 0))        # Expected: Error + None
print(gcd("a", 3))      # Expected: Error + None


"""
⚠️ Small Optimization Suggestion:
    You could reduce the number of conversions by ensuring a is always the larger one at the start (this is optional):
        a, b = max(abs(a), abs(b)), min(abs(a), abs(b))
    Though the Euclidean algorithm works regardless of order, this might slightly reduce recursion depth in some cases.

    Also consider that booleans evaluate as ints (ex: true = 1)
"""
