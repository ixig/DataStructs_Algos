from random import randint
import numpy as np

def fermat_test_prime(p, k=20):
    prev_k = set()
    for _ in range(k):
        while (n := randint(1, p - 1)) in prev_k:
            pass
        prev_k.add(n)
        if (n ** (p - 1) % p) != 1:
            return False
    return True  # Probably ;-)

if False:
    print(fermat_test_prime(16))
    print(fermat_test_prime(21))
    print(fermat_test_prime(199))
    print(fermat_test_prime(1999))

def find_primes(n):
    # n: up to but not including
    # Sieve of Eratosthenes
    array = np.arange(n)
    for i in range(4, len(array), 2):
        array[i] = 0
    for i in range(1, int(np.sqrt(len(array)))):
        m = i * 2 + 1
        for j in range(m * m, n, m):
            array[j] = 0
    
    # find largest prime < n
    for i in range(len(array) - 1, 1, -1):
        if array[i] != 0: break

    return array, i

if True:
    print(find_primes(99))
    print(find_primes(100))
    print(find_primes(200))
