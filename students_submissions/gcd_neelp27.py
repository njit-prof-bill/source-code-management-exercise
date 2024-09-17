def gcd(a: int, b:int) -> int:

    if a==0:
        return b
    

    return gcd(b%a, a)



print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1