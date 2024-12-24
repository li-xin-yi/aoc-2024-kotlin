from collections import defaultdict
with open('../inputs/day24.txt') as f:
    lines = f.readlines()

wires = {}
equations = {}
adj = defaultdict(list)
for i, line in enumerate(lines):
    line = line.strip()
    if line:
        name, val = line.split(': ')
        wires[name] = int(val)
    else:
        for line in lines[i+1:]:
            parts = line.strip().split(' ')
            equations[parts[-1]] = tuple(parts[:3])
            adj[parts[0]].append(parts[-1])
            adj[parts[2]].append(parts[-1])
        break

def calc(val1, op, val2):
    if op == 'AND':
        return wires[val1] & wires[val2]
    elif op == 'OR':
        return wires[val1] | wires[val2]
    elif op == 'XOR':
        return wires[val1] ^ wires[val2]

q = []
for k, v in equations.items():
    val1, op, val2 = v
    if val1 in wires and val2 in wires:
        wires[k] = calc(val1, op, val2)
        for node in adj[k]:
            if equations[node][0] in wires and equations[node][2] in wires:
                q.append(node)

for node in q:
    val1, op, val2 = equations[node]
    wires[node] = calc(val1, op, val2)
    for n in adj[node]:
        if equations[n][0] in wires and equations[n][2] in wires:
            q.append(n)

# print(wires)
# print(equations)
print(int(''.join(str(wires[k]) for k in sorted(wires.keys(), reverse=True) if k.startswith('z')), 2))