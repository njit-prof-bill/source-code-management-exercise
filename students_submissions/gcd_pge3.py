"""
Paul Ellameh
pge3
CS490-141
Exercise 2
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    
    if a == 0 and b == 0:
        print("Error: GCD is undefined when a is 0 and b is 0")
        return None
    if b == 0:
        return abs(a)
    return gcd(b, a % b)


#Regulr test cases
print("--------------------------------------------")
print("Regular Testing")
print("gcd(60, 24):", gcd(60, 24))      # Expected: 12
print("gcd(48, 18):", gcd(48, 18))      # Expected: 6
print("gcd(75, 30):", gcd(75, 30))      # Expected: 15
print("--------------------------------------------")

# Prime number test cases
print("Prime  number testing")
print("gcd(17, 29):", gcd(17, 29))      # Expected: 1
print("gcd(19, 38):", gcd(19, 38))      # Expected: 19
print("gcd(23, 46):", gcd(23, 46))      # Expected: 23 
print("--------------------------------------------")

#Negative number test cases
print("Negative number testing")
print("gcd(-48, 18):", gcd(-48, 18))    # Expected: 6
print("gcd(48, -18):", gcd(48, -18))    # Expected: 6
print("gcd(-48, -18):", gcd(-48, -18))  # Expected: 6
print("--------------------------------------------")

# One zero test cases
print("One zero testing")
print("gcd(0, 5):", gcd(0, 5))          # Expected: 5
print("gcd(7, 0):", gcd(7, 0))          # Expected: 7
print("--------------------------------------------")

# Both zero test cases
print("Both zeros testing")
print("gcd(0, 0):", gcd(0, 0))          # Expected: None
print("--------------------------------------------")
