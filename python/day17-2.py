with open('../inputs/day17.txt') as f:
    lines = f.readlines()

registers = [int(line.strip().split()[-1]) for line in lines[:3]]
instructions = list(map(int, lines[-1].strip().split()[-1].split(',')))
outputs = []

def operand(num):
    if num <= 3:
        return num
    if num <= 6:
        return registers[num-4]
    raise ValueError('Invalid operand')

def adv(x):
    registers[0] = registers[0] // (1<<operand(x))
    return -1

def bsl(x):
    registers[1] = registers[1] ^ x
    return -1

def bst(x):
    registers[1] = operand(x) % 8
    return -1

def jnz(x):
    if registers[0]:
        return x
    return -1

def bxc(x):
    registers[1] = registers[1] ^ registers[2]
    return -1

def out(x):
    outputs.append(operand(x)%8)
    return -1

def bdv(x):
    registers[1] = registers[0] // (1<<operand(x))
    return -1

def cdv(x):
    registers[2] = registers[0] // (1<<operand(x))
    return -1

inst = [adv, bsl, bst, jnz, bxc, out, bdv, cdv]

# Register A: 64584136
# Register B: 0
# Register C: 0

# Program: 2,4,1,2,7,5,1,3,4,3,5,5,0,3,3,0

# 2, 4: bst(combo(4)) -> A % 8 -> B
# 1, 2: bxl(2) -> B ^ 2 -> B (B = (A % 8) ^ 2)
# 7, 5: cdv(5) -> C = A // (1 << B) -> C (C = A // (1 << (A % 8) ^ 2))
# 1, 3: bxl(3) -> B ^ 3 -> B (B = (A % 8) ^ 2 ^ 3)
# 4, 3: bxc -> B ^ C -> B (B = (A % 8) ^ 2 ^ 3 ^ (A // (1 << (A % 8) ^ 2)))
# 5, 5: out(combo(5)) -> B % 8 -> Output = 2

# 0, 3: adv(3) -> A // (1 << 3) -> A (A = A // 8)
# 3, 0: jnz(0) -> jump to 0 -> Loop


# (A // (1 << (A % 8)^2)) ^ ((A % 8)^2^3) = x
# (A // (1 << (A % 8)^2))) ^ (A % 8) = 3


def check(lower, higher, target):
    for x in range(lower, higher):
        x_8 = x % 8
        x_div = (x // (1 << (x_8 ^ 2)))
        res = (x_div ^ (x_8 ^ 2 ^ 3)) % 8
        if res == target:

            yield x
        

instructions_rev = instructions[::-1]
def dfs(i, cur):
    if i == len(instructions_rev):
        return cur
    for x in check(cur*8, cur*8+8, instructions_rev[i]):
        if (res := dfs(i+1, x)) is not None:
            return res
    return None
    
start = dfs(0, 0)

registers = [start, 0, 0]
pc = 0
outputs = []
while pc < len(instructions):
    res = inst[instructions[pc]](instructions[pc+1])
    if res != -1:
        pc = res
    else:
        pc += 2
print(start)
print(','.join(map(str, outputs)))