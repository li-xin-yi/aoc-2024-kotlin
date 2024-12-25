
with open("../inputs/day13.txt") as f:
    lines = f.readlines()

prizes = []
for i in range(0, len(lines), 4):
    x, y = lines[i].strip().split(': ')[-1].split(', ')
    xa, ya = int(x.split('+')[-1]), int(y.split('+')[-1])
    x, y = lines[i+1].strip().split(': ')[-1].split(', ')
    xb, yb = int(x.split('+')[-1]), int(y.split('+')[-1])
    x, y = lines[i+2].strip().split(': ')[-1].split(', ')
    x0, y0 = int(x.split('+')[-1]), int(y.split('+')[-1])
    prizes.append((xa, ya, xb, yb, x0, y0))

