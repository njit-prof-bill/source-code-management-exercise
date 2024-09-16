def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


# Test cases
# print(gcd(54, 24))  # Expected output: 6
# print(gcd(48, 18))  # Expected output: 6
# print(gcd(101, 10))  # Expected output: 1


def gcd_test() -> None:
    x = [
        (10, 5),
        (5, 7),
        (20, 4),
        (32, 16),
        (55, 36),
        (6, 74),
        (51, 34),
        (101, 10),
        (54, 24),
        (48, 18),
    ]
    for a, b in x:
        print(f"GCP({a},{b}) = {gcd(a, b)}")


gcd_test()
