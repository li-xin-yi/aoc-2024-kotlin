from collections import defaultdict

with open('../inputs/day07.txt') as f:
    lines = f.readlines()

def check_feasible(result, operands):
    cur = set([operands[0]])
    for num in operands[1:]:
        temp = set()
        for prev in cur:
            if prev + num <= result:
                temp.add(prev + num)
            if prev * num <= result:
                temp.add(prev * num)
        if not temp:
            return False
        cur = temp
    return result in cur

res = 0
for line in lines:
    left, right = line.strip().split(':')
    operands = list(map(int, right.strip().split(' ')))
    left = int(left)
    if check_feasible(left, operands):
        res += left

print(res)
