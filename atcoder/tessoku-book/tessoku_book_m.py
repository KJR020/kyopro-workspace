import bisect

# param
N, K = map(int, input().split())
a = [x for x in map(int, input().split())]

# solve
ans = 0
for li in range(N - 1):
    x = a[li] + K
    ri = bisect.bisect_right(a, x, lo=li + 1) - 1
    ans += ri - li

# answer
print(ans)
