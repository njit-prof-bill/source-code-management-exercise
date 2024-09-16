def gcd(a: int, b: int) -> int:
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """
    while b: 
        a, b = b, a % b 
    return a


'''def tests():
    # Test cases
    print("GCD of 48 and 18 is:", gcd(48, 18))  # Expected: 6
    print("GCD of 100 and 10 is:", gcd(100, 10))  # Expected: 10
    print("GCD of 27 and 36 is:", gcd(27, 36))  # Expected: 9
    print("GCD of 7 and 1 is:", gcd(7, 1))  # Expected: 1

if __name__ == "__main__":
    tests()
'''