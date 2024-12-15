with open('../inputs/day14.txt') as f:
    lines = f.readlines()

# n, m = 11, 7
n, m = 101, 103

def process(line, T):
    left, part = line.split()
    x, y = map(int, left.split('=')[1].split(','))
    dx, dy = map(int, part.split('=')[1].split(','))
    return (x + dx * T) % n, (y + dy * T) % m


def longest_path(graph, n, m):
    res = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            if graph[i][j] == 0:
                res = max(res, cur)
                cur = 0
            else:
                cur += 1
        res = max(res, cur)

    for j in range(m):
        cur = 0
        for i in range(n):
            if graph[i][j] == 0:
                res = max(res, cur)
                cur = 0
            else:
                cur += 1
        res = max(res, cur)
    return res

paths = []
# set to 10000s, get the longest path
for i in range(7339):
    graph = [[0]*n for _ in range(m)]
    for line in lines:
        x, y = process(line, i)
        graph[y][x] += 1
    length = longest_path(graph, m, n)
    paths.append(length)
    # print(f'After {i+1} seconds:, the length is {length}')

for i in range(m):
    for j in range(n):
        print(graph[i][j] if graph[i][j] else '.', end='')
    print()
idx = max(range(len(paths)), key=paths.__getitem__)
print(idx, paths[idx])