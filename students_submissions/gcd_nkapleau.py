def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
    
print(gcd(54,24))

print(gcd(48,18))

print(gcd(101,10))

