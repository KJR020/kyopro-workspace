import sys

# param

N, M = map(int, input().split())

# G = [[0 for _ in range(N)] for _ in range(N)]
G = dict()

if M > 0:
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1][v-1] += 1 
        G[v-1][u-1] += 1     
else:
    print("No")
    sys.exit()


edge_count = 0
for row in G:
    if sum(row) >= 3:
        print("No")
        sys.exit()
    elif sum(row) == 1:
        edge_count+=1
    elif sum(row) == 0:
        print("No")
        sys.exit()

if edge_count == 2:
    print("Yes")

else:
    print("No")
    