def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

print(gcd(32, 6))
print(gcd(48, 8))
print(gcd(1134, 14))