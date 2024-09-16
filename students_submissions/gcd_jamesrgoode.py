def gcd(a: int, b: int) -> int:
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

print(gcd(12,30))
print(gcd(30,12))
print(gcd(100,100))
print(gcd(30,100))
print(gcd(100,30))
print(gcd(12,30))
print(gcd(7,77))
print(gcd(12,21057))
