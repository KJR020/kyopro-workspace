# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1

# param
s = input()

# solve
if s[0] != s[1]:
    ans = 1 if s[1] == s[2] else 2
else:
    for i in range(1, len(s)):
        if s[i] != s[0]:
            ans = i + 1
            break

# answer
print(ans)
