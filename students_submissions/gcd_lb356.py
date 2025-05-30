def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    print(f"Taking the GCD of gcd({a},{b})")
    a, b = abs(a), abs(b)

    # gcd(0,0)
    if a == 0 and b == 0:
        print("Error: GCD is undefined when a and b are both 0")
        return None

    # base case
    if b == 0:
        if a == 1:
            print("These two numbers are co-prime") # If they are co-prime
        return a
    
    # Recursive GCD method using euclidean algorithm
    # the algorithm flips if a > b or b > a so it doesn't matter
    return gcd(b, a%b)
    
# Test Cases
print(gcd(-5,0)) # when gcd has 0
print(gcd(0,5)) # when gcd has 0
print(gcd(0,0)) # gcd(0,0) edge case
print(gcd(48,18)) # regular case
print(gcd(18,48)) # regular case
print(gcd(19, 29)) # co-prime
print(gcd(1,0)) # co-prime
print(gcd(-48,18)) # 1 is negative
print(gcd(48,-18)) # 1 is negative
print(gcd(-48,-18)) # both are negative
print(gcd(54, 24))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
