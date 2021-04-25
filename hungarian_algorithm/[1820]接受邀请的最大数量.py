# 班级中有m个男孩和n个女孩要参加一个聚会。
#
# 给你一个 m x n 的整数矩阵 grid， 其中grid[i][j] 是0 或1。 grid[i][j] == 1表示第 i 个男孩可以邀请第 j 个女孩参加聚会。
# 一个男孩最多可以 邀请一个女孩，一个女孩最多可以接受 一个男孩的邀请。
#
# 返回接受邀请的最大数量。
#
#
#
#  示例 1：
#
# 输入: grid = [[1,1,1],
#              [1,0,1],
#              [0,0,1]]
# 输出: 3
# 解释: 邀请情况如下:
# - 第1个男孩邀请第2个女孩。
# - 第2个男孩邀请第1个女孩。
# - 第3个男孩邀请第3个女孩。
#
#  示例 2：
#
# 输入: grid = [[1,0,1,0],
#              [1,0,0,0],
#              [0,0,1,0],
#              [1,1,1,0]]
# 输出: 3
# 解释: 邀请情况如下:
# - 第1个男孩邀请第3个女孩。
# - 第2个男孩邀请第1个女孩。
# - 第3个男孩不邀请任何女孩。
# - 第4个男孩邀请第2个女孩。
#
#
#
#
#  提示：
#
#
# grid.length == m
# grid[i].length == n
# 1 <= m, n <= 200
# grid[i][j] 是 0 或1
#
#  Related Topics 匈牙利算法
#  👍 5 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        # 匈牙利算法

        # match(i): 第i个男孩是否能找到女孩
        def match(i):
            for j in range(n):  # 遍历每一个女孩
                if grid[i][j] == 1 and j not in visited:  # 只要是没尝试过的就尝试一下
                    visited.add(j)  # 记录尝试
                    if j not in girl2boy or match(girl2boy[j]):  # 如果该女孩还没有匹配，或者匹配了但与之匹配的男孩可以改选
                        girl2boy[j] = i  # 与女孩j匹配的男孩是i
                        return True  # 匹配成功返回
            return False  # 遍历所有女孩都没能找到匹配的，匹配失败

        m, n = len(grid), len(grid[0])
        ans = 0
        girl2boy = {}  # 女孩对应的男孩
        for i in range(m):  # 遍历每一个男孩
            visited = set()  # 记录该男孩尝试匹配的女孩
            if match(i):  # 如果男孩能找到匹配的女孩
                ans += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
