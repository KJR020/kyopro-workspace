# param
T = int(input())
tests = [list(map(int, input().split())) for _ in range(T)]

# solve
for t in tests:
    N, D, K = t
    b = [i * D % N for i in range(N)]

    for l in range(1, N - 1):
        if b[l] in b[: l - 1]:
            b[l:] = [x + 1 for x in b[l:]]

    print(b[K - 1])
