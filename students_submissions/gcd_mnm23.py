def gcd(a, b):
    if a == 0 and b == 0:
        return None
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(24, 54))     
