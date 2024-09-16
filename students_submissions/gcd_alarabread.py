def gcd(a: int, b: int) -> int:
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """
    # Implement your solution here
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a
