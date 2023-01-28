# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1


# param
n = int(input())

majority_num = n // 2 + 1

s_ary = [input() for i in range(n)] 

count_for = 0
for s in s_ary:
    if s == "For":
        count_for += 1

if count_for >= majority_num:
            print("Yes")
else:
    print("No")