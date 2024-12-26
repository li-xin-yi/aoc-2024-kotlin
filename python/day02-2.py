with open('../inputs/day02.txt') as f:
    lines = f.readlines()

def check(lst):
    for removed in range(len(lst)+1):
        nums = lst[:removed] + lst[removed+1:]
        diff = [b-a for a, b in zip(nums, nums[1:])]
        if any(d * diff[0] <= 0 for d in diff[1:]):
            continue
        if all(abs(d) <=3 for d in diff):
            return True
    return False

res = 0
for line in lines:
    lst = list(map(int, line.strip().split()))
    res += int(check(lst))

print(res)