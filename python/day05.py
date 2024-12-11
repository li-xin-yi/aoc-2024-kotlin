from collections import defaultdict

with open('../inputs/day05.txt') as f:
    lines = f.readlines()

before = defaultdict(set)
after = defaultdict(set)
updates = []
for line in lines:
    if '|' in line:
        left, right = line.strip().split('|')
        before[int(left)].add(int(right))
        after[int(right)].add(int(left))
    else:
        if line.strip():
            updates.append(list(map(int, line.strip().split(','))))

def check(lst):
    prev = set()
    for num in lst:
        if prev & before[num]:
            return 0
        prev.add(num)
    return lst[len(lst)//2]

print(sum(map(check, updates)))