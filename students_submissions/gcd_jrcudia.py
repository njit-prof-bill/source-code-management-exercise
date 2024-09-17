def gcd(a: int, b: int) -> int: 
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """ 
    # Implement your solution here pass
    while b:
        a, b = b, a % b
    return a

print(gcd(54,24))
print(gcd(101, 10))