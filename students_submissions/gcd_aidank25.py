def gcd(a: int, b: int) -> int: 
    print("running gcd")
    while b: 
        a, b = b, a % b 
    return a 