def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    try:
        # Validate the input types
        if not isinstance(a, int) or not isinstance(b, int):
            print("Error: Inputs have to be integers.")
            return None

        # Edge case: if both are zero
        if a == 0 and b == 0:
            print("Error: GCD undefined when a = 0 and b = 0.")
            return None

        # Apply absolute value to handle negative integers
        a, b = abs(a), abs(b)

        # Base case: if b is zero, gcd is a
        if b == 0:
            return a

        # eecursive case
        return gcd(b, a % b)

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# ---- Test Cases ----

print(gcd(54, 24))    
print(gcd(48, 18))    
print(gcd(101, 10))   
print(gcd(-22, 56))   
print(gcd(0, 121))     
print(gcd(0, 0))      
print(gcd("45", 8))  