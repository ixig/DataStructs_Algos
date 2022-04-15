import math

# O(sqrt(2)**N), where N: #bits to represent n
def prime_factors(n):
    factors = []

    while (n % 2) == 0:
        n //= 2
        factors.append(2)

    stop = math.sqrt(n)
    factor = 3
    while factor <= stop:
        while (n % factor) == 0:
            n //= factor
            factors.append(factor)
            stop = math.sqrt(n)
        factor += 2

    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(204))
print(prime_factors(123456789012345678))
