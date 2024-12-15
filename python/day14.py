from collections import Counter
with open('../inputs/day14.txt') as f:
    lines = f.readlines()

# n, m = 11, 7
n, m = 101, 103
T = 100

def process(line):
    left, part = line.split()
    x, y = map(int, left.split('=')[1].split(','))
    dx, dy = map(int, part.split('=')[1].split(','))
    return (x + dx * T) % n, (y + dy * T) % m

cnt = Counter()
for line in lines:
    x, y = process(line)
    if x == n // 2 or y == m // 2:
        continue
    i = int(x < n // 2)
    j = int(y < m // 2)
    cnt[(i, j)] += 1

res = 1
for i, j in (0, 0), (0, 1), (1, 0), (1, 1):
    res *= cnt[(i, j)]
print(res)