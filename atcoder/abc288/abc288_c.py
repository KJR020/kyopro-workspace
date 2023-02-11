# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1


# param
n, m = map(int, input().split())

p = [-1] * (n + 1)


def root(x):
    if p[x] < 0:
        return x
    p[x] = root(p[x])
    return p[x]


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    p[x] += p[y]
    p[y] = x


def size(x):
    x = root(x)
    return -p[x]


ans = 0
for _ in range(m):
    a, b = map(int, input().split())
    if root(a) == root(b):
        ans += 1
    unite(a, b)


print(ans)
