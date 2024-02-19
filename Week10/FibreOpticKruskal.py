class UnionFind:

    def __init__(self, n):
        for i in range(n):
            self.p = [i for i in range(n)]
            self.sz = [1 for _ in range(n)]

    def find(self, x):
        if (x == self.p[x]):
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self, u, v):
        rU = self.find(u)
        rV = self.find(v)

        if rU != rV:
            if self.sz[rU] < self.sz[rV]:
                rU, rV = rV, rU
            self.p[rV] = rU
            self.sz[rU] += self.sz[rV]

    def connected(self, u, v):
        return self.find(u) == self.find(v)


N, M = list(map(int, input().split()))
edges = []

for _ in range(M):
    A, B, W = map(int, input().split())
    edges.append((A - 1, B - 1, W))

edges.sort(key=lambda edge: edge[2])

total_price = 0
u = UnionFind(N)
for i in range(len(edges)):
    A, B, W = edges[i]

    if not u.connected(A, B):
        u.union(A, B)
        total_price += W

print(total_price)
