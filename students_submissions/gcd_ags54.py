def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
num1 = 54
num2 = 24
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
print(f"The GCD of {num1} and {num2} is {gcd(48, 18)}")
print(f"The GCD of {num1} and {num2} is {gcd(101, 10)}")
