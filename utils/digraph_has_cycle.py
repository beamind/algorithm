import collections
from typing import Dict, Set


# 判断有向图是否有环
# n: 有向图的节点个数
# graph: 有向图
# 时间复杂度: O(m + n), 空间复杂度: O(m + n), 其中m是边数, n是顶点数
def digraph_has_cycle(n, graph: Dict[int, Set]) -> bool:
    indegree = collections.defaultdict(int)
    for u, vs in graph.items():
        for v in vs:
            indegree[v] += 1
    nodes = collections.deque()
    for i in graph:
        if indegree[i] == 0:
            nodes.append(i)
    if not nodes:
        return True
    ans = []
    while nodes:
        u = nodes.popleft()
        ans.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                nodes.append(v)
    return len(ans) < n


# 判断有向图是否有环
def digraph_has_cycle2(graph: Dict[int, Set]) -> bool:
    def dfs(v):
        visited.add(v)
        onstack.add(v)
        for w in graph[v]:
            if w not in visited:
                if dfs(w):
                    return True
            elif w in onstack:
                return True
        onstack.remove(v)
        return False

    visited = set()
    onstack = set()
    for v in graph:
        if v not in visited:
            if dfs(v):
                return True
    return False


if __name__ == '__main__':
    graph = {0: {5}, 3: {5}, 4: {3}, 5: {4}}
    print(digraph_has_cycle(6, graph))
    print(digraph_has_cycle2(graph))
