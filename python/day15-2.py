with open('../inputs/day15.txt') as f:
    lines = f.readlines()


moves = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

wider = {
    '#': '##',
    'O': '[]',
    '.': '..',
    '@': '@.'
}

graph = []
operations = []
for i in range(len(lines)):
    if lines[i].strip():
        graph.append(list(''.join([wider[c] for c in lines[i].strip()])))
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

def bfs(x, y, dx, dy):
    q = [(x, y)]
    seen = set(q)
    for i, j in q:
        if graph[i][j] == '[':
            if (i, j+1) not in seen:
                q.append((i, j+1))
                seen.add((i, j+1))
        else:
            if (i, j-1) not in seen:
                q.append((i, j-1))
                seen.add((i, j-1))
        if graph[i+dx][j+dy] == '#':
            return False
        elif (graph[i+dx][j+dy] == '[' or graph[i+dx][j+dy] == ']') and (i+dx, j+dy) not in seen:
            seen.add((i+dx, j+dy))
            q.append((i+dx, j+dy))
    for i,j in q[::-1]:
        graph[i+dx][j+dy] = graph[i][j]
        graph[i][j] = '.'
    return True


for operation in operations:
    for char in operation:
        dx, dy = moves[char]
        next_x, next_y = x + dx, y + dy
        if graph[next_x][next_y] == '.':
            x, y = next_x, next_y
        elif graph[next_x][next_y] == '[' or graph[next_x][next_y] == ']':
            if bfs(next_x, next_y, dx, dy):
                x, y = next_x, next_y


res = 0
for i in range(n):
    for j in range(m-1):
        if graph[i][j] == '[':
            res += i * 100 + j
print(res)



