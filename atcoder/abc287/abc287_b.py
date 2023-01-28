# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N, M = map(int, input().split())

S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

ans = 0
for s in S:
   if s[-3:] in T:
       ans += 1

print(ans)