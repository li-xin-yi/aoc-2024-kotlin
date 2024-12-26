with open('../inputs/day04.txt') as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]
n, m = len(grid), len(grid[0])

target = 'MAS'
targets = {target, target[::-1]}
def word_search(i, j):
    if i < 1 or i >= n-1 or j < 1 or j >= m-1:
        return 0
    if grid[i][j] != 'A':
        return 0
    first = ''.join(grid[i+dx][j-dx] for dx in range(-1, 2))
    second = ''.join(grid[i+dx][j+dx] for dx in range(-1, 2))
    if first in targets and second in targets:
        return 1
    return 0

res = 0
for i in range(n):
    for j in range(m):
        res += word_search(i, j)
print(res)
    