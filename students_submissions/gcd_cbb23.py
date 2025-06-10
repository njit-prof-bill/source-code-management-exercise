def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            print("Error: not an integer")
            return None
        if a == 0 and b == 0:
            print("Error: GCD is undefined for b = 0 or a= 0")
            return None
        
        a = abs(a)
        b = abs(b)
        
        if b == 0:
            return a
        return gcd(b, a % b)
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    
print(gcd(54, 24))
print(gcd(-48, -18))
print(gcd(101,10))