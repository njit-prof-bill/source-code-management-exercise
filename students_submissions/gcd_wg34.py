def gcd(a: int, b: int) -> int:
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            print("Error: Inputs must be integers.")
            return None
        a, b = abs(a), abs(b)
        if a == 0 and b == 0:
            print("Error: GCD is undefined for (0, 0).")
            return 0  # or return None if you'd prefer
        if b == 0:
            return a
        return gcd(b, a % b)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test cases
print(gcd(54, 24))  
print(gcd(48, 18))  
print(gcd(101, 10))  