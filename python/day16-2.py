import heapq
from collections import defaultdict

with open('../inputs/day16.txt') as f:
    lines = f.readlines()

graph = [line.strip() for line in lines]
n, m = len(graph), len(graph[0])

start = (0, 0)
end = (0, 0)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            start = (i, j)
        elif graph[i][j] == 'E':
            end = (i, j)

dist = {(start[0], start[1], 0, 1): 0}
prev = defaultdict(list)
h = [(0, start[0], start[1], 0, 1)]

target = 0
while h:
    d, x, y, dx, dy = heapq.heappop(h)
    if (x, y) == end:
        target = d
        print(target)
        break
    if d > dist[(x, y, dx, dy)]:
        continue
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx, ny = x + di, y + dj
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
            if (di, dj) == (-dx, -dy):
                continue
            if (di, dj) == (dx, dy):
                if (nx, ny, di, dj) not in dist or d + 1 <= dist[(nx, ny, di, dj)]:
                    prev[(nx, ny, di, dj)].append((x, y, dx, dy))
                    dist[(nx, ny, di, dj)] = d + 1
                    heapq.heappush(h, (d + 1, nx, ny, di, dj))
            else:
                if (nx, ny, di, dj) not in dist or d + 1001 <= dist[(nx, ny, di, dj)]:
                    prev[(nx, ny, di, dj)].append((x, y, dx, dy))
                    dist[(nx, ny, di, dj)] = d + 1001
                    heapq.heappush(h, (d + 1001, nx, ny, di, dj))

paths = set()
def dfs(x, y, dx, dy):
    for px, py, pdx, pdy in prev[(x, y, dx, dy)]:
        if (px, py, pdx, pdy) not in paths:
            paths.add((px, py, pdx, pdy))
            dfs(px, py, pdx, pdy)

for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
    if dist.get((end[0], end[1], dx, dy), float('inf')) == target:
        paths.add((end[0], end[1], dx, dy))
        dfs(end[0], end[1], dx, dy)

print(len(set((x,y) for x,y,_,_ in paths)))