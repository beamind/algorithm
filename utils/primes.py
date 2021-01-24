# 计算小于等于n的所有素数
def get_primes(n: int):
    if n < 2:
        return []
    nums = [True] * (n + 1)
    nums[0] = False
    nums[1] = False
    i = 2
    while i <= n:
        if nums[i]:
            j = 2 * i
            while j <= n:
                nums[j] = False
                j += i
        i += 1
    return [i for i in range(n + 1) if nums[i]]


if __name__ == '__main__':
    print(get_primes(100))
