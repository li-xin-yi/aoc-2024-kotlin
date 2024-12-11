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

def topo_sort(lst):
    nums = set(lst)
    sub_before = {i: nums&before[i] for i in nums}
    sub_after = {i: nums&after[i] for i in nums}
    q = [i for i in nums if not sub_after[i]]
    for i in q:
        for j in sub_before[i]:
            sub_after[j].remove(i)
            if not sub_after[j]:
                q.append(j)
    pos = {num: i for i, num in enumerate(q)}
    lst.sort(key=pos.__getitem__)
    return lst[len(lst)//2]

def check(lst):
    prev = set()
    for num in lst:
        if prev & before[num]:
            return topo_sort(lst)
        prev.add(num)
    return 0

print(sum(map(check, updates)))