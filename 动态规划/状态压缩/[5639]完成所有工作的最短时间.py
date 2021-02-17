# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
#
#  请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你
# 设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
#
#  返回分配方案中尽可能 最小 的 最大工作时间 。
#
#
#
#  示例 1：
#
#
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#
#
#  示例 2：
#
#
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
#
#
#
#  提示：
#
#
#  1 <= k <= jobs.length <= 12
#  1 <= jobs[i] <= 107
#
#  Related Topics 递归 回溯算法
#  👍 16 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        if n == k:
            return max(jobs)
        elif k == 1:
            return sum(jobs)
        dp = [[0] * k for _ in range(1 << n)]
        for i in range(1 << n):
            for j in range(n):
                if i & (1 << j) > 0:
                    dp[i][0] = dp[i - (1 << j)][0] + jobs[j]
                    break

        for i in range(1 << n):
            for kk in range(1, k):
                res = float('inf')
                ii = i
                while True:
                    ii = (ii - 1) & i  # 枚举子集(漂亮！！)
                    if ii <= 0:
                        break
                    res = min(res, max(dp[i][0] - dp[ii][0], dp[ii][kk - 1]))
                dp[i][kk] = res
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.minimumTimeRequired(jobs=[46, 13, 54, 51, 38, 49, 54, 67, 26, 78, 33], k=10))
