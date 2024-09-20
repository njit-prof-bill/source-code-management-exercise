def gcd(a: int, b: int) -> int: #""" Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """ # Implement your solution here pass 
    if(b < a):
        return gcd(b, a)
    if(b%a == 0):
        return a
    return gcd(b%a, a)

