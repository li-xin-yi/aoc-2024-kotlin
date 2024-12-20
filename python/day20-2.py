with open('../inputs/day20.txt') as f:
    lines = f.readlines()

graph = [line.strip() for line in lines]
n, m = len(graph), len(graph[0])

x_start, y_start = 0, 0
y_start, y_end = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            x_start, y_start = i, j
        elif graph[i][j] == 'E':
            x_end, y_end = i, j


def bfs(x0, y0):
    dist = {(x0, y0): 0}
    seen = set([(x0, y0)])
    q = [(x0, y0, 0)]
    for x, y, d in q:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and graph[nx][ny] != '#':
                seen.add((nx, ny))
                q.append((nx, ny, d+1))
                dist[(nx, ny)] = d + 1
    return dist

def bfs_rev(x0, y0):
    dist = {}
    seen = set([(x0, y0)])
    q = [(x0, y0, 0)]
    for x, y, d in q:
        if d >= 20:
            break
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append((nx, ny, d+1))
                dist[(nx, ny)] = d + 1
    return dist

dist1 = bfs(x_start, y_start)
dist2 = bfs(x_end, y_end)
base = dist1[(x_end, y_end)]
saving = 100
res = 0

for i in range(n):
    for j in range(m):
        if (i, j) in dist1:
            dist3 = bfs_rev(i, j)
            for x, y in dist3:
                if (x, y) in dist2 and dist1[(i, j)] + dist2[(x, y)] + dist3[(x,y)] <= base - saving:
                    res += 1

print(res)