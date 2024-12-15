with open('../inputs/day15.txt') as f:
    lines = f.readlines()

moves = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

graph = []
operations = []
for i in range(len(lines)):
    if lines[i].strip():
        graph.append(list(lines[i].strip()))
    else:
        operations = ''.join(line.strip() for line in lines[i+1:])
        break

n, m = len(graph), len(graph[0])

x = y = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '@':
            x, y = i, j
            graph[i][j] = '.'
            break

def move_box(x, y, dx, dy):
    x0, y0 = x, y
    while 0 <= x < n and 0 <= y < m and graph[x][y] == 'O':
        x += dx
        y += dy
    if 0 <= x < n and 0 <= y < m and graph[x][y] != '#':
        graph[x0][y0] = '.'
        graph[x][y] = 'O'
        return True
    return False

for operation in operations:
    for char in operation:
        dx, dy = moves[char]
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < m:
            if graph[next_x][next_y] == '.':
                x, y = next_x, next_y
            elif graph[next_x][next_y] == 'O':
                if move_box(next_x, next_y, dx, dy):
                    x, y = next_x, next_y

res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'O':
            res += i * 100 + j
print(res)
