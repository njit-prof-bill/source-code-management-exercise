def gcd(a: int, b: int) -> int:
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """
    while b: 
        a, b = b, a % b 
    return a


def run_tests():
    """Run a set of test cases for the GCD function."""
    test_cases = [
        (48, 18, 6),
        (100, 10, 10),
        (27, 36, 9),
        (7, 1, 1)
    ]
    
    for a, b, expected in test_cases:
        result = gcd(a, b)
        print(f"GCD of {a} and {b} is: {result} (Expected: {expected})")
        assert result == expected, f"Test failed for inputs {a} and {b}"

if __name__ == "__main__":
    run_tests()