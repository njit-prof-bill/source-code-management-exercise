def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    if b == 0:
        if a == 0:
            #undefined case
            print("Error: GCD is undefined.")
            return None
        #negative result
        return abs(a)
    return gcd(b, a % b)

#test cases
print("gcd(321, 666) =", gcd(321, 666))
print("gcd(29, 5) =", gcd(29, 5))
print("gcd(1000, 250) =", gcd(1000, 250))
print("gcd(0, 54010) =", gcd(0, 54010))
print("gcd(-120, 88) =", gcd(-120, 88))
