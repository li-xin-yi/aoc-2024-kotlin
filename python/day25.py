with open("../inputs/day25.txt") as f:
    lines = f.readlines()
lines.append('')

keys = []
locks = []
cur = []
for i, line in enumerate(lines):
    line = line.strip()
    if line:
        cur.append(line)
    else:
        pattern = []
        for k in range(5):
            for j in range(len(cur) - 1):
                if cur[j+1][k] != cur[j][k]:
                    pattern.append(j)
                    break
            else:
                pattern.append(len(cur) - 1)
        if cur[0][0] == '#':
            locks.append(tuple(pattern))
        else:
            keys.append(tuple([len(cur) - 2 - t for t in pattern]))
        cur = []

res = 0
for key in keys:
    for lock in locks:
        if all(a+b < 6 for a, b in zip(key, lock)):
            res += 1
print(res)