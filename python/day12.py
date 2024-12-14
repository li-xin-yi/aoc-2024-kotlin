with open('../inputs/day12.txt') as f:
    graph = f.readlines()

graph = [row.strip() for row in graph]


n, m = len(graph), len(graph[0])

def dfs(i, j, k, seen):
    res_area, res_perimeter = 0, 0
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < n and 0 <= y < m:
            if graph[x][y] == k:
                if (x, y) not in seen:
                    seen.add((x, y))
                    area, perimeter = dfs(x, y, k, seen)
                    res_area += area
                    res_perimeter += perimeter
            else:
                res_perimeter += 1
        else:
            res_perimeter += 1
    return res_area + 1, res_perimeter

seen = set()
res = 0
for i in range(n):
    for j in range(m):
        if (i, j) not in seen:
            seen.add((i, j))
            area, perimeter = dfs(i, j, graph[i][j], seen)
            res += area * perimeter
print(res)
