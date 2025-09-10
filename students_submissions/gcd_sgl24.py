def gcd(a: int, b: int) -> int:
    if b == 0:
        result = a
    else:
        result = abs(gcd(b, a % b))
    return result

print(gcd(54, 24))
print(gcd(7, 2))
print(gcd(9, -3))
