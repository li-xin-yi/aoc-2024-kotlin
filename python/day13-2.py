
with open("../inputs/day13.txt") as f:
    lines = f.readlines()

B = 10000000000000
prizes = []
for i in range(0, len(lines), 4):
    x, y = lines[i].strip().split(': ')[-1].split(', ')
    xa, ya = int(x.split('+')[-1]), int(y.split('+')[-1])
    x, y = lines[i+1].strip().split(': ')[-1].split(', ')
    xb, yb = int(x.split('+')[-1]), int(y.split('+')[-1])
    x, y = lines[i+2].strip().split(': ')[-1].split(', ')
    x0, y0 = int(x.split('=')[-1]) + B, int(y.split('=')[-1]) + B
    prizes.append((xa, ya, xb, yb, x0, y0))


def solve(xa, ya, xb, yb, x0, y0):
    # a * xa + b * xb = x0
    # a * ya + b * yb = y0
    # D = xa * yb - xb * ya
    # a = (x0 * yb - xb * y0) / D
    # b = (xa * y0 - x0 * ya) / D
    D = xa * yb - xb * ya
    if D == 0:
        return float('inf')
    if (x0 * yb - xb * y0) % D != 0 or (xa * y0 - x0 * ya) % D != 0:
        return float('inf')
    a = (x0 * yb - xb * y0) // D
    b = (xa * y0 - x0 * ya) // D
    if a < 0 or b < 0:
        return float('inf')
    return a*3 + b


res = 0
for prize in prizes:
    if (token := solve(*prize)) != float('inf'):
        res += token
print(res)
