import random

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if a < 0 or b < 0:
        print("You cannot use a negative number, sorry :/")
        return None

    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

print("GCD of prime numbers 59 and 151:", gcd(59, 151))  # output = 1
print("GCD of 35 and 105:", gcd(35, 105))                # output = 35
print("GCD of 92 and 16:", gcd(92, 16))                  # output = 4
print("GCD of 0 and 10000:", gcd(0, 10000))              # output = 10000

#trying with random integers with "a" having the range (1-100) and "b" having the range (1-200)
ayy = random.randrange(100)
bee = random.randrange(200)
print("GCD of 2 random numbers %d and %d: %d" % (ayy, bee, gcd(ayy, bee)))

print("\nGCD of -2 and 0:")
print(gcd(-2, 0))                    # output = "You cannot use a negative number, sorry :/"