# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n, k = map(int, input().split())

s = [input() for _ in range(n)]

# answer
for name in sorted(s[:k]):
    print(name)
