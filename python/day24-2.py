from collections import defaultdict
with open('../inputs/day24.txt') as f:
    lines = f.readlines()


# z_{i+1} = x_{i+1} XOR y_{i+1} XOR c_i
# c_{i+1} = (x_{i+1} AND y_{i+1}) OR (c_i AND (x_{i+1} XOR y_{i+1}))

switch = {
    'mvb': 'z08',
    'z08': 'mvb',
    'rds': 'jss',
    'jss': 'rds',
    'wss': 'z18',
    'z18': 'wss',
    'bmn': 'z23',
    'z23': 'bmn',
}

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
            if parts[-1] in switch:
                parts[-1] = switch[parts[-1]]
            equations[parts[-1]] = tuple([parts[1], parts[0], parts[2]])
            adj[parts[0]].append(parts[-1])
            adj[parts[2]].append(parts[-1])
        break

definitions = {}
for i in range(len(wires)//2):
    if i == 0:
        definitions[('XOR', 'x00', 'y00')] =  'z00'
        definitions[('AND', 'x00', 'y00')] =  'c01'
    else:
        cur_num = str(i).zfill(2)
        next_num = str(i+1).zfill(2)
        definitions[('XOR', f'x{cur_num}', f'y{cur_num}')] = f'tmp_a_{cur_num}'
        definitions[('AND', f'x{cur_num}', f'y{cur_num}')] = f'tmp_b_{cur_num}'
        definitions[('XOR', f'c{cur_num}', f'tmp_a_{cur_num}')] = f'z{cur_num}'
        definitions[('AND', f'c{cur_num}', f'tmp_a_{cur_num}')] = f'tmp_c_{cur_num}'
        definitions[('OR', f'tmp_b_{cur_num}', f'tmp_c_{cur_num}')] = f'c{next_num}'

aliases = {i:i for i in wires}
q = []
for k in equations:
    op, val1, val2 = equations[k]
    val1, val2 = sorted([val1, val2])
    if (op, val1, val2) in definitions:
        aliases[k] = definitions[(op, val1, val2)]
        q.append(k)

# print(q)

for k in q:
    for node in adj[k]:
        op, val1, val2 = equations[node]
        old_val1, old_val2 = val1, val2
        if val1 in aliases and val2 in aliases:
            val1 = aliases[val1]
            val2 = aliases[val2]
            val1, val2 = sorted([val1, val2])
            if (op, val1, val2) in definitions:
                if definitions[(op, val1, val2)].startswith('z'):
                    print("found", node, op, val1, val2, definitions[(op, val1, val2)])
                    assert node == definitions[(op, val1, val2)]
                aliases[node] = definitions[(op, val1, val2)]
                q.append(node)
                # print(f"found {node} = {val1} {op} {val2}")
            else:
                # not found OR tmp_b_08 z09 ('OR', 'mvb', 'wdc')
                print("not found", k, op, val1, val2, equations[node], node)

# print([k for k, v in aliases.items() if v == 'tmp_a_08']) # ['z08']
# print([k for k, v in aliases.items() if v == 'tmp_b_08']) # ['mvb']
print([k for k, v in aliases.items() if v == 'tmp_b_14'])
print([k for k, v in aliases.items() if v == 'tmp_a_14'])
# print([k for k in equations if k not in aliases])

for k in equations:
    if k in aliases:
        continue
    op, val1, val2 = equations[k]
    if val1 in aliases or val2 in aliases:
        val1 = aliases.get(val1, val1)
    # if val2 in wires:
        val2 = aliases.get(val2, val2)
        val1, val2 = sorted([val1, val2])
        print(f"{k} = {val1} {op} {val2}")

print(','.join(sorted(list(switch.keys()))))