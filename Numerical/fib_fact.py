'''
Fibonacci, Factorial
'''

def fib1(n):  # Recursive
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)

def fib2(n):  # Iterative
    nm2, nm1 = -1, 1
    for _ in range(n):
        nm2, nm1 = nm1, nm1 + nm2
    return nm1 + nm2

print([fib1(n) for n in range(10)])
print([fib2(n) for n in range(10)])


def fact1(n):  # Recursive
    if n <= 1:
        return 1
    return n * fact1(n - 1)

def fact2(n):  # Iterative
    nm1 = 1
    for i in range(1, n + 1):
        nm1 *= i
    return nm1

print([fact1(n) for n in range(7)])
print([fact2(n) for n in range(7)])
