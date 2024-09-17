def gcd(a: int, b: int) -> int: 
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """ # Implement your solution here pass
    if a == 0:
        return b
    return gcd(b % a, a)

