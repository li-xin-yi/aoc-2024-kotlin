from collections import Counter

with open('../inputs/day01.txt') as f:
    lines = f.readlines()

left, right = [], []
for line in lines:
    a, b = map(int, line.strip().split())
    left.append(a)
    right.append(b)

cnt = Counter(right)
res = 0
for a in left:
    res += a * cnt[a]
print(res)