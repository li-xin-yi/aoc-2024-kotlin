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
    dist = [[float('inf')]*m for _ in range(n)]
    dist[x0][y0] = 0
    q = [(x0, y0, 0)]
    for x, y, d in q:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and dist[nx][ny] == float('inf'):
                    q.append((nx, ny, d+1))
                if dist[nx][ny] == float('inf'):
                    dist[nx][ny] = d + 1
    return dist


dist1 = bfs(x_start, y_start)
dist2 = bfs(x_end, y_end)

saving = 100

base = dist1[x_end][y_end]
res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != '#':
            continue
        for x,y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < n and 0 <= y < m and graph[x][y]!='#' and dist1[i][j] + dist2[x][y] + 1 <= base - saving:
                res += 1

print(res)