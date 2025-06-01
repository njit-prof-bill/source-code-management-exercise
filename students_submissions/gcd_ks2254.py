def gcd(a: int, b: int):
    
    if b == 0:
        return abs(a)
    else:
        return gcd(abs(b) , abs(a % b))

