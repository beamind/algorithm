import math
from functools import lru_cache


# 求a和b的最大公因数
@lru_cache(None)
def gcd(a, b):
    if b == 0:
        return a
    while (a % b != 0):
        m = a % b
        a = b
        b = m
    return b


def gcd2(a, b):
    return math.gcd(a, b)


if __name__ == '__main__':
    print(gcd(121, 22))
    print(gcd(49, 63))
    print(gcd(5, 0))
    print(gcd(0, 5))

    gcd.cache_clear()

    print(gcd2(121, 22))
