def gcd(a: int, b: int) -> int:
    if a < 0 or b < 0:
        print("No negative inputs allowed")
        return None

    if a == 0 and b == 0:
        print("Algorithm undefined for input a = 0 and b = 0")
        return None

    if b == 0:
        return a

    return gcd(b, a % b)

print(gcd(123456, 789012))    # 12 : large unrelated looking numbers
print(gcd(77, 121))           # 11 : odd numbers with shared factor
print(gcd(4620, 1071))        # 21 : both divisible by 21 but look unrelated
print(gcd(4444, 8888))        # 4444 : one is double the other
print(gcd(867, 255))          # 51: not obvious, but shared factor
print(gcd(9991, 789))         # 1 : coprime
print(gcd(10203, 12345))      # 3 : messy looking numbers with small factor
print(gcd(111, 185))          # 37 :not a common pairing
print(gcd(1210, 5445))        # 605 
print(gcd(99991, 100001))     # 1 : close but no common factor
print(gcd(0, 0))              # None: invalid
print(gcd(-11, 11))           # None: invalid
print(gcd(11, -11))           # None: invalid
print(gcd(11, 0))             # 11: b is 0 so a
print(gcd(0, 11))             # 11: a is 0 so b