import collections


class UnionFind:
    def __init__(self):
        self.tree = {}

    def find(self, n):
        if n not in self.tree:
            self.tree[n] = n
            return n
        if self.tree[n] != n:
            self.tree[n] = self.find(self.tree[n])
        return self.tree[n]

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 != r2:
            self.tree[r1] = r2

    def cluster(self):
        cls = collections.defaultdict(set)
        for n in self.tree:
            r = self.find(n)
            cls[r].add(n)
        return list(cls.values())


if __name__ == '__main__':
    uf = UnionFind()
    uf.union(1, 2)
    uf.union(1, 4)
    uf.union(1, 3)
    uf.union(2, 5)
    uf.union(6, 7)
    uf.union(7, 9)
    uf.union(7, 8)
    print(uf.cluster())
