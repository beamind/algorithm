from typing import Dict, Set


# 判断是否是二分图
def grapth_is_bipartite(graph: Dict[int, Set[int]]):
    def dfs(v, c):
        visited[v] = c
        for n in graph[v]:
            if n not in visited:
                if not dfs(n, 1 - c):
                    return False
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


if __name__ == '__main__':
    graph = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
    print(grapth_is_bipartite(graph))
