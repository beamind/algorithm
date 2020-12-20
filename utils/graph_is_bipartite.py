from typing import Dict, Set


# 判断是否是二分图
def grapth_is_bipartite(self, graph: Dict[int, Set[int]]):
    def dfs(v, c):
        visited[v] = c
        for n in graph[v]:
            if n not in visited:
                dfs(n, 1 - c)
            elif visited[n] == c:
                return False
        return True

    if not graph:
        return True
    visited = {}
    for v in graph:
        if v not in visited:
            if not dfs(v, 0):
                return False
    return True