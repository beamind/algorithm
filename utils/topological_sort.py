import collections
from typing import Dict, List, Set


# 有向图的拓扑排序
# n: 有向图的节点个数
# graph: 有向图
# 时间复杂度: O(m + n), 空间复杂度: O(m + n), 其中m是边数, n是顶点数
def topological_sort(n, graph: Dict[int, Set]) -> List[int]:
    indegree = collections.defaultdict(int)
    for u, vs in graph.items():
        for v in vs:
            indegree[v] += 1
    nodes = collections.deque()
    for i in graph:
        if indegree[i] == 0:
            nodes.append(i)
    if not nodes:
        return []
    ans = []
    while nodes:
        u = nodes.popleft()
        ans.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                nodes.append(v)
    if len(ans) == n:
        return ans
    else:
        return []


if __name__ == '__main__':
    graph = {0: {1, 2}, 1: {4}, 2: {5}, 3: {1}, 4: {5}, 5: {}}
    order = topological_sort(6, graph)
    print(order)
