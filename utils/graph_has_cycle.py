import collections
from typing import Dict, Set


# 判断无向图中是否有环
# n: 有向图的节点个数
# graph: 有向图
# 时间复杂度: O(m + n), 空间复杂度: O(m + n), 其中m是边数, n是顶点数
def graph_has_cycle(n, graph: Dict[int, Set]) -> bool:
    degree = collections.defaultdict(int)
    for u, vs in graph.items():
        degree[u] = len(vs)
    nodes = collections.deque()
    for i in graph:
        if degree[i] < 2:
            nodes.append(i)
    if not nodes:
        return True
    cnt = 0
    while nodes:
        cnt += 1
        u = nodes.popleft()
        for v in graph[u]:
            degree[v] -= 1
            if degree[v] < 2:
                nodes.append(v)
    return cnt < n


# 判断无向图中是否有环
def graph_has_cycle2(graph: Dict[int, Set]) -> bool:
    def dfs(c, p):
        visited.add(c)
        for n in graph[c]:
            if n not in visited:
                dfs(n, c)
            elif n != p:
                return True
        return False

    if not graph:
        return False
    visited = set()

    for v in graph:  # 遍历每个连通分量
        if v not in visited:
            if dfs(v, v):
                return True
    return False

if __name__ == '__main__':
    graph = {}