# 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， dependencies[i] = [xi, yi]
#  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。
#
#  在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
#
#  请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。
#
#
#
#  示例 1：
#
#
#
#  输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# 输出：3
# 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
#
#
#  示例 2：
#
#
#
#  输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# 输出：4
# 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
#
#
#  示例 3：
#
#  输入：n = 11, dependencies = [], k = 2
# 输出：6
#
#
#
#
#  提示：
#
#
#  1 <= n <= 15
#  1 <= k <= n
#  0 <= dependencies.length <= n * (n-1) / 2
#  dependencies[i].length == 2
#  1 <= xi, yi <= n
#  xi != yi
#  所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。
#  题目输入的图是个有向无环图。
#
#  Related Topics 图
#  👍 49 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        def dfs(cur, cand):
            # print(bin(cur)[2:], bin(cand)[2:])
            # 如果已经学习完n门功课则还需要0学期
            if bin(cur).count('1') == n:
                return 0

            # 如果递归过程中已经对状态cur搜索过，则直接返回搜索结果即可
            if cur in mem:
                return mem[cur]

            # 如果当前可学习的课程数小于等于k，则该学期把可学习的课程都学习完
            if bin(cand).count('1') <= k:
                cur2 = cur | cand
                invalid = ((1 << n) - 1) ^ cur2
                cand2 = ((1 << n) - 1) ^ cur2
                for i in range(1, n + 1):
                    if invalid & (1 << (i - 1)) > 0:
                        for j in graph[i]:
                            if cand2 & (1 << (j - 1)) > 0:
                                cand2 ^= (1 << (j - 1))
                res = dfs(cur2, cand2) + 1
                mem[cur] = res
                return res

            # 如果当前可学习的课程数大于k，则枚举可学习课程的大小为k的子集
            res = float('inf')
            sub = cand
            while sub > 0:
                sub = (sub - 1) & cand  # 枚举子集(!!漂亮)
                if bin(sub).count('1') == k:
                    cur2 = cur | sub
                    invalid = ((1 << n) - 1) ^ cur2
                    cand2 = ((1 << n) - 1) ^ cur2
                    for i in range(1, n + 1):
                        if invalid & (1 << (i - 1)) > 0:
                            for j in graph[i]:
                                if cand2 & (1 << (j - 1)) > 0:
                                    cand2 ^= (1 << (j - 1))
                    res = min(res, dfs(cur2, cand2) + 1)
            mem[cur] = res
            return res

        graph = collections.defaultdict(list)
        indegree = {i: 0 for i in range(1, n + 1)}
        for u, v in dependencies:
            graph[u].append(v)
            indegree[v] += 1

        cand = 0
        for v, dgr in indegree.items():
            if dgr == 0:
                cand += (1 << (v - 1))

        mem = {}
        return dfs(0, cand)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.minNumberOfSemesters(12, [[1, 2], [1, 3], [7, 5], [7, 6], [4, 8], [8, 9], [9, 10], [10, 11], [11, 12]], 2))
