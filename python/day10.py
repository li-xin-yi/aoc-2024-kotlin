from collections import defaultdict

with open('../inputs/day10.txt') as f:
    lines = f.readlines()

graph = [list(map(int, list(line.strip()))) for line in lines]
n, m = len(graph), len(graph[0])
prev = defaultdict(set)
q = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            q.append((0, i, j))
            prev[(i, j)].add((i, j))

res = 0
cnt = 0
for num, i, j in q:
    if num == 9:
        res += len(prev[(i, j)])
        print(prev[(i, j)])
        continue
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < n and 0 <= y < m and graph[x][y] == num + 1:
            if (x, y) not in prev:
                q.append((num+1, x, y))
            prev[(x, y)].update(prev[(i, j)])
print(cnt)
print(res)