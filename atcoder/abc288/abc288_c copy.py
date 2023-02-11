import sys, os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def get_root(s):
    v = []
    while not s == root[s]:
        v.append(s)
        s = root[s]
    for i in v:
        root[s] = s
    return s


def unite(s, t):
    rs, rt = get_root(s), get_root(t)
    if not rs ^ rt:
        return
    if rank[s] == rank[t]:
        rank[rs] += 1
    if rank[s] >= rank[t]:
        root[rt] = rs
        size[rs] += size[rt]
    else:
        root[rs] = rt
        size[rt] += size[rs]
    return


def same(s, t):
    return True if get_root(s) == get_root(t) else False


def get_size(s):
    return size[get_root(s)]


n, m = map(int, input().split())
root = [i for i in range(n + 1)]
rank = [1 for i in range(n + 1)]
size = [1 for i in range(n + 1)]
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    if not same(a, b):
        unite(a, b)
    else:
        ans += 1
print(ans)
