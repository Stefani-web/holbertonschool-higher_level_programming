#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    result = 1
    while b > 0:
        if b % 2 == 1:  # If b is odd
            result *= a
        a *= a
        b //= 2
    return result
