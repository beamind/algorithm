from typing import Dict, Set


# 判断图中是否有环
def graph_has_cycle(self, graph: Dict[int, Set]) -> bool:
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
