from collections import defaultdict

with open('../inputs/day08.txt') as f:
    lines = f.readlines()

antennas = defaultdict(list)
res = set()
n, m = len(lines), len(lines[0].strip())
for i in range(n):
    for j in range(m):
        if lines[i][j] != '.':
            antennas[lines[i][j]].append((i, j))
            res.add((i, j))

def get_antinodes(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    i = 1
    while 0 <= x2 + i * dx < n and 0 <= y2 + i * dy < m:
        yield x2 + i * dx, y2 + i * dy
        i += 1
    i = 1
    while 0 <= x1 - i * dx < n and 0 <= y1 - i * dy < m:
        yield x1 - i * dx, y1 - i * dy
        i += 1



for freq in antennas:
    lst = antennas[freq]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            a, b = lst[i], lst[j]
            for x, y in get_antinodes(*a, *b):
                if (x, y) not in res:
                    res.add((x, y))
print(len(res))