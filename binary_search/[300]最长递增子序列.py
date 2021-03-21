# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。
#
#
#  示例 1：
#
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
#
#  示例 2：
#
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
#
#  示例 3：
#
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2500
#  -104 <= nums[i] <= 104
#
#
#
#
#  进阶：
#
#
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#
#  Related Topics 二分查找 动态规划
#  👍 1249 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        tails = [nums[0]]
        for i in range(1, n):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                b, e = 0, len(tails) - 1
                while b < e:
                    m = b + (e - b) // 2
                    if tails[m] < nums[i]:
                        b = m + 1
                    elif tails[m] > nums[i]:
                        e = m
                    else:
                        b = m
                        break
                tails[b] = nums[i]
        return len(tails)
# leetcode submit region end(Prohibit modification and deletion)
