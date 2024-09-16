def gcd(a: int, b: int) -> int:
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """
    
    # This can be optimized more, but this code demonstrates the Euclidean
    # algorithm in a way that makes more sense/is more readable to the user

    # Find the remainder r by dividing a by b
    # If a is smaller than b, the remainder will be a
    # This essentially swaps them
    r = a % b

    # If the remainder is not zero
    # We have not found the greatest common divisor
    if r != 0:
        # Run gcd again with b as a, and the non-zero remainder as b
        return gcd(b, r)
    
    # Otherwise b is our greatest common divisor
    return b

print("Testing the function:")
# Expected value: 21
print(f"The greatest common divisor of 1071 and 462 is {gcd(1071, 462)}")
# Expected value: 21
print(f"The greatest common divisor of 462 and 1071 is {gcd(462, 1071)}")
# Expected value: 5
print(f"The greatest common divisor of 5 and 10 is {gcd(5, 10)}")
# Expected value: 36
print(f"The greatest common divisor of 252 and 108 is {gcd(252, 108)}")
# Expected value: 231
print(f"The greatest common divisor of 19,402,845 and 23,485,539 is {gcd(19402845, 23485539)}")