from collections import defaultdict

with open('input/day08.txt') as f:
    lines = f.readlines()

antennas = defaultdict(list)
n, m = len(lines), len(lines[0].strip())
for i in range(n):
    for j in range(m):
        if lines[i][j] != '.':
            antennas[lines[i][j]].append((i, j))

def get_antinodes(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (x2 + dx, y2 + dy), (x1 - dx, y1 - dy)

res = set()


for freq in antennas:
    lst = antennas[freq]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            a, b = lst[i], lst[j]
            for x, y in get_antinodes(*a, *b):
                if 0 <= x < n and 0 <= y < m and (x, y) not in res:
                    res.add((x, y))

print(len(res))