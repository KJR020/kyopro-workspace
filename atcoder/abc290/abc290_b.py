# param
n, k = map(int, input().split())
s = input()

# solve
idx = 0
cnt = 0


while cnt < k and idx < n:
    if s[idx] == "o":
        cnt += 1
    idx += 1

ans = s[:idx] + s[idx:].replace("o", "x")

# answer
print(ans)
