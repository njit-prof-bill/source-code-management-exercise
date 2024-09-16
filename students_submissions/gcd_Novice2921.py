def gcd(a: int, b: int) -> int:
    while b != a:
        if b > a: b -= a
        else: a -= b
    return a #whether you return a or b, it doesnt matter as both will be equal
