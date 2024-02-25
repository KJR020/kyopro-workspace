def rotate(matrix):
    return list(zip(*matrix[::-1]))


def can_match(A, B):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == 1 and B[i][j] != 1:
                return False
    return True


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for _ in range(4):
    A = rotate(A)
    if can_match(A, B):
        print("Yes")
        exit()

print("No")
