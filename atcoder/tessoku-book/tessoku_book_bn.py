# Union-Find 木
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)  # 最初は親がない状態 → -1
        self.size = [1] * (n + 1)  # 最初はグループの頂点数は１

    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.par[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.par[root_v] = root_u
                self.size[root_u] += self.size[root_v]

    # 要素uとvが同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)


# 入力
N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for i in range(Q)]

# クエリの処理
uf = UnionFind(N)
for tp, u, v in queries:
    if tp == 1:
        uf.unite(u, v)
    if tp == 2:
        if uf.same(u, v):
            print("Yes")
        else:
            print("No")
