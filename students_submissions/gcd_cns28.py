def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))