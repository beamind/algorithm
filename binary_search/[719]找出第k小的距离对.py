# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
#
#  示例 1:
#
#
# 输入：
# nums = [1,3,1]
# k = 1
# 输出：0
# 解释：
# 所有数对如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
#
#
#  提示:
#
#
#  2 <= len(nums) <= 10000.
#  0 <= nums[i] < 1000000.
#  1 <= k <= len(nums) * (len(nums) - 1) / 2.
#
#  Related Topics 堆 数组 二分查找
#  👍 157 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import bisect
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        b, e = 0, nums[-1] - nums[0]
        while b <= e:
            m = (b + e) // 2
            cnt = 0
            for i, n in enumerate(nums):
                left = bisect.bisect_left(nums, n - m)
                cnt += i - left
                right = bisect.bisect(nums, n + m)
                cnt += right - i - 1
                if right < len(nums) and nums[right] == n + m:
                    cnt += 1
            cnt = cnt // 2
            if cnt < k:
                b = m + 1
            elif cnt >= k:
                e = m - 1
        return e + 1


if __name__ == '__main__':
    s = Solution()
    print(s.smallestDistancePair(nums=[1, 3, 1], k=1))
# leetcode submit region end(Prohibit modification and deletion)
