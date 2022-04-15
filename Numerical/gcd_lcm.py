def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(78, 66))
print(gcd(66, 78))
print(gcd(11, 12))
print(gcd(12, 11))

def lcm(a, b):
    # return a * b // gcd(a, b)
    # alternatively for large a, b
    a, b = (b, a) if b > a else (a, b)
    return a // gcd(a, b) * b

print(lcm(12, 15))
print(lcm(15, 12))
print(lcm(12, 13))
print(lcm(13, 12))
