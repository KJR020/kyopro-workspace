# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# solve
ans = sum([a[i - 1] for i in b])

# answer
print(ans)
