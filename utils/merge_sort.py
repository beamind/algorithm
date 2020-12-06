def merge_sort(nums, lo, hi):
    if lo >= hi:
        return
    aux = nums[lo:hi + 1]
    mid = (hi - lo) // 2
    merge_sort(aux, 0, mid)
    merge_sort(aux, mid + 1, hi - lo)
    i, j = 0, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            nums[k] = aux[j]
            j += 1
        elif j > hi - lo:
            nums[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            nums[k] = aux[i]
            i += 1
        else:
            nums[k] = aux[j]
            j += 1


if __name__ == '__main__':
    for nums in [[], [1], [4, 3], [4, 3, 2], [1, 0, 2, 4]]:
        merge_sort(nums, 0, len(nums) - 1)
        print(nums)
