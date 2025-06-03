def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    try:
        if b == 0:
            if a == 0:
                return
            return abs(a)
        else:
            return gcd(b, a % b)
    except Exception as e:
        print("An error has occurred:", e)

# Test Cases
print(gcd("Error",0)) # Expected to be none
print(gcd(48,-18)) # Expected to be 6
print(gcd(-18, 48)) # Expected to be 6
print(gcd(17,2)) # Expected to be 1
print(gcd(0,0)) # Expected to be None as per requirements, though GCD(0,0) is mathematically 0
print(gcd(-12,0)) # Expected to be 12
print(gcd(2147483646,155393970)) #Expected to be 6