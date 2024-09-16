def gcd(a: int, b: int) -> int:
    '''
    Calculate the greatest common divisor 
    (GCD) of two integers a and b
    using the Euclidean algorithm.

    GCD = the largest common number between
    2 values that is divisible WITHOUT a
    remainder

    Ex: gcd(54, 24)
    54 = 1, 54, 2, 27, 3, 18, 6, 9
    24 = 1, 24, 2, 12, 3, 8, 4, 6, 
    Common: 1, 2, 3, 6 <-- where 6 is GCD
    '''
    # Implement your solution here
    while b:
        a, b = b, a % b
    return a
    
# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1