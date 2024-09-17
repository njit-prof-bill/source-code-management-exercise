def gcd(a: int, b:int) -> int: 
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """
    while b:
        temp = b
        b = a%b
        a = temp
    return a
print(gcd(54, 24)) # =6
print(gcd(48, 18)) # =6
print(gcd(101, 10)) # =1
