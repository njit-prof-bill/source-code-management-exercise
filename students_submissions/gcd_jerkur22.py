def gcd(a: int, b: int) -> int: 
    while b:
        a, b = b, a % b
    return a


print(gcd(10, 30)) # 10
print( gcd(5, 5)) #5
print(gcd(7, 14)) #7
print(gcd(50, 75)) # 25
