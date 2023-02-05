# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
n, k = map(int, input().split())
a = [_ for _ in map(int, input().split())]
q = int(input())
lr = []

for i in range(q):
    l, r = map(int, input().split())
    lr.append(a[l - 1 : r - 1])


# answer
for ary in lr:
    print(ary)
    ary.sort()
    print(ary)
