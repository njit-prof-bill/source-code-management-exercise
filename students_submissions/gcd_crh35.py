def gcd(a: int, b: int) -> int:

    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, int) or not isinstance(b, int):
        print("Error: gcd(a, b) two integers are required.")
        return None

    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    a = abs(a)
    b = abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(20, 8))
print(gcd(100, 25))
print(gcd(101, 10))
print(gcd(13, 7))
print(gcd(17, 3))
print(gcd(54, -24))
print(gcd(-54, 24))
print(gcd(0,9))
print(gcd(9,0))
print(gcd(18, 18))
print(gcd(2.5, 2))

