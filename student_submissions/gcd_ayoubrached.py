def gcd(a: int, b: int) -> int:
    """ 
    Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. 
    """
    while a and b > 0:
        temp = b
        b = a % b
        a = temp
    return temp

# Test cases 
print(gcd(54, 24)) # Expected output: 6 
print(gcd(48, 18)) # Expected output: 6 
print(gcd(101, 10)) # Expected output: 1
print(gcd(128, 24)) # Expected output: 8