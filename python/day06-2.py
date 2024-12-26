with open('../inputs/day06.txt') as f:
    lines = f.readlines()

graph = [list(line.strip()) for line in lines]

n, m = len(graph), len(graph[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

seen = set()

for i in range(n):
    for j in range(m):
        if graph[i][j] == '^':
            x0, y0 = i, j
            seen.add((i, j))
            break

d = 0
x, y = x0 + directions[d][0], y0 + directions[d][1]

d = 0
x, y = x0 + directions[d][0], y0 + directions[d][1]
while 0<=x<n and 0<=y<m:
    seen.add((x, y))
    # graph[x][y] = 'X'
    next_x, next_y = x + directions[d][0], y + directions[d][1]
    while 0<=next_x<n and 0<=next_y<m and graph[next_x][next_y] == '#':
        d = (d + 1) % 4
        next_x, next_y = x + directions[d][0], y + directions[d][1]
    x, y = next_x, next_y

def check(x1, y1):
    d = 0
    seen = set([(x0, y0, 0)])
    x, y = x0 + directions[d][0], y0 + directions[d][1]
    while 0<=x<n and 0<=y<m:
        if (x, y, d) in seen:
            return True
        seen.add((x, y, d))
        next_x, next_y = x + directions[d][0], y + directions[d][1]
        while 0<=next_x<n and 0<=next_y<m and (graph[next_x][next_y] == '#' or (next_x, next_y) == (x1, y1)):
            d = (d + 1) % 4
            next_x, next_y = x + directions[d][0], y + directions[d][1]
        x, y = next_x, next_y
    return False

print(sum(check(i, j) for i in range(n) for j in range(m)))