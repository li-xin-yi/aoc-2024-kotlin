with open('../inputs/day04.txt') as f:
    lines = f.readlines()

grid = [list(line.strip()) for line in lines]
n, m = len(grid), len(grid[0])

target = 'XMAS'
def word_search(i, j):
    res = 0
    if i >= 3:
        if ''.join(grid[i-dx][j] for dx in range(4)) == target:
            res += 1
        elif ''.join(grid[i-dx][j] for dx in range(4)) == target[::-1]:
            res += 1
    if j >= 3:
        if ''.join(grid[i][j-dy] for dy in range(4)) == target:
            res += 1
        elif ''.join(grid[i][j-dy] for dy in range(4)) == target[::-1]:
            res += 1
    if i >= 3 and j >= 3:
        if ''.join(grid[i-dx][j-dx] for dx in range(4)) == target:
            res += 1
        elif ''.join(grid[i-dx][j-dx] for dx in range(4)) == target[::-1]:
            res += 1
    if i >= 3 and j < m-3:
        if ''.join(grid[i-dx][j+dx] for dx in range(4)) == target:
            res += 1
        elif ''.join(grid[i-dx][j+dx] for dx in range(4)) == target[::-1]:
            res += 1
    return res

res = 0
for i in range(n):
    for j in range(m):
        res += word_search(i, j)
print(res)