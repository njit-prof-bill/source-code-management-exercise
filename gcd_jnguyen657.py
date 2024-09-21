def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def main():
    # Test cases
    print("GCD of 48 and 18:", gcd(48, 18))  # Should return 6
    print("GCD of 56 and 98:", gcd(56, 98))  # Should return 14
    print("GCD of 101 and 10:", gcd(101, 10))  # Should return 1
    print("GCD of 0 and 5:", gcd(0, 5))  # Should return 5
    print("GCD of 5 and 0:", gcd(5, 0))  # Should return 5
    print("GCD of -8 and 12:", gcd(-8, 12))  # Should return 4
    print("GCD of 8 and -12:", gcd(8, -12))  # Should return 4

if __name__ == "__main__":
    main()