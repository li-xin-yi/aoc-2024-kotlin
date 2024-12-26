from collections import defaultdict, Counter
with open('../inputs/day12.txt') as f:
    graph = f.readlines()

graph = [list(row.strip()) for row in graph]

n, m = len(graph), len(graph[0])

area = Counter()
category = {}
sides = Counter()

def dfs(i, j, c, k):
    area[k] += 1
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < n and 0 <= y < m and graph[x][y] == c:
            graph[x][y] = k
            dfs(x, y, c, k)

cnt = 0
for i in range(n):
    for j in range(m):
        if isinstance(graph[i][j], str):
            c = graph[i][j]
            category[cnt] = c
            graph[i][j] = cnt
            dfs(i, j, c, cnt)
            cnt += 1



res = 0

for i in range(n):
    if i == 0 or i == n-1:
        for j in range(1, m):
            if graph[i][j]!=graph[i][j-1]:
                sides[graph[i][j-1]] += 1
        sides[graph[i][m-1]] += 1
    if i!=0:
        edges = [(j, graph[i-1][j], graph[i][j]) for j in range(m) if graph[i-1][j] != graph[i][j]]
        if not edges:
            continue
        for j in range(1, len(edges)):
            if edges[j][0] != edges[j-1][0] + 1:
                sides[edges[j-1][1]] += 1
                sides[edges[j-1][2]] += 1
            else:
                if edges[j][1] != edges[j-1][1]:
                    sides[edges[j-1][1]] += 1
                if edges[j][2] != edges[j-1][2]:
                    sides[edges[j-1][2]] += 1
        sides[edges[-1][1]] += 1
        sides[edges[-1][2]] += 1


for j in range(m):
    if j == 0 or j == m-1:
        for i in range(1, n):
            if graph[i][j]!=graph[i-1][j]:
                sides[graph[i-1][j]] += 1
        sides[graph[n-1][j]] += 1
    if j!=0:
        edges = [(i, graph[i][j-1], graph[i][j]) for i in range(n) if graph[i][j-1] != graph[i][j]]
        if not edges:
            continue
        for i in range(1, len(edges)):
            if edges[i][0] != edges[i-1][0] + 1:
                sides[edges[i-1][1]] += 1
                sides[edges[i-1][2]] += 1
            else:
                if edges[i][1] != edges[i-1][1]:
                    sides[edges[i-1][1]] += 1
                if edges[i][2] != edges[i-1][2]:
                    sides[edges[i-1][2]] += 1
        sides[edges[-1][1]] += 1
        sides[edges[-1][2]] += 1

res = 0
for k, v in area.items():
    res += v * sides[k]
#     print(f"{category[k]}: {v} * {sides[k]}")
print(res)