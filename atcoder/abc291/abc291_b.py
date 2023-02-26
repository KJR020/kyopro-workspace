# param
n = int(input())
x_ = list(map(int, input().split()))


# solve
x_.sort()
x_extracted = x_[n:-n]
ans = sum(x_extracted) / len(x_extracted)


# answer
print(ans)
