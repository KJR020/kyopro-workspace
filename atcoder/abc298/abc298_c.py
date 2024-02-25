import sys
from collections import defaultdict


def main():
    N = int(input().strip())
    Q = int(input().strip())

    boxes = [defaultdict(int) for _ in range(N)]

    for _ in range(Q):
        query = list(map(int, input().strip().split()))

        if query[0] == 1:
            i, j = query[1], query[2] - 1
            boxes[j][i] += 1

        elif query[0] == 2:
            i = query[1] - 1
            for num, count in sorted(boxes[i].items()):
                print(" ".join(str(num) for _ in range(count)), end=" ")
            print()

        elif query[0] == 3:
            i = query[1]
            for j, box in enumerate(boxes):
                if i in box:
                    print(j + 1, end=" ")
            print()


if __name__ == "__main__":
    main()
