import sys

input = sys.stdin.readline
nums = list(map(int, input().strip()))

cur = 0
res = 0
last = len(nums) // 2 * 2
for i, num in enumerate(nums):
    if i % 2 == 0:
        if num == 0:
            break
        res += (i//2) * ((cur + cur + num - 1) * num // 2)
    else:
        for j in range(num):
            while last > i and nums[last] == 0:
                last -= 2
            if last <= i:
                break
            res += (cur + j) * (last//2)
            nums[last] -= 1
    cur += num

print(res)

            


