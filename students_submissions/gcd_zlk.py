

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if a%b == 0:
        return b
    else:
        c = a%b
        if a%c == b%c:
            return c
        elif a%c == 0:
            return b%c
        else:
            return 1

        
            
    

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
