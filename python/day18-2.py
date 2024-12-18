with open('../inputs/day18.txt') as f:
    lines = f.readlines()

n, m = 71, 71
coordinates = [tuple(map(int, line.strip().split(','))) for line in lines]


def check(k):
    points = set(coordinates[:k])
    seen = set([(0, 0)])
    q = [(0, 0 , 0)]

    for x,y,step in q:
        if (x, y) == (n-1, m-1):
            return True
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in seen and (nx, ny) not in points:
                q.append((nx, ny, step+1))
                seen.add((nx, ny))
    return False

left, right = 0, len(lines)
while left < right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid

print(right)
print(coordinates[right-1])
