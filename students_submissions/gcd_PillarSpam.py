

def gcd(a: int, b: int) -> int:
    temp = a % b
    while temp > 0:
        a = b
        b = temp
        temp = a % b
    return b
