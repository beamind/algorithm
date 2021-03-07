# 有 n 个网络节点，标记为 1 到 n。
#
#  给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， w
# i 是一个信号从源节点传递到目标节点的时间。
#
#  现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
#
#
#
#  示例 1：
#
#
#
#
# 输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# 输出：2
#
#
#  示例 2：
#
#
# 输入：times = [[1,2,1]], n = 2, k = 1
# 输出：1
#
#
#  示例 3：
#
#
# 输入：times = [[1,2,1]], n = 2, k = 2
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= k <= n <= 100
#  1 <= times.length <= 6000
#  times[i].length == 3
#  1 <= ui, vi <= n
#  ui != vi
#  0 <= wi <= 100
#  所有 (ui, vi) 对都 互不相同（即，不含重复边）
#
#  Related Topics 堆 深度优先搜索 广度优先搜索 图
#  👍 231 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
import heapq
from typing import List


# Dijkstra算法每次扩展一个距离最短的点，更新与其相邻点的距离。
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        hq = []
        heapq.heapify(hq)
        heapq.heappush(hq, (0, k))
        visited = set()
        ans = -1
        while hq:
            t, u = heapq.heappop(hq)
            if u not in visited:
                visited.add(u)
                ans = t
            for v, dt in graph[u]:
                if v not in visited:
                    heapq.heappush(hq, (t + dt, v))
        return ans if len(visited) == n else -1
# leetcode submit region end(Prohibit modification and deletion)
