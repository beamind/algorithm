# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴
# 都要用到。
#
#  输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。
#
#  示例 1:
#
#
# 输入: [1,1,2,2,2]
# 输出: true
#
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
#
#
#  示例 2:
#
#
# 输入: [3,3,3,3,4]
# 输出: false
#
# 解释: 不能用所有火柴拼成一个正方形。
#
#
#  注意:
#
#
#  给定的火柴长度和在 0 到 10^9之间。
#  火柴数组的长度不超过15。
#
#  Related Topics 深度优先搜索
#  👍 156 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        def check(x):
            res = 0
            for i in range(n):
                if x & (1 << i) > 0:
                    res += nums[i]
            return res == t

        def dfs(status, cnt):
            if cnt == 0:
                return True
            if (status, cnt) in mem:
                return mem[(status, cnt)]
            for i in range(1 << n):
                if i & status == i and check(i) and dfs(status ^ i, cnt - 1):
                    mem[(status, cnt)] = True
                    return True
            mem[(status, cnt)] = False
            return False

        if len(nums) < 4:
            return False

        total = sum(nums)
        if total % 4 > 0:
            return False

        t = total // 4
        n = len(nums)
        mem = {}
        return dfs((1 << n) - 1, 4)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.makesquare([1, 1, 2, 2, 2]))
