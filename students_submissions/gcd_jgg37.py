# students_submissions/gcd_jgg37.py

def gcd(a: int, b: int) -> int:
    """
    Recursively calculates the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm. Returns None if both inputs are 0.
    """
    a = abs(a)
    b = abs(b)
    if a == 0 and b == 0:
        return None
    if b == 0:
        return a
    return gcd(b, a % b)

