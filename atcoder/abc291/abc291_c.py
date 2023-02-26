# number of moves by Takahashi
N = int(input())
# movement record
S = input()

x, y = 0, 0
# list of visited places
visited = [(x, y)]
for i in range(N):
    if S[i] == "R":
        x += 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "U":
        y += 1
    else:
        y -= 1
    # Appending the position to visited list.
    visited.append((x, y))

# Checks for duplicates in visited list.
result = "Yes" if len(set(visited)) != len(visited) else "No"

print(result)
