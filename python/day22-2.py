from collections import Counter
M = 16777216

with open("../inputs/day22.txt") as f:
    lst = list(map(lambda x: int(x.strip()), f.readlines()))


def secret(x):
    x ^= x*64
    x %= M
    x ^= x//32
    x %= M
    x ^= x*2048
    x %= M
    return x

cnt = Counter()

def gen(x):
    digits = [x%10]
    for _ in range(2000):
        x = secret(x)
        digits.append(x%10)
    diff = []
    seq = Counter()
    for i in range(1, len(digits)):
        diff.append(digits[i] - digits[i-1])
        if len(diff) >= 4:
            k = tuple(diff[-4:])
            if k not in seq:
                seq[k] = digits[i]
    return seq

for num in lst:
    cnt += gen(num)

print(max(cnt.values()))