def gcd(a: int, b: int) -> int: 
    while b: a, b = b, a % b 
    return a # Test cases print(gcd(54, 24))
