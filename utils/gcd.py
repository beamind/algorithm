from functools import lru_cache


# 求a和b的最大公因数
@lru_cache(None)
def gcd(a, b):
    while (a % b != 0):
        m = a % b
        a = b
        b = m
    return b


if __name__ == '__main__':
    print(gcd(121, 22))
    print(gcd(49, 63))
    gcd.cache_clear()
