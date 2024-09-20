#!/usr/bin/env python3
""" Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """ 
# Implement your solution here pass
def gcd(a: int, b: int) -> int: 
    while b: a, b = b, a % b 
    return a 
# Test cases 
print(gcd(54, 24)) # Expected output: 6 
print(gcd(48, 18)) # Expected output: 6 
print(gcd(101, 10)) # Expected output: 1

