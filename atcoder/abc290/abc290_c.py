# param
n, k = map(int, input().split())
a = [int(ai) for ai in input().split()]

# solve
b = set(a)
ans = 0

while ans < k and ans in b:
    ans += 1

# answer
print(ans)
