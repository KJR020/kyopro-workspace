# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
N = int(input())
P = list(map(int, input().split()))
q = int(input())
AB = [list(map(int, input().split())) for _ in range(q)]

# solve
# queryの数だけ次の判定を行う
# A, Bのそれぞれ、並び順をPから取得する
# それぞれを比較して、値が小さい方を回答する

for query in AB:
    a, b = query
    a_pos = P.index(a) + 1
    b_pos = P.index(b) + 1
    if a_pos < b_pos:
        ans = a
    else:
        ans = b

    print(ans)
