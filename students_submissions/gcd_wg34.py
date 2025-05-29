def gcd(a: int, b: int) -> int:
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            print("Error: Inputs must be integers.")
            return None
        a, b = abs(a), abs(b)
        if b == 0:
            return a
        return gcd(b, a % b)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test cases
print(gcd(54, 24))  # Expected output: 6 
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1