# param
N, M = map(int, input().split())
if M >= 1:
    a = list(map(int, input().split()))
else:
    a = []

ans = []
L = 1

while L <= N:
    R = L
    while R in a:
        R += 1
    ans += list(range(R, L - 1, -1))
    L = R + 1

# answer
print(" ".join(list(map(str, ans))))
