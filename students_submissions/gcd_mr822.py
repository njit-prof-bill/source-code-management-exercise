def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the recursive Euclidean algorithm. Returns None on invalid input.
    """
    try:
        if b == 0:
            return abs(a)
        return gcd(b, a % b)
    except Exception as e:
        print(f"Error: {e}")
        return None

# Basic test cases
print(gcd(54, 24))    # 6
print(gcd(48, 18))    # 6
print(gcd(101, 10))   # 1
print(gcd(-48, 18))   # 6
print(gcd(0, 5))      # 5
print(gcd(0, 0))      # 0 (Edge case)
