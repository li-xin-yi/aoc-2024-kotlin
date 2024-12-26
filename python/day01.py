
with open('../inputs/day01.txt') as f:
    lines = f.readlines()

left, right = [], []
for line in lines:
    a, b = map(int, line.strip().split())
    left.append(a)
    right.append(b)

left.sort()
right.sort()

print(sum(abs(a-b) for a, b in zip(left, right)))