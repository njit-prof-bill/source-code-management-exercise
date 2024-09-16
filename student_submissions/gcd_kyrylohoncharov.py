def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


assert gcd(54, 24) == 6
assert gcd(48, 18) == 6
assert gcd(101, 10) == 1
assert gcd(500, 10) == 10
assert gcd(123456, 654321) == 3
assert gcd(15, 150) == 15
assert gcd(333, 666) == 333