def gcd(a: int, b: int) -> int:
    #Calculate the GCD using the Euclidean algorithm
    if a==0:
        return b
    
    return gcd(b%a, a)

print(gcd(54, 24))