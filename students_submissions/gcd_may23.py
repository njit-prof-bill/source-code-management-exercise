def gcd(a: int, b: int) -> int:

    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(54, 24))      
print(gcd(48, 18))      
print(gcd(101, 10))     
print(gcd(-81, 27))    
print(gcd(0, 5))       
print(gcd(0, 0))        