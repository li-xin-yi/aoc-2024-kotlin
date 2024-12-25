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

def gen(x):
    for _ in range(2000):
        x = secret(x)
        # print(x)
    return x


res = 0
for num in lst:
    s = gen(num)
    # print(f"{num}: {s}")
    res += s

print(res)

