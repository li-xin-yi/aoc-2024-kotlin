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

pc = 0
while pc < len(instructions):
    res = inst[instructions[pc]](instructions[pc+1])
    # print(pc, registers, instructions[pc:pc+2], res)
    if res != -1:
        pc = res
    else:
        pc += 2

print(','.join(map(str, outputs)))
