
with open("../inputs/day13.txt") as f:
    lines = f.readlines()

prizes = []
for i in range(0, len(lines), 4):
    x, y = lines[i].strip().split(': ')[-1].split(', ')
    xa, ya = int(x.split('+')[-1]), int(y.split('+')[-1])
    x, y = lines[i+1].strip().split(': ')[-1].split(', ')
    xb, yb = int(x.split('+')[-1]), int(y.split('+')[-1])
    x, y = lines[i+2].strip().split(': ')[-1].split(', ')
    x0, y0 = int(x.split('=')[-1]), int(y.split('=')[-1])
    prizes.append((xa, ya, xb, yb, x0, y0))


def solve(xa, ya, xb, yb, x0, y0):
    res = float('inf')
    for i in range(min(x0//xa + 1, 101)):
        if y0 - i*ya >= 0 and (x0 - i*xa) % xb == 0 and (y0 - i*ya) % yb == 0 and (y0 - i*ya) // yb == (x0 - i*xa) // xb:
            res = min(res, i*3 + (x0 - i*xa) // xb)
    return res


res = 0
for prize in prizes:
    if (token := solve(*prize)) != float('inf'):
        res += token
print(res)
