# param
N = int(input())
S = list(input())
Q = int(input())

mapping = {chr(i): chr(i) for i in range(ord("a"), ord("z") + 1)}

for _ in range(Q):
    c_i, d_i = input().split()
    for k, v in mapping.items():
        if v == c_i:
            mapping[k] = d_i

final_s = "".join(mapping[c] for c in S)

print(final_s)
