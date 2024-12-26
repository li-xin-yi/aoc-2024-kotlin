
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
from functools import cache

grid0 = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['', '0', 'A']
]

pos0 = {}
for i in range(len(grid0)):
    for j in range(len(grid0[i])):
        if grid0[i][j] != '':
            pos0[grid0[i][j]] = (i, j)

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
grid1 = [
    ['', '^', 'A'],
    ['<', 'v', '>']
]
pos1 = {
    '^': (0, 1),
    'v': (1, 1),
    '<': (1, 0),
    '>': (1, 2),
    'A': (0, 2)
}

positions = [pos0, pos1]
grids = [grid0, grid1]

@cache
def move(start, end, degree):
    if degree == 0:
        pos = positions[0]
        grid = grids[0]
    else:
        pos = positions[1]
        grid = grids[1]
    dx, dy = pos[end][0] - pos[start][0], pos[end][1] - pos[start][1]
    left, right = '', ''
    if dy > 0:
        left = '>' * dy
    elif dy < 0:
        left = '<' * abs(dy)
    if dx < 0:
        right = '^' * abs(dx)
    elif dx > 0:
        right = 'v' * dx
    cand = [left+right+'A']
    if left and right:
        cand = [left+right+'A', right+left+'A']
        for i in range(len(left)):
            sign = -1 if left[i] == '<' else 1
            if grid[pos[start][0]][pos[start][1] + sign * (i+1)] == '':
                cand = [right+left+'A']
                break
        for i in range(len(right)):
            sign = -1 if right[i] == '^' else 1
            if grid[pos[start][0] + sign * (i+1)][pos[start][1]] == '':
                cand = [left+right+'A']
                break
    if degree == 25:
        return min(len(c) for c in cand)
    else:
        cand = ['A' + c for c in cand]
        return min([sum(move(c[i], c[i+1], degree+1) for i in range(len(c)-1)) for c in cand])

def get_instructions(input):
    res = 0
    input = 'A' + input
    for i in range(len(input)-1):
        res += move(input[i], input[i+1], 0)
    return res


with open('../inputs/day21.txt') as f:
    lines = f.readlines()

res = 0
for line in lines:
    line = line.strip()
    instr = get_instructions(line)
    res += instr * int(line[:-1])

print(res)