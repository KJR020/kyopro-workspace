import sys

# param
s = input()

# solve
ans = 0

for i, c in enumerate(s):
    if c.isupper():
        print(i + 1)
        sys.exit()
