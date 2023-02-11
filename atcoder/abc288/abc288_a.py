# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n = int(input())

ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

for a, b in ab:
    print(a + b)
