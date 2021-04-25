# 给你两个长度分别 n 和 m 的整数数组 nums 和 multipliers ，其中 n >= m ，数组下标 从 1 开始 计数。
#
#  初始时，你的分数为 0 。你需要执行恰好 m 步操作。在第 i 步操作（从 1 开始 计数）中，需要：
#
#
#  选择数组 nums 开头处或者末尾处 的整数 x 。
#  你获得 multipliers[i] * x 分，并累加到你的分数中。
#  将 x 从数组 nums 中移除。
#
#
#  在执行 m 步操作后，返回 最大 分数。
#
#
#
#  示例 1：
#
#  输入：nums = [1,2,3], multipliers = [3,2,1]
# 输出：14
# 解释：一种最优解决方案如下：
# - 选择末尾处的整数 3 ，[1,2,3] ，得 3 * 3 = 9 分，累加到分数中。
# - 选择末尾处的整数 2 ，[1,2] ，得 2 * 2 = 4 分，累加到分数中。
# - 选择末尾处的整数 1 ，[1] ，得 1 * 1 = 1 分，累加到分数中。
# 总分数为 9 + 4 + 1 = 14 。
#
#  示例 2：
#
#  输入：nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# 输出：102
# 解释：一种最优解决方案如下：
# - 选择开头处的整数 -5 ，[-5,-3,-3,-2,7,1] ，得 -5 * -10 = 50 分，累加到分数中。
# - 选择开头处的整数 -3 ，[-3,-3,-2,7,1] ，得 -3 * -5 = 15 分，累加到分数中。
# - 选择开头处的整数 -3 ，[-3,-2,7,1] ，得 -3 * 3 = -9 分，累加到分数中。
# - 选择末尾处的整数 1 ，[-2,7,1] ，得 1 * 4 = 4 分，累加到分数中。
# - 选择末尾处的整数 7 ，[-2,7] ，得 7 * 6 = 42 分，累加到分数中。
# 总分数为 50 + 15 - 9 + 4 + 42 = 102 。
#
#
#
#
#  提示：
#
#
#  n == nums.length
#  m == multipliers.length
#  1 <= m <= 103
#  m <= n <= 105
#  -1000 <= nums[i], multipliers[i] <= 1000
#
#  Related Topics 动态规划
#  👍 5 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from functools import lru_cache


class Solution:
    # 解法一：斜着遍历的动态规划
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        pre = [0] * (m + 1)
        for k in range(1, m + 1):  # 总共选取k个数的最大得分
            cur = [0] * (m + 1)
            cur[0] = pre[0] + multipliers[k - 1] * nums[n - k]  # k个数都在右边的最大得分
            cur[k] = pre[k - 1] + multipliers[k - 1] * nums[k - 1]  # k个数都在左边的最大得分
            for l in range(1, k):  # k个数中有l个数在左边的最大得分
                cur[l] = max(pre[l - 1] + multipliers[k - 1] * nums[l - 1],
                             pre[l] + multipliers[k - 1] * nums[n - k + l])
            pre = cur
        return max(pre)

    # 解法二：记忆化递归
    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        @lru_cache(None)
        def helper(i, j, idx):
            if idx == m:
                return 0
            r1 = multipliers[idx] * nums[i] + helper(i + 1, j, idx + 1)
            r2 = multipliers[idx] * nums[j] + helper(i, j - 1, idx + 1)
            return max(r1, r2)

        res = helper(0, n - 1, 0)

        helper.cache_clear()  # 此处是关键，否则超出时间限制。教训是记忆化递归时应优先使用lru_cache，并及时cache_clear，不要自己用字典记录。
        return res
# leetcode submit region end(Prohibit modification and deletion)
