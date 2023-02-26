import itertools


def check_duplicate(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i - 1]:
            return True
    return False


# param
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

ans = 0


print(num_dup)
