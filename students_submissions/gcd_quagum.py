def gcd(a: int, b: int) -> int: 
    """ Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm. """ 
    # Implement your solution here pass
    true_a = int(a)
    true_b = int(b)
    while True:
        r = a % b
        if not r:
            break
        a = b
        b = r

    print("GCD of {} and {} is: {}".format(true_a, true_b, b))

gcd(54, 24)  # Expected output: 6
gcd(48, 18)  # Expected output: 6
gcd(101, 10)  # Expected output: 1