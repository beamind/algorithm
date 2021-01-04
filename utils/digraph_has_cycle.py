from typing import Dict, Set


# 判断有向图是否有环
def digraph_has_cycle(graph: Dict[int, Set]) -> bool:
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
    print(digraph_has_cycle(graph))

