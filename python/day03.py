import re

with open("../inputs/day03.txt") as f:
    lines = f.readlines()
    text = ''.join([line.strip() for line in lines])

pattern = r"(do\(\)|don't\(\)|mul\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*\))"
disabled = False
res = 0
for match in re.finditer(pattern, text):
    token = match.group(1)
    if token == "do()":
        disabled = False
    elif token == "don't()":
        disabled = True
    else:
        if disabled:
            continue
        x, y = map(int, match.groups()[1:])
        res += x * y
print(res)