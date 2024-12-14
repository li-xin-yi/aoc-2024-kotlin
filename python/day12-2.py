from collections import defaultdict, Counter
with open('../inputs/day12.txt') as f:
    graph = f.readlines()

graph = [row.strip() for row in graph]

n, m = len(graph), len(graph[0])

seen = set()


def bfs(i, j):
    edges = []
    q = [(i, j)]
    for x, y in q:
        nei = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == graph[i][j]:
                    if (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))
                else:
                    nei.append((nx, ny))
            else:
                nei.append((nx, ny))
            

                                                                                                                        

    # print(set(root.values()), graph[i][j], len(set(root.values())))
    cnt = Counter(root.values())
    print(cnt)
    
    d = len(set(root.values()))

    return d * len(q)


res = 0
for i in range(n):
    for j in range(m):
        if (i, j) not in seen:
            seen.add((i, j))
            res += bfs(i, j)
print(res)
    
    



