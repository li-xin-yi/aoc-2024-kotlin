with open('../inputs/day18.txt') as f:
    lines = f.readlines()

n, m = 71, 71

points = set([tuple(map(int, line.strip().split(','))) for line in lines[:1024]])
# print(points)

seen = set([(0, 0)])
q = [(0, 0 , 0)]

for x,y,step in q:
    # print(x, y, step)
    if (x, y) == (n-1, m-1):
        print(step)
        break
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and (nx, ny) not in points:
            q.append((nx, ny, step+1))
            seen.add((nx, ny))