import heapq

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
h = [(0, start[0], start[1], 0, 1)]

while h:
    d, x, y, dx, dy = heapq.heappop(h)
    if (x, y) == end:
        print(d)
        break
    if d > dist[(x, y, dx, dy)]:
        continue
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx, ny = x + di, y + dj
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':
            if (di, dj) == (-dx, -dy):
                continue
            if (di, dj) == (dx, dy):
                if (nx, ny, di, dj) not in dist or d + 1 < dist[(nx, ny, di, dj)]:
                    dist[(nx, ny, di, dj)] = d + 1
                    heapq.heappush(h, (d + 1, nx, ny, di, dj))
            else:
                if (nx, ny, di, dj) not in dist or d + 1001 < dist[(nx, ny, di, dj)]:
                    dist[(nx, ny, di, dj)] = d + 1001
                    heapq.heappush(h, (d + 1001, nx, ny, di, dj))
    
                

